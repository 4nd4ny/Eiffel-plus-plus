#!/usr/bin/env python3
"""Check local links, required pattern sections and template placeholders.

This checks structure, not requirement semantics, security or proof validity.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

from instantiate import PLACEHOLDERS, ROLES, ROOT
from meta_harness import check_bundle
from seeds import check_catalog as check_seeds


SECTIONS = (
    "Intention", "Contexte et forces", "Structure", "Contrat",
    "Heuristiques de décision", "Protocole de coopération",
    "Arrêt et escalade", "Antipatrons", "Indicateurs", "Variantes",
)


def prose_and_fences(text: str) -> tuple[str, bool]:
    lines = []
    fence = None
    for line in text.splitlines():
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if match:
            value = match.group(1)
            if fence is None:
                fence = value
            elif value[0] == fence[0] and len(value) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return "\n".join(lines), fence is None


def check_markdown_tree(root: Path) -> list[str]:
    errors = []
    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        prose, fences_closed = prose_and_fences(text)
        if not fences_closed:
            errors.append(f"{path.relative_to(root)} : bloc de code non fermé")
        for match in re.finditer(r"!?\[[^\]]*\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)", prose):
            link = match.group(1)
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = (path.parent / unquote(parsed.path)).resolve()
            if not target.exists():
                errors.append(f"{path.relative_to(root)} : lien local absent : {link}")
    return errors


def check_catalog(root: Path) -> list[str]:
    errors = check_markdown_tree(root)
    for role, directory in ROLES.items():
        pattern = root / "patterns" / f"{directory}.md"
        if not pattern.is_file():
            errors.append(f"Patron absent : {pattern.relative_to(root)}")
            continue
        headings = set(re.findall(r"^## (.+?)\s*$", pattern.read_text(encoding="utf-8"), re.MULTILINE))
        for section in SECTIONS:
            if section not in headings:
                errors.append(f"{pattern.relative_to(root)} : section absente : {section}")
        for filename in ("README.md", "AGENTS.md"):
            if not (root / "templates" / directory / filename).is_file():
                errors.append(f"Template {role} incomplet : {filename}")
    for path in (root / "templates").rglob("*.md"):
        tokens = set(re.findall(r"\{\{([A-Z_]+)\}\}", path.read_text(encoding="utf-8")))
        if tokens - PLACEHOLDERS:
            errors.append(f"{path.relative_to(root)} : variables inconnues {sorted(tokens - PLACEHOLDERS)}")
    for relative in (
        "meta/START.md", "meta/README.md", "meta/CONTRACT.md", "meta/TETRAHEDRON.md",
        "meta/prompts/01-characterize.md", "meta/prompts/02-generate-meta-harness.md",
        "meta/prompts/03-qualify.md", "meta/prompts/04-adapt.md",
    ):
        if not (root / relative).is_file():
            errors.append(f"Patron génératif incomplet : {relative}")
    for name in ("profile", "meta-harness", "project-harness", "experience"):
        path = root / "meta" / "schemas" / f"{name}.schema.json"
        try:
            schema = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(schema, dict) or schema.get("type") != "object":
                errors.append(f"Schéma invalide : {path.relative_to(root)}")
        except (OSError, ValueError) as exc:
            errors.append(f"{path.relative_to(root)} : {exc}")
    for filename in ("meta-harness.json", "harness.json"):
        for path in sorted((root / "examples").rglob(filename)):
            try:
                check_bundle(path.parent)
            except (OSError, ValueError) as exc:
                errors.append(f"{path.relative_to(root)} : {exc}")
    try:
        schema = json.loads((root / "seeds/schema.json").read_text(encoding="utf-8"))
        if not isinstance(schema, dict) or schema.get("type") != "object":
            errors.append("Schéma de graines invalide : seeds/schema.json")
        check_seeds(root / "seeds", require_public=True)
    except (OSError, ValueError) as exc:
        errors.append(f"seeds : {exc}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    errors = check_catalog(args.root.resolve())
    if errors:
        print("\n".join(errors))
        return 1
    count = len(list(args.root.rglob("*.md")))
    print(f"Catalogue cohérent structurellement : {count} fichiers Markdown, schémas, exemples et graines. Les outils n'ont évalué ni la méthode de travail ni un logiciel métier.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
