# Rapport de changement — {{PROJECT_NAME}}

Version du gabarit : **0.1.0**. Projet : `{{PROJECT_SLUG}}`.

Remplir ce rapport à partir de résultats observés, selon le [protocole commun](../../../protocol/README.md). Une case vide ne signifie pas une réussite.

## Candidat remis

- Changement : référence `CHG-0001` effectivement allouée.
- Ordre de travail : référence et révision à renseigner.
- Dépôt : produit (`{{PRODUCT_REPO}}`).
- `product_commit` : commit candidat vérifié, à renseigner après sa création effective.
- Artefact construit et empreinte, si applicable : à renseigner.
- `governance_commit` : révision exacte des règles applicables.
- `stbl_commit` : révision exacte des besoins, décisions et contrats applicables.
- `audit_commit` : révision exacte du plan et des oracles figés avant l'exécution concernée.

Le hash du candidat désigne l'objet vérifié, pas un futur commit supposé. Le `report_commit`, qui désigne le commit contenant le rapport, est inscrit dans le reçu ou l'enveloppe extérieure après enregistrement du rapport. Ne pas l'inventer dans le contenu dont il dépend. Il ne remplace pas `audit_commit`.

## Résultat et portée

Expliquer le comportement changé, son lien avec le besoin et les zones réellement modifiées. Référencer les exigences, contrats et décisions concernés. Signaler tout écart au mandat ; ne pas présenter une proposition de changement de contrat comme déjà acceptée.

## Vérifications observées

| Élément `EVD-0001` | Objet exact et contrôle | État | Journal ou résultat | Limites et conditions |
| --- | --- | --- | --- | --- |

États autorisés : `NOT_RUN`, `PASS`, `FAIL`, `UNKNOWN`, `STALE`. Pour une preuve, préciser la propriété et les hypothèses. Pour un résultat réutilisé, référencer sa provenance et justifier l'applicabilité de son cache. Conserver les commandes réelles et l'environnement pertinent dans le dossier référencé.

## Intégration

- Révision intégrée vérifiée, si différente du candidat : à renseigner.
- Contrôles exécutés sur cette révision : références à renseigner.
- Contrôles encore nécessaires : à renseigner ; ne pas laisser entendre qu'ils ont été effectués.

## Constats et questions

| Référence `FND-0001` ou `Q-0001` | Constat ou décision attendue | Impact | Destinataire |
| --- | --- | --- | --- |

Déclarer les défauts connus, inconnues, contrôles bloqués et éventuelles limitations d'exploitation. Une dette identifiée doit désigner un problème concret et ses conséquences.

## Audit et suite

Référencer le rapport `AUD-0001` reçu de l'audit (`{{AUDIT_REPO}}`), s'il existe, avec sa révision et son candidat. Ne pas attribuer soi-même un verdict absent. Les verdicts possibles sont `ACCEPT`, `REJECT`, `INCONCLUSIVE`, `ACCEPT_WITH_RESERVATIONS`.

Les réserves restent visibles et sont traitées selon la gouvernance (`{{GOVERNANCE_REPO}}`). `ACCEPT_WITH_RESERVATIONS` ne donne aucune autorisation automatique de livraison ; l'autorité prévue par la politique statue sur les risques résiduels. Une correction de spécification se propose à STBL (`{{STBL_REPO}}`). Indiquer la prochaine action utile sans inventer d'autorisation de mise en service.
