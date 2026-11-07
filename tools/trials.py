#!/usr/bin/env python3
"""Essais locaux explicites et sélection conservatrice, sans appel de modèle.

Exécute du Python autorisé : ce programme n'est PAS un confinement de code hostile.
Les reçus relient les observations aux octets ; ils ne sont pas des signatures.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tempfile
import time

import meta_harness as meta
from seeds import artifact_digest


BOOTSTRAP = """
import hashlib, os, sys
path, fd = sys.argv[1], int(sys.argv[2])
with open(path, 'rb') as stream:
    raw = stream.read()
code = compile(raw, path, 'exec')
os.write(fd, hashlib.sha256(raw).hexdigest().encode('ascii'))
os.close(fd)
sys.argv = [path] + sys.argv[3:]
sys.path.insert(0, os.path.dirname(os.path.abspath(path)))
exec(code, {'__name__': '__main__', '__file__': path, '__builtins__': __builtins__})
"""


def _copy(files, destination):
    destination.mkdir(parents=True, exist_ok=True)
    for path, raw in files.items():
        meta._write(destination, path, raw, files.modes[path])


@contextmanager
def _staging(destination, origins):
    destination = meta._plain_path(destination)
    if os.path.lexists(destination):
        raise FileExistsError(f"La destination existe déjà : {destination}")
    for origin in origins:
        origin = meta._plain_path(origin)
        if destination == origin or origin in destination.parents or destination in origin.parents:
            raise ValueError("La destination doit être distincte des sources et des reçus.")
    destination.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix=".eiffel-trial-", dir=destination.parent))
    try:
        yield stage
        meta._publish(stage, destination, "receipt.json")
    finally:
        if stage.exists():
            shutil.rmtree(stage)


def _execute(argv, cwd, stage, timeout, pass_fds=()):
    if os.name != "posix":
        raise ValueError("L'exécuteur local requiert POSIX pour gérer les groupes de processus.")
    if not meta._finite_number(timeout) or timeout <= 0:
        raise ValueError("Le délai doit être fini et strictement positif.")
    scratch = stage / "scratch"
    scratch.mkdir()
    env = {"PATH": os.defpath + os.pathsep + os.environ.get("PATH", ""),
           "LANG": "C.UTF-8", "TZ": "UTC", "PYTHONNOUSERSITE": "1",
           "TMPDIR": str(scratch), "PYTHONDONTWRITEBYTECODE": "1"}
    start = time.monotonic()
    code, error, status = None, "", "UNKNOWN"
    with (stage / "stdout.txt").open("wb") as out, (stage / "stderr.txt").open("wb") as err:
        try:
            process = subprocess.Popen(argv, cwd=cwd, env=env, stdin=subprocess.DEVNULL,
                                       stdout=out, stderr=err, start_new_session=True,
                                       pass_fds=pass_fds)
            try:
                code = process.wait(timeout=timeout)
                status = "PASS" if code == 0 else "FAIL"
            except subprocess.TimeoutExpired:
                error = "timeout"
            finally:
                # Also terminate descendants left behind after a parent's normal exit.
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                process.wait()
        except OSError as exc:
            error = f"{type(exc).__name__}: {exc}"
    return {"status": status, "exitcode": code, "error": error,
            "seconds": time.monotonic() - start, "timeout_seconds": timeout}


def probe(bundle, component_id, destination, *, args=(), timeout=30):
    files = meta._snapshot(bundle)
    _, manifest, _ = meta._validate_bundle(files)
    found = [c for c in manifest.get("components", []) if c["id"] == component_id]
    if not found or found[0]["kind"] != "script":
        raise ValueError("probe exige un composant script déclaré ; une procédure texte reste non vérifiée.")
    component = found[0]
    expected = meta.digest(files[component["path"]])
    with _staging(destination, [bundle]) as stage:
        _copy(files, stage / "work")
        read_fd, write_fd = os.pipe()
        try:
            try:
                execution = _execute(
                    [sys.executable, "-I", "-c", BOOTSTRAP, component["path"], str(write_fd), *args],
                    stage / "work", stage, timeout, (write_fd,))
            finally:
                os.close(write_fd)
            observed = os.read(read_fd, 65).decode("ascii", errors="replace")
        finally:
            os.close(read_fd)
        receipt = {"format": "eiffel-probe-1", "component": component_id,
                   "component_path": component["path"], "component_sha256": expected,
                   "bundle_sha256": artifact_digest(files), "observed_sha256": observed or None,
                   "activation_status": "PASS" if observed == expected else "UNKNOWN",
                   "execution": execution, "behavior_status": "NOT_RUN", "args": list(args),
                   "scope": "Octets lus et compilés par le lanceur avant exec ; aucune preuve d'obéissance LLM."}
        meta._write_json(stage, "receipt.json", receipt)
    return receipt


def check_probe(bundle, receipt_dir):
    receipt_path = meta._plain_path(Path(receipt_dir) / "receipt.json")
    if not receipt_path.exists():
        return {"activation_status": "NOT_RUN", "reason": "Aucun reçu de lancement fourni."}
    receipt = meta._json(meta._read_file(receipt_path), "probe")
    if receipt.get("format") != "eiffel-probe-1":
        raise ValueError("Reçu de lancement attendu.")
    files = meta._snapshot(bundle)
    if artifact_digest(files) != receipt.get("bundle_sha256"):
        return {"activation_status": "STALE", "reason": "Le paquet a changé depuis le lancement."}
    path = meta._relative(receipt.get("component_path"), "component_path")
    sha = meta.digest(files[path]) if path in files else None
    if not sha or sha != receipt.get("component_sha256") or sha != receipt.get("observed_sha256"):
        return {"activation_status": "UNKNOWN", "reason": "Lancement exact non établi."}
    return {"activation_status": "PASS", "execution": receipt["execution"],
            "behavior_status": "NOT_RUN"}


def _assessment(raw):
    value = meta._json(raw, "Sortie du vérificateur")
    criteria = meta._object(value.get("criteria"), "criteria")
    if not criteria or any(not isinstance(k, str) or not k.strip() or
                           v not in ("PASS", "FAIL", "UNKNOWN") for k, v in criteria.items()):
        raise ValueError("criteria doit contenir des critères nommés PASS, FAIL ou UNKNOWN.")
    score = value.get("score")
    if not meta._finite_number(score) or score < 0:
        raise ValueError("score doit être un nombre fini positif ou nul, hors booléen.")
    return {"criteria": criteria, "score": score}


def evaluate(artifact, checker, destination, *, timeout=30):
    files = meta._snapshot(artifact)
    if not files:
        raise ValueError("Artefact vide.")
    checker_raw = meta._read_file(checker)
    before = artifact_digest(files)
    with _staging(destination, [artifact, checker]) as stage:
        _copy(files, stage / "artifact")
        meta._write(stage, "checker.py", checker_raw)
        # The checker has a separate cwd; generated checker files cannot alter the artifact implicitly.
        (stage / "checker-work").mkdir()
        execution = _execute([sys.executable, "-I", str(stage / "checker.py"), str(stage / "artifact")],
                             stage / "checker-work", stage, timeout)
        assessment, error = None, ""
        if execution["status"] == "PASS":
            try:
                assessment = _assessment(meta._read_file(stage / "stdout.txt"))
            except ValueError as exc:
                error = str(exc)
        try:
            unchanged = artifact_digest(meta._snapshot(stage / "artifact")) == before
        except (OSError, ValueError):
            unchanged = False
        checker_unchanged = meta.digest(meta._read_file(stage / "checker.py")) == meta.digest(checker_raw)
        status = "UNKNOWN"
        if not unchanged or not checker_unchanged:
            status = "STALE"
        elif assessment:
            values = assessment["criteria"].values()
            status = "FAIL" if "FAIL" in values else "UNKNOWN" if "UNKNOWN" in values else "PASS"
        receipt = {"format": "eiffel-evaluation-1", "artifact_sha256": before,
                   "checker_sha256": meta.digest(checker_raw), "execution": execution,
                   "status": status, "assessment": assessment, "error": error,
                   "scope": "Vérificateur fourni explicitement ; aucune authenticité ni isolation hostile garantie."}
        meta._write_json(stage, "receipt.json", receipt)
    return receipt


def _evaluation(directory):
    directory = meta._plain_path(directory)
    receipt = meta._json(meta._read_file(directory / "receipt.json"), "evaluation")
    if receipt.get("format") != "eiffel-evaluation-1":
        raise ValueError("Reçu d'évaluation attendu.")
    if meta.digest(meta._read_file(directory / "checker.py")) != receipt.get("checker_sha256"):
        raise ValueError("Vérificateur modifié depuis l'évaluation.")
    files = meta._snapshot(directory / "artifact")
    if artifact_digest(files) != receipt.get("artifact_sha256"):
        raise ValueError("Artefact modifié depuis l'évaluation.")
    eligible = False
    if receipt.get("status") == "PASS" and receipt.get("execution", {}).get("status") == "PASS":
        assessment = _assessment(meta.canonical(receipt.get("assessment")))
        # Re-read the actual checker output too; a label edited in receipt.json cannot promote it.
        if assessment != _assessment(meta._read_file(directory / "stdout.txt")):
            raise ValueError("Évaluation différente de la sortie du vérificateur.")
        eligible = all(v == "PASS" for v in assessment["criteria"].values())
    return receipt, files, eligible


def select(baseline, candidates, destination):
    directories = [meta._plain_path(d) for d in [baseline, *candidates]]
    if len(set(directories)) != len(directories):
        raise ValueError("Les reçus doivent être distincts.")
    loaded = [_evaluation(d) for d in directories]
    if len({r["checker_sha256"] for r, _, _ in loaded}) != 1:
        raise ValueError("Le même vérificateur doit évaluer tous les candidats et la référence.")
    eligible = [(i, r, f) for i, (r, f, ok) in enumerate(loaded) if ok]
    if len({tuple(sorted(r["assessment"]["criteria"])) for _, r, _ in eligible}) > 1:
        raise ValueError("Les candidats admissibles ne partagent pas les mêmes critères.")
    # max is stable: the baseline wins equal scores, with no invented cost trade-off.
    chosen = max(eligible, key=lambda item: item[1]["assessment"]["score"], default=None)
    with _staging(destination, directories) as stage:
        decision = {"format": "eiffel-selection-1", "outcome": "INCONCLUSIVE",
                    "selected_index": None, "artifact_sha256": None,
                    "evaluations": [r for r, _, _ in loaded],
                    "policy": "Tous les critères obligatoires PASS, score maximal ; égalité en faveur de la référence."}
        if chosen:
            index, receipt, files = chosen
            _copy(files, stage / "artifact")
            if artifact_digest(meta._snapshot(stage / "artifact")) != receipt["artifact_sha256"]:
                raise ValueError("La copie sélectionnée diffère de l'artefact évalué.")
            decision.update(outcome="KEEP_BASE" if index == 0 else "ADOPT", selected_index=index,
                            artifact_sha256=receipt["artifact_sha256"])
        meta._write_json(stage, "receipt.json", decision)
    return decision


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("probe", help="Exécuter explicitement un composant script autorisé.")
    p.add_argument("bundle", type=Path)
    p.add_argument("--component", required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--timeout", type=float, default=30)
    p.add_argument("--arg", action="append", default=[])
    p = sub.add_parser("check-probe")
    p.add_argument("bundle", type=Path)
    p.add_argument("receipt", type=Path)
    p = sub.add_parser("evaluate", help="Exécuter le vérificateur Python explicitement fourni.")
    p.add_argument("artifact", type=Path)
    p.add_argument("--checker", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--timeout", type=float, default=30)
    p = sub.add_parser("select")
    p.add_argument("--baseline", type=Path, required=True)
    p.add_argument("--candidate", type=Path, action="append", default=[])
    p.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == "probe":
            result = probe(args.bundle, args.component, args.output, args=args.arg, timeout=args.timeout)
        elif args.command == "check-probe":
            result = check_probe(args.bundle, args.receipt)
        elif args.command == "evaluate":
            result = evaluate(args.artifact, args.checker, args.output, timeout=args.timeout)
        else:
            result = select(args.baseline, args.candidate, args.output)
    except (OSError, ValueError) as exc:
        parser.exit(2, f"Essai interrompu : {exc}\n")
    print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
