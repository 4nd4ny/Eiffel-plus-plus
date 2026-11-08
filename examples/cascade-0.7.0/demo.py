#!/usr/bin/env python3
"""Exemple fictif du journal ; ne constitue ni expérience LLM ni accord humain."""
import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
import cascade


def run(destination):
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=False)
    journal = destination / "journal"
    cascade.start(journal)
    report = {"kind": "synthetic-fixture", "human_review": "SIMULATED_FOR_TEST_ONLY", "levels": []}
    for level in (2, 1, 0):
        for iteration in (1, 2):
            bundle = destination / f"n{level}-{iteration}"
            bundle.mkdir()
            (bundle / "scope.md").write_text("Cas fictif : conserver l'ordre d'une liste lors du retrait des doublons.\n")
            (bundle / "evidence.md").write_text("Sonde fictive de dossier, pas un essai produit : couverture et entrées présentes.\n")
            (bundle / "DESIGN.md").write_text("L'exemple montre le passage gardé. Aucun modèle ni besoin client n'est qualifié.\n")
            data = {"level": level, "purpose": "Tester la cohérence du dossier de passage fictif.",
                    "criteria": {"scope-covered": "PASS"}, "evidence": ["evidence.md"],
                    "coverage": [{"requirement": "REQ-demo", "criterion": "scope-covered"}],
                    "required_inputs": [{"id": "scope", "status": "AVAILABLE", "source": "scope.md"}],
                    "blocking_unknowns": [], "observation": "Dossier fictif complet.",
                    "hypothesis": "Un dossier cohérent sans réponse doit rester inconclusif.",
                    "change": "Maintenir le candidat pour éprouver la porte.",
                    "novelty": ["Premier dossier"] if iteration == 1 else [],
                    "stability_probe": "Revue fictive des mêmes obligations.",
                    "limits": ["Fixture synthétique : aucun humain ni modèle évalué."]}
            (bundle / "cycle.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
            event = cascade.cycle(journal, bundle)
        before = cascade.gate(journal)
        assert before["verdict"] == "INCONCLUSIVE"
        response = destination / f"response-n{level}.md"
        response.write_text("FIXTURE SYNTHÉTIQUE — décision simulée uniquement pour tester le programme.\n")
        cascade.review(journal, event["event_sha256"], "DESCEND" if level else "ACCEPT", "synthetic-test-fixture", response)
        after = cascade.gate(journal)
        assert after["verdict"] == "READY"
        cascade.advance(journal)
        report["levels"].append({"level": level, "before": before["verdict"], "after": after["verdict"]})
    report["journal"] = cascade.verify(journal)
    (destination / "result.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    print(json.dumps(run(parser.parse_args().destination), ensure_ascii=False, indent=2))
