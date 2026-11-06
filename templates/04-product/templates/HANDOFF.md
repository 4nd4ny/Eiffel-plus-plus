# Passation — {{PROJECT_NAME}}

Version du gabarit : **0.1.0**. Projet : `{{PROJECT_SLUG}}`.

Créer une passation lorsqu'une autre session ou un autre agent doit reprendre. Transmettre l'état utile et les raisons des décisions, sans recopier toute la conversation. Voir le [protocole commun](../../../protocol/README.md).

## Point de reprise

- Changement et ordre de travail : références à renseigner.
- Dépôt : produit (`{{PRODUCT_REPO}}`).
- Branche et commit de reprise : à renseigner.
- Travail non commité, s'il existe : décrire précisément et donner son support de récupération ; ne pas le confondre avec le commit.
- Révisions des exigences et contrats : références à STBL (`{{STBL_REPO}}`) ; politique applicable à référencer dans la gouvernance (`{{GOVERNANCE_REPO}}`).

## État utile

| Élément | Référence persistante | État constaté | Conséquence pour la reprise |
| --- | --- | --- | --- |

Employer `NOT_RUN`, `PASS`, `FAIL`, `UNKNOWN`, `STALE` pour les contrôles. Référencer les journaux et éléments `EVD-0001` au lieu de les résumer par « tout est vert ». Un service ou processus mentionné n'est pas présumé encore actif.

## Ce qui reste à résoudre

- Dernier défaut ou contre-exemple reproductible : à renseigner si applicable.
- Tentatives utiles déjà effectuées et enseignement observable : à renseigner brièvement.
- Questions ou décisions attendues : références `Q-0001` et `DEC-0001` si applicables.
- Échanges avec l'audit (`{{AUDIT_REPO}}`) : références `AUD-0001` ou `FND-0001` si existantes.
- Budget ou limites de mandat restants : à renseigner si connus.

## Prochaine action

Indiquer une prochaine opération concrète et la condition permettant de choisir la suivante. Si la reprise dépend d'un arbitrage, nommer la question et son destinataire. Ne pas recommencer les contrôles coûteux dont l'applicabilité reste établie ; ne pas réutiliser ceux dont les conditions ont changé.
