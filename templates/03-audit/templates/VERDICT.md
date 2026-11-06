# Verdict — AUD-0001

Version du métapatron : **0.2.0**. Modèle non exécuté : l'état initial est inconclusif. Appliquer le [protocole commun](../../../protocol/README.md) et la [politique](../POLICY.md).

```yaml
template_version: "0.2.0"
audit_id: AUD-0001
project: "{{PROJECT_SLUG}}"
decision_status: PROPOSED
audit_verdict: INCONCLUSIVE
binding_manifest_ref: null
binding_manifest_sha256: null
candidate_artifact_sha256: null
issuer_identity: null
issued_at: null
authorization_decision: null
finding_ids: []
evidence_ids: []
reservation_decision_ids: []
```

## Objet exact du verdict

Référencer le plan et le manifeste immuable contenant les quatre adresses et SHA complets `governance_commit`, `stbl_commit`, `audit_commit`, `product_commit`, la construction du candidat et les environnements examinés. La présente conclusion ne s'applique qu'à cette liaison et à cet artefact. `audit_commit` précède les observations ; le `report_commit` ultérieur est celui contenant le rapport, sans autoréférence dans le document.

Décrire le périmètre examiné et les exclusions. Ne pas présenter un audit du code source comme une validation d'un binaire dont la provenance n'a pas été vérifiée.

## Couverture des critères

La ligne ci-dessous est un schéma de saisie, sans contrôle réalisé.

| Besoin ou contrat | Critère obligatoire ? | État | Preuves | Limites | Constat bloquant |
|---|---|---|---|---|---|
| Non renseigné | À établir | `NOT_RUN` | Aucune | Non établies | Non déterminé |

Chaque critère obligatoire du plan doit apparaître. La matrice doit permettre de distinguer absence de contrôle, échec, indétermination et péremption ; aucun de ces états ne peut être présenté comme `PASS`.

## Justification du verdict

- **`ACCEPT`** : critères obligatoires satisfaits par des résultats valides et aucun constat bloquant restant ; citer les éléments qui l'établissent.
- **`REJECT`** : violation bloquante établie ; citer le critère, le constat et la preuve.
- **`INCONCLUSIVE`** : élément obligatoire manquant ou indéterminé ; préciser exactement ce qui manque et la prochaine action utile. Le passage automatique vers l'acceptation s'arrête.
- **`ACCEPT_WITH_RESERVATIONS`** : critères obligatoires satisfaits, mais limites non bloquantes appelant une décision explicite. Ce verdict n'autorise aucune livraison automatique.

Ne pas utiliser une réserve pour masquer un contrôle obligatoire `NOT_RUN`, `UNKNOWN`, `STALE` ou un `FAIL` bloquant. Les réserves doivent avoir un impact, un destinataire, une action ou une acceptation explicite et un critère de réexamen.

## Portée des garanties

Distinguer ce qui est observé sur des cas, établi dans des bornes, prouvé sous hypothèses et validé par le client. Nommer les hypothèses extérieures et les limites de la séparation des rôles. Un avis favorable de plusieurs agents ne remplace pas ces résultats.

## Autorité et suite

Identifier l'émetteur et les protections empêchant l'auteur du candidat de falsifier ce verdict ou ses pièces. Une proposition reste `PROPOSED` jusqu'à la décision de l'autorité désignée. Les autres états de décision sont `ACCEPTED`, `REJECTED`, `SUPERSEDED`.

La livraison relève de l'autorité désignée dans le mandat, selon les règles de gouvernance applicables. Un changement du sens métier relève du Product Owner ou de son délégataire, avec une décision enregistrée dans le STBL. Si le candidat, le besoin, un oracle ou une hypothèse pertinente change, le verdict doit être réévalué ; son acceptation ancienne ne couvre pas la nouvelle version.

## Publication

Vérifier les pièces et liens publiables. Indiquer quelles preuves restent dans un emplacement à accès restreint et qui a réellement pu les examiner. L'absence d'accès public n'invalide pas une preuve autorisée, mais elle limite ce qu'un lecteur public peut vérifier lui-même.
