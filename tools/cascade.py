#!/usr/bin/env python3
"""Journal local de cycles, preuves liées et revues humaines. Aucun appel LLM.

Les empreintes vérifient une cohérence, pas la vérité des résultats ni l'identité
du déclarant. Conserver le head hors du journal (par exemple dans une revue Git).
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import json
from pathlib import Path
import shutil
import sys

import meta_harness as meta

FORMAT = "eiffel-cascade-1"
NOTICE = "Preuves déclarées liées aux fichiers ; authenticité et suffisance métier non automatisées."


def _tree(root):
    files = meta._snapshot(Path(root))
    return _inventory(files)


def _inventory(files):
    return {p: {"sha256": meta.digest(raw), "mode": files.modes[p]} for p, raw in files.items()}


def _read(path):
    return meta._json(meta._read_file(Path(path)), str(path))


def _write_new(path, value):
    with Path(path).open("xb") as stream:
        stream.write(meta.canonical(value) + b"\n")


def _cycle_data(bundle, files=None):
    if files is None:
        files = meta._snapshot(Path(bundle))
    if "cycle.json" not in files:
        raise ValueError("cycle.json requis.")
    data = meta._json(files["cycle.json"], "cycle")
    if type(data.get("level")) is not int or data["level"] not in (0, 1, 2):
        raise ValueError("level doit être 0, 1 ou 2.")
    for key in ("purpose", "observation", "hypothesis", "change"):
        meta._text(data.get(key), key)
    for key in ("novelty", "blocking_unknowns", "limits"):
        meta._texts(data.get(key), key)
    if not isinstance(data.get("stability_probe"), str):
        raise ValueError("stability_probe doit être un texte (vide si non exécutée).")
    criteria = meta._object(data.get("criteria"), "criteria")
    if not criteria or any(not isinstance(k, str) or not k.strip() or v not in ("PASS", "FAIL", "UNKNOWN") for k, v in criteria.items()):
        raise ValueError("criteria : inventaire non vide de PASS/FAIL/UNKNOWN requis.")
    evidence = meta._texts(data.get("evidence"), "evidence")
    if not evidence:
        raise ValueError("Au moins une pièce de preuve est requise.")
    def resource(path):
        name = meta._relative(path, "pièce")
        if name == "cycle.json" or name not in files or not files[name].strip():
            raise ValueError(f"Pièce manquante/vide : {name}")
    for path in evidence:
        resource(path)
    coverage = data.get("coverage")
    if not isinstance(coverage, list) or not coverage:
        raise ValueError("coverage non vide requise.")
    covered = set()
    for row in coverage:
        meta._object(row, "coverage row")
        meta._text(row.get("requirement"), "requirement")
        if row.get("criterion") not in criteria:
            raise ValueError("Critère de couverture absent de criteria.")
        covered.add(row["criterion"])
    if covered != set(criteria):
        raise ValueError("Chaque critère doit être relié à un besoin.")
    inputs = data.get("required_inputs")
    if not isinstance(inputs, list) or not inputs:
        raise ValueError("required_inputs non vide requis.")
    seen = set()
    for row in inputs:
        meta._object(row, "required_input")
        ident = meta._text(row.get("id"), "input.id")
        if ident in seen or row.get("status") not in ("AVAILABLE", "MISSING", "EXCLUDED"):
            raise ValueError("Input répété ou statut invalide.")
        seen.add(ident)
        if row["status"] == "AVAILABLE":
            resource(row.get("source"))
        elif row["status"] == "EXCLUDED":
            meta._text(row.get("reason"), "exclusion.reason")
    return data


def _scope(root, event, data):
    """Périmètre comparable, sans figer les nouvelles observations d'un essai.

    Les oracles et spécifications qui doivent rester identiques sont des entrées
    requises. Les pièces evidence peuvent contenir de nouvelles sorties d'essai.
    """
    inputs = []
    for row in data["required_inputs"]:
        value = dict(row)
        if row["status"] == "AVAILABLE":
            value["source_identity"] = event["files"][row["source"]]
        inputs.append(value)
    return {"purpose": data["purpose"], "criteria": sorted(data["criteria"]),
            "coverage": sorted((row["requirement"], row["criterion"]) for row in data["coverage"]),
            "inputs": sorted(inputs, key=lambda row: row["id"]), "limits": data["limits"]}


def _state(session, events):
    state = {"level": 2 if session["mode"] == "cascade" else 0,
             "epoch": 0, "completed": False, "active_gates": {}}
    for event in events:
        if event["kind"] == "advance":
            state["active_gates"][str(state["level"])] = event["event_sha256"]
            if state["level"]:
                state["level"] -= 1
            else:
                state["completed"] = True
        elif event["kind"] == "reopen":
            state["level"] = event["level"]
            state["epoch"] += 1
            state["completed"] = False
            state["active_gates"] = {k: v for k, v in state["active_gates"].items() if int(k) > event["level"]}
    return state


def _load(root, expected_head=None):
    root = meta._plain_path(Path(root))
    session_raw = meta._read_file(root / "session.json")
    session = meta._json(session_raw, "session")
    if session.get("format") != FORMAT or session.get("mode") not in ("cascade", "direct"):
        raise ValueError("Session invalide.")
    paths = sorted((root / "events").iterdir())
    if not paths:
        raise ValueError("Événement initial absent.")
    events, previous, objects = [], None, set()
    for seq, path in enumerate(paths, 1):
        if path.name != f"{seq:06d}.json":
            raise ValueError("Séquence du journal invalide.")
        event = _read(path)
        body = {k: v for k, v in event.items() if k != "event_sha256"}
        if event.get("event_sha256") != meta.digest(meta.canonical(body)) or event.get("previous") != previous:
            raise ValueError("Chaîne d'empreintes altérée.")
        if event.get("session_sha256") != meta.digest(session_raw) or event.get("sequence") != seq:
            raise ValueError("Session ou séquence altérée.")
        if event.get("kind") not in ("start", "cycle", "review", "advance", "reopen") or (seq == 1) != (event["kind"] == "start"):
            raise ValueError("Type d'événement invalide.")
        obj = event.get("object")
        if obj:
            if obj != f"{seq:06d}" or _tree(root / "objects" / obj) != event.get("files"):
                raise ValueError("Pièces liées absentes ou altérées.")
            objects.add(obj)
        _validate_event(root, session, events, event)
        events.append(event)
        previous = event["event_sha256"]
    if set(p.name for p in (root / "objects").iterdir()) != objects:
        raise ValueError("Objet orphelin ou pièce ajoutée au journal.")
    if expected_head is not None and previous != expected_head:
        raise ValueError("Le head diffère de l'ancre externe.")
    return session, events, _state(session, events)


def _validate_event(root, session, events, event):
    """Vérifier aussi la légalité des transitions ; une empreinte seule ne suffit pas."""
    state = _state(session, events)
    kind = event["kind"]
    if kind in ("cycle", "review"):
        if not event.get("object") or state["completed"]:
            raise ValueError("Cycle/revue sans pièce ou niveau déjà fermé.")
    elif event.get("object"):
        raise ValueError("Pièce inattendue pour cette transition.")
    if kind == "start":
        if event.get("mode") != session["mode"]:
            raise ValueError("Mode initial différent de la session.")
    elif kind == "cycle":
        data = _cycle_data(root / "objects" / event["object"])
        if (event.get("level"), event.get("epoch"), data["level"]) != (state["level"], state["epoch"], state["level"]):
            raise ValueError("Cycle hors du niveau ou de l'époque active.")
    elif kind == "review":
        cycles = [e for e in events if e["kind"] == "cycle" and e["level"] == state["level"] and e["epoch"] == state["epoch"]]
        expected = "DESCEND" if state["level"] else "ACCEPT"
        if not cycles or event.get("cycle_sha256") != cycles[-1]["event_sha256"] or event.get("decision") not in (expected, "REVISE"):
            raise ValueError("Revue hors du dernier cycle ou décision invalide.")
        meta._text(event.get("reviewer"), "reviewer")
        if event.get("authority") != "DECLARED_NOT_AUTHENTICATED" or set(event["files"]) != {"response.md"}:
            raise ValueError("Reçu de revue invalide.")
        raw = meta._read_file(root / "objects" / event["object"] / "response.md")
        meta._text(raw.decode("utf-8"), "response")
    elif kind == "advance":
        if (event.get("level"), event.get("epoch")) != (state["level"], state["epoch"]) or event.get("gate_head") != events[-1]["event_sha256"]:
            raise ValueError("Passage lié à une autre porte.")
        if _gate_state(root, events, state)["verdict"] != "READY":
            raise ValueError("Passage sans porte prête.")
    elif kind == "reopen":
        level = event.get("level")
        if type(level) is not int or level not in range(state["level"], 3) or (session["mode"] == "direct" and level != 0):
            raise ValueError("Réouverture hors du niveau courant ou d'un ancêtre.")
        meta._text(event.get("reason"), "reason")


def verify(root, expected_head=None):
    try:
        _, events, state = _load(root, expected_head)
        return {"verdict": "PASS", "head": events[-1]["event_sha256"], **state, "notice": NOTICE}
    except (ValueError, OSError, KeyError, TypeError) as exc:
        return {"verdict": "STALE", "reason": str(exc)}


@contextmanager
def _lock(root):
    root = meta._plain_path(Path(root))
    lock = root / ".writer-lock"
    try:
        stream = lock.open("xb")
    except FileExistsError as exc:
        raise ValueError("Un écrivain est déjà actif ; examiner le verrou avant reprise.") from exc
    try:
        stream.close()
        yield root
    finally:
        lock.unlink()


def _append(root, kind, payload, files=None):
    session_raw = meta._read_file(root / "session.json")
    paths = sorted((root / "events").iterdir())
    seq = len(paths) + 1
    event = {"sequence": seq, "kind": kind,
             "at": datetime.now(timezone.utc).isoformat(),
             "session_sha256": meta.digest(session_raw),
             "previous": _read(paths[-1])["event_sha256"] if paths else None, **payload}
    obj = root / "objects" / f"{seq:06d}"
    try:
        if files is not None:
            obj.mkdir()
            for name, raw in files.items():
                meta._write(obj, name, raw, files.modes[name] if hasattr(files, "modes") else 0o644)
            event.update(object=obj.name, files=_tree(obj))
        event["event_sha256"] = meta.digest(meta.canonical(event))
        _write_new(root / "events" / f"{seq:06d}.json", event)
    except BaseException:
        if obj.exists():
            shutil.rmtree(obj)
        raise
    return event


def start(root, mode="cascade"):
    if mode not in ("cascade", "direct"):
        raise ValueError("Mode cascade ou direct requis.")
    root = meta._plain_path(Path(root))
    root.mkdir(parents=True, exist_ok=False)
    (root / "events").mkdir()
    (root / "objects").mkdir()
    _write_new(root / "session.json", {"format": FORMAT, "schema_version": "0.7.0", "mode": mode})
    return _append(root, "start", {"mode": mode})


def cycle(root, bundle):
    with _lock(root) as root:
        _, _, state = _load(root)
        files = meta._snapshot(Path(bundle))
        data = _cycle_data(bundle, files)
        if state["completed"] or data["level"] != state["level"]:
            raise ValueError("Niveau fermé ou différent du niveau actif ; advance/reopen requis.")
        return _append(root, "cycle", {"level": state["level"], "epoch": state["epoch"]}, files)


def review(root, cycle_sha, decision, reviewer, response_file):
    with _lock(root) as root:
        _, events, state = _load(root)
        current = [e for e in events if e["kind"] == "cycle" and e["level"] == state["level"] and e["epoch"] == state["epoch"]]
        if not current or current[-1]["event_sha256"] != cycle_sha or state["completed"]:
            raise ValueError("La revue doit viser le dernier cycle actif.")
        expected = "DESCEND" if state["level"] else "ACCEPT"
        if decision not in (expected, "REVISE"):
            raise ValueError(f"Décision requise : {expected} ou REVISE.")
        meta._text(reviewer, "reviewer")
        raw = meta._read_file(Path(response_file))
        meta._text(raw.decode("utf-8"), "response")
        return _append(root, "review", {"cycle_sha256": cycle_sha, "decision": decision,
                       "reviewer": reviewer, "authority": "DECLARED_NOT_AUTHENTICATED"}, {"response.md": raw})


def gate(root):
    try:
        _, events, state = _load(root)
        return _gate_state(Path(root), events, state)
    except (ValueError, OSError, KeyError, TypeError) as exc:
        return {"verdict": "INCONCLUSIVE", "reasons": ["Journal STALE : " + str(exc)]}


def _gate_state(root, events, state):
    reasons = []
    cycles = [e for e in events if e["kind"] == "cycle" and e["level"] == state["level"] and e["epoch"] == state["epoch"]]
    if state["completed"]:
        reasons.append("Niveau déjà clôturé ; rouvrir pour une nouvelle appréciation.")
    if len(cycles) < 2:
        reasons.append("Deux cycles au minimum sont nécessaires pour observer une stabilisation.")
    if cycles:
        last = cycles[-1]
        data = _cycle_data(Path(root) / "objects" / last["object"])
        if any(v != "PASS" for v in data["criteria"].values()):
            reasons.append("Des critères sont FAIL ou UNKNOWN.")
        if data["blocking_unknowns"] or any(i["status"] == "MISSING" for i in data["required_inputs"]):
            reasons.append("Des inconnues ou données nécessaires restent bloquantes.")
        if data["novelty"] or not data["stability_probe"].strip():
            reasons.append("La stabilité après la dernière amélioration n'est pas observée.")
        if len(cycles) >= 2:
            prior = _cycle_data(Path(root) / "objects" / cycles[-2]["object"])
            if _scope(root, cycles[-2], prior) != _scope(root, last, data) or any(v != "PASS" for v in prior["criteria"].values()) or prior["blocking_unknowns"]:
                reasons.append("Périmètre, couverture ou entrées modifiés, ou précédent cycle non concluant ; réitérer.")
        reviews = [e for e in events if e["kind"] == "review" and e["cycle_sha256"] == last["event_sha256"]]
        if not reviews or reviews[-1]["decision"] != ("DESCEND" if state["level"] else "ACCEPT"):
            reasons.append("Revue humaine favorable de ce cycle absente.")
    return {"verdict": "READY" if not reasons else "INCONCLUSIVE", "reasons": reasons,
            "head": events[-1]["event_sha256"], "level": state["level"], "epoch": state["epoch"], "notice": NOTICE}


def advance(root):
    with _lock(root) as root:
        result = gate(root)
        if result["verdict"] != "READY":
            raise ValueError("Passage refusé : " + "; ".join(result["reasons"]))
        return _append(root, "advance", {"level": result["level"], "epoch": result["epoch"], "gate_head": result["head"]})


def reopen(root, level, reason):
    with _lock(root) as root:
        session, _, state = _load(root)
        if type(level) is not int or level not in range(state["level"], 3) or (session["mode"] == "direct" and level != 0):
            raise ValueError("Rouvrir le niveau courant ou un ancêtre ; direct reste N0.")
        meta._text(reason, "reason")
        return _append(root, "reopen", {"level": level, "reason": reason})


def export_reviewed(source, review_file, destination):
    """Exporter uniquement un dossier public préparé séparément et revu par empreinte.

    Ne copie jamais automatiquement un journal privé, ni son histoire Git.
    La déclaration de publication reste sous la responsabilité de l'opérateur.
    """
    from trials import _staging
    source = Path(source)
    files = meta._snapshot(source)
    declaration = _read(review_file)
    if declaration.get("publication") != "public" or declaration.get("contains_private_material") is not False:
        raise ValueError("Revue explicite d'un paquet public sans contenu privé requise.")
    for key in ("authorization_ref", "reviewer", "license", "scope"):
        meta._text(declaration.get(key), key)
    if declaration.get("files") != _inventory(files):
        raise ValueError("Le paquet diffère de la version revue.")
    if "PUBLICATION.json" in files:
        raise ValueError("PUBLICATION.json est réservé au reçu d'export.")
    with _staging(Path(destination), [source, Path(review_file)]) as stage:
        for name, raw in files.items():
            meta._write(stage, name, raw, files.modes[name])
        meta._write_json(stage, "PUBLICATION.json", declaration)
    return {"verdict": "PASS", "files": len(files), "notice": "Export d'une déclaration revue, sans détection exhaustive de secrets ni publication réseau."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    p = commands.add_parser("start"); p.add_argument("root", type=Path); p.add_argument("--mode", choices=["cascade", "direct"], default="cascade")
    p = commands.add_parser("cycle"); p.add_argument("root", type=Path); p.add_argument("bundle", type=Path)
    p = commands.add_parser("review"); p.add_argument("root", type=Path); p.add_argument("cycle_sha"); p.add_argument("decision", choices=["DESCEND", "ACCEPT", "REVISE"]); p.add_argument("reviewer"); p.add_argument("response_file", type=Path)
    for name in ("gate", "advance", "verify"):
        p = commands.add_parser(name); p.add_argument("root", type=Path)
        if name == "verify": p.add_argument("--expected-head")
    p = commands.add_parser("reopen"); p.add_argument("root", type=Path); p.add_argument("level", type=int); p.add_argument("reason")
    p = commands.add_parser("export"); p.add_argument("source", type=Path); p.add_argument("review_file", type=Path); p.add_argument("destination", type=Path)
    args = vars(parser.parse_args()); command = args.pop("command")
    try:
        result = (export_reviewed if command == "export" else globals()[command])(**args)
    except (ValueError, OSError) as exc:
        parser.exit(2, str(exc) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("verdict", "PASS") in ("PASS", "READY") else 1


if __name__ == "__main__":
    sys.exit(main())
