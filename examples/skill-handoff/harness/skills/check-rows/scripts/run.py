"""Oracle illustratif indépendant du script de production, même auteur."""
import csv
import json
from pathlib import Path
import sys


def read(path):
    with path.open(newline='', encoding='utf-8') as stream:
        rows = list(csv.reader(stream, strict=True))
    if not rows or 'category' not in rows[0] or len(set(rows[0])) != len(rows[0]) or any(len(row) != len(rows[0]) for row in rows):
        raise ValueError('CSV irrégulier')
    return rows


def main():
    source, rules, candidate, output = map(Path, sys.argv[1:])
    result = {'status': 'UNKNOWN', 'criteria': {}, 'scope': 'Transformation CSV locale ; pas de décision de livraison'}
    code = 2
    try:
        original = read(source)
        category = json.loads(rules.read_text())['category']
        if not isinstance(category, str):
            raise ValueError('Catégorie non textuelle')
        try:
            actual = read(candidate)
            wanted = [original[0]]
            for row in original[1:]:
                if dict(zip(original[0], row))['category'] == category:
                    wanted.append(row)
            good = actual == wanted
        except (ValueError, csv.Error):
            good = False
        result.update(status='PASS' if good else 'FAIL', criteria={'exact_rows': 'PASS' if good else 'FAIL'})
        code = 0 if good else 1
    except (OSError, ValueError, TypeError, KeyError, csv.Error) as error:
        result['error'] = str(error)
    with output.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2)
        stream.write('\n')
    return code


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except OSError as error:
        print(str(error), file=sys.stderr)
        raise SystemExit(2)
