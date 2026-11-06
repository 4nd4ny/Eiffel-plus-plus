# Plan de campagne — AUD-0001

Version du métapatron : **0.2.0**. Modèle non exécuté pour {{PROJECT_NAME}}.

Ce document suit le [protocole commun](../../../protocol/README.md), la [charte](../AUDIT_CHARTER.md) et la [politique](../POLICY.md). Réserver l'identifiant de campagne avant usage. `null` signifie « non renseigné » et ne satisfait aucune précondition.

## Identification et liaison

```yaml
template_version: "0.2.0"
audit_id: AUD-0001
project: "{{PROJECT_SLUG}}"
decision_status: PROPOSED
authorization_decision: null
repositories:
  governance: "{{GOVERNANCE_REPO}}"
  stbl: "{{STBL_REPO}}"
  audit: "{{AUDIT_REPO}}"
  product: "{{PRODUCT_REPO}}"
references:
  governance_commit: null
  stbl_commit: null
  audit_commit: null
  product_commit: null
candidate:
  source_ref: references.product_commit
  artifact_ref: null
  artifact_sha256: null
  build_record_ref: null
  build_recipe_sha256: null
  dependency_lock_sha256: null
  build_environment_ref: null
  build_environment_sha256: null
execution:
  runner_ref: null
  runner_sha256: null
  environment_ref: null
  environment_sha256: null
  configuration_sha256: null
  fixture_sha256: null
binding_manifest_ref: null
binding_manifest_sha256: null
```

Le bloc décrit les métadonnées à résoudre dans le dossier d'exécution. Figer d'abord le plan et les oracles dans un commit, en laissant `audit_commit` à `null` dans ce plan préparatoire. Observer ensuite le SHA obtenu et renseigner les **quatre SHA complets dans le manifeste distinct**. Ne pas modifier le plan pour lui faire contenir son propre SHA. Aucun cinquième dépôt n'est implicitement admis dans cette liaison. Le candidat se rattache au SHA produit déjà déclaré. Les dépendances externes figurent dans les enregistrements de construction et d'exécution.

`audit_commit` désigne le plan, les politiques et les oracles utilisés avant exécution. Le compte rendu et les résultats sont ajoutés dans un commit ultérieur, `report_commit`, retrouvé par le commit contenant le rapport ; le rapport n'inscrit pas son propre SHA.

Le manifeste de liaison est un objet distinct, figé avant les observations. Il contient les quatre références, l'identité de l'artefact, sa construction et les environnements ; il ne contient pas sa propre empreinte. Conserver ses octets exacts et calculer leur SHA-256, puis inscrire sa référence et cette empreinte dans les éléments probants et le verdict. Le plan préparatoire peut laisser ces champs à `null` ; ils doivent être résolus dans le dossier d'exécution avant toute conclusion favorable.

Construire depuis un arbre propre au commit déclaré. Si un autre instantané immuable est autorisé, l'identifier explicitement et justifier sa relation au commit ; un arbre modifié ne peut pas être présenté comme le commit seul. Suivre le [format des échanges](../../../protocol/EXCHANGE.md) et le [modèle de confiance](../../../protocol/TRUST.md).

## Mandat et périmètre

| Question | Réponse à établir |
|---|---|
| Quel service ou changement évaluer ? | Non renseigné |
| Quels besoins et contrats font autorité ? | Non renseignés ; citer `REQ-0001` et `CTR-0001` applicables |
| Quels changements sont inclus ? | Non renseignés ; citer `CHG-0001` applicables |
| Quels environnements et actions sont autorisés ? | Non renseignés |
| Quelles exclusions limitent le verdict ? | Non renseignées |
| Quel budget et quel responsable d'arbitrage ? | Non renseignés |
| Où conserver les observations sensibles ? | Non renseigné |

## Matrice de contrôles

La ligne suivante est un schéma de saisie, pas un résultat. Ajouter une ligne pour chaque critère applicable ; ne pas inventer sa traçabilité.

| Besoin ou contrat | Critère observable | Origine de l'oracle | Contrôle et données | Obligatoire ? | État | Preuve |
|---|---|---|---|---|---|---|
| Non renseigné | Non renseigné | Non renseignée | Non renseignés | À décider | `NOT_RUN` | Aucune |

Examiner, selon le périmètre : comportements de réussite, erreurs, permissions, invariants, concurrence, idempotence, intégration, migrations, performances, maintenabilité, parcours et adéquation au besoin client. Un audit uniquement statique doit annoncer qu'il n'établit aucun comportement d'exécution.

## Indépendance et environnement

Décrire les droits réellement configurés sur les oracles, l'exécuteur, la collecte et le verdict. Référencer leur vérification. Identifier les entrées non fiables, l'isolation du build, les accès réseau autorisés, les secrets exclus et les limites de ressources.

L'agent constructeur peut fournir des pistes, mais aucune de ses déclarations ne remplace les observations. La vérification d'un besoin ne doit pas reposer uniquement sur un oracle copié de sa propre implémentation.

## Réutilisation autorisée

Lister chaque preuve réutilisée, sa liaison précédente, ses dépendances et la raison de sa validité actuelle. Si l'analyse de dépendances est incomplète, inscrire les contrôles plus larges à réexécuter. Des entrées inconnues ne sont pas une clé de cache fiable.

## Sortie attendue et arrêt

Produire les constats, preuves et le verdict de la campagne. Un critère obligatoire non exécuté, périmé ou indéterminé conduit à `INCONCLUSIVE` et arrête le passage automatique vers l'acceptation. Une violation bloquante établie conduit à `REJECT`. Les réserves non bloquantes nécessitent une décision explicite avant livraison.
