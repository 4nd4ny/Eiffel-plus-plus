from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import meta_harness as meta


def profile():
    return {
        "schema_version": "0.2.0",
        "project": {"slug": "demonstration", "name": "Démonstration", "brief": "Cas fictif de test."},
        "preferences": {
            "status": "PROPOSED", "source": "Fixture de test, sans décision du PO.",
            "weights": {"speed": 0.4, "economy": 0.2, "scope": 0.3, "autonomy": 0.1},
            "measures": {
                axis: {"metric": axis, "unit": "unité de test", "direction": "maximize" if axis == "scope" else "minimize", "target": None}
                for axis in meta.AXES
            },
        },
        "constraints": [{"id": "TEST-01", "statement": "Ne pas modifier les oracles.", "verification": "Essai contrôlé."}],
        "authority": {"mandate": "Fixture seulement", "autonomous_actions": [], "human_decisions": ["Adopter le besoin"]},
        "unknowns": [],
        "generation_budget": {"max_candidates": 2, "max_iterations": 2, "max_tokens": None},
    }


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class MetaHarnessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.n1 = self.base / "n1"
        self.n0 = self.base / "n0"
        self.n1.mkdir()
        self.n0.mkdir()
        write_json(self.n1 / "profile.json", profile())
        write_json(self.n0 / "profile.json", profile())
        (self.n1 / "prompts").mkdir()
        for prompt in ("GENERATE", "CHECK", "ADAPT"):
            (self.n1 / "prompts" / f"{prompt}.md").write_text(f"# {prompt}\n\nInstruction fictive.\n", encoding="utf-8")
        (self.n1 / "GENERATION_CONTRACT.md").write_text("# Contrat\n\nConserver les responsabilités.\n", encoding="utf-8")
        self.generator = {
            "schema_version": "0.2.0", "kind": "meta-harness", "level": 1, "status": "PROPOSED",
            "profile": "profile.json", "entrypoint": "prompts/GENERATE.md",
            "prompts": [f"prompts/{name}.md" for name in ("GENERATE", "CHECK", "ADAPT")],
            "output_contract": "GENERATION_CONTRACT.md", "source_pattern": "Eiffel++ 0.2.0",
        }
        write_json(self.n1 / "meta-harness.json", self.generator)
        self.harness = {
            "schema_version": "0.2.0", "kind": "project-harness", "level": 0, "status": "PROPOSED",
            "profile": "profile.json", "generator": "Référence déclarée au N1 de test",
            "repositories": {role: role for role in meta.ROLES},
        }
        write_json(self.n0 / "harness.json", self.harness)
        for role in meta.ROLES:
            folder = self.n0 / role
            folder.mkdir()
            (folder / "AGENTS.md").write_text(f"# Agent {role}\n\nMéthode spécifique {role}.\n", encoding="utf-8")
            (folder / "README.md").write_text(f"# Dépôt {role}\n\nExemple généré fictif.\n", encoding="utf-8")

    def test_tetrahedron_rejects_invalid_weights_without_normalization(self):
        valid = profile()
        before = copy.deepcopy(valid)
        meta.validate_profile(valid)
        self.assertEqual(valid, before)
        for value in (-0.1, 1.1, True, float("nan"), float("inf"), "0.4", 10 ** 400):
            invalid = profile()
            invalid["preferences"]["weights"]["speed"] = value
            with self.subTest(value=repr(value)), self.assertRaises(ValueError):
                meta.validate_profile(invalid)
        invalid = profile()
        invalid["preferences"]["weights"]["speed"] = 0.3
        with self.assertRaisesRegex(ValueError, "somme"):
            meta.validate_profile(invalid)

    def test_qualitative_priorities_need_neither_weights_nor_four_measurements(self):
        qualitative = profile()
        qualitative["schema_version"] = "0.3.0"
        preferences = qualitative["preferences"]
        preferences.pop("weights")
        preferences.pop("measures")
        preferences["priorities"] = ["Préserver les données avant d'ajouter une option."]
        original = copy.deepcopy(qualitative)
        meta.validate_profile(qualitative)
        self.assertEqual(qualitative, original)
        preferences["measures"] = {"autonomy": {"metric": "human_minutes", "unit": "minutes", "direction": "minimize"}}
        meta.validate_profile(qualitative)
        preferences["priorities"] = []
        with self.assertRaises(ValueError):
            meta.validate_profile(qualitative)
        preferences["priorities"] = ["Préserver les données."]
        preferences["weights"] = {axis: 0.1 for axis in meta.AXES}
        with self.assertRaisesRegex(ValueError, "somme"):
            meta.validate_profile(qualitative)

    def test_structural_check_never_claims_semantic_or_authority_validation(self):
        for bundle in (self.n1, self.n0):
            result = meta.check_bundle(bundle)
            self.assertEqual(result["structure_status"], "PASS")
            self.assertEqual(result["semantic_status"], "NOT_RUN")
            self.assertEqual(result["authority_status"], "NOT_RUN")
            self.assertEqual(result["declared_status"], "PROPOSED")
        self.generator["entrypoint"] = "GENERATION_CONTRACT.md"
        write_json(self.n1 / "meta-harness.json", self.generator)
        with self.assertRaisesRegex(ValueError, "entrypoint"):
            meta.check_bundle(self.n1)

    def test_paths_cannot_escape_and_repositories_cannot_overlap(self):
        for invalid in ("../outside", "/absolute", "C:\\outside", "folder//role", "folder/./role", "folder/_eiffel", "folder/.git"):
            manifest = copy.deepcopy(self.harness)
            manifest["repositories"]["product"] = invalid
            write_json(self.n0 / "harness.json", manifest)
            with self.subTest(path=invalid), self.assertRaises(ValueError):
                meta.check_bundle(self.n0)
        for invalid in ("governance", "governance/subdirectory"):
            manifest = copy.deepcopy(self.harness)
            manifest["repositories"]["product"] = invalid
            write_json(self.n0 / "harness.json", manifest)
            with self.subTest(path=invalid), self.assertRaisesRegex(ValueError, "non imbriqués"):
                meta.check_bundle(self.n0)

    def test_symlink_sources_are_rejected_even_when_not_in_manifest(self):
        external = self.base / "external.txt"
        external.write_text("Ne pas copier.", encoding="utf-8")
        (self.n0 / "product" / "linked.md").symlink_to(external)
        with self.assertRaises(ValueError):
            meta.materialize(self.n0, self.base / "result")
        self.assertFalse((self.base / "result").exists())

    def test_materialization_preserves_custom_files_profile_and_generator(self):
        # JSON formatting differs; the declared profile content is identical.
        (self.n1 / "profile.json").write_bytes(meta.canonical(profile()))
        original_prompt = (self.n1 / "prompts/GENERATE.md").read_bytes()
        repos = meta.materialize(self.n0, self.base / "result", meta_harness=self.n1)
        self.assertEqual({repo.name for repo in repos}, {f"demonstration-{r}" for r in meta.ROLES})
        for repo in repos:
            role = repo.name.removeprefix("demonstration-")
            self.assertEqual((repo / "AGENTS.md").read_bytes(), (self.n0 / role / "AGENTS.md").read_bytes())
            self.assertEqual((repo / "_eiffel/profile.json").read_bytes(), (self.n0 / "profile.json").read_bytes())
            info = json.loads((repo / "_eiffel/project.json").read_text(encoding="utf-8"))
            self.assertEqual(info["binding_status"], "UNBOUND")
            self.assertTrue(all(v["commit"] is None and v["remote"] is None for v in info["repositories"].values()))
            self.assertTrue(info["generator_snapshot_present"])
            self.assertEqual(info["semantic_status"], "NOT_RUN")
            self.assertEqual(info["source_sha256"]["bundle/harness.json"], hashlib.sha256((self.n0 / "harness.json").read_bytes()).hexdigest())
            protocol = (repo / "_eiffel/protocol/README.md").read_bytes()
            self.assertEqual(info["source_sha256"]["protocol/README.md"], hashlib.sha256(protocol).hexdigest())
            self.assertEqual((repo / "_eiffel/meta-harness").exists(), role == "governance")
            self.assertEqual((repo / "_eiffel/meta").exists(), role == "governance")
            self.assertEqual(info["pattern_snapshot_purpose"], "available-for-regeneration")
            self.assertEqual(info["pattern_generation_provenance_status"], "NOT_RUN")
            if role == "governance":
                pattern = (repo / "_eiffel/meta/START.md").read_bytes()
                self.assertEqual(pattern, (ROOT / "meta/START.md").read_bytes())
                self.assertEqual(info["pattern_source_sha256"]["START.md"], hashlib.sha256(pattern).hexdigest())
        saved = self.base / "result/demonstration-governance/_eiffel/meta-harness/prompts/GENERATE.md"
        (self.n1 / "prompts/GENERATE.md").write_text("Version ultérieure", encoding="utf-8")
        self.assertEqual(saved.read_bytes(), original_prompt)

    def test_scripts_remain_executable_without_copying_special_permission_bits(self):
        source = self.n0 / "product" / "verify.sh"
        source.write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
        source.chmod(0o4755)
        private_note = self.n0 / "product" / "local-note.md"
        private_note.write_text("Fixture locale, sans donnée réelle.\n", encoding="utf-8")
        private_note.chmod(0o600)
        repos = meta.materialize(self.n0, self.base / "mode-result")
        product = next(repo for repo in repos if repo.name.endswith("-product"))
        self.assertEqual((product / "verify.sh").read_bytes(), source.read_bytes())
        self.assertEqual(stat.S_IMODE((product / "verify.sh").stat().st_mode), 0o755)
        self.assertEqual(stat.S_IMODE((product / "local-note.md").stat().st_mode), 0o600)

    def test_one_repository_can_hold_four_responsibilities_without_n1_or_n2_copy(self):
        single = self.base / "single"
        single.mkdir()
        current_profile = profile()
        current_profile["schema_version"] = "0.3.0"
        write_json(single / "profile.json", current_profile)
        for filename in ("AGENTS.md", "SPEC.md", "CHECKS.md"):
            (single / filename).write_text(f"# {filename}\n\nFixture de méthode directe.\n", encoding="utf-8")
        manifest = {
            "schema_version": "0.3.0", "kind": "project-harness", "level": 0,
            "status": "PROPOSED", "profile": "profile.json", "generator": "Conception directe fictive",
            "layout": "single-repo", "entrypoint": "AGENTS.md",
            "responsibilities": {"governance": "AGENTS.md", "stbl": "SPEC.md", "audit": "CHECKS.md", "product": "AGENTS.md"},
        }
        write_json(single / "harness.json", manifest)
        self.assertEqual(meta.check_bundle(single)["layout"], "single-repo")
        repos = meta.materialize(single, self.base / "single-output", git_init=bool(shutil.which("git")))
        self.assertEqual([p.name for p in repos], ["demonstration"])
        repo = repos[0]
        self.assertFalse((repo / "_eiffel/meta").exists())
        self.assertFalse((repo / "_eiffel/meta-harness").exists())
        self.assertEqual((repo / "AGENTS.md").read_bytes(), (single / "AGENTS.md").read_bytes())
        info = json.loads((repo / "_eiffel/project.json").read_text(encoding="utf-8"))
        self.assertFalse(info["pattern_snapshot_present"])
        self.assertFalse(info["generator_snapshot_present"])
        self.assertEqual(info["semantic_status"], "NOT_RUN")
        self.assertEqual({r["directory"] for r in info["repositories"].values()}, {"demonstration"})
        if shutil.which("git"):
            result = subprocess.run(["git", "-C", str(repo), "rev-parse", "--show-toplevel"], check=True, capture_output=True, text=True)
            self.assertEqual(Path(result.stdout.strip()).resolve(), repo)
            self.assertEqual(len(list((self.base / "single-output").rglob(".git"))), 1)
        manifest["responsibilities"]["audit"] = "../private.md"
        write_json(single / "harness.json", manifest)
        with self.assertRaises(ValueError):
            meta.check_bundle(single)

    def test_mismatched_profiles_and_inactive_generators_block_materialization(self):
        changed = profile()
        changed["preferences"]["weights"].update(speed=0.5, economy=0.1)
        write_json(self.n1 / "profile.json", changed)
        with self.assertRaisesRegex(ValueError, "profils N1 et N0 diffèrent"):
            meta.materialize(self.n0, self.base / "result", meta_harness=self.n1)
        self.assertFalse((self.base / "result").exists())
        write_json(self.n1 / "profile.json", profile())
        for status in ("REJECTED", "SUPERSEDED"):
            self.generator["status"] = status
            write_json(self.n1 / "meta-harness.json", self.generator)
            with self.subTest(status=status), self.assertRaisesRegex(ValueError, "N1 rejeté ou remplacé"):
                meta.materialize(self.n0, self.base / "result", meta_harness=self.n1)
            self.assertFalse((self.base / "result").exists())

    def test_generator_reference_is_never_followed_implicitly(self):
        self.harness["generator"] = "../../private-meta-harness"
        write_json(self.n0 / "harness.json", self.harness)
        repos = meta.materialize(self.n0, self.base / "result")
        for repo in repos:
            info = json.loads((repo / "_eiffel/project.json").read_text(encoding="utf-8"))
            self.assertFalse(info["generator_snapshot_present"])
            self.assertIsNone(info["generator_snapshot_sha256"])
            self.assertFalse((repo / "_eiffel/meta-harness").exists())

    def test_existing_destinations_and_publication_races_never_overwrite(self):
        destination = self.base / "result"
        destination.mkdir()
        sentinel = destination / "valuable.txt"
        sentinel.write_text("Conserver.", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            meta.materialize(self.n0, destination)
        self.assertEqual(sentinel.read_text(encoding="utf-8"), "Conserver.")
        # Simulate a directory created between preparation and publication.
        staging = self.base / "staging"
        staging.mkdir()
        (staging / "marker.json").write_text("{}", encoding="utf-8")
        empty_rival = self.base / "created-concurrently"
        empty_rival.mkdir()
        with self.assertRaises(FileExistsError):
            meta._publish(staging, empty_rival, "marker.json")
        self.assertEqual(list(empty_rival.iterdir()), [])
        self.assertTrue((staging / "marker.json").is_file())

    def test_preparation_is_only_an_input_packet_and_preserves_sources(self):
        catalogue = self.base / "catalogue"
        (catalogue / "meta").mkdir(parents=True)
        (catalogue / "protocol").mkdir()
        (catalogue / "meta/START.md").write_text("# Générer N1\n", encoding="utf-8")
        (catalogue / "protocol/README.md").write_text("# Contrat\n", encoding="utf-8")
        brief = self.base / "brief.md"
        brief.write_text("# Projet de test\n", encoding="utf-8")
        destination = self.base / "prepared"
        with patch.object(meta, "ROOT", catalogue):
            meta.prepare(brief, self.n0 / "profile.json", destination)
        self.assertTrue((destination / "START.md").is_file())
        self.assertTrue((destination / "meta/START.md").is_file())
        self.assertFalse((destination / "meta-harness.json").exists())
        self.assertFalse((destination / "harness.json").exists())
        result = json.loads((destination / "preparation.json").read_text(encoding="utf-8"))
        self.assertEqual(result["generation_status"], "NOT_RUN")
        self.assertEqual(result["source_sha256"]["BRIEF.md"], hashlib.sha256(brief.read_bytes()).hexdigest())

    @unittest.skipUnless(shutil.which("git"), "Git indisponible")
    def test_four_git_roots_have_neither_commits_nor_remotes(self):
        repos = meta.materialize(self.n0, self.base / "git-result", git_init=True, meta_harness=self.n1)
        for repo in repos:
            result = subprocess.run(["git", "-C", str(repo), "rev-parse", "--show-toplevel"], check=True, capture_output=True, text=True)
            self.assertEqual(Path(result.stdout.strip()).resolve(), repo)
            remotes = subprocess.run(["git", "-C", str(repo), "remote"], check=True, capture_output=True, text=True)
            self.assertEqual(remotes.stdout.strip(), "")
            head = subprocess.run(["git", "-C", str(repo), "rev-parse", "--verify", "HEAD"], capture_output=True, text=True)
            self.assertNotEqual(head.returncode, 0)


if __name__ == "__main__":
    unittest.main()
