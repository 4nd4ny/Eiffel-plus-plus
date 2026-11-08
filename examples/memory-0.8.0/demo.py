#!/usr/bin/env python3
"""Sources fictives, aucun appel LLM ; écrire uniquement dans une destination neuve."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import memory


def demo(destination):
    destination = memory.meta._destination(Path(destination))
    destination.mkdir(parents=True)
    store = destination / "store"
    memory.init(store, "fictif", {"maintainers": ["owner"], "writers": ["worker"]})

    def change(ops, actor, reason):
        proposal = memory.propose(store, actor, ops, reason)
        return memory.apply(store, proposal, memory.meta.digest(memory.meta.canonical(proposal)), actor)

    obligation = "Préserver les accents des noms importés."
    temporary = "Pour le pilote uniquement, limiter chaque import à deux lignes."
    change([
        {"op": "source", "id": "business", "origin": "human", "locator": "fixture:brief", "text": obligation},
        {"op": "remember", "id": "R1", "kind": "requirement", "source": "business", "quote": obligation,
         "scope": ["*"], "depends_on": [], "basis": {}, "expires_at": None},
    ], "owner", "Enregistrer une exigence de la fixture, sans décision humaine réelle.")
    change([
        {"op": "source", "id": "pilot", "origin": "agent", "locator": "fixture:pilot", "text": temporary},
        {"op": "remember", "id": "T1", "kind": "choice", "source": "pilot", "quote": temporary,
         "scope": ["import"], "depends_on": [], "basis": {"phase": "pilot"}, "expires_at": None},
    ], "worker", "Choix temporaire de la fixture.")
    inputs = ("import", {"phase": "pilot"}, "Préparer le prochain import fictif.")
    before = memory.prepare(store, destination / "before", *inputs)
    change([
        {"op": "source", "id": "end", "origin": "agent", "locator": "fixture:end", "text": "Le choix de pilote est abandonné."},
        {"op": "retire", "id": "T1", "source": "end", "quote": "Le choix de pilote est abandonné."},
    ], "worker", "Retrait explicite du choix autonome.")
    old_rejected = False
    try:
        memory.launch_request(store, destination / "before", before["packet_sha256"], *inputs)
    except ValueError:
        old_rejected = True
    after = memory.prepare(store, destination / "after", *inputs)
    request = memory.launch_request(store, destination / "after", after["packet_sha256"], *inputs)
    content = json.loads(request["messages"][1]["content"])
    passed = old_rejected and [n["id"] for n in content["notes"]] == ["R1"] and temporary not in json.dumps(request, ensure_ascii=False)
    result = {"status": "PASS" if passed else "FAIL", "old_context_rejected": old_rejected,
              "requirements_preserved": after["required_ids"], "omitted": after["omitted"],
              "model_called": False, "limits": "Données et décisions fictives ; contrôle de contexte, pas benchmark LLM."}
    (destination / "result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    result = demo(parser.parse_args().destination)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["status"] == "PASS" else 1)
