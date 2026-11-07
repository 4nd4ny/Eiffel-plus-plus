#!/usr/bin/env python3
"""Sélection déterministe de compétences ; aucune inférence métier implicite."""
import argparse
import json
from pathlib import Path
import shutil

MODES = {'full': (None, 'Atelier complet : moteur et interface disponibles, chargés selon le lot.'),
         'import': ('modifier-interface', 'Lot Import : compétence UI retirée ; contrats de format et erreurs actifs.'),
         'interface': ('modifier-moteur', 'Lot Interface : compétence moteur retirée ; navigateur requis et absent de cet exemple.')}

def generate(mode, output):
    source = Path(__file__).resolve().parent / 'blueprint'
    output = Path(output).absolute()
    if output.exists() or output.is_symlink():
        raise ValueError('Destination nouvelle requise.')
    for p in (output, *output.parents):
        if p.is_symlink():
            raise ValueError('Destination sans lien requise.')
    if source == output or source in output.parents or output in source.parents:
        raise ValueError('Destination extérieure au blueprint requise.')
    removed, reason = MODES[mode]
    shutil.copytree(source, output)
    manifest = json.loads((output/'harness.json').read_text())
    if removed:
        shutil.rmtree(output/'skills'/removed)
        manifest['components'] = [c for c in manifest['components'] if c['id'] != removed]
        manifest['capabilities'] = [c for c in manifest['capabilities'] if c.get('skill') != removed]
    (output/'harness.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n')
    with (output/'DESIGN.md').open('a') as stream:
        stream.write('\n## Choix de cette génération\n\n'+reason+' Les quatre responsabilités sont conservées. La couverture réelle sera fixée dans le contrat du lot ; aucun contrôle manquant ne devient PASS.\n')
    (output/'LOT.md').write_text('# Mode '+mode+'\n\n'+reason+'\n')
    return output

if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--mode', choices=MODES, required=True)
    p.add_argument('--output', type=Path, required=True)
    a=p.parse_args(); print(generate(a.mode,a.output))
