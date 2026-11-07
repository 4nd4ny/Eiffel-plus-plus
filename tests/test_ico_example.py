"""Behavioral qualification of the public workshop, using only fictional fixtures."""
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
EX = ROOT / 'examples/ico-0.6.0'
sys.path.insert(0, str(ROOT / 'tools'))
import meta_harness as meta
import skills
import trials


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


w = load(EX / 'N0/tools/workshop.py', 'ico_workshop')
gen = load(EX / 'N1/generate.py', 'ico_generate')
demo = load(EX / 'demo.py', 'ico_demo')


class ICOExampleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.lot = self.root / 'lot'

    def open(self, checker=None, code=None, contract=None):
        self.anchor = w.open_lot(meta, trials, EX / 'N0', code or EX / 'fixtures/code',
                                 checker or EX / 'fixtures/checker', contract or EX / 'fixtures/contract.json',
                                 self.lot)['anchor_sha256']

    def frozen(self):
        self.candidate = self.root / 'candidate'
        self.csha = w.freeze(meta, trials, self.lot, self.anchor, self.candidate)['candidate_sha256']

    def evals(self):
        b = w.evaluate(meta, trials, self.lot, self.anchor, self.root / 'base-eval')
        c = w.evaluate(meta, trials, self.lot, self.anchor, self.root / 'candidate-eval', self.candidate, self.csha)
        return b, c

    def choose(self, b, c):
        return w.compare(meta, trials, self.lot, self.anchor,
                         [(self.root / 'base-eval', b['evaluation_sha256']),
                          (self.root / 'candidate-eval', c['evaluation_sha256'])], self.root / 'choice')

    def test_equal_keeps_complete_reference_and_does_not_write_sources(self):
        before = w.tree(meta, EX)
        self.open(); self.frozen()
        self.assertEqual(self.choose(*self.evals())['outcome'], 'KEEP_BASE')
        self.assertEqual(w.tree(meta, self.root / 'choice/artifact'), w.tree(meta, EX / 'fixtures/code'))
        self.assertEqual(w.tree(meta, EX), before)

    def test_improvement_flows_through_actual_handoffs(self):
        def improve(code):
            p = code / 'normalize.py'; p.write_text(p.read_text().replace('v.strip()', 'v.strip().lower()'))
        result = demo.workflow(ROOT, EX / 'N0', EX / 'fixtures/code', EX / 'fixtures/checker',
                               EX / 'fixtures/contract.json', self.root / 'workflow', improve)
        self.assertEqual(result['outcome'], 'ADOPT')
        self.assertEqual(result['selected_files'], 2)
        self.assertEqual(len(result['missions']), 6)
        self.assertEqual(result['model_calls'], 0)
        # Receiver uses the delivered copy, not an unbound original document.
        receipt = w.read(self.root / 'workflow/mission-specifier-contrat/receipt.json')
        self.assertIn('remise-mission-orchestrer-lot', receipt['inputs']['mandate']['source'])

    def test_regression_cannot_be_compensated_by_score(self):
        self.open()
        p = self.lot / 'work/normalize.py'
        p.write_text('def normalize(values):\n    return ["a"]\n')
        self.frozen(); b, c = self.evals()
        self.assertEqual(c['status'], 'FAIL')
        self.assertEqual(c['assessment']['score'], 1)
        self.assertEqual(self.choose(b, c)['outcome'], 'KEEP_BASE')

    def test_no_valid_reference_or_candidate_is_inconclusive(self):
        code = self.root / 'invalid'; shutil.copytree(EX / 'fixtures/code', code)
        (code / 'normalize.py').write_text('def normalize(values):\n    return []\n')
        self.open(code=code); self.frozen()
        self.assertEqual(self.choose(*self.evals())['outcome'], 'INCONCLUSIVE')

    def test_partial_or_extra_oracle_criteria_are_unknown(self):
        checker = self.root / 'checker'; checker.mkdir()
        (checker / 'check.py').write_text('import json\nprint(json.dumps({"criteria":{"invalid-input":"PASS"},"score":99}))\n')
        self.open(checker=checker); self.frozen(); b, c = self.evals()
        self.assertEqual(b['status'], 'UNKNOWN')
        self.assertEqual(self.choose(b, c)['outcome'], 'INCONCLUSIVE')

    def test_missing_checker_dependency_is_unknown(self):
        checker = self.root / 'checker'; checker.mkdir()
        (checker / 'check.py').write_text('import nonexistent_dependency_ico_example\n')
        self.open(checker=checker); self.frozen(); b, c = self.evals()
        self.assertEqual(b['status'], 'UNKNOWN')
        self.assertEqual(self.choose(b, c)['outcome'], 'INCONCLUSIVE')

    def test_frozen_contract_roles_skills_rationale_and_controls_cannot_drift(self):
        self.open()
        for relative in ('contract.json', 'plan.md', 'harness/roles/product/AGENTS.md', 'harness/DESIGN.md',
                         'harness/skills/modifier-moteur/SKILL.md', 'checker/check.py',
                         'checker-bound.py', 'baseline/unrelated.txt'):
            with self.subTest(path=relative):
                p = self.lot / relative; original = p.read_bytes(); p.write_bytes(original + b'\nchanged\n')
                try:
                    with self.assertRaisesRegex(ValueError, 'STALE'):
                        w.freeze(meta, trials, self.lot, self.anchor, self.root / 'forbidden-candidate')
                    self.assertFalse((self.root / 'forbidden-candidate').exists())
                finally:
                    p.write_bytes(original)

    def test_receipt_rewrite_cannot_reanchor_itself(self):
        self.open()
        p = self.lot / 'receipt.json'; v = w.read(p); v['scope'] = 'pretend new authority'; w.write(p, v)
        with self.assertRaisesRegex(ValueError, 'STALE'):
            w.verify(meta, self.lot, self.anchor)

    def test_complete_candidate_tracks_unrelated_edits_additions_and_deletions(self):
        self.open(); self.frozen()
        p = self.candidate / 'code/unrelated.txt'; original = p.read_bytes()
        for mutation in ('edit', 'delete', 'add'):
            with self.subTest(mutation=mutation):
                if mutation == 'edit': p.write_text('changed')
                elif mutation == 'delete': p.unlink()
                else: (self.candidate / 'code/new.txt').write_text('extra')
                try:
                    with self.assertRaisesRegex(ValueError, 'STALE'):
                        w.verify(meta, self.lot, self.anchor, self.candidate, self.csha)
                finally:
                    p.write_bytes(original)
                    (self.candidate / 'code/new.txt').unlink(missing_ok=True)

    def test_links_and_overlapping_output_rejected_without_touching_source(self):
        code = self.root / 'linked'; shutil.copytree(EX / 'fixtures/code', code)
        (code / 'alias').symlink_to(code / 'normalize.py')
        with self.assertRaises(ValueError): self.open(code=code)
        self.assertFalse(self.lot.exists())
        with self.assertRaises(ValueError):
            w.open_lot(meta, trials, EX / 'N0', EX / 'fixtures/code', EX / 'fixtures/checker',
                       EX / 'fixtures/contract.json', EX / 'fixtures/code/nested-output')

    def test_selection_rejects_tampered_receipt_or_wrong_reference(self):
        self.open(); self.frozen(); b, c = self.evals()
        receipt = self.root / 'candidate-eval/receipt.json'; original = receipt.read_bytes()
        receipt.write_bytes(original + b'\n')
        with self.assertRaisesRegex(ValueError, 'STALE'): self.choose(b, c)
        receipt.write_bytes(original)
        (self.root / 'base-eval/artifact/unrelated.txt').write_text('altered')
        with self.assertRaisesRegex(ValueError, 'STALE'): self.choose(b, c)

    def test_modes_preserve_roles_and_remove_unused_production_skill(self):
        meta.check_bundle(EX / 'N1')
        for mode, removed in [('import', 'modifier-interface'), ('interface', 'modifier-moteur')]:
            dest = gen.generate(mode, self.root / mode)
            self.assertEqual(meta.check_bundle(dest)['structure_status'], 'PASS')
            listing = skills.catalogue(dest)
            self.assertEqual({c['role'] for c in listing['capabilities']}, set(meta.ROLES))
            self.assertNotIn(removed, {s['id'] for s in listing['skills']})
            self.assertTrue(any('unavailable' in c for c in listing['capabilities']))
            for q in range(1, 15): self.assertIn(f'Q{q:02}', (dest / 'QUALITE.md').read_text())
            self.assertIn('Choix de cette génération', (dest / 'DESIGN.md').read_text())

    def test_bad_assignment_recipient_and_rationale_drift_block_missions(self):
        bundle = self.root / 'bundle'; shutil.copytree(EX / 'N0', bundle)
        request = self.root / 'request'; request.write_text('local task')
        with self.assertRaises(ValueError):
            skills.prepare(bundle, 'orchestrer-lot', 'product', {'request': request}, self.root / 'wrong')
        order = self.root / 'order'
        receipt = skills.prepare(bundle, 'orchestrer-lot', 'governance', {'request': request}, order)
        anchor = receipt['order_sha256']
        with self.assertRaises(ValueError): skills.handoff(order, 'audit', {'mandate': request}, self.root / 'wrong-to', anchor)
        with self.assertRaises(ValueError): skills.handoff(order, 'stbl', {}, self.root / 'missing', anchor)
        (bundle / 'DESIGN.md').write_text('changed rationale')
        self.assertEqual(skills.verify(order, anchor)['validity_status'], 'STALE')
        with self.assertRaises(ValueError): skills.handoff(order, 'stbl', {'mandate': request}, self.root / 'stale', anchor)

    def test_materialization_keeps_both_level_rationales(self):
        repos = meta.materialize(EX / 'N0', self.root / 'materialized', meta_harness=EX / 'N1')
        metadata = w.read(repos[0] / '_eiffel/project.json')
        self.assertEqual(metadata['design_rationale']['sha256'], w.sha(EX / 'N0/DESIGN.md'))
        self.assertEqual(metadata['generator_design_rationale']['sha256'], w.sha(EX / 'N1/DESIGN.md'))


if __name__ == '__main__':
    unittest.main()
