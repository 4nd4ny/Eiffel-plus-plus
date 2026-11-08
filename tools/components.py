"""Contrats optionnels de composants et d'expériences ; aucun code exécuté."""

from __future__ import annotations

import meta_harness as meta


def _nonempty_texts(value, label):
    if not meta._texts(value, label):
        raise ValueError(f"{label} doit contenir au moins une entrée.")


def _refs(files, value, label, *, required=False):
    refs = meta._texts(value, label)
    if required and not refs:
        raise ValueError(f"{label} exige une référence locale.")
    if len(refs) != len(set(refs)):
        raise ValueError(f"{label} contient des références répétées.")
    for ref in refs:
        meta._relative(ref, label)
        if ref not in files:
            raise ValueError(f"{label} : fichier absent : {ref}")


def validate_components(files, manifest):
    components = manifest.get("components", [])
    if not isinstance(components, list):
        raise ValueError("components doit être un tableau.")
    ids = set()
    for item in components:
        item = meta._object(item, "component")
        identifier = meta._text(item.get("id"), "component.id")
        if identifier in ids:
            raise ValueError("component.id répété.")
        ids.add(identifier)
        if item.get("kind") not in ("procedure", "script", "skill"):
            raise ValueError("component.kind doit être procedure, script ou skill.")
        if item["kind"] == "skill" and manifest["schema_version"] not in ("0.5.0", "0.6.0", "0.7.0", "0.8.0"):
            raise ValueError("Les skills exigent schema_version 0.5.0, 0.6.0, 0.7.0 ou 0.8.0.")
        path = meta._file(files, item.get("path"), "component.path")
        if item["kind"] == "script" and not path.endswith(".py"):
            raise ValueError("Les composants script pris en charge sont des fichiers Python .py.")
        meta._text(item.get("trigger"), "component.trigger")
        for key in ("inputs", "outputs", "limitations"):
            _nonempty_texts(item.get(key), f"component.{key}")
        _refs(files, item.get("dependencies"), "component.dependencies")
    return len(components)


def validate_experience(files, manifest):
    if "experience" not in manifest:
        return False
    path = meta._file(files, manifest["experience"], "experience")
    experience = meta._json(files[path], path)
    if experience.get("schema_version") != "1.0":
        raise ValueError("experience.schema_version doit être 1.0.")
    problem = meta._object(experience.get("problem"), "experience.problem")
    for key in ("observation", "hypothesis", "expected_change"):
        meta._text(problem.get(key), f"problem.{key}")
    _refs(files, problem.get("evidence"), "problem.evidence", required=True)
    context = meta._object(experience.get("context"), "experience.context")
    for key in ("applies_when", "avoid_when"):
        _nonempty_texts(context.get(key), f"context.{key}")
    runs = experience.get("runs")
    if not isinstance(runs, list) or not runs:
        raise ValueError("experience.runs doit contenir au moins la référence.")
    by_id = {}
    for run in runs:
        run = meta._object(run, "run")
        identifier = meta._text(run.get("id"), "run.id")
        if identifier in by_id:
            raise ValueError("run.id répété.")
        by_id[identifier] = run
        if run.get("status") not in ("NOT_RUN", "PASS", "FAIL", "UNKNOWN", "STALE"):
            raise ValueError("run.status inconnu.")
        meta._text(run.get("outcome"), "run.outcome")
        _refs(files, run.get("evidence"), "run.evidence", required=run["status"] != "NOT_RUN")
        costs = meta._object(run.get("costs"), "run.costs")
        for key in ("seconds", "tokens", "usd"):
            if key not in costs:
                raise ValueError(f"costs.{key} requis ; null si inconnu.")
            value = costs[key]
            if value is not None and (not meta._finite_number(value) or value < 0):
                raise ValueError(f"costs.{key} doit être positif ou nul, ou null.")
            if key == "tokens" and value is not None and type(value) is not int:
                raise ValueError("costs.tokens doit être un entier ou null.")
    reference = experience.get("reference_run")
    if not isinstance(reference, str) or reference not in by_id:
        raise ValueError("experience.reference_run doit désigner un essai.")
    decision = meta._object(experience.get("decision"), "experience.decision")
    meta._text(decision.get("reason"), "decision.reason")
    _nonempty_texts(decision.get("limitations"), "decision.limitations")
    outcome, selected = decision.get("outcome"), decision.get("selected_run")
    if outcome not in ("KEEP_BASE", "ADOPT", "INCONCLUSIVE"):
        raise ValueError("decision.outcome inconnu.")
    if outcome == "INCONCLUSIVE":
        if selected is not None:
            raise ValueError("INCONCLUSIVE ne désigne pas un essai retenu.")
    elif not isinstance(selected, str) or selected not in by_id or by_id[selected]["status"] != "PASS":
        raise ValueError("Un essai retenu exige un résultat déclaré PASS et référencé.")
    elif (outcome == "KEEP_BASE") != (selected == reference):
        raise ValueError("La décision doit distinguer référence et adaptation.")
    return True
