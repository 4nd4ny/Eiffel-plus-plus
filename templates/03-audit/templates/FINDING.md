# Constat — FND-0001

Version du métapatron : **0.3.0**. Modèle sans défaut observé. Réserver un identifiant unique avant usage et suivre le [protocole commun](../../../protocol/README.md).

```yaml
template_version: "0.3.0"
finding_id: FND-0001
audit_id: AUD-0001
decision_status: PROPOSED
check_status: NOT_RUN
binding_manifest_ref: null
binding_manifest_sha256: null
requirement_ids: []
contract_ids: []
change_ids: []
evidence_ids: []
blocking: null
```

## Résumé et impact

Décrire le comportement observé en une phrase, puis ses conséquences métier ou techniques. Distinguer bug, écart au besoin, défaut d'oracle, limite d'environnement et risque à investiguer. La gravité découle de l'impact et de l'exposition établis ; elle ne découle pas du ton de la description.

## Source du critère

Référencer le besoin ou contrat, sa source et la décision applicable. Expliquer ce que le client attendait. Si cette attente n'est pas établie, ouvrir une question `Q-0001` au lieu de transformer une préférence de l'auditeur en défaut avéré.

## Observation et reproduction

| Élément | À consigner |
|---|---|
| Candidat et liaison | Manifeste de campagne et artefact concernés |
| Conditions initiales | État, données, configuration et permissions |
| Entrée ou trace minimale | Actions ordonnées, concurrence et interruptions utiles |
| Attendu | Résultat fondé sur le critère applicable |
| Observé | Résultat réellement capturé |
| Source brute | Référence autorisée vers `EVD-0001` et pièces associées |
| Répétabilité et limites | Ce qui a été reproduit et ce qui reste indéterminé |

Une piste issue d'un LLM ou d'un scanner doit rester distinguée d'un défaut reproduit. Si la preuve manque, conserver `UNKNOWN` ou `NOT_RUN` selon l'état réel du contrôle ; ne pas fabriquer une trace.

## Disposition proposée

Expliquer si le constat bloque un critère obligatoire et citer la politique. Proposer une correction ou une investigation sans changer silencieusement le besoin. Toute modification d'oracle suit le document dédié.

Les décisions de disposition utilisent `PROPOSED`, `ACCEPTED`, `REJECTED`, `SUPERSEDED`. Une décision sur un constat n'altère pas rétroactivement le résultat du contrôle qui l'a produit.

## Réexamen

Référencer le nouveau `CHG-0001`, la nouvelle liaison de candidat et les nouveaux éléments `EVD-0001`. Vérifier la correction et les obligations affectées. Conserver la première observation ; elle ne disparaît pas lorsque le défaut est corrigé.

## Diffusion

Indiquer les destinataires autorisés et les expurgations nécessaires. Ne pas publier de secret, donnée personnelle ou information client non autorisée dans une reproduction. Une copie expurgée doit rester reliée à l'original accessible aux personnes habilitées.
