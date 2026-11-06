from __future__ import annotations

import copy
import json
from pathlib import Path
import stat
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import meta_harness as meta
import seeds


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def note():
    return {
        "schema_version": "0.3.0", "id": "local-test", "kind": "local-example",
        "title": "Fixture de capture", "summary": "Aucun opérateur ou résultat réel.",
        "source": {"url": None, "revision": None, "paths": [], "license": "MIT",
                   "visibility": "local", "reviewed_on": "2026-11-06", "discovered_via": "Fixture de test"},
        "context": {"suitable_for": ["Test du copieur"], "avoid_when": [], "required_capabilities": [], "cost_notes": []},
        "recipe": ["Lire les besoins avant de proposer le travail."], "operator_questions": [],
        "evidence": {"level": "untested", "claims": [], "limitations": ["Fixture seulement"], "runs": []},
        "lineage": {"parents": []},
        "publication": {"status": "unreviewed", "contains_private_material": False},
        "review": {"status": "unreviewed", "decision_ref": None},
    }


class SeedTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.bundle = self.base / "n0"
        self.bundle.mkdir()
        self.profile = {
            "schema_version": "0.3.0",
            "project": {"slug": "test", "name": "Test", "brief": "Fixture locale."},
            "preferences": {"status": "PROPOSED", "source": "Fixture", "priorities": ["Garder une méthode courte."]},
            "constraints": [], "unknowns": [],
            "authority": {"mandate": "Fixture seulement", "autonomous_actions": [], "human_decisions": []},
            "generation_budget": {"max_candidates": 1, "max_iterations": 1, "max_tokens": None},
        }
        write_json(self.bundle / "profile.json", self.profile)
        write_json(self.bundle / "harness.json", {
            "schema_version": "0.3.0", "kind": "project-harness", "level": 0, "status": "PROPOSED",
            "profile": "profile.json", "generator": "Fixture directe", "layout": "single-repo",
            "entrypoint": "AGENTS.md", "responsibilities": {role: "AGENTS.md" for role in meta.ROLES},
        })
        (self.bundle / "AGENTS.md").write_text("# Méthode fictive\n", encoding="utf-8")
        self.script = self.bundle / "verify.sh"
        self.script.write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
        self.script.chmod(0o755)
        self.record = self.base / "note.json"
        write_json(self.record, note())

    def test_capture_preserves_declarations_and_checks_content_and_executable_bit(self):
        destination = self.base / "captured"
        result = seeds.capture(self.bundle, self.record, destination)
        captured = json.loads((destination / "record.json").read_text(encoding="utf-8"))
        for key, value in note().items():
            self.assertEqual(captured[key], value)
        self.assertEqual(result["authority_status"], "NOT_VERIFIED")
        self.assertEqual(seeds.check_catalog(destination)["artifacts_checked"], 1)
        copied = destination / "harness/verify.sh"
        self.assertEqual(stat.S_IMODE(copied.stat().st_mode), 0o755)
        self.script.write_text("Version source ultérieure\n", encoding="utf-8")
        self.assertIn("exit 0", copied.read_text(encoding="utf-8"))
        copied.chmod(0o644)
        with self.assertRaisesRegex(ValueError, "empreinte"):
            seeds.check_catalog(destination)
        copied.chmod(0o755)
        copied.write_text("Contenu modifié\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "empreinte"):
            seeds.check_catalog(destination)

    def test_private_extension_is_readable_but_cannot_enter_public_catalog(self):
        private = note()
        private["publication"] = {"status": "private", "contains_private_material": True}
        private["source"]["visibility"] = "private"
        catalog = self.base / "private-catalog"
        write_json(catalog / "records/private.json", private)
        self.assertEqual(seeds.check_catalog(catalog)["record_count"], 1)
        with self.assertRaisesRegex(ValueError, "public"):
            seeds.check_catalog(catalog, require_public=True)
        write_json(self.record, private)
        public = self.base / "public-catalog"
        with patch.object(seeds, "DEFAULT_CATALOG", public):
            with self.assertRaisesRegex(ValueError, "public"):
                seeds.capture(self.bundle, self.record, public / "instances/new")
        self.assertFalse(public.exists())
        result = seeds.capture(self.bundle, self.record, self.base / "private-copy")
        self.assertEqual(result["review_status"], "unreviewed")

    def test_human_review_and_observation_labels_require_references_without_authentication(self):
        for level in ("local-observation", "comparison"):
            invalid = note()
            invalid["evidence"]["level"] = level
            with self.subTest(level=level), self.assertRaisesRegex(ValueError, "runs"):
                seeds.validate_record(invalid)
        declared = note()
        declared["kind"] = "co-designed-instance"
        declared["review"]["status"] = "co-designed"
        with self.assertRaisesRegex(ValueError, "decision_ref"):
            seeds.validate_record(declared)
        declared["review"]["decision_ref"] = "Fixture de référence, non authentifiée"
        before = copy.deepcopy(declared)
        seeds.validate_record(declared)
        self.assertEqual(declared, before)

    def test_capture_neither_overwrites_nor_follows_source_symlinks(self):
        destination = self.base / "existing"
        destination.mkdir()
        sentinel = destination / "keep.txt"
        sentinel.write_text("Conserver", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            seeds.capture(self.bundle, self.record, destination)
        self.assertEqual(sentinel.read_text(encoding="utf-8"), "Conserver")
        (self.bundle / "linked").symlink_to(self.record)
        with self.assertRaises(ValueError):
            seeds.capture(self.bundle, self.record, self.base / "unsafe")
        self.assertFalse((self.base / "unsafe").exists())

    def test_catalog_reports_unknown_parents_and_rejects_duplicate_ids_or_escaping_artifacts(self):
        catalog = self.base / "catalog"
        item = note()
        item["lineage"]["parents"] = ["another-catalog-parent"]
        write_json(catalog / "records/item.json", item)
        self.assertEqual(seeds.check_catalog(catalog)["unresolved_parents"], {"local-test": ["another-catalog-parent"]})
        write_json(catalog / "records/duplicate.json", item)
        with self.assertRaisesRegex(ValueError, "répété"):
            seeds.check_catalog(catalog)
        item["artifact"] = {"path": "../outside", "sha256": "0" * 64, "format": seeds.ARTIFACT_FORMAT}
        with self.assertRaises(ValueError):
            seeds.validate_record(item)

    def test_preparation_loads_only_selected_records_and_marks_private_context(self):
        catalog = self.base / "catalog"
        selected = note()
        selected["publication"] = {"status": "private", "contains_private_material": True}
        selected["source"]["visibility"] = "private"
        # A valid artifact reference is data only. This directory deliberately does not exist.
        selected["artifact"] = {"path": "unavailable-runtime", "sha256": "0" * 64, "format": seeds.ARTIFACT_FORMAT}
        write_json(catalog / "records/selected.json", selected)
        other = note()
        other["id"] = "unused"
        write_json(catalog / "records/other.json", other)
        brief = self.base / "brief.md"
        brief.write_text("# Besoin de test\n", encoding="utf-8")
        destination = self.base / "prepared"
        meta.prepare(brief, self.bundle / "profile.json", destination, ("local-test",), catalog)
        self.assertEqual((destination / "context/seeds/local-test.json").read_bytes(), (catalog / "records/selected.json").read_bytes())
        self.assertFalse((destination / "context/seeds/unused.json").exists())
        self.assertFalse((destination / "unavailable-runtime").exists())
        info = json.loads((destination / "preparation.json").read_text(encoding="utf-8"))
        self.assertEqual(info["publication_status"], "private")
        self.assertEqual(info["selected_seed_ids"], ["local-test"])
        self.assertFalse(info["seed_artifacts_loaded"])
        self.assertEqual(info["generation_status"], "NOT_RUN")


if __name__ == "__main__":
    unittest.main()
