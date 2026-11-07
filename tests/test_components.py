import copy
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import components
import meta_harness as meta


class ComponentTests(unittest.TestCase):
    def setUp(self):
        self.files = meta._snapshot(ROOT / "examples/observed-adaptation/harness")
        self.manifest = meta._json(self.files["harness.json"], "fixture")

    def test_optional_contracts_do_not_require_new_layout_or_promote_evidence(self):
        self.assertEqual(components.validate_components(self.files, self.manifest), 2)
        self.assertTrue(components.validate_experience(self.files, self.manifest))
        self.assertEqual(meta.check_bundle(ROOT / "examples/forge-local/harness")["level"], 0)
        record = meta._json(self.files["EXPERIENCE.json"], "fixture")
        self.assertEqual(record["decision"]["outcome"], "INCONCLUSIVE")

    def test_component_missing_or_escaping_dependency_is_rejected(self):
        for dep in ("missing.py", "../outside.py"):
            changed = copy.deepcopy(self.manifest)
            changed["components"][0]["dependencies"] = [dep]
            with self.subTest(dep=dep), self.assertRaises(ValueError):
                components.validate_components(self.files, changed)

    def test_duplicate_component_and_non_python_script_are_rejected(self):
        duplicate = copy.deepcopy(self.manifest)
        duplicate["components"].append(duplicate["components"][0])
        with self.assertRaises(ValueError):
            components.validate_components(self.files, duplicate)
        invalid = copy.deepcopy(self.manifest)
        invalid["components"][1]["path"] = "AGENTS.md"
        with self.assertRaises(ValueError):
            components.validate_components(self.files, invalid)

    def test_proposed_adaptation_requires_resolvable_observation(self):
        changed = dict(self.files)
        del changed["SITUATION.md"]
        with self.assertRaises(ValueError):
            components.validate_experience(changed, self.manifest)

    def test_inconclusive_runs_cannot_be_promoted_by_decision_label(self):
        item = meta._json(self.files["EXPERIENCE.json"], "fixture")
        item["decision"].update(outcome="ADOPT", selected_run="candidate")
        changed = dict(self.files, **{"EXPERIENCE.json": meta.canonical(item)})
        with self.assertRaisesRegex(ValueError, "PASS"):
            components.validate_experience(changed, self.manifest)

    def test_unknown_costs_stay_unknown_invalid_costs_are_rejected(self):
        item = meta._json(self.files["EXPERIENCE.json"], "fixture")
        self.assertIsNone(item["runs"][0]["costs"]["usd"])
        for value in (-1, True, float("inf"), "0"):
            changed = copy.deepcopy(item)
            changed["runs"][0]["costs"]["usd"] = value
            # Serialize inf deliberately to test the strict JSON reader too.
            files = dict(self.files, **{"EXPERIENCE.json": json.dumps(changed).encode()})
            with self.subTest(value=value), self.assertRaises(ValueError):
                components.validate_experience(files, self.manifest)

    def test_bundle_check_covers_component_files_and_experience(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "bundle"
            shutil.copytree(ROOT / "examples/observed-adaptation/harness", root)
            name, manifest, profile = meta._validate_bundle(meta._snapshot(root))
            self.assertEqual(name, "harness.json")
            self.assertEqual(profile["schema_version"], "0.4.0")
            self.assertEqual(manifest["experience"], "EXPERIENCE.json")
            (root / "scripts/verify_csv.py").unlink()
            with self.assertRaises(ValueError):
                meta.check_bundle(root)


if __name__ == "__main__":
    unittest.main()
