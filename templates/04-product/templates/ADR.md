# Décision d'architecture — {{PROJECT_NAME}}

Version du gabarit : **0.2.0**. Projet : `{{PROJECT_SLUG}}`.

Utiliser ce support pour un choix durable qui mérite d'être retrouvé. Il ne crée aucun arbitrage accepté. Voir le [protocole commun](../../../protocol/README.md).

## Identité

- Référence : identifiant `DEC-0001` effectivement alloué.
- Statut initial : `PROPOSED`.
- Objet : à renseigner.
- Auteur de la proposition et autorité de décision : à renseigner selon le mandat.
- Changement, exigences et contrats concernés : références et révisions à renseigner.

Les statuts possibles sont `PROPOSED`, `ACCEPTED`, `REJECTED`, `SUPERSEDED`. Une acceptation ou un remplacement doit référencer la décision de l'autorité compétente ; une mise à jour du statut ne vaut pas preuve de cette décision.

## Contexte et alternatives

Décrire le problème concret, les contraintes et les alternatives plausibles, y compris l'absence de changement lorsqu'elle est pertinente. Distinguer observations, hypothèses et préférences. Référencer les sources normatives dans STBL (`{{STBL_REPO}}`).

## Proposition et conséquences

Expliquer le choix proposé et ses conséquences sur les interfaces, les invariants, la compréhension du code, la maintenance et les exigences de sécurité applicables. Justifier les dépendances ou abstractions nouvelles par leur utilité présente.

## Vérification et décision

Indiquer ce qui permet de comparer les alternatives ou de vérifier les conséquences annoncées. Référencer les éléments observés dans le produit (`{{PRODUCT_REPO}}`) et, s'ils existent, les constats de l'audit (`{{AUDIT_REPO}}`).

Si le choix change le besoin ou le sens d'un contrat, transmettre la proposition à STBL pour décision du responsable métier. Une modification d'oracle relève de l'audit et de la décision métier correspondante si elle change l'attente. Une modification de méthode, de politique ou d'autorité relève de la gouvernance (`{{GOVERNANCE_REPO}}`). Renseigner ensuite la référence de décision et, le cas échéant, la décision remplacée ou celle qui remplace la présente.
