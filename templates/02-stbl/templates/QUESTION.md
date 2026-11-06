# Q-0001 — Question à arbitrer

Modèle Eiffel++ **0.2.0**. L'identifiant est illustratif. Aucune réponse du PO n'est présumée.

| Champ | Valeur initiale |
| --- | --- |
| État | `OPEN` |
| Exigences / contrats concernés | À renseigner. |
| Source de l'ambiguïté | Référence et formulation exacte ou extrait autorisé. |
| Classement | Choisir : bloquante ou traitable sous mandat. |
| Motif du classement | Conséquence sur le comportement et l'acceptation. |
| Décideur ou mandat existant | À renseigner. |
| Décision associée | Aucune. |

## Question courte

Poser une seule question qui distingue des comportements observables. Éviter de demander au PO de choisir un détail d'implémentation sans conséquence métier.

## Options et conséquences

| Option | Comportement obtenu | Coût / risque / conséquence pour l'utilisateur |
| --- | --- | --- |
| A — À renseigner. | À renseigner. | À renseigner. |
| B — À renseigner. | À renseigner. | À renseigner. |

**Recommandation de l'agent :** à renseigner, avec justification et incertitude. Cette recommandation n'est pas une décision.

## Travail en attendant la décision

- Éléments réellement bloqués : à renseigner.
- Éléments indépendants qui peuvent continuer : à renseigner.
- Si traitement sous mandat : référence du mandat, option retenue et conditions de réexamen.
- Échéance utile et conséquence de l'absence de réponse : à renseigner, sans inventer une acceptation tacite.

## Réponse et clôture

Référencer une fiche `DEC` contenant la réponse, son auteur, sa provenance et son périmètre. Ne pas recopier une approbation non obtenue. Mettre à jour les dépendances seulement lorsque cette décision est applicable.

Les états autorisés sont `OPEN`, `ANSWERED`, `SUPERSEDED`. Garder `OPEN` tant qu'aucune décision applicable ne répond effectivement à la question. Passer à `ANSWERED` en référençant cette décision ; cela ne vaut pas acceptation d'une exigence. Utiliser `SUPERSEDED` lorsqu'une autre question remplace celle-ci, en conservant l'historique et le lien vers la question remplaçante.

Voir le [protocole commun](../../../protocol/README.md).
