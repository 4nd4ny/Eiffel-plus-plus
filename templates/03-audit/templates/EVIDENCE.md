# Élément de preuve — EVD-0001

Version du métapatron : **0.1.0**. Modèle non exécuté. Les champs vides ne sont pas des observations. Suivre le [protocole commun](../../../protocol/README.md).

```yaml
template_version: "0.1.0"
evidence_id: EVD-0001
audit_id: AUD-0001
check_status: NOT_RUN
binding_manifest_ref: null
binding_manifest_sha256: null
candidate_artifact_sha256: null
criterion_ref: null
oracle_ref: null
oracle_sha256: null
tool_and_version: null
invocation_ref: null
parameters_sha256: null
input_data_sha256: null
environment_sha256: null
started_at: null
completed_at: null
collector_identity: null
raw_result_ref: null
raw_result_sha256: null
public_excerpt_ref: null
public_excerpt_sha256: null
```

## Liaison et provenance

Référencer le manifeste immuable de campagne, qui contient les quatre adresses et SHA complets des dépôts gouvernance, STBL, audit et produit, ainsi que la construction et le candidat. L'empreinte de l'artefact ci-dessus doit correspondre à ce manifeste. Une divergence nécessite une nouvelle liaison, pas une modification silencieuse.

L'original est une sortie capturée, une trace d'exécution, un certificat vérifié ou une observation humaine explicitement identifiée. Décrire comment il a été obtenu et conservé hors écriture de l'auteur du candidat. Une description rédigée par un agent sans résultat source n'est pas une preuve exécutée.

## Énoncé et méthode

| Élément | À établir |
|---|---|
| Question vérifiée | Proposition précise liée à un besoin ou contrat |
| Méthode | Test, analyse, preuve formelle, inspection ou validation client |
| Domaine et limites | Cas, bornes, modèle, environnement et configuration couverts |
| Hypothèses | Conditions externes et propriétés admises |
| Résultat source | Sortie exacte ou référence autorisée |
| Interprétation | Conclusion permise par ce résultat, sans extension de portée |

Pour une preuve formelle, enregistrer l'énoncé, les hypothèses admises, l'outil, les options et le lien établi avec l'implémentation. Pour un test, enregistrer les cas ou générateurs, graines et conditions pertinentes. Pour une inspection humaine, identifier l'observateur, la procédure et les éléments examinés.

Un échec de démonstration sans contre-exemple exploitable peut être `UNKNOWN`. Une preuve de modèle ne devient pas une preuve du code par proximité de vocabulaire. Une suite sans cas découvert ne justifie pas `PASS` sur le comportement attendu.

## Réutilisation et péremption

Déclarer les dépendances nécessaires à la validité : besoins, oracles, candidat, build, configuration, données, services et conditions temporelles. Identifier les changements qui rendent le résultat `STALE`. Une dépendance inconnue impose une réexécution ou une invalidation conservatrice.

Si une preuve est réutilisée dans une autre campagne, conserver l'original et expliquer la validité de la nouvelle association. Ne pas antidater une exécution ni présenter une ancienne observation comme une nouvelle.

## Diffusion publique

Conserver séparément original et extrait expurgé, avec leurs empreintes propres. Indiquer les retraits, leur justification et l'emplacement autorisé de l'original. Ne pas inclure de secrets ou de données non publiables dans les noms, URLs, journaux et métadonnées. Une empreinte publique de donnée sensible peut elle-même révéler de l'information ; la publier seulement si sa diffusion est autorisée.
