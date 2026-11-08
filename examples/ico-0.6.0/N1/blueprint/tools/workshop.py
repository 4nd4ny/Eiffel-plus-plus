#!/usr/bin/env python3
"""Atelier local de copies complètes ; Eiffel++ 0.6.0, aucun appel de modèle.

Un reçu lie des octets, pas des identités. Le vérificateur est du code local
explicitement autorisé, pas du code hostile confiné. Ne jamais y fournir de secret.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True


def runtime(root):
    sys.path.insert(0, str(Path(root).resolve() / 'tools'))
    import meta_harness
    import skills
    import trials
    if meta_harness.VERSION not in ('0.6.0', '0.7.0'):
        raise ValueError('Runtime Eiffel++ 0.6.0 ou 0.7.0 requis.')
    return meta_harness, skills, trials


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def write(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def tree(meta, path):
    files = meta._snapshot(path)
    return {p: {'sha256': meta.digest(raw), 'executable': bool(files.modes[p] & 0o111)}
            for p, raw in files.items()}


def copy_tree(meta, trials, source, dest):
    before = tree(meta, source)
    if not before:
        raise ValueError('Source vide.')
    trials._copy(meta._snapshot(source), dest)
    if tree(meta, dest) != before or tree(meta, source) != before:
        raise ValueError('STALE : source modifiée pendant la copie.')


def contract_value(path):
    value = read(path)
    criteria = value.get('criteria')
    if (not isinstance(criteria, list) or not criteria
            or any(not isinstance(k, str) or not k.strip() for k in criteria)
            or len(set(criteria)) != len(criteria)):
        raise ValueError('Contrat : critères obligatoires distincts et non vides requis.')
    for field in ('scope', 'score_meaning', 'authority', 'excluded'):
        if not isinstance(value.get(field), str) or not value[field].strip():
            raise ValueError('Contrat incomplet : ' + field)
    return value


def open_lot(meta, trials, harness, code, checker, contract, dest, plan=None):
    """La sortie doit être neuve et disjointe des quatre entrées ; aucune écriture source."""
    meta.check_bundle(harness)
    contract_value(contract)
    if not (checker / 'check.py').is_file():
        raise ValueError('Le dossier de contrôles doit fournir check.py.')
    with trials._staging(dest, [harness, code, checker, contract, *([plan] if plan else [])]) as stage:
        for name, origin in [('harness', harness), ('baseline', code), ('work', code), ('checker', checker)]:
            copy_tree(meta, trials, origin, stage / name)
        meta._write(stage, 'contract.json', meta._read_file(contract))
        # Sans plan séparé, le contrat et le vérificateur constituent le plan minimal.
        meta._write(stage, 'plan.md', meta._read_file(plan or contract))
        # L'adaptateur fournit à trials.evaluate une fermeture déterministe de ses ressources.
        # Le chemin final (et non le staging temporaire) est incorporé dans le script figé.
        wrapper = ('import hashlib, json, runpy, sys\nfrom pathlib import Path\n'
                   'sys.dont_write_bytecode=True\n'
                   'root=Path(' + repr(str(dest.resolve() / 'checker')) + ')\n'
                   'expected=' + repr(tree(meta, stage / 'checker')) + '\n'
                   'actual={}\n'
                   'for p in root.rglob("*"):\n'
                   ' if p.is_symlink(): raise ValueError("STALE: lien dans les contrôles")\n'
                   ' if p.is_file(): actual[p.relative_to(root).as_posix()]={"sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"executable":bool(p.stat().st_mode & 0o111)}\n'
                   'if actual != expected: raise ValueError("STALE: contrôles modifiés")\n'
                   'sys.path.insert(0,str(root))\n'
                   'sys.argv=[str(root/"check.py"),sys.argv[1]]\n'
                   'runpy.run_path(str(root/"check.py"),run_name="__main__")\n')
        (stage / 'checker-bound.py').write_text(wrapper, encoding='utf-8')
        seal = {'format': 'ico-workshop-1', 'trees': {n: tree(meta, stage / n)
                for n in ('harness', 'baseline', 'checker')},
                'files': {n: sha(stage / n) for n in ('contract.json', 'plan.md', 'checker-bound.py')},
                'scope': contract_value(stage / 'contract.json')['scope']}
        write(stage / 'receipt.json', seal)
        anchor = sha(stage / 'receipt.json')
    return {'workspace': str(dest), 'anchor_sha256': anchor, 'status': 'PASS',
            'meaning': 'Copies et contrat identifiés ; qualité du produit NOT_RUN.'}


def verify(meta, workspace, anchor, candidate=None, candidate_anchor=None):
    def stale(message):
        raise ValueError('STALE : ' + message)
    meta._plain_path(workspace)
    if sha(workspace / 'receipt.json') != anchor:
        stale('référence du lot modifiée')
    seal = read(workspace / 'receipt.json')
    for name, expected in seal['trees'].items():
        if tree(meta, workspace / name) != expected:
            stale(name)
    for name, expected in seal['files'].items():
        if sha(workspace / name) != expected:
            stale(name)
    if candidate is not None:
        candidate = meta._plain_path(candidate)
        if sha(candidate / 'receipt.json') != candidate_anchor:
            stale('reçu candidat')
        receipt = read(candidate / 'receipt.json')
        if receipt['lot_anchor'] != anchor or receipt['code'] != tree(meta, candidate / 'code'):
            stale('candidat ou lot différent')
    return {'status': 'PASS', 'product_status': 'NOT_RUN'}


def freeze(meta, trials, workspace, anchor, dest):
    verify(meta, workspace, anchor)
    with trials._staging(dest, [workspace]) as stage:
        copy_tree(meta, trials, workspace / 'work', stage / 'code')
        verify(meta, workspace, anchor)
        write(stage / 'receipt.json', {'lot_anchor': anchor, 'code': tree(meta, stage / 'code')})
        candidate_anchor = sha(stage / 'receipt.json')
    return {'candidate': str(dest), 'candidate_sha256': candidate_anchor}


def evaluate(meta, trials, workspace, anchor, dest, candidate=None, candidate_anchor=None):
    verify(meta, workspace, anchor, candidate, candidate_anchor)
    artifact = candidate / 'code' if candidate else workspace / 'baseline'
    result = trials.evaluate(artifact, workspace / 'checker-bound.py', dest, timeout=45)
    verify(meta, workspace, anchor, candidate, candidate_anchor)
    required = set(contract_value(workspace / 'contract.json')['criteria'])
    if result['assessment'] and set(result['assessment']['criteria']) != required:
        result.update(status='UNKNOWN', error='Inventaire de critères différent du contrat figé.')
        write(dest / 'receipt.json', result)
    return dict(result, evaluation_sha256=sha(dest / 'receipt.json'))


def compare(meta, trials, workspace, anchor, evaluations, dest):
    """evaluations : liste (dossier, empreinte du reçu), référence d'abord."""
    verify(meta, workspace, anchor)
    if len(evaluations) < 2:
        raise ValueError('Référence et au moins un candidat requis.')
    required = set(contract_value(workspace / 'contract.json')['criteria'])
    for directory, expected in evaluations:
        if sha(directory / 'receipt.json') != expected:
            raise ValueError('STALE : reçu évaluation')
        result = read(directory / 'receipt.json')
        if result['checker_sha256'] != sha(workspace / 'checker-bound.py'):
            raise ValueError('STALE : contrôles étrangers au lot')
        if result['assessment'] and set(result['assessment']['criteria']) != required:
            if result['status'] != 'UNKNOWN':
                raise ValueError('STALE : critères changés')
    if tree(meta, evaluations[0][0] / 'artifact') != tree(meta, workspace / 'baseline'):
        raise ValueError('STALE : la première évaluation doit être celle de la référence complète')
    result = trials.select(evaluations[0][0], [p for p, _ in evaluations[1:]], dest)
    verify(meta, workspace, anchor)
    return dict(result, scope=read(workspace / 'contract.json')['scope'],
                product_adoption='NOT_RUN', note='Sélection expérimentale ; aucun déploiement ni fusion.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--eiffel', type=Path, required=True, help='Racine du runtime Eiffel++ 0.6.0 ou 0.7.0')
    sub = parser.add_subparsers(dest='action', required=True)
    op = sub.add_parser('open')
    for name in ('harness', 'code', 'checker', 'contract', 'output'):
        op.add_argument('--' + name, type=Path, required=True)
    op.add_argument('--plan', type=Path, help='Plan d’audit ; sans ce fichier, contrat et contrôles font office de plan minimal.')
    for action in ('verify', 'freeze', 'evaluate', 'compare'):
        p = sub.add_parser(action)
        p.add_argument('--workspace', type=Path, required=True)
        p.add_argument('--anchor', required=True)
        if action != 'verify':
            p.add_argument('--output', type=Path, required=True)
        if action in ('verify', 'evaluate'):
            p.add_argument('--candidate', type=Path)
            p.add_argument('--candidate-anchor')
        if action == 'compare':
            p.add_argument('--evaluation', nargs=2, action='append', required=True, metavar=('PATH', 'SHA256'))
    a = parser.parse_args()
    meta, _, trials = runtime(a.eiffel)
    if a.action == 'open':
        result = open_lot(meta, trials, a.harness, a.code, a.checker, a.contract, a.output, a.plan)
    elif a.action == 'verify':
        result = verify(meta, a.workspace, a.anchor, a.candidate, a.candidate_anchor)
    elif a.action == 'freeze':
        result = freeze(meta, trials, a.workspace, a.anchor, a.output)
    elif a.action == 'evaluate':
        result = evaluate(meta, trials, a.workspace, a.anchor, a.output, a.candidate, a.candidate_anchor)
    else:
        result = compare(meta, trials, a.workspace, a.anchor, [(Path(p), s) for p, s in a.evaluation], a.output)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, KeyError) as exc:
        print(json.dumps({'status': 'UNKNOWN', 'error': str(exc)}, ensure_ascii=False), file=sys.stderr)
        sys.exit(2)
