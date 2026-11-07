"""Oracle synthétique public ; aucun code ICO."""
import importlib.util
import json
from pathlib import Path
import sys

spec = importlib.util.spec_from_file_location('candidate', Path(sys.argv[1]) / 'normalize.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
rejects = True
for value in (None, 'text', [1]):
    try:
        module.normalize(value)
        rejects = False
    except ValueError:
        pass
same_count = module.normalize([]) == [] and len(module.normalize([' A ', 'b'])) == 2
print(json.dumps({'criteria': {'invalid-input': 'PASS' if rejects else 'FAIL',
                               'preserve-count': 'PASS' if same_count else 'FAIL'},
                  'score': int(module.normalize([' A ']) == ['a'])}))
