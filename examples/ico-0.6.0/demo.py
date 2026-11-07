#!/usr/bin/env python3
"""Cas public reproductible, six missions et six remises, sans appel de modèle."""
import argparse
import importlib.util
import json
from pathlib import Path
import sys
import time

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def workflow(eiffel, harness, code, checker, contract, output, change=None):
    w = load(harness / 'tools/workshop.py', 'workshop')
    meta, skills, trials = w.runtime(eiffel)
    output.mkdir(parents=True, exist_ok=False)
    start = time.perf_counter()
    records = []
    def file(name, content):
        p = output / name
        p.write_text(content, encoding='utf-8')
        return p
    def mission(name, role, inputs):
        dest = output / ('mission-' + name)
        receipt = skills.prepare(harness, name, role, inputs, dest)
        records.append({'skill': name, 'role': role, 'order_sha256': receipt['order_sha256']})
        return dest, receipt['order_sha256']
    def handoff(order, role, outputs):
        path, anchor = order
        destination = output / ('remise-' + path.name)
        skills.handoff(path, role, outputs, destination, anchor)
        records[-1]['handoff'] = role
        return {key: destination / 'outputs' / key for key in outputs}

    request = file('request.md', 'Exercer le cycle sur une copie ; sélectionner seulement selon le contrat fourni.\n')
    m = mission('orchestrer-lot', 'governance', {'request': request})
    mandate = file('mandate.md', 'Une référence, un candidat, deux cycles au plus. Auto-examen. Aucune adoption produit.\n')
    mandate = handoff(m, 'stbl', {'mandate': mandate})['mandate']
    m = mission('specifier-contrat', 'stbl', {'mandate': mandate})
    bound_contract = file('contract.json', contract.read_text())
    bound_contract = handoff(m, 'audit', {'contract': bound_contract})['contract']
    m = mission('planifier-audit', 'audit', {'contract': bound_contract})
    plan = file('plan.md', 'Exécuter check.py sur référence et candidat complet ; garder exactement les critères du contrat.\n'
                'Contrôles figés et limites dans contract.json. Les défauts injectés sont exercés par la qualification séparée.\n')
    plan = handoff(m, 'product', {'plan': plan})['plan']
    lot = output / 'lot'
    opened = w.open_lot(meta, trials, harness, code, checker, bound_contract, lot, plan)
    anchor = opened['anchor_sha256']
    m = mission('modifier-moteur', 'product', {'contract': bound_contract, 'plan': plan}) if change else None
    if change:
        change(lot / 'work')
    candidate = output / 'candidate'
    frozen = w.freeze(meta, trials, lot, anchor, candidate)
    rationale = file('rationale.md', ('Changement local décrit par le scénario ; les autres fichiers sont conservés.\n'
                     if change else 'Référence inchangée : l’égalité doit conserver la base.\n')
                     + 'La sélection demeure limitée aux critères fournis ; aucune preuve du système complet.\n')
    pieces = {'candidate': candidate / 'receipt.json', 'rationale': rationale}
    delivered = handoff(m, 'audit', pieces) if m else pieces
    m = mission('verifier-candidat', 'audit', delivered)
    baseline = w.evaluate(meta, trials, lot, anchor, output / 'eval-baseline')
    result = w.evaluate(meta, trials, lot, anchor, output / 'eval-candidate', candidate, frozen['candidate_sha256'])
    report = file('report.json', json.dumps({'baseline': baseline, 'candidate': result}, ensure_ascii=False, indent=2))
    report = handoff(m, 'governance', {'report': report})['report']
    m = mission('decider-livraison', 'governance', {'report': report})
    decision = w.compare(meta, trials, lot, anchor,
                         [(output / 'eval-baseline', baseline['evaluation_sha256']),
                          (output / 'eval-candidate', result['evaluation_sha256'])], output / 'selection')
    decision_path = file('decision.json', json.dumps(decision, ensure_ascii=False, indent=2))
    # La dernière remise retourne au Produit la décision technique ; pas une autorisation de déployer.
    handoff(m, 'product', {'decision': decision_path})
    summary = {'outcome': decision['outcome'], 'missions': records,
               'native_capabilities': [] if change else ['Produit identifie et fige la référence sans compétence d’édition.'],
               'source_files': len(w.tree(meta, code)), 'selected_files': len(w.tree(meta, output / 'selection/artifact')) if decision['outcome'] != 'INCONCLUSIVE' else 0,
               'seconds': time.perf_counter() - start, 'model_calls': 0,
               'model_cost_usd': 0, 'design_model_cost_usd': None,
               'audit_independence': 'AUTO_EXAMEN', 'product_adoption': 'NOT_RUN',
               'lot_anchor': anchor, 'candidate_anchor': frozen['candidate_sha256']}
    w.write(output / 'summary.json', summary)
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--eiffel', type=Path, default=ROOT.parents[1])
    args = parser.parse_args()
    def change(code):
        path = code / 'normalize.py'
        path.write_text(path.read_text().replace('v.strip()', 'v.strip().lower()'))
    print(json.dumps(workflow(args.eiffel, ROOT / 'N0', ROOT / 'fixtures/code',
                             ROOT / 'fixtures/checker', ROOT / 'fixtures/contract.json',
                             args.output, change), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
