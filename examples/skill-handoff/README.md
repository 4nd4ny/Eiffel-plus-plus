# Deux compétences, trois remises

Exemple fictif rédigé pour appliquer le patron N2 0.6.0. Le [brief](brief.md) justifie un [N1](meta-harness/GENERATE.md) réemployable et le [N0](harness/AGENTS.md) du mode production puis examen. Il ne s'agit pas d'une génération indépendante par un autre modèle. Les tests exécutent les opérations déterministes et les remises, pas plusieurs agents LLM.

- STBL fournit les règles du lot.
- Produit utilise `filter-rows` et remet un candidat à Audit.
- Audit utilise `check-rows`, lit son rapport et le remet à Gouvernance.
- Gouvernance conserve les références de mission et décide la suite dans son mandat.

Pour un lot d'examen seul, N1 conserve uniquement `check-rows` dans N0. Produit reçoit et identifie le candidat existant ; aucune compétence de production n'est chargée. Les obligations du contrat restent identiques.

## Essai depuis la racine d'Eiffel++

Choisir un dossier de travail neuf à l'extérieur du catalogue. Dans les commandes ci-dessous, remplacer TRAVAIL par ce chemin. Les scripts Python du paquet et l'outil de mission n'effectuent aucun appel réseau ou modèle.

```bash
python3 tools/meta_harness.py check examples/skill-handoff/meta-harness
python3 tools/meta_harness.py check examples/skill-handoff/harness
python3 tools/skills.py list examples/skill-handoff/harness --role product
python3 tools/skills.py prepare examples/skill-handoff/harness --role product --skill filter-rows --input source=examples/skill-handoff/fixtures/source.csv --input rules=examples/skill-handoff/fixtures/rules.json --output TRAVAIL/produit
```

Le coordinateur conserve `order_sha256` renvoyé : SHA_PRODUIT dans la suite. Cette valeur doit venir de la préparation ; la recalculer après une modification ne restaure pas la validité de la mission.

```bash
python3 -B TRAVAIL/produit/resources/skills/filter-rows/scripts/run.py TRAVAIL/produit/inputs/source TRAVAIL/produit/inputs/rules TRAVAIL/candidat.csv
python3 tools/skills.py handoff TRAVAIL/produit --order-sha256 SHA_PRODUIT --to audit --artifact candidate=TRAVAIL/candidat.csv --output TRAVAIL/remise-produit
python3 tools/skills.py prepare examples/skill-handoff/harness --role audit --skill check-rows --input source=examples/skill-handoff/fixtures/source.csv --input rules=examples/skill-handoff/fixtures/rules.json --input candidate=TRAVAIL/remise-produit/outputs/candidate --output TRAVAIL/audit
```

Conserver cette seconde empreinte sous SHA_AUDIT. Lire le contrat et les instructions de la mission Audit, puis :

```bash
python3 -B TRAVAIL/audit/resources/skills/check-rows/scripts/run.py TRAVAIL/audit/inputs/source TRAVAIL/audit/inputs/rules TRAVAIL/audit/inputs/candidate TRAVAIL/rapport.json
python3 tools/skills.py handoff TRAVAIL/audit --order-sha256 SHA_AUDIT --to governance --artifact report=TRAVAIL/rapport.json --output TRAVAIL/remise-audit
```

Le contenu de rapport.json établit seulement le résultat du contrôle CSV exécuté. La remise conserve `semantic_status: NOT_RUN` : elle ne juge pas le rapport et ne décide pas de l'adoption.

## Épreuves conservées dans le code

`tests/test_skills.py` rejoue production, audit, catégorie absente et examen seul. Il vérifie aussi candidat tronqué, source invalide, ressource manquante, mauvais rôle, entrée ou sortie absente, mauvais destinataire, lien symbolique, contrôle/plan/entrée modifié et tentative de supprimer des références dans le reçu de mission. Une modification invalide la mission même si le script altéré pourrait annoncer un succès.

Le fonctionnement est borné à des fichiers locaux, à des dépendances déclarées et à une empreinte conservée par l'appelant. Pas d'identité d'agent authentifiée, de confinement de code hostile, de validation de toutes les descriptions de compétences ou de gain LLM démontré.

Les notes [N1](meta-harness/DESIGN.md) et [N0](harness/DESIGN.md) expliquent des choix différents : méthode réemployable et lot concret. Elles indiquent les changements nécessaires pour une autre catégorie, un examen seul, un format différent ou une exigence de séparation ; aucune politique d’entreprise n’est supposée acceptée.
