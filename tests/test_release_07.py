"""Compatibilité de paquets et préparation autonome du parcours 0.7."""
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import meta_harness as meta
from check_catalog import check_markdown_tree


class Release07Tests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.example = ROOT / "examples/ico-0.6.0"

    def test_06_and_07_preserve_skills_and_require_design(self):
        for version in ("0.6.0", "0.7.0"):
            for folder, manifest_name in (("N0", "harness.json"), ("N1", "meta-harness.json")):
                bundle = self.root / (folder + version)
                shutil.copytree(self.example / folder, bundle)
                for name in (manifest_name, "profile.json"):
                    path = bundle / name
                    value = json.loads(path.read_text())
                    value["schema_version"] = version
                    path.write_bytes(meta.canonical(value))
                with self.subTest(version=version, level=folder):
                    result = meta.check_bundle(bundle)
                    self.assertEqual(result["structure_status"], "PASS")
                    self.assertIsNotNone(result["design_rationale"])
                    path = bundle / manifest_name
                    value = json.loads(path.read_text())
                    del value["design_rationale"]
                    path.write_bytes(meta.canonical(value))
                    with self.assertRaisesRegex(ValueError, "design_rationale"):
                        meta.check_bundle(bundle)

    def test_preparation_keeps_requested_path_and_resolves_links(self):
        for mode in (None, "cascade", "direct"):
            destination = self.root / str(mode)
            meta.prepare(self.example / "N2/BRIEF.md", self.example / "N2/profile.json", destination, mode=mode)
            info = json.loads((destination / "preparation.json").read_text())
            self.assertEqual(info["requested_mode"], mode)
            self.assertEqual(info["generation_status"], "NOT_RUN")
            for name in ("HISTORY.md", "REFERENCES.md"):
                source = (ROOT / "docs" / name).read_bytes()
                self.assertEqual((destination / "docs" / name).read_bytes(), source)
                self.assertEqual(info["source_sha256"]["docs/" + name], meta.digest(source))
            self.assertEqual(check_markdown_tree(destination), [])
            start = (destination / "START.md").read_text()
            if mode == "cascade":
                self.assertIn("Parcours demandé : cascade", start)
                self.assertNotIn("N1 reste facultatif", start)
            elif mode == "direct":
                self.assertIn("Parcours demandé : N0 direct", start)

    def test_invalid_path_is_rejected_without_creating_destination(self):
        destination = self.root / "invalid"
        with self.assertRaises(ValueError):
            meta.prepare(self.example / "N2/BRIEF.md", self.example / "N2/profile.json", destination, mode="automatic")
        self.assertFalse(destination.exists())


if __name__ == "__main__":
    unittest.main()
