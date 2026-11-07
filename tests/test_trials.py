import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import meta_harness as meta
import trials


CHECKER = '''import json,sys
from pathlib import Path
value=int((Path(sys.argv[1])/'value.txt').read_text())
print(json.dumps({'criteria':{'nonnegative':'PASS' if value>=0 else 'FAIL'},'score':max(value,0)}))
'''


class TrialTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.bundle = self.root / "bundle"
        shutil.copytree(ROOT / "examples/observed-adaptation/harness", self.bundle)
        self.checker = self.root / "checker.py"
        self.checker.write_text(CHECKER)

    def evaluate(self, name, value, checker=None):
        source = self.root / name
        source.mkdir()
        (source / "value.txt").write_text(str(value))
        dest = self.root / (name + "-evaluation")
        trials.evaluate(source, checker or self.checker, dest)
        return dest

    def test_presence_is_not_activation_and_text_is_not_automatically_executed(self):
        self.assertEqual(meta.check_bundle(self.bundle)["level"], 0)
        self.assertFalse((self.root / "probe").exists())
        self.assertEqual(trials.check_probe(self.bundle, self.root / "probe")["activation_status"], "NOT_RUN")
        with self.assertRaisesRegex(ValueError, "procédure"):
            trials.probe(self.bundle, "csv-procedure", self.root / "probe")
        self.assertFalse((self.root / "probe").exists())

    def test_probe_binds_executed_bytes_and_does_not_modify_source(self):
        script = self.bundle / "scripts/verify_csv.py"
        script.write_text("from pathlib import Path\nPath('activated.txt').write_text('yes')\n")
        before = meta._snapshot(self.bundle)
        output = self.root / "probe"
        receipt = trials.probe(self.bundle, "csv-check", output)
        self.assertEqual(receipt["activation_status"], "PASS")
        self.assertEqual(receipt["execution"]["status"], "PASS")
        self.assertEqual(receipt["behavior_status"], "NOT_RUN")
        self.assertEqual((output / "work/activated.txt").read_text(), "yes")
        self.assertEqual(before, meta._snapshot(self.bundle))
        self.assertEqual(trials.check_probe(self.bundle, output)["activation_status"], "PASS")
        script.write_text("print('different')\n")
        self.assertEqual(trials.check_probe(self.bundle, output)["activation_status"], "STALE")

    def test_compile_error_does_not_claim_activation(self):
        (self.bundle / "scripts/verify_csv.py").write_text("this is not valid python !!!\n")
        result = trials.probe(self.bundle, "csv-check", self.root / "probe")
        self.assertEqual(result["activation_status"], "UNKNOWN")
        self.assertEqual(result["execution"]["status"], "FAIL")

    def test_runtime_error_and_timeout_do_not_claim_functional_success(self):
        script = self.bundle / "scripts/verify_csv.py"
        for name, body, expected in [("error", "raise RuntimeError('broken')", "FAIL"),
                                     ("timeout", "import time\ntime.sleep(10)", "UNKNOWN")]:
            script.write_text(body)
            result = trials.probe(self.bundle, "csv-check", self.root / name, timeout=0.3)
            self.assertEqual(result["activation_status"], "PASS")
            self.assertEqual(result["execution"]["status"], expected)

    def test_keeps_passing_reference_against_regression_or_tie(self):
        base = self.evaluate("base", 5)
        for name, value in [("regression", -1), ("tie", 5), ("lower", 4)]:
            candidate = self.evaluate(name, value)
            result = trials.select(base, [candidate], self.root / (name + "-selected"))
            self.assertEqual(result["outcome"], "KEEP_BASE")
            self.assertEqual((self.root / (name + "-selected/artifact/value.txt")).read_text(), "5")

    def test_adopts_proven_gain_and_never_falls_back_to_invalid_baseline(self):
        base = self.evaluate("base", -1)
        good = self.evaluate("good", 2)
        bad = self.evaluate("bad", -2)
        result = trials.select(base, [good], self.root / "adopt")
        self.assertEqual(result["outcome"], "ADOPT")
        self.assertEqual((self.root / "adopt/artifact/value.txt").read_text(), "2")
        result = trials.select(base, [bad], self.root / "none")
        self.assertEqual(result["outcome"], "INCONCLUSIVE")
        self.assertFalse((self.root / "none/artifact").exists())

    def test_modified_artifact_or_checker_invalidates_selection(self):
        base = self.evaluate("base", 1)
        candidate = self.evaluate("candidate", 2)
        (candidate / "artifact/value.txt").write_text("-100")
        with self.assertRaisesRegex(ValueError, "Artefact modifié"):
            trials.select(base, [candidate], self.root / "selected")
        (candidate / "artifact/value.txt").write_text("2")
        (candidate / "checker.py").write_text("print('fake')")
        with self.assertRaisesRegex(ValueError, "Vérificateur modifié"):
            trials.select(base, [candidate], self.root / "selected")

    def test_checker_crash_or_missing_json_is_unknown_not_a_zero_score(self):
        base = self.evaluate("base", 1)
        for name, body in [("crash", "raise RuntimeError()"), ("empty", "print('PASS')")]:
            checker = self.root / (name + ".py")
            checker.write_text(body)
            result_dir = self.evaluate(name, 3, checker)
            result = meta._json((result_dir / "receipt.json").read_bytes(), "result")
            self.assertEqual(result["status"], "UNKNOWN")
            self.assertIsNone(result["assessment"])
            with self.assertRaisesRegex(ValueError, "même vérificateur"):
                trials.select(base, [result_dir], self.root / (name + "-selected"))

    def test_checker_cannot_repair_artifact_and_claim_it_was_evaluated_unchanged(self):
        self.checker.write_text("import sys,json\nfrom pathlib import Path\n"
                               "(Path(sys.argv[1])/'value.txt').write_text('10')\n"
                               "print(json.dumps({'criteria':{'ok':'PASS'},'score':1}))\n")
        result_dir = self.evaluate("changed", -1)
        receipt = meta._json((result_dir / "receipt.json").read_bytes(), "result")
        self.assertEqual(receipt["status"], "STALE")

    def test_forged_success_label_does_not_override_checker_output(self):
        base = self.evaluate("base", 1)
        candidate = self.evaluate("candidate", -1)
        receipt = meta._json((candidate / "receipt.json").read_bytes(), "result")
        receipt["status"] = "PASS"
        receipt["assessment"] = {"criteria": {"nonnegative": "PASS"}, "score": 100}
        (candidate / "receipt.json").write_bytes(meta.canonical(receipt))
        with self.assertRaisesRegex(ValueError, "différente"):
            trials.select(base, [candidate], self.root / "selected")

    def test_destinations_are_exclusive_and_cannot_be_inside_sources(self):
        base = self.evaluate("base", 1)
        with self.assertRaises(FileExistsError):
            trials.select(base, [], base)
        with self.assertRaises(ValueError):
            trials.select(base, [], base / "child")
        with self.assertRaises(ValueError):
            trials.probe(self.bundle, "csv-check", self.bundle / "child")


if __name__ == "__main__":
    unittest.main()
