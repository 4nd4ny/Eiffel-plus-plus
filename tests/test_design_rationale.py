"""Conservation et invalidation de la justification ; pas de score de prose."""
import copy
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import meta_harness as meta
import seeds
import skills
from check_catalog import check_markdown_tree
from test_seeds import note

EXAMPLE = ROOT / 'examples/skill-handoff'


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


class DesignRationaleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.n0, self.n1 = self.root/'n0', self.root/'n1'
        shutil.copytree(EXAMPLE/'harness', self.n0)
        shutil.copytree(EXAMPLE/'meta-harness', self.n1)

    def test_new_n1_and_n0_require_real_nonempty_companion_document(self):
        for bundle, name in ((self.n0,'harness.json'), (self.n1,'meta-harness.json')):
            original = meta._snapshot(bundle)
            manifest = meta._json(original[name], name)
            for problem in ('no-reference','missing','empty','not-markdown','instruction-alias','skill-alias','escaping','invalid-encoding'):
                files, changed = dict(original), copy.deepcopy(manifest)
                if problem == 'no-reference':
                    del changed['design_rationale']
                elif problem == 'missing':
                    del files['DESIGN.md']
                elif problem == 'empty':
                    files['DESIGN.md'] = b' \n'
                elif problem == 'not-markdown':
                    files['note.txt'] = files['DESIGN.md']
                    changed['design_rationale'] = 'note.txt'
                elif problem == 'instruction-alias':
                    changed['design_rationale'] = changed['entrypoint']
                elif problem == 'skill-alias':
                    changed['design_rationale'] = changed['components'][0]['path']
                elif problem == 'escaping':
                    changed['design_rationale'] = '../outside.md'
                else:
                    files['DESIGN.md'] = b'\xff'
                files[name] = meta.canonical(changed)
                with self.subTest(level=manifest['level'], problem=problem), self.assertRaises(ValueError):
                    meta._validate_bundle(files)

    def test_structural_identity_does_not_claim_review_of_arguments(self):
        for bundle in (self.n0,self.n1):
            result = meta.check_bundle(bundle)
            self.assertEqual(result['design_rationale']['sha256'],meta.digest((bundle/'DESIGN.md').read_bytes()))
            self.assertEqual(result['design_rationale']['review_status'],'NOT_RUN')
            self.assertEqual(result['semantic_status'],'NOT_RUN')
        # Même une note insuffisante peut être présente : la pertinence demande une revue.
        (self.n0/'DESIGN.md').write_text('Justification insuffisante.\n')
        self.assertEqual(meta.check_bundle(self.n0)['design_rationale']['review_status'],'NOT_RUN')

    def test_legacy_05_bundles_are_not_backfilled_or_rewritten(self):
        for bundle,name in ((self.n0,'harness.json'),(self.n1,'meta-harness.json')):
            manifest=json.loads((bundle/name).read_text());manifest['schema_version']='0.5.0';del manifest['design_rationale']
            profile=json.loads((bundle/'profile.json').read_text());profile['schema_version']='0.5.0'
            write_json(bundle/name,manifest);write_json(bundle/'profile.json',profile)
            (bundle/'DESIGN.md').unlink()
            before=meta._snapshot(bundle)
            self.assertIsNone(meta.check_bundle(bundle)['design_rationale'])
            self.assertEqual(meta._snapshot(bundle),before)

    def test_preparation_exports_the_n2_note_and_its_hash_without_generating_n1(self):
        output=self.root/'prepared'
        meta.prepare(EXAMPLE/'brief.md',self.n0/'profile.json',output)
        raw=(ROOT/'meta/DESIGN.md').read_bytes()
        self.assertEqual((output/'meta/DESIGN.md').read_bytes(),raw)
        preparation=json.loads((output/'preparation.json').read_text())
        self.assertEqual(preparation['source_sha256']['meta/DESIGN.md'],meta.digest(raw))
        self.assertEqual(preparation['generation_status'],'NOT_RUN')
        self.assertFalse((output/'meta-harness.json').exists())

    def test_materialization_preserves_distinct_n1_n0_notes_and_metadata(self):
        n0raw=(self.n0/'DESIGN.md').read_bytes();n1raw=(self.n1/'DESIGN.md').read_bytes()
        self.assertNotEqual(n0raw,n1raw)
        result=meta.materialize(self.n0,self.root/'result',meta_harness=self.n1)[0]
        self.assertEqual((result/'DESIGN.md').read_bytes(),n0raw)
        self.assertEqual((result/'_eiffel/meta-harness/DESIGN.md').read_bytes(),n1raw)
        info=json.loads((result/'_eiffel/project.json').read_text())
        self.assertEqual(info['design_rationale']['sha256'],meta.digest(n0raw))
        self.assertEqual(info['generator_design_rationale']['sha256'],meta.digest(n1raw))
        self.assertEqual(info['design_rationale']['location'],{'role':'governance','path':'DESIGN.md'})
        self.assertEqual(info['source_sha256']['bundle/DESIGN.md'],meta.digest(n0raw))

    def test_four_repo_note_cannot_be_silently_dropped_and_location_resolves(self):
        manifest=json.loads((self.n0/'harness.json').read_text())
        manifest.pop('responsibilities');manifest.pop('entrypoint');manifest['layout']='four-repos'
        manifest['repositories']={role:role for role in meta.ROLES}
        manifest['components']=[]
        manifest['capabilities']=[{'role':role,'task':'Tâche de fixture '+role,'native':'Méthode de fixture dans AGENTS.md.'} for role in meta.ROLES]
        for role in meta.ROLES:
            directory=self.n0/role;directory.mkdir()
            (directory/'AGENTS.md').write_text('Instructions de fixture.\n')
            (directory/'README.md').write_text('Fixture, pas de génération réelle.\n')
        write_json(self.n0/'harness.json',manifest)
        with self.assertRaisesRegex(ValueError,'racine de rôle'):
            meta.materialize(self.n0,self.root/'refused')
        self.assertFalse((self.root/'refused').exists())
        (self.n0/'DESIGN.md').rename(self.n0/'governance/DESIGN.md')
        (self.n0/'governance/DESIGN.md').write_text(
            '# Décision de fixture\n\nLa note est conservée dans Gouvernance ; '
            'les [instructions](AGENTS.md) restent distinctes. Cette fixture teste la localisation, '
            'sans justifier une organisation réelle à quatre dépôts.\n')
        manifest['design_rationale']='governance/DESIGN.md';write_json(self.n0/'harness.json',manifest)
        repos=meta.materialize(self.n0,self.root/'result')
        for repo in repos:
            info=json.loads((repo/'_eiffel/project.json').read_text());ref=info['design_rationale']
            owner=info['repositories'][ref['location']['role']]['directory']
            actual=self.root/'result'/owner/ref['location']['path']
            self.assertEqual(meta.digest(actual.read_bytes()),ref['sha256'])
            self.assertEqual(check_markdown_tree(repo),[])

    def test_capture_binds_document_bytes_and_detects_later_tampering(self):
        record=self.root/'record.json';write_json(record,note())
        destination=self.root/'captured'
        seeds.capture(self.n0,record,destination)
        self.assertEqual((destination/'harness/DESIGN.md').read_bytes(),(self.n0/'DESIGN.md').read_bytes())
        self.assertEqual(seeds.check_catalog(destination)['artifacts_checked'],1)
        (destination/'harness/DESIGN.md').write_text('Autre compromis.\n')
        with self.assertRaisesRegex(ValueError,'empreinte'):
            seeds.check_catalog(destination)

    def test_mission_exposes_note_and_rejects_changed_justification(self):
        inputs={'source':EXAMPLE/'fixtures/source.csv','rules':EXAMPLE/'fixtures/rules.json'}
        order=self.root/'mission'
        receipt=skills.prepare(self.n0,'filter-rows','product',inputs,order)
        self.assertEqual(receipt['design_rationale'],'resources/DESIGN.md')
        self.assertEqual((order/receipt['design_rationale']).read_bytes(),(self.n0/'DESIGN.md').read_bytes())
        (self.n0/'DESIGN.md').write_text('Règle différente, non requalifiée.\n')
        self.assertEqual(skills.verify(order,receipt['order_sha256'])['validity_status'],'STALE')
        with self.assertRaisesRegex(ValueError,'STALE'):
            skills.handoff(order,'audit',{'candidate':EXAMPLE/'fixtures/wrong.csv'},self.root/'delivery',receipt['order_sha256'])
        self.assertFalse((self.root/'delivery').exists())

    def test_missing_note_blocks_materialization_before_any_publication(self):
        (self.n0/'DESIGN.md').unlink()
        with self.assertRaisesRegex(ValueError,'design_rationale'):
            meta.materialize(self.n0,self.root/'result',meta_harness=self.n1)
        self.assertFalse((self.root/'result').exists())


if __name__=='__main__':
    unittest.main()
