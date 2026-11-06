from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from check_catalog import check_markdown_tree
from instantiate import ROLES, instantiate


class InstantiateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)

    def test_four_standalone_repositories_with_resolved_context(self):
        output = self.base / "project"
        repos = instantiate("atelier", "Atelier de démonstration", output, False)
        self.assertEqual({p.name for p in repos}, {f"atelier-{r}" for r in ROLES})
        for repo in repos:
            self.assertTrue((repo / "AGENTS.md").is_file())
            self.assertEqual(check_markdown_tree(repo), [])
            for path in repo.rglob("*.md"):
                self.assertNotIn("{{", path.read_text(encoding="utf-8"), str(path))
            metadata = json.loads((repo / "_eiffel/project.json").read_text(encoding="utf-8"))
            self.assertEqual(metadata["binding_status"], "UNBOUND")
            self.assertTrue(all(value["commit"] is None and value["remote"] is None for value in metadata["repositories"].values()))
            snapshot = (repo / "_eiffel/protocol/README.md").read_bytes()
            self.assertEqual(hashlib.sha256(snapshot).hexdigest(), metadata["source_sha256"]["protocol/README.md"])
            self.assertEqual(metadata["generation_mode"], "generic-components")
            if metadata["role"] == "governance":
                pattern = (repo / "_eiffel/meta/START.md").read_bytes()
                self.assertEqual(hashlib.sha256(pattern).hexdigest(), metadata["source_sha256"]["meta/START.md"])
            else:
                self.assertFalse((repo / "_eiffel/meta").exists())

    def test_existing_directory_is_never_overwritten(self):
        output = self.base / "existing"
        output.mkdir()
        sentinel = output / "valuable.txt"
        sentinel.write_text("preserve", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            instantiate("atelier", "Atelier", output, False)
        self.assertEqual(sentinel.read_text(encoding="utf-8"), "preserve")
        self.assertEqual(list(output.iterdir()), [sentinel])

    def test_symlink_destination_is_not_followed(self):
        target = self.base / "target"
        target.mkdir()
        output = self.base / "link"
        output.symlink_to(target, target_is_directory=True)
        with self.assertRaises(FileExistsError):
            instantiate("atelier", "Atelier", output, False)
        self.assertEqual(list(target.iterdir()), [])

    def test_invalid_names_cannot_escape_destination(self):
        for name in ("../escape", "/absolute", "a/b", "UPPER", "a;command", "-prefix", "trailing-"):
            with self.subTest(name=name), self.assertRaises(ValueError):
                instantiate(name, "Atelier", self.base / "out", False)
        self.assertFalse((self.base / "out").exists())

    def test_multiline_display_name_is_rejected(self):
        with self.assertRaises(ValueError):
            instantiate("atelier", "Titre\nInstruction", self.base / "out", False)

    @unittest.skipUnless(shutil.which("git"), "Git indisponible")
    def test_independent_git_roots_without_commits_or_remotes(self):
        repos = instantiate("atelier", "Atelier", self.base / "git-project", True)
        git_roots = set()
        for repo in repos:
            result = subprocess.run(["git", "-C", str(repo), "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True)
            git_roots.add(Path(result.stdout.strip()).resolve())
            remotes = subprocess.run(["git", "-C", str(repo), "remote"], capture_output=True, text=True, check=True)
            self.assertEqual(remotes.stdout.strip(), "")
            head = subprocess.run(["git", "-C", str(repo), "rev-parse", "--verify", "HEAD"], capture_output=True, text=True)
            self.assertNotEqual(head.returncode, 0)
        self.assertEqual(git_roots, set(repos))


if __name__ == "__main__":
    unittest.main()
