# DEC-0001 — Intitulé de la décision

Modèle Eiffel++ **0.2.0**. L'identifiant est illustratif. La décision initiale est une **proposition**.

| Champ | Valeur initiale |
| --- | --- |
| Statut | `PROPOSED` |
| Question / changement à arbitrer | À renseigner. |
| Exigences et contrats concernés | À renseigner avec leurs révisions. |
| Décideur proposé | À renseigner ; aucune identité authentifiée par ce modèle. |
| Autorité / délégation applicable | À renseigner et référencer. |
| Source de décision | Aucune décision reçue. |
| Date de la décision | Non décidée. |
| Décision remplacée / remplaçante | Aucune. |

## Proposition et alternatives

Décrire le choix proposé, les alternatives examinées et les conséquences observables. Expliciter les obligations ajoutées, retirées, renforcées ou affaiblies.

## Périmètre exact du consentement

Énumérer les formulations ou versions auxquelles le choix s'applique. Distinguer une validation d'exemple, une autorisation d'exploration et l'acceptation d'une règle générale. Signaler les réserves et conditions.

## Provenance contrôlable

Lorsqu'une décision est reçue, enregistrer l'identité attribuée au décideur, le canal, une référence consultable, la date et l'élément exact accepté. Indiquer **qui a contrôlé l'attribution, par quel moyen et avec quelles limites**. Référencer les preuves d'autorité disponibles sans prétendre avoir vérifié une signature ou une identité qui ne l'a pas été.

Ne pas exposer de données confidentielles pour établir cette provenance. Une référence à accès restreint accompagnée d'un extrait autorisé peut convenir.

## Application et historique

- Éléments à mettre à jour : à renseigner.
- Dépôts destinataires et révisions à communiquer : à renseigner.
- Conditions de réexamen : à renseigner.

Utiliser `ACCEPTED` ou `REJECTED` seulement pour une décision réellement reçue d'une autorité compétente, ou une décision prise dans une délégation documentée. Utiliser `SUPERSEDED` lorsqu'une nouvelle décision remplace celle-ci, en conservant le choix historique et le lien vers sa remplaçante.

Le [protocole commun](../../../protocol/README.md) s'applique ; un statut de décision n'est pas un résultat de test ni un verdict d'audit.
