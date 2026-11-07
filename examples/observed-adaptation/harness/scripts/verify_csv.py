"""Auxiliaire illustratif : deux colonnes, score numérique fini, lignes complètes."""
import csv
import math
from pathlib import Path
import sys


def verify(path):
    with Path(path).open(newline="", encoding="utf-8") as stream:
        rows = csv.DictReader(stream)
        if rows.fieldnames != ["name", "score"]:
            raise ValueError("Colonnes attendues : name,score")
        for row in rows:
            if None in row or not row.get("name") or not row.get("score"):
                raise ValueError("Ligne incomplète ou colonnes supplémentaires")
            if not math.isfinite(float(row["score"])):
                raise ValueError("Score non fini")


if __name__ == "__main__":
    verify(sys.argv[1])
    print("PASS : format CSV contrôlé")
