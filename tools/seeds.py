#!/usr/bin/env python3
"""Consulter des graines et capturer un paquet N0, sans modèle ni réseau.

Les fiches sont des données. Ce programme ne décide pas quel harnais convient,
n'exécute pas les fichiers copiés et n'authentifie aucune décision ou mesure.
"""

from __future__ import annotations

import argparse
import copy
from datetime import date
import json
import os
from pathlib import Path
import re
import shutil
import tempfile
from urllib.parse import urlsplit

import meta_harness as meta


VERSION = meta.VERSION
DEFAULT_CATALOG = meta.ROOT / "seeds"
KINDS = ("external-pattern", "local-example", "co-designed-instance")
EVIDENCE_LEVELS = ("source-inspected", "illustrative", "untested", "local-observation", "comparison")
ARTIFACT_FORMAT = "sha256-files-executable-v1"
NOTICE = (
    "Structure et empreinte seulement. Une fiche ne prouve ni son origine, ni une "
    "co-construction humaine, ni ses droits de publication, ni l'efficacité du harnais. "
    "Les fichiers et références ne sont jamais exécutés ou chargés depuis le réseau."
)


def _identifier(value, label):
    value = meta._text(value, label)
    if not re.fullmatch(r"[a-z0-9](?:[a-z0-9-]{0,94}[a-z0-9])?", value):
        raise ValueError(f"{label} : identifiant de 1 à 96 minuscules, chiffres ou tirets requis.")
    return value


def _public_location(path: Path) -> bool:
    root = DEFAULT_CATALOG.resolve()
    return path == root or root in path.parents


def validate_record(record: dict, require_public: bool = False) -> None:
    """Contrôler des déclarations ; aucune source ou approbation n'est authentifiée."""
    record = meta._object(record, "record")
    if record.get("schema_version") not in ("0.3.0", VERSION):
        raise ValueError(f"record.schema_version doit être 0.3.0 ou {VERSION}.")
    _identifier(record.get("id"), "id")
    if record.get("kind") not in KINDS:
        raise ValueError(f"kind doit appartenir à {KINDS}.")
    for key in ("title", "summary"):
        meta._text(record.get(key), key)
    source = meta._object(record.get("source"), "source")
    for key in ("url", "revision"):
        if key not in source:
            raise ValueError(f"source.{key} est requis (null si non établi).")
        if source[key] is not None:
            meta._text(source[key], f"source.{key}")
    if source["url"] is not None:
        parsed = urlsplit(source["url"])
        if parsed.scheme not in ("https", "http") or not parsed.netloc or parsed.username or parsed.password:
            raise ValueError("source.url : URL HTTP(S) sans identifiant incorporé requise.")
    if record["kind"] == "external-pattern" and source["url"] is None:
        raise ValueError("Une graine externe exige son URL source.")
    for key in ("license", "discovered_via"):
        meta._text(source.get(key), f"source.{key}")
    meta._texts(source.get("paths"), "source.paths")
    if source.get("visibility") not in ("public", "private", "local"):
        raise ValueError("source.visibility doit être public, private ou local.")
    reviewed = meta._text(source.get("reviewed_on"), "source.reviewed_on")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", reviewed):
        raise ValueError("source.reviewed_on : date YYYY-MM-DD requise.")
    date.fromisoformat(reviewed)
    context = meta._object(record.get("context"), "context")
    for key in ("suitable_for", "avoid_when", "required_capabilities", "cost_notes"):
        meta._texts(context.get(key), f"context.{key}")
    if not meta._texts(record.get("recipe"), "recipe"):
        raise ValueError("recipe doit contenir au moins une étape.")
    meta._texts(record.get("operator_questions"), "operator_questions")
    evidence = meta._object(record.get("evidence"), "evidence")
    if evidence.get("level") not in EVIDENCE_LEVELS:
        raise ValueError(f"evidence.level doit appartenir à {EVIDENCE_LEVELS}.")
    for key in ("claims", "limitations", "runs"):
        meta._texts(evidence.get(key), f"evidence.{key}")
    if evidence["level"] in ("local-observation", "comparison") and not evidence["runs"]:
        raise ValueError("Une observation ou comparaison exige des références dans evidence.runs.")
    lineage = meta._object(record.get("lineage"), "lineage")
    for parent in meta._texts(lineage.get("parents"), "lineage.parents"):
        _identifier(parent, "lineage.parents")
        if parent == record["id"]:
            raise ValueError("Une graine ne peut être son propre parent.")
    publication = meta._object(record.get("publication"), "publication")
    if publication.get("status") not in ("public", "private", "unreviewed"):
        raise ValueError("publication.status doit être public, private ou unreviewed.")
    if type(publication.get("contains_private_material")) is not bool:
        raise ValueError("publication.contains_private_material doit être un booléen explicite.")
    if require_public and (publication["status"] != "public" or publication["contains_private_material"]):
        raise ValueError("Le catalogue public refuse une fiche privée ou sans décision de publication déclarée.")
    review = meta._object(record.get("review"), "review")
    if review.get("status") not in ("unreviewed", "co-designed"):
        raise ValueError("review.status doit être unreviewed ou co-designed.")
    if "decision_ref" not in review:
        raise ValueError("review.decision_ref est requis (null si absent).")
    if review["status"] == "co-designed" or review["decision_ref"] is not None:
        meta._text(review["decision_ref"], "review.decision_ref")
    if record["kind"] == "co-designed-instance" and review["status"] != "co-designed":
        raise ValueError("co-designed-instance exige une co-construction déclarée et sa décision référencée.")
    if "artifact" in record:
        artifact = meta._object(record["artifact"], "artifact")
        meta._relative(artifact.get("path"), "artifact.path")
        if artifact.get("format") != ARTIFACT_FORMAT:
            raise ValueError(f"artifact.format doit être {ARTIFACT_FORMAT}.")
        if not re.fullmatch(r"[0-9a-f]{64}", meta._text(artifact.get("sha256"), "artifact.sha256")):
            raise ValueError("artifact.sha256 : empreinte SHA-256 complète requise.")


def artifact_digest(files: meta.Snapshot) -> str:
    """SHA-256 du JSON canonique {chemin: {sha256, executable}} ; portable en Git."""
    return meta.digest(meta.canonical({
        path: {"sha256": meta.digest(raw), "executable": bool(files.modes[path] & 0o111)}
        for path, raw in files.items()
    }))


def read_records(catalog: Path, require_public: bool | None = None) -> list[tuple[Path, dict]]:
    catalog = meta._plain_path(catalog)
    if not catalog.is_dir():
        raise ValueError(f"Catalogue absent : {catalog}")
    if require_public is None:
        require_public = _public_location(catalog)
    paths = [catalog / "record.json"] if (catalog / "record.json").exists() else sorted([
        *(catalog / "records").glob("*.json"),
        *(catalog / "instances").glob("*/record.json"),
    ])
    if not paths:
        raise ValueError("Aucune fiche dans records/*.json, instances/*/record.json ou record.json.")
    records, ids = [], set()
    for path in paths:
        record = meta._json(meta._read_file(path), str(path))
        validate_record(record, require_public=require_public)
        if record["id"] in ids:
            raise ValueError(f"Identifiant de graine répété : {record['id']}")
        ids.add(record["id"])
        records.append((path, record))
    return records


def check_catalog(catalog: Path, require_public: bool | None = None) -> dict:
    records = read_records(catalog, require_public)
    ids = {record["id"] for _, record in records}
    unresolved, artifacts = {}, 0
    for path, record in records:
        missing = [parent for parent in record["lineage"]["parents"] if parent not in ids]
        if missing:
            unresolved[record["id"]] = missing
        if "artifact" in record:
            files = meta._snapshot(path.parent / record["artifact"]["path"])
            _, manifest, _ = meta._validate_bundle(files)
            if manifest["level"] != 0:
                raise ValueError(f"{record['id']} : l'artefact capturé doit être un harnais N0.")
            if artifact_digest(files) != record["artifact"]["sha256"]:
                raise ValueError(f"{record['id']} : empreinte d'artefact différente ; créer une nouvelle capture.")
            artifacts += 1
    return {
        "structure_status": "PASS", "record_count": len(records), "artifacts_checked": artifacts,
        "unresolved_parents": unresolved, "authority_status": "NOT_VERIFIED",
        "effectiveness_status": "NOT_RUN", "note": NOTICE,
    }


def capture(bundle: Path, record_path: Path, destination: Path) -> dict:
    """Copier un paquet N0 explicite ; conserver les déclarations, sans les promouvoir."""
    files = meta._snapshot(bundle)
    _, manifest, _ = meta._validate_bundle(files)
    if manifest["level"] != 0:
        raise ValueError("La capture exige un paquet N0, pas un générateur ou un dépôt produit.")
    record = meta._json(meta._read_file(record_path), str(record_path))
    if "artifact" in record:
        raise ValueError("La note de nouvelle capture ne doit pas réutiliser un ancien champ artifact.")
    destination = Path(destination).absolute()
    if os.path.lexists(destination):
        raise FileExistsError(f"La destination existe déjà : {destination}")
    destination = meta._plain_path(destination)
    for origin in (meta._plain_path(bundle), meta._plain_path(record_path)):
        if destination == origin or origin in destination.parents:
            raise ValueError("Choisir une destination extérieure aux sources de capture.")
    validate_record(record, require_public=_public_location(destination))
    captured = copy.deepcopy(record)
    captured["artifact"] = {"path": "harness", "format": ARTIFACT_FORMAT, "sha256": artifact_digest(files)}
    destination.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".eiffel-seed-", dir=destination.parent))
    try:
        for path, raw in files.items():
            meta._write(staging / "harness", path, raw, files.modes[path])
        meta._write_json(staging, "record.json", captured)
        check_catalog(staging, require_public=_public_location(destination))
        meta._publish(staging, destination, "record.json")
    finally:
        if staging.exists():
            shutil.rmtree(staging)
    return {"output": str(destination), "id": captured["id"], "artifact": captured["artifact"],
            "review_status": captured["review"]["status"], "evidence_level": captured["evidence"]["level"],
            "authority_status": "NOT_VERIFIED", "note": NOTICE}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("list", "show", "check"):
        current = sub.add_parser(command)
        current.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
        current.add_argument("--public", action="store_true", help="Exiger les déclarations nécessaires au catalogue public.")
        if command == "show":
            current.add_argument("id")
    current = sub.add_parser("capture", help="Capturer un paquet N0 et sa fiche dans un nouveau dossier.")
    current.add_argument("bundle", type=Path)
    current.add_argument("--record", type=Path, required=True)
    current.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == "capture":
            result = capture(args.bundle, args.record, args.output)
        elif args.command == "check":
            result = check_catalog(args.catalog, True if args.public else None)
        else:
            records = read_records(args.catalog, True if args.public else None)
            if args.command == "show":
                matches = [record for _, record in records if record["id"] == args.id]
                if not matches:
                    raise ValueError(f"Graine absente : {args.id}")
                result = matches[0]
            else:
                result = [{"id": r["id"], "title": r["title"], "kind": r["kind"],
                           "summary": r["summary"], "evidence_level": r["evidence"]["level"],
                           "review_status": r["review"]["status"], "publication": r["publication"]["status"]}
                          for _, r in records]
    except (OSError, ValueError) as exc:
        parser.exit(2, f"Opération interrompue : {exc}\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
