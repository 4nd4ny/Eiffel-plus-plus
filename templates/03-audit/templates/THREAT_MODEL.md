# Modèle de menaces — AUD-0001

Version du métapatron : **0.2.0**. Document de travail pour {{PROJECT_NAME}}, sans menace confirmée par défaut. Référence : [protocole commun](../../../protocol/README.md).

```yaml
template_version: "0.2.0"
audit_id: AUD-0001
decision_status: PROPOSED
binding_manifest_ref: null
binding_manifest_sha256: null
requirement_ids: []
contract_ids: []
question_ids: []
evidence_ids: []
```

## Actifs, acteurs et frontières

Identifier les données et opérations à protéger, leurs propriétaires, les acteurs légitimes, les acteurs non autorisés et les frontières de confiance. Inclure le produit, ses dépendances, ses services, sa construction et le mécanisme d'audit lui-même lorsque pertinents.

| Frontière | Entrée non fiable | Pouvoir accordé | Protection attendue | Contrôle | État |
|---|---|---|---|---|---|
| À établir | À établir | À établir | À établir | À établir | `NOT_RUN` |

## Scénarios à étudier selon le périmètre

Les éléments suivants sont des pistes illustratives, pas des constats :

- un utilisateur tente une opération avec une identité ou un rôle insuffisant ;
- deux actions concurrentes contournent un invariant métier ;
- une entrée, un fichier ou un message distant influence un interpréteur, une requête ou un agent ;
- un script de construction ou une dépendance cherche à accéder aux secrets de l'auditeur ;
- une modification du sélecteur de tests supprime silencieusement un contrôle ;
- des journaux ou des preuves destinés au dépôt public révèlent des données client ;
- une ressource externe change après un résultat mis en cache ;
- le système dégrade son service sous une charge ou une panne relevant du besoin.

Pour chaque scénario retenu, préciser conditions, impact, surface exposée, contrôles attendus et hypothèses. Les tests actifs restent dans les environnements et actions déjà autorisés par le mandat ; ce modèle ne confère aucun droit sur un système tiers.

## Construction et processus d'audit

Documenter l'isolation du code non fiable, les permissions minimales, l'accès réseau, les limites de ressources et l'absence de secrets de l'auditeur. Vérifier la provenance de l'artefact et la protection des oracles, de l'exécuteur, de la collecte et du verdict.

Si une protection existe uniquement dans un document et pas dans la configuration réelle, la noter comme non établie. La CI doit observer l'exécution effective des contrôles ; un succès rapporté par un script modifiable par l'auteur ne suffit pas.

## Risques résiduels et validation

Relier chaque scénario aux preuves et constats éventuels. Une analyse sans alerte ou un avis LLM favorable ne démontre pas l'absence de risque. Décrire ce qui reste inconnu et les hypothèses à faire confirmer par les responsables du domaine.

Les décisions suivent `PROPOSED`, `ACCEPTED`, `REJECTED`, `SUPERSEDED`. Les contrôles suivent `NOT_RUN`, `PASS`, `FAIL`, `UNKNOWN`, `STALE`. Un élément obligatoire non établi maintient le verdict `INCONCLUSIVE` ; il ne devient pas une réserve de convenance.
