# Contribuer

Une contribution doit préciser le problème traité, le changement de comportement attendu et la manière de l'examiner. Utiliser des exemples fictifs ou expurgés. Ne pas ajouter de données client ou de secrets.

## Modifier un métapatron

Préserver la structure : intention, contexte et forces, structure, contrat, heuristiques de décision, coopération, arrêt/escalade, antipatrons, indicateurs et variantes. Donner aux agents une autonomie concrète et des limites vérifiables. Éviter les répétitions de consignes sans mécanisme associé.

## Modifier le protocole

Évaluer l'impact sur les quatre modèles et sur les instantanés des projets. Documenter la compatibilité et la migration. Les contrats et résultats anciens restent interprétés selon leur version d'origine. Changer la version du protocole si sa sémantique change.

## Vérifier

```bash
python3 tools/check_catalog.py
python3 -m unittest discover -s tests -v
```

Vérifier manuellement les préconditions, postconditions, invariants et responsabilités. Les contrôles structurels ne prouvent pas la qualité de la méthode. Une affirmation sur un outil ou une publication doit renvoyer à une source primaire pertinente.
