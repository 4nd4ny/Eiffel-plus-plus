#!/usr/bin/env python3
"""Copy the four generic Eiffel++ component templates without network access.

For a contextually generated harness, use meta_harness.py materialize instead.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import tempfile

from meta_harness import SEED_CATALOG_REFERENCE, support_documents


VERSION = "0.7.0"
ROOT = Path(__file__).resolve().parents[1]
ROLES = {
    "governance": "01-governance",
    "stbl": "02-stbl",
    "audit": "03-audit",
    "product": "04-product",
}
PLACEHOLDERS = {
    "PROJECT_NAME", "PROJECT_SLUG", "GOVERNANCE_REPO", "STBL_REPO",
    "AUDIT_REPO", "PRODUCT_REPO",
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def source_files(folder: Path) -> list[Path]:
    files = []
    for path in sorted(folder.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Lien symbolique de source interdit : {path}")
        if path.is_file():
            files.append(path)
    return files


def render(text: str, relative_file: Path, project: str, name: str) -> str:
    replacements = {
        "PROJECT_NAME": name,
        "PROJECT_SLUG": project,
        **{f"{role.upper()}_REPO": f"{project}-{role}" for role in ROLES},
    }
    unknown = set(re.findall(r"\{\{([A-Z_]+)\}\}", text)) - PLACEHOLDERS
    if unknown:
        raise ValueError(f"Variables inconnues : {sorted(unknown)}")
    for key, value in replacements.items():
        text = text.replace("{{" + key + "}}", value)
    # Source templates link back to the catalogue's canonical protocol.
    # Instantiated repositories use their own explicitly pinned snapshot.
    prefix = "../" * len(relative_file.parent.parts)
    for namespace in ("protocol", "meta"):
        text = re.sub(r"(?:\.\./)+" + namespace + "/", prefix + "_eiffel/" + namespace + "/", text)
    return text


def instantiate(project: str, name: str, destination: Path, git_init: bool) -> list[Path]:
    if not re.fullmatch(r"[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?", project):
        raise ValueError("Le nom technique doit contenir 1 à 64 lettres minuscules, chiffres ou tirets, sans tiret aux extrémités.")
    if not name.strip() or any(c in name for c in "\r\n\x00") or "{{" in name:
        raise ValueError("Le nom lisible doit tenir sur une ligne non vide, sans variable de template.")
    if os.path.lexists(destination):
        raise FileExistsError(f"La destination existe déjà : {destination}")
    destination = destination.resolve()
    if destination == ROOT or ROOT in destination.parents:
        raise ValueError("Choisir une destination extérieure au catalogue.")
    if git_init and shutil.which("git") is None:
        raise ValueError("Git est nécessaire pour --git-init.")

    templates = {role: source_files(ROOT / "templates" / directory) for role, directory in ROLES.items()}
    for role, files in templates.items():
        if not files or not (ROOT / "templates" / ROLES[role] / "AGENTS.md").is_file():
            raise ValueError(f"Template incomplet : {role}")
    protocol = source_files(ROOT / "protocol")
    if not protocol:
        raise ValueError("Protocole absent.")
    meta_pattern = source_files(ROOT / "meta")
    if not meta_pattern:
        raise ValueError("Patron de génération absent.")
    docs = support_documents(ROOT)

    destination.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".eiffel-staging-", dir=destination.parent))
    try:
        for role, files in templates.items():
            repo = staging / f"{project}-{role}"
            repo.mkdir()
            origin = ROOT / "templates" / ROLES[role]
            source_manifest = {}
            for path in files:
                relative = path.relative_to(origin)
                raw = path.read_bytes()
                source_manifest[str(path.relative_to(ROOT))] = digest(raw)
                target = repo / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                if path.suffix == ".md":
                    target.write_text(render(raw.decode("utf-8"), relative, project, name), encoding="utf-8")
                else:
                    target.write_bytes(raw)
                target.chmod(stat.S_IMODE(path.stat().st_mode) & 0o777)
            for path in protocol:
                relative = path.relative_to(ROOT / "protocol")
                raw = path.read_bytes()
                source_manifest[str(path.relative_to(ROOT))] = digest(raw)
                target = repo / "_eiffel" / "protocol" / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(raw)
                target.chmod(stat.S_IMODE(path.stat().st_mode) & 0o777)
            if role == "governance":
                for path in meta_pattern:
                    relative = path.relative_to(ROOT / "meta")
                    raw = path.read_bytes()
                    source_manifest[str(path.relative_to(ROOT))] = digest(raw)
                    target = repo / "_eiffel" / "meta" / relative
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(raw)
                    target.chmod(stat.S_IMODE(path.stat().st_mode) & 0o777)
                (repo / "_eiffel/seeds").mkdir()
                (repo / "_eiffel/seeds/README.md").write_text(SEED_CATALOG_REFERENCE, encoding="utf-8")
            for relative, raw in docs.items():
                target = repo / "_eiffel/docs" / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(raw)
                target.chmod(docs.modes[relative])
                source_manifest["docs/" + relative] = digest(raw)
            shutil.copyfile(ROOT / "LICENSE", repo / "_eiffel" / "LICENSE")
            metadata = {
                "template_version": VERSION,
                "protocol_version": VERSION,
                "role": role,
                "project_name": name,
                "project_slug": project,
                "generation_mode": "generic-components",
                "binding_status": "UNBOUND",
                "repositories": {
                    key: {"directory": f"{project}-{key}", "remote": None, "commit": None}
                    for key in ROLES
                },
                "source_sha256": source_manifest,
                "note": "Empreintes de contenu, sans preuve de provenance ni attestation d'exécution. Résoudre les références avant acceptation.",
            }
            (repo / "_eiffel" / "project.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            (repo / ".gitignore").write_text(".DS_Store\n__pycache__/\n*.py[cod]\n.env\n.env.*\n!.env.example\nartifacts-local/\n", encoding="utf-8")
            if git_init:
                subprocess.run(["git", "init", "--quiet", "--initial-branch=main", str(repo)], check=True, capture_output=True, text=True)

        # Exclusive creation prevents replacing an existing file, directory or symlink,
        # including one created while the templates were being prepared.
        destination.mkdir(exist_ok=False)
        results = []
        for role in ROLES:
            target = destination / f"{project}-{role}"
            (staging / f"{project}-{role}").rename(target)
            results.append(target)
        return results
    finally:
        # Only remove the staging directory created by this invocation.
        shutil.rmtree(staging)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, help="Nom technique : lettres minuscules, chiffres et tirets.")
    parser.add_argument("--name", help="Nom lisible du projet, par défaut le nom technique.")
    parser.add_argument("--output", required=True, type=Path, help="Nouveau dossier extérieur au catalogue.")
    parser.add_argument("--git-init", action="store_true", help="Initialiser quatre dépôts locaux, sans commit ni remote.")
    args = parser.parse_args()
    try:
        repositories = instantiate(args.project, args.name or args.project, args.output, args.git_init)
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        parser.exit(2, f"Instanciation interrompue : {exc}\n")
    print(json.dumps({"version": VERSION, "repositories": [str(p) for p in repositories], "binding_status": "UNBOUND", "git_initialized": args.git_init}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
