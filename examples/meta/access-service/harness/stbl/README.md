# Politique et contrat d'accès proposés

Toutes les exigences restent PROPOSED ; aucune matrice de rôles réelle n'a été acceptée.

| Exigence | Contrat comportemental |
| --- | --- |
| REQ-0001 | Refuser l'accès à une ressource étrangère hors d'une exception explicitement décidée. |
| REQ-0002 | Fonder la décision sur une identité et un contexte d'organisation provenant d'une frontière de confiance déclarée. |
| REQ-0003 | Refuser lorsqu'aucune permission applicable n'est établie ; ne pas transformer une politique indéterminée en autorisation. |
| REQ-0004 | Relier l'acceptation aux versions de politique, code et contrôles effectivement utilisés. |

## Contrat de décision

**Entrées :** contexte du sujet établi, action demandée, ressource identifiée, version de politique.

**Postcondition proposée :** une permission est accordée exactement lorsque la politique applicable autorise cette combinaison et que les conditions d'isolation sont satisfaites. Les cas positifs prévus doivent fonctionner ; une politique qui refuse tout ne satisfait pas le besoin.

**Invariants :** un identifiant fourni par l'appelant ne modifie pas à lui seul son périmètre ; aucune exception implicite n'est ajoutée ; l'absence d'une information nécessaire reste un refus ou une erreur explicitement distinguée selon la décision métier.

## Questions ouvertes

- Q-0001, OPEN : quels rôles et actions sont prévus ?
- Q-0002, OPEN : existe-t-il une exception entre organisations et qui peut l'autoriser ?
- Q-0003, OPEN : quelle garantie temporelle s'applique à une révocation ?
- Q-0004, OPEN : quelle délégation permet la livraison automatique ?

La préparation d'interfaces et de cas synthétiques peut continuer. L'acceptation métier dépend des réponses authentifiables pertinentes. Voir les [instructions STBL](AGENTS.md).
