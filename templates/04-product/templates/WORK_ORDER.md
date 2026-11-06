# Ordre de travail — {{PROJECT_NAME}}

Version du gabarit : **0.3.0**. Projet : `{{PROJECT_SLUG}}`.

Ce document prépare un travail dans le produit (`{{PRODUCT_REPO}}`). Il ne crée pas d'exigence acceptée ni de verdict. Les champs sont à renseigner selon le [protocole commun](../../../protocol/README.md) ; les sections inutiles peuvent être retirées.

## Identité et mandat

- Identifiant du changement : à allouer selon le protocole, au format `CHG-0001`.
- Objectif concret : à renseigner.
- Origine du mandat et responsable : à renseigner ; vérifier l'autorité selon la gouvernance (`{{GOVERNANCE_REPO}}`).
- Révision initiale du produit : commit exact à renseigner.
- Périmètre d'écriture autorisé : à renseigner.
- Limites de coût, de temps et d'itération applicables : à renseigner si définies par le mandat.

## Références normatives

| Référence | Objet | Dépôt et révision exacte | Effet attendu sur le travail |
| --- | --- | --- | --- |

Utiliser les exigences `REQ-0001`, contrats `CTR-0001` et décisions `DEC-0001` effectivement applicables. Les contrats viennent de STBL (`{{STBL_REPO}}`). Une question `Q-0001` ouverte n'est pas une décision.

Conserver les références de l'enveloppe : `governance_commit` pour les règles applicables, `stbl_commit` pour les besoins et contrats, `audit_commit` pour le plan et les oracles figés avant leur exécution. `product_commit` sera le candidat effectivement remis ; il est résolu après sa création. Ne pas fabriquer de SHA pour compléter un champ encore inconnu.

Les questions utilisent `OPEN`, `ANSWERED` ou `SUPERSEDED`. Une réponse qui exige un arbitrage renvoie à une décision authentifiée ; l'agent ne la transforme pas seul en exigence acceptée.

## Obligations et contrôles

| Obligation comportementale ou qualité | Référence | Contrôle envisagé ou requis | Autorité du contrôle | État initial |
| --- | --- | --- | --- | --- |

Les contrôles non exécutés ont l'état `NOT_RUN`. Identifier les critères relevant de l'audit (`{{AUDIT_REPO}}`) sans les recopier comme des critères modifiables par le producteur. Préciser les hypothèses et limites des preuves ou recherches bornées envisagées.

## Dépendances et stratégie

- Interfaces ou travaux dont dépend le candidat : à renseigner avec leur révision.
- Lot initial choisi et raison de ce choix : à renseigner brièvement.
- Contrôles sur l'état fusionné : à renseigner selon l'impact et la politique.
- Hypothèses, inconnues ou arbitrages bloquants : à renseigner, ou indiquer explicitement qu'aucun n'est identifié.

## Conditions de remise

Décrire l'artefact attendu, les éléments de vérification à fournir et le destinataire. La remise doit identifier le candidat réel, les contrôles effectués, les limites et les questions restantes. Elle ne préjuge pas de la décision d'acceptation.
