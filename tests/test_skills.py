import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import meta_harness as meta
import skills

EXAMPLE = ROOT / 'examples/skill-handoff'


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False) + '\n')


class SkillTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.bundle = self.root / 'bundle'
        shutil.copytree(EXAMPLE / 'harness', self.bundle)
        self.inputs = self.root / 'data'
        shutil.copytree(EXAMPLE / 'fixtures', self.inputs)
        self.manifest = json.loads((self.bundle / 'harness.json').read_text())

    def prepare(self, role='product', skill='filter-rows', name='mission', candidate=None, rules='rules.json'):
        inputs = {'source': self.inputs / 'source.csv', 'rules': self.inputs / rules}
        if candidate is not None:
            inputs['candidate'] = candidate
        order = self.root / name
        receipt = skills.prepare(self.bundle, skill, role, inputs, order)
        return order, receipt['order_sha256']

    def execute(self, order, skill, output):
        ports = ['source', 'rules'] + (['candidate'] if skill == 'check-rows' else [])
        return subprocess.run([sys.executable, '-B', str(order / f'resources/skills/{skill}/scripts/run.py'),
                               *(str(order / 'inputs' / port) for port in ports), str(output)],
                              cwd=order, capture_output=True, text=True, timeout=10)

    def test_index_routes_without_loading_all_skill_bodies(self):
        listing = skills.catalogue(self.bundle, 'audit')
        self.assertEqual([s['id'] for s in listing['skills']], ['check-rows'])
        self.assertEqual(listing['execution_status'], 'NOT_RUN')
        self.assertNotIn('body', listing['skills'][0])
        self.assertEqual(skills.catalogue(self.bundle, 'governance')['skills'], [])
        order, sha = self.prepare()
        self.assertFalse((order / 'resources/skills/check-rows').exists())
        self.assertEqual(skills.verify(order, sha)['validity_status'], 'PASS')

    def test_capability_references_and_missing_roles_are_rejected(self):
        changes = []
        missing_role = copy.deepcopy(self.manifest)
        missing_role['capabilities'] = missing_role['capabilities'][1:]
        changes.append(missing_role)
        missing_skill = copy.deepcopy(self.manifest)
        missing_skill['capabilities'][-1]['skill'] = 'absent'
        changes.append(missing_skill)
        ambiguous = copy.deepcopy(self.manifest)
        ambiguous['capabilities'][-1]['native'] = 'Ambigu'
        changes.append(ambiguous)
        for manifest in changes:
            with self.subTest(manifest=manifest['capabilities']):
                write_json(self.bundle / 'harness.json', manifest)
                with self.assertRaises(ValueError):
                    meta.check_bundle(self.bundle)

    def test_native_and_missing_capabilities_do_not_invent_skills(self):
        self.manifest['components'] = []
        for cap in self.manifest['capabilities']:
            cap.pop('skill', None)
            if 'native' not in cap:
                cap['unavailable'] = 'Compétence absente ; cette tâche ne peut pas commencer.'
        write_json(self.bundle / 'harness.json', self.manifest)
        self.assertEqual(meta.check_bundle(self.bundle)['semantic_status'], 'NOT_RUN')
        with self.assertRaisesRegex(ValueError, 'non attribué'):
            self.prepare()

    def test_skill_identity_ports_dependencies_and_assignment_are_checked(self):
        original = meta._snapshot(self.bundle)
        for mode in ('orphan', 'name', 'port', 'dependency', 'recipient'):
            files = dict(original)
            manifest = copy.deepcopy(self.manifest)
            if mode == 'orphan':
                manifest['capabilities'][-1] = {'role':'audit','task':'Examiner','unavailable':'Pas de moyen.'}
            elif mode == 'name':
                key = 'skills/check-rows/SKILL.md'
                files[key] = files[key].replace(b'name: check-rows', b'name: other')
            elif mode == 'port':
                manifest['components'][0]['inputs'] = ['source', 'source']
            elif mode == 'dependency':
                manifest['components'][0]['dependencies'] = ['../outside']
            else:
                manifest['components'][0]['handoff_to'] = ['unknown']
            files['harness.json'] = meta.canonical(manifest)
            with self.subTest(mode=mode), self.assertRaises(ValueError):
                meta._validate_bundle(files)

    def test_role_and_exact_inputs_are_required_before_preparation(self):
        with self.assertRaisesRegex(ValueError, 'non attribué'):
            self.prepare(role='audit')
        with self.assertRaisesRegex(ValueError, 'exactement'):
            skills.prepare(self.bundle, 'filter-rows', 'product', {'source':self.inputs/'source.csv'}, self.root/'bad')
        self.assertFalse((self.root/'bad').exists())
        with self.assertRaisesRegex(ValueError, 'N0'):
            skills.prepare(EXAMPLE/'meta-harness', 'filter-rows', 'product', {}, self.root/'bad')

    def test_product_to_audit_to_governance_preserves_inputs_and_contract(self):
        before = meta._snapshot(self.inputs)
        order, sha = self.prepare()
        candidate = self.root/'candidate.csv'
        self.assertEqual(self.execute(order, 'filter-rows', candidate).returncode, 0)
        handoff = self.root/'handoff-product'
        delivery = skills.handoff(order, 'audit', {'candidate':candidate}, handoff, sha)
        self.assertEqual(delivery['semantic_status'], 'NOT_RUN')
        audit, audit_sha = self.prepare('audit', 'check-rows', 'audit', handoff/'outputs/candidate')
        report = self.root/'report.json'
        self.assertEqual(self.execute(audit, 'check-rows', report).returncode, 0)
        self.assertEqual(json.loads(report.read_text())['criteria'], {'exact_rows':'PASS'})
        result = skills.handoff(audit, 'governance', {'report':report}, self.root/'handoff-audit', audit_sha)
        self.assertTrue(result['handoff_recorded'])
        self.assertEqual(result['semantic_status'], 'NOT_RUN')
        self.assertEqual(meta._snapshot(self.inputs), before)
        self.assertEqual(skills.verify(order, sha)['validity_status'], 'PASS')

    def test_empty_selection_is_valid_and_truncated_candidate_is_rejected(self):
        order, _ = self.prepare(rules='empty-rules.json')
        candidate = self.root/'empty.csv'
        self.assertEqual(self.execute(order, 'filter-rows', candidate).returncode, 0)
        self.assertEqual(candidate.read_text().splitlines(), ['category,item'])
        audit, _ = self.prepare('audit','check-rows','empty-audit',candidate,'empty-rules.json')
        self.assertEqual(self.execute(audit,'check-rows',self.root/'empty-report.json').returncode,0)
        audit, _ = self.prepare('audit','check-rows','bad-audit',self.inputs/'wrong.csv')
        report = self.root/'bad-report.json'
        self.assertEqual(self.execute(audit,'check-rows',report).returncode,1)
        self.assertEqual(json.loads(report.read_text())['status'],'FAIL')

    def test_invalid_source_and_missing_runtime_do_not_create_success(self):
        (self.inputs/'source.csv').write_text('other,item\nx,A\n')
        order, _ = self.prepare()
        candidate = self.root/'candidate.csv'
        self.assertEqual(self.execute(order,'filter-rows',candidate).returncode,2)
        self.assertFalse(candidate.exists())
        audit, _ = self.prepare('audit','check-rows','audit',self.inputs/'wrong.csv')
        report = self.root/'report.json'
        self.assertEqual(self.execute(audit,'check-rows',report).returncode,2)
        self.assertEqual(json.loads(report.read_text())['status'],'UNKNOWN')
        (self.bundle/'skills/filter-rows/scripts/run.py').unlink()
        with self.assertRaises(ValueError):
            self.prepare(name='missing-script')

    def test_malformed_rules_remain_unknown_and_existing_outputs_are_preserved(self):
        (self.inputs/'rules.json').write_text('[]\n')
        audit,_=self.prepare('audit','check-rows','audit',self.inputs/'wrong.csv')
        report=self.root/'report.json'
        self.assertEqual(self.execute(audit,'check-rows',report).returncode,2)
        self.assertEqual(json.loads(report.read_text())['status'],'UNKNOWN')
        previous=report.read_bytes()
        self.assertEqual(self.execute(audit,'check-rows',report).returncode,2)
        self.assertEqual(report.read_bytes(),previous)

    def test_modified_oracle_plan_input_and_instruction_invalidate_order(self):
        for relative in ['skills/filter-rows/scripts/run.py','SPEC.md','harness.json','AGENTS.md']:
            with self.subTest(resource=relative):
                order, sha = self.prepare(name='mission-'+str(len(list(self.root.glob('mission-*')))))
                path = self.bundle/relative
                original = path.read_bytes()
                path.write_bytes(original+b'\n')
                self.assertEqual(skills.verify(order,sha)['validity_status'],'STALE')
                with self.assertRaisesRegex(ValueError,'STALE'):
                    skills.handoff(order,'audit',{'candidate':self.inputs/'wrong.csv'},self.root/'refused',sha)
                self.assertFalse((self.root/'refused').exists())
                path.write_bytes(original)
        order,sha=self.prepare(name='source-change')
        (self.inputs/'source.csv').write_text('category,item\nx,B\n')
        self.assertEqual(skills.verify(order,sha)['validity_status'],'STALE')

    def test_receipt_omission_and_copied_resource_changes_are_stale(self):
        order,sha=self.prepare()
        receipt=json.loads((order/'receipt.json').read_text())
        receipt['resources']={}
        write_json(order/'receipt.json',receipt)
        self.assertEqual(skills.verify(order,sha)['validity_status'],'STALE')
        order,sha=self.prepare(name='other')
        (order/'resources/skills/filter-rows/scripts/run.py').write_text('pass\n')
        self.assertEqual(skills.verify(order,sha)['validity_status'],'STALE')

    def test_added_import_and_removed_obligation_cannot_escape_frozen_mission(self):
        order,sha=self.prepare()
        (order/'resources/skills/filter-rows/scripts/csv.py').write_text('raise RuntimeError("shadow module")\n')
        self.assertEqual(skills.verify(order,sha)['validity_status'],'STALE')
        order,sha=self.prepare(name='plan-change')
        self.manifest['capabilities'] = [c for c in self.manifest['capabilities'] if c['role'] != 'audit']
        write_json(self.bundle/'harness.json',self.manifest)
        self.assertEqual(skills.verify(order,sha)['validity_status'],'STALE')

    def test_wrong_recipient_missing_output_and_existing_destination_are_refused(self):
        order,sha=self.prepare()
        with self.assertRaisesRegex(ValueError,'Destinataire'):
            skills.handoff(order,'governance',{'candidate':self.inputs/'wrong.csv'},self.root/'bad',sha)
        with self.assertRaisesRegex(ValueError,'exactement'):
            skills.handoff(order,'audit',{},self.root/'bad',sha)
        destination=self.root/'existing';destination.mkdir();(destination/'keep').write_text('keep')
        with self.assertRaises(FileExistsError):
            skills.handoff(order,'audit',{'candidate':self.inputs/'wrong.csv'},destination,sha)
        self.assertEqual((destination/'keep').read_text(),'keep')

    def test_symlink_dependency_is_never_copied(self):
        p=self.bundle/'skills/filter-rows/scripts/run.py';p.unlink();p.symlink_to(self.inputs/'wrong.csv')
        with self.assertRaisesRegex(ValueError,'symbolique'):
            self.prepare()

    def test_n1_n0_materialization_and_review_only_variation(self):
        meta.check_bundle(EXAMPLE/'meta-harness')
        output=meta.materialize(self.bundle,self.root/'materialized',meta_harness=EXAMPLE/'meta-harness')[0]
        self.assertEqual((output/'skills/check-rows/SKILL.md').read_bytes(),(self.bundle/'skills/check-rows/SKILL.md').read_bytes())
        self.assertTrue((output/'_eiffel/meta-harness/skills/check-rows/SKILL.md').exists())
        self.manifest['components']=[c for c in self.manifest['components'] if c['id']!='filter-rows']
        self.manifest['capabilities'][2]={'role':'product','task':'Recevoir le candidat fourni','native':'Identifier le fichier reçu, sans le modifier ; aucune production demandée.'}
        write_json(self.bundle/'harness.json',self.manifest)
        shutil.rmtree(self.bundle/'skills/filter-rows')
        (self.bundle/'AGENTS.md').write_text('Examen seul : Produit identifie le candidat fourni, Audit utilise check-rows, Gouvernance reçoit le rapport. SPEC.md reste le contrat.\n')
        (self.bundle/'DESIGN.md').write_text(
            '# Choix du lot d’examen seul\n\n'
            'Le candidat est fourni : produire à nouveau ne répond pas au besoin. '
            'Produit identifie le fichier reçu et Audit conserve check-rows ; filter-rows est retiré. '
            'SPEC.md reste le contrat, avec les mêmes lignes, ordre et doublons dus. '
            'Une demande de production réintroduirait sa compétence et sa remise, puis réviserait '
            'capabilities, AGENTS.md et cette note. Aucun gain de coût ni audit indépendant n’est établi.\n')
        self.assertEqual(skills.catalogue(self.bundle,'product')['skills'],[])
        self.assertEqual(len(skills.catalogue(self.bundle,'audit')['skills']),1)
        order,sha=self.prepare('audit','check-rows','audit',self.inputs/'wrong.csv')
        report=self.root/'report.json'
        self.assertEqual(self.execute(order,'check-rows',report).returncode,1)
        self.assertTrue(skills.handoff(order,'governance',{'report':report},self.root/'delivery',sha)['handoff_recorded'])

    def test_cli_requires_external_order_reference_and_preserves_unknown_semantics(self):
        order,sha=self.prepare()
        command=[sys.executable,'-B',str(ROOT/'tools/skills.py'),'verify',str(order)]
        self.assertNotEqual(subprocess.run(command,capture_output=True,text=True).returncode,0)
        result=subprocess.run(command+['--order-sha256',sha],capture_output=True,text=True,check=True)
        self.assertEqual(json.loads(result.stdout)['semantic_status'],'NOT_RUN')


if __name__=='__main__':
    unittest.main()
