"""Transformation CSV locale illustrant une compétence déterministe."""
import csv
import json
from pathlib import Path
import sys


def main():
    source, rules, output = map(Path, sys.argv[1:])
    with source.open(newline='', encoding='utf-8') as stream:
        rows = list(csv.reader(stream, strict=True))
    category = json.loads(rules.read_text())['category']
    if not isinstance(category, str) or not rows or 'category' not in rows[0] or len(set(rows[0])) != len(rows[0]) or any(len(row) != len(rows[0]) for row in rows):
        raise ValueError('CSV ou règles invalides')
    index = rows[0].index('category')
    selected = [rows[0]] + [row for row in rows[1:] if row[index] == category]
    with output.open('x', newline='', encoding='utf-8') as stream:
        csv.writer(stream).writerows(selected)


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, TypeError, KeyError, csv.Error) as error:
        print(str(error), file=sys.stderr)
        raise SystemExit(2)
