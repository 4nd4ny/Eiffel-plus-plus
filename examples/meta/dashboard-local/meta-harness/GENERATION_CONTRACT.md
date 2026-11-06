# Contrat de génération N1 → N0 — tableau de bord local

Statut : PROPOSED. Origine : scénario fictif Eiffel++ 0.2.0. Validation opérationnelle : NOT_RUN.

## Entrées

Le profil, le brief et les décisions disponibles, les capacités vérifiées et les traces pertinentes. Chaque inconnue reste visible. L'absence de mandat adopté autorise ici la préparation d'un candidat documentaire ; elle ne donne pas de droit d'exécution réel.

## Préconditions de synthèse

- Les obligations de traitement local et de fidélité des données sont identifiables.
- Les poids sont interprétés comme des préférences d'arbitrage, avec leurs sources.
- Les capacités techniques disponibles sont distinguées de celles qu'il reste à installer ou vérifier.
- Le budget de génération borne les candidats et révisions.

## Postconditions attendues

Le N0 contient quatre responsabilités, des instructions exécutables adaptées à une petite livraison locale et un chemin de reprise. Chaque règle ajoutée a une raison liée au besoin, à une contrainte ou à un fait d'environnement. Les métadonnées répétitives sont confiées à l'outillage lorsqu'il existe.

Le contexte initial est limité et les sources canoniques restent accessibles. La méthode donne un traitement explicite aux doublons et quantités manquantes : décision sourcée ou inconnue ouverte. Elle prévoit des contrôles observables, sans en annoncer le succès avant exécution.

## Invariants

La génération ne change pas les besoins pour simplifier le produit. Aucun contrôle manquant ne devient réussi. Le producteur ne réécrit ni les critères indépendants ni une décision métier. Une demande d'autonomie n'élargit pas son mandat. Une adaptation N0 ne réécrit pas silencieusement ce contrat N1.

## Acceptabilité du candidat

Examiner la structure, la cohérence des responsabilités et la possibilité réelle d'appliquer le workflow. La séparation des droits et l'exécuteur doivent encore être qualifiés dans l'environnement cible. Un fichier `AGENTS.md` ne les installe pas.

Le contrôle structurel est distinct d'une décision d'adoption, d'une qualification du harnais et d'une acceptation du logiciel. Le cas illustratif n'a produit aucun logiciel ni résultat métier.
