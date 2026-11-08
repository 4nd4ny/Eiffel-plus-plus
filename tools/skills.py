#!/usr/bin/env python3
"""Capacités, missions et remises locales ; aucun agent ni script lancé implicitement."""
from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath
import re

import meta_harness as meta
from trials import _staging

IDENTIFIER = r"[a-z0-9]+(?:-[a-z0-9]+)*"


def identifier(value):
    value = meta._text(value, 'identifiant de skill ou de port')
    if len(value) > 64 or not re.fullmatch(IDENTIFIER, value):
        raise ValueError('Identifiant attendu : 1 à 64 minuscules, chiffres ou tirets.')
    return value


def skill_header(raw):
    """Sous-ensemble explicite : name et description YAML monolignes, scalaires simples."""
    text = raw.decode('utf-8')
    parts = re.fullmatch(r'---\r?\n(.*?)\r?\n---\r?\n(.+)', text, re.DOTALL)
    if parts is None or not parts[2].strip():
        raise ValueError('SKILL.md exige un frontmatter et une méthode non vide.')
    header = {}
    for line in parts[1].splitlines():
        match = re.fullmatch(r'(name|description):\s*(.+)', line)
        if not match:
            continue
        key, value = match.groups()
        if key in header:
            raise ValueError('Champ de skill répété : ' + key)
        if value.startswith('"'):
            value = json.loads(value)
        elif value.startswith("'") and value.endswith("'"):
            value = value[1:-1].replace("''", "'")
        elif value in ('|', '>') or value.startswith(('[', '{', '&', '*', '!')) or ': ' in value or ' #' in value:
            raise ValueError('name et description : texte YAML monoligne simple ou chaîne JSON requise.')
        header[key] = meta._text(value, 'skill.' + key)
    identifier(header.get('name'))
    meta._text(header.get('description'), 'skill.description')
    if len(header['description']) > 1024:
        raise ValueError('skill.description : 1024 caractères maximum.')
    return header


def validate_capabilities(files, manifest):
    skills = {c['id']: c for c in manifest.get('components', []) if c['kind'] == 'skill'}
    if manifest['schema_version'] not in ('0.5.0', '0.6.0', '0.7.0'):
        if 'capabilities' in manifest or skills:
            raise ValueError('Les capacités explicites exigent schema_version 0.5.0, 0.6.0 ou 0.7.0.')
        return
    capabilities = manifest.get('capabilities')
    if not isinstance(capabilities, list) or not capabilities:
        raise ValueError('capabilities doit couvrir les tâches des quatre responsabilités.')
    covered, used, tasks = set(), set(), set()
    for item in capabilities:
        item = meta._object(item, 'capability')
        role, task = item.get('role'), meta._text(item.get('task'), 'capability.task')
        if role not in meta.ROLES:
            raise ValueError('Responsabilité inconnue dans capabilities.')
        if (role, task) in tasks:
            raise ValueError('Tâche répétée pour la même responsabilité.')
        tasks.add((role, task))
        covered.add(role)
        forms = set(item) & {'skill', 'native', 'unavailable'}
        if len(forms) != 1 or set(item) != {'role', 'task'} | forms:
            raise ValueError('Une capacité exige exactement skill, native ou unavailable, avec role et task.')
        form = forms.pop()
        value = meta._text(item[form], 'capability.' + form)
        if form == 'skill':
            if value not in skills:
                raise ValueError('Skill attribué absent : ' + value)
            used.add(value)
    if covered != set(meta.ROLES):
        raise ValueError('capabilities doit couvrir les quatre responsabilités, y compris les moyens manquants.')
    if used != set(skills):
        raise ValueError('Un skill embarqué doit servir une tâche attribuée ; retirer les skills inutilisés.')
    for key, skill in skills.items():
        identifier(key)
        path = PurePosixPath(skill['path'])
        if path.name != 'SKILL.md' or path.parent.name != key:
            raise ValueError('Un skill utilise <id>/SKILL.md.')
        header = skill_header(files[skill['path']])
        if header['name'] != key:
            raise ValueError('Le nom du skill diffère de component.id.')
        for field in ('inputs', 'outputs'):
            ports = skill[field]
            for port in ports:
                identifier(port)
            if len(set(ports)) != len(ports):
                raise ValueError('Ports répétés : ' + field)
        recipients = meta._texts(skill.get('handoff_to'), 'skill.handoff_to')
        if not recipients or len(set(recipients)) != len(recipients) or set(recipients) - set(meta.ROLES):
            raise ValueError('handoff_to doit désigner des responsabilités distinctes et connues.')


def catalogue(bundle, role=None):
    files = meta._snapshot(bundle)
    _, manifest, _ = meta._validate_bundle(files)
    if role is not None and role not in meta.ROLES:
        raise ValueError('Responsabilité inconnue.')
    selected = [c for c in manifest.get('capabilities', []) if role is None or c['role'] == role]
    skills = {c['id']: c for c in manifest.get('components', []) if c['kind'] == 'skill'}
    return {'capabilities': selected, 'skills': [
        dict(id=key, path=skills[key]['path'], trigger=skills[key]['trigger'],
             **skill_header(files[skills[key]['path']]))
        for key in sorted({c['skill'] for c in selected if 'skill' in c})],
        'execution_status': 'NOT_RUN'}


def _bindings(bindings, ports):
    if set(bindings) != set(ports):
        raise ValueError('Les pièces doivent correspondre exactement aux ports : ' + ', '.join(ports))
    result = {}
    for key, path in bindings.items():
        path = meta._plain_path(path)
        raw = meta._read_file(path)
        result[key] = (path, raw)
    return result


def prepare(bundle, skill_id, role, inputs, destination):
    bundle = meta._plain_path(bundle)
    files = meta._snapshot(bundle)
    name, manifest, _ = meta._validate_bundle(files)
    if manifest['level'] != 0 or manifest['status'] not in ('PROPOSED', 'ACCEPTED'):
        raise ValueError('Une mission exige un N0 utilisable ; N1 reste un générateur.')
    if not any(c['role'] == role and c.get('skill') == skill_id for c in manifest.get('capabilities', [])):
        raise ValueError('Skill non attribué à cette responsabilité.')
    skill = next(c for c in manifest['components'] if c['id'] == skill_id)
    bound = _bindings(inputs, skill['inputs'])
    role_path = (manifest['responsibilities'][role] if manifest.get('layout') == 'single-repo'
                 else manifest['repositories'][role] + '/AGENTS.md')
    paths = {name, manifest['profile'], role_path, skill['path'], *skill['dependencies']}
    if 'entrypoint' in manifest:
        paths.add(manifest['entrypoint'])
    if 'design_rationale' in manifest:
        paths.add(manifest['design_rationale'])
    with _staging(destination, [bundle, *(p for p, _ in bound.values())]) as stage:
        for path in sorted(paths):
            meta._write(stage, 'resources/' + path, files[path], files.modes[path])
        for key, (_, raw) in bound.items():
            meta._write(stage, 'inputs/' + key, raw)
        receipt = {'format': 'eiffel-skill-order-1', 'bundle': str(bundle), 'role': role,
                   'skill': skill_id, 'entrypoint': 'resources/' + skill['path'],
                   'design_rationale': ('resources/' + manifest['design_rationale']) if 'design_rationale' in manifest else None,
                   'resources': {p: meta.digest(files[p]) for p in sorted(paths)},
                   'inputs': {k: {'source': str(p), 'sha256': meta.digest(raw)} for k, (p, raw) in bound.items()},
                   'outputs': skill['outputs'], 'handoff_to': skill['handoff_to'],
                   'execution_status': 'NOT_RUN', 'semantic_status': 'NOT_RUN',
                   'note': 'Mission préparée, ni permission nouvelle ni preuve de compétence. Lire les préconditions du skill.'}
        meta._write_json(stage, 'receipt.json', receipt)
        order_sha256 = meta.digest(meta._read_file(stage / 'receipt.json'))
        if verify(stage, order_sha256)['validity_status'] != 'PASS':
            raise ValueError('STALE : ressources modifiées pendant la préparation.')
    return dict(receipt, order_sha256=order_sha256)


def verify(order, expected_sha256):
    order = meta._plain_path(order)
    raw = meta._read_file(order / 'receipt.json')
    if not isinstance(expected_sha256, str) or not re.fullmatch('[a-f0-9]{64}', expected_sha256):
        raise ValueError('Empreinte de mission attendue requise, issue de sa préparation.')
    if meta.digest(raw) != expected_sha256:
        return {'validity_status': 'STALE', 'changed': ['receipt.json'],
                'execution_status': 'NOT_RUN', 'semantic_status': 'NOT_RUN'}
    receipt = meta._json(raw, 'mission')
    if receipt.get('format') != 'eiffel-skill-order-1':
        raise ValueError('Mission de skill attendue.')
    changes = []
    # Refuser aussi un module ajouté au contexte copié : il pourrait être importé
    # sans modifier les octets d'un script déjà déclaré.
    for folder, expected in (('resources', set(receipt['resources'])), ('inputs', set(receipt['inputs']))):
        try:
            if set(meta._snapshot(order / folder)) != expected:
                changes.append(folder + ' : inventaire modifié')
        except (OSError, ValueError):
            changes.append(folder + ' : inventaire illisible')
    for path, expected in receipt['resources'].items():
        meta._relative(path, 'resource')
        for actual in (Path(receipt['bundle']) / path, order / 'resources' / path):
            try:
                if meta.digest(meta._read_file(actual)) != expected:
                    changes.append(str(actual))
            except (OSError, ValueError):
                changes.append(str(actual))
    for key, value in receipt['inputs'].items():
        identifier(key)
        for actual in (Path(value['source']), order / 'inputs' / key):
            try:
                if meta.digest(meta._read_file(actual)) != value['sha256']:
                    changes.append(str(actual))
            except (OSError, ValueError):
                changes.append(str(actual))
    return {'validity_status': 'STALE' if changes else 'PASS', 'changed': changes,
            'execution_status': 'NOT_RUN', 'semantic_status': 'NOT_RUN'}


def handoff(order, recipient, outputs, destination, expected_sha256):
    result = verify(order, expected_sha256)
    if result['validity_status'] != 'PASS':
        raise ValueError('STALE : mission, entrées ou contrôles modifiés ; nouvelle qualification requise.')
    receipt = meta._json(meta._read_file(Path(order) / 'receipt.json'), 'mission')
    if recipient not in receipt['handoff_to']:
        raise ValueError('Destinataire absent du contrat de remise.')
    bound = _bindings(outputs, receipt['outputs'])
    with _staging(destination, [order, *(p for p, _ in bound.values())]) as stage:
        for key, (_, raw) in bound.items():
            meta._write(stage, 'outputs/' + key, raw)
        # Relever aussi les changements intervenus pendant la préparation de la remise.
        if verify(order, expected_sha256)['validity_status'] != 'PASS':
            raise ValueError('STALE : mission modifiée pendant la remise.')
        result = {'format': 'eiffel-skill-handoff-1', 'from_role': receipt['role'], 'to_role': recipient,
                  'skill': receipt['skill'], 'order_sha256': expected_sha256,
                  'outputs': {k: meta.digest(raw) for k, (_, raw) in bound.items()},
                  'handoff_recorded': True, 'semantic_status': 'NOT_RUN',
                  'note': 'Pièces conservées pour examen ; leur existence ne constitue pas un verdict.'}
        meta._write_json(stage, 'receipt.json', result)
    return result


def pairs(values):
    result = {}
    for value in values:
        key, sep, path = value.partition('=')
        if not sep or not path or key in result:
            raise ValueError('Pièces nom=chemin distinctes requises.')
        identifier(key)
        result[key] = Path(path)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    listing = sub.add_parser('list')
    listing.add_argument('bundle', type=Path)
    listing.add_argument('--role', choices=meta.ROLES)
    prep = sub.add_parser('prepare')
    prep.add_argument('bundle', type=Path)
    prep.add_argument('--skill', required=True)
    prep.add_argument('--role', required=True, choices=meta.ROLES)
    prep.add_argument('--input', action='append', default=[])
    prep.add_argument('--output', type=Path, required=True)
    check = sub.add_parser('verify')
    check.add_argument('order', type=Path)
    check.add_argument('--order-sha256', required=True)
    delivery = sub.add_parser('handoff')
    delivery.add_argument('order', type=Path)
    delivery.add_argument('--order-sha256', required=True)
    delivery.add_argument('--to', required=True, choices=meta.ROLES)
    delivery.add_argument('--artifact', action='append', default=[])
    delivery.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == 'list':
            result = catalogue(args.bundle, args.role)
        elif args.command == 'prepare':
            result = prepare(args.bundle, args.skill, args.role, pairs(args.input), args.output)
        elif args.command == 'verify':
            result = verify(args.order, args.order_sha256)
        else:
            result = handoff(args.order, args.to, pairs(args.artifact), args.output, args.order_sha256)
    except (OSError, ValueError, KeyError, TypeError, UnicodeError) as exc:
        parser.exit(2, f'Opération interrompue : {exc}\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 2 if result.get('validity_status') == 'STALE' else 0


if __name__ == '__main__':
    raise SystemExit(main())
