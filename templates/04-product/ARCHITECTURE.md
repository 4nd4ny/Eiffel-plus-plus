# Architecture — {{PROJECT_NAME}}

Version du gabarit : **0.2.0**. Projet : `{{PROJECT_SLUG}}`.

Ce document décrit l'architecture réellement observée ou décidée. Les sections vides ne prescrivent ni langage, ni framework, ni découpage. Une proposition reste une proposition jusqu'à la décision correspondant à son niveau d'autorité.

## Sources et révisions

| Source | Référence précise à renseigner |
| --- | --- |
| Produit `{{PROJECT_SLUG}}` (`{{PRODUCT_REPO}}`) | Commit observé |
| Gouvernance (`{{GOVERNANCE_REPO}}`) | Méthode, autorité et politique applicables |
| STBL (`{{STBL_REPO}}`) | Exigences, décisions métier, contrats et révision normative |
| Audit (`{{AUDIT_REPO}}`) | Critères et version du dispositif de contrôle |

Voir le [protocole commun](../../protocol/README.md) pour les identifiants et les échanges.

## Responsabilités et frontières

Renseigner seulement les composants existants ou justifiés par un besoin actuel.

| Composant ou zone | Responsabilité | Entrées et sorties | Contrats applicables | Dépendances |
| --- | --- | --- | --- | --- |

Pour chaque frontière importante, préciser qui valide les entrées, qui possède l'état et quels effets sont possibles. Lorsque concurrence, temps, transactions ou appels externes influencent le résultat, leurs hypothèses doivent être visibles.

## Invariants et garanties

Référencer les invariants métiers dans STBL et indiquer où le produit les préserve. Une assertion locale, un type ou une contrainte de base de données ne couvre pas nécessairement l'ensemble d'un scénario.

| Invariant ou propriété | Référence du contrat | Mécanisme de préservation | Moyen de vérification | Limites connues |
| --- | --- | --- | --- | --- |

## Qualités attendues

Décrire les exigences pertinentes de performance, compatibilité, accessibilité, sécurité, observabilité et maintenabilité avec leurs références. Ne pas inventer un seuil pour remplir le document. Une qualité encore non définie devient une question à son propriétaire si elle affecte le choix d'architecture.

## Décisions d'architecture

Utiliser [le gabarit ADR](templates/ADR.md) pour une décision durable avec alternatives ou conséquences significatives. Les statuts sont `PROPOSED`, `ACCEPTED`, `REJECTED`, `SUPERSEDED` ; ils ne sont pas des résultats de test.

| Décision | Statut | Objet | Autorité et référence | Remplacée par, si applicable |
| --- | --- | --- | --- | --- |

## Intégration et évolution

Préciser les contraintes de compatibilité des interfaces, les migrations éventuelles et les contrôles à réexécuter lorsque ces frontières changent. Le code intégré est évalué dans son état réel ; une collection de composants vérifiés séparément ne suffit pas à démontrer le comportement du système.

## Dette et inconnues

| Problème concret | Effet observable ou risque | Référence | Traitement prévu et propriétaire |
| --- | --- | --- | --- |

Une préférence stylistique ne devient pas automatiquement une dette. Toute limite acceptée garde sa justification et l'autorité qui l'a acceptée.
