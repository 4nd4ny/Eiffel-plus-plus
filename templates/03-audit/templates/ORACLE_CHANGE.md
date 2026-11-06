# Proposition de changement d'oracle — DEC-0001

Version du métapatron : **0.2.0**. Proposition non acceptée. Suivre le [protocole commun](../../../protocol/README.md).

```yaml
template_version: "0.2.0"
decision_id: DEC-0001
decision_status: PROPOSED
audit_id: AUD-0001
binding_manifest_ref: null
binding_manifest_sha256: null
question_ids: []
requirement_ids: []
contract_ids: []
finding_ids: []
evidence_ids: []
old_oracle_ref: null
old_oracle_sha256: null
proposed_oracle_ref: null
proposed_oracle_sha256: null
decision_authority: null
```

## Problème établi

Décrire pourquoi l'oracle actuel est incorrect, obsolète ou insuffisant, avec sa source et ses observations. « Le candidat échoue » n'est pas une justification suffisante. Distinguer une erreur du test, une évolution du besoin, une hypothèse d'environnement fausse et un défaut du produit.

## Source de vérité

Relier la proposition aux besoins et décisions applicables. Si le sens du besoin n'est pas déterminé, ouvrir une question `Q-0001` et maintenir l'indétermination jusqu'à l'arbitrage approprié. L'audit ne peut pas inventer un nouveau besoin au nom du client.

## Différence proposée

| Élément | Version actuelle | Version proposée | Justification sourcée |
|---|---|---|---|
| Critère ou oracle concerné | Non renseigné | Non renseigné | Non renseignée |

Préciser ce que le nouveau contrôle détecte, ce qu'il ne détecte plus et comment préserver les protections requises. Un contrôle qualifié n'est jamais affaibli uniquement pour faire passer le candidat. Une règle métier volontairement modifiée doit être décidée par le Product Owner ou son délégataire, puis enregistrée dans le STBL avant de changer l'acceptation.

## Contradiction et qualification

Prévoir une vérification indépendante de la proposition : exemple client, modèle de référence, contre-exemple, inspection ou propriété appropriée. L'auteur du changement ne peut pas être l'unique source de l'attendu et de son acceptation. Vérifier qu'un comportement manifestement incorrect demeure détectable.

Les procédures de qualification doivent elles-mêmes être exécutées ; une description de leur résultat attendu n'est pas une preuve.

## Décision et conséquences

La proposition suit `PROPOSED`, puis `ACCEPTED` ou `REJECTED`. Une décision remplacée devient `SUPERSEDED` en conservant sa trace. Identifier l'autorité et sa source de délégation.

Après acceptation, produire une nouvelle version de l'oracle et une nouvelle liaison de campagne. Marquer `STALE` les preuves dont les critères ou hypothèses ont changé, recalculer les contrôles affectés et réexaminer les verdicts concernés. Si les dépendances sont incomplètes, invalider plus largement.

Ne pas réécrire les anciens résultats pour les faire apparaître favorables sous les nouveaux critères. La nouvelle décision explique l'évolution ; elle ne modifie pas ce qui avait été observé.

## Diffusion

Publier uniquement les sources, extraits et exemples autorisés. Conserver les observations sensibles et leur provenance dans leur emplacement prévu ; ne pas recopier de secrets ou de données client dans cette proposition.
