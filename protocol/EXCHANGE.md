# Enveloppe d'échange facultative

Une note courte avec des références peut suffire. Employer une enveloppe lorsque plusieurs acteurs ou un outil ont besoin d'un format commun. Le YAML conserve des déclarations ; il ne rend pas les phrases exécutables et n'authentifie personne.

```yaml
protocol_version: "0.3.0"
type: CANDIDATE
id: CHG-0001
from_role: product
to_role: audit
status: PROPOSED
references:
  governance_commit: "À_RÉSOUDRE"
  stbl_commit: "À_RÉSOUDRE"
  audit_commit: "À_RÉSOUDRE"
  product_commit: "À_RÉSOUDRE"
requirements: [REQ-0001]
contracts: []
evidence: []
```

Cet exemple ne permet aucune acceptation : les références sont non résolues et aucun résultat n'est fourni. Les quatre références peuvent désigner un même commit lorsque les responsabilités partagent un dépôt. Ajouter les chemins concernés ; ne jamais inventer un SHA. La liste `contracts` est utile seulement si le projet emploie des contrats identifiés.

## Corps utile

Indiquer l'objet de la décision ou de l'observation, le périmètre, le changement, sa raison, les éléments probants, les inconnues et la prochaine action attendue. Regrouper les informations déjà présentes ailleurs par référence ; ne pas recopier tous les échanges de la séance.

Un élément probant décrit le critère, le candidat exact, le moyen de contrôle, les commandes ou paramètres, le statut, les sorties conservées et les limites. Ajouter l'empreinte de l'artefact et l'environnement pertinent. Un mot `PASS` ou un identifiant de test ne remplace pas ces informations.

Les journaux volumineux peuvent rester dans un stockage adapté ; Git conserve les références nécessaires. Les données privées gardent leur périmètre d'accès.

## Révisions

Avant une écriture partagée, vérifier la révision attendue avec un mécanisme conditionnel réellement disponible. En cas de conflit, relire et réévaluer l'impact plutôt que d'écraser le travail concurrent.

Un changement sémantique d'exigence conserve sa relation avec la version antérieure. Un audit fixe les critères avant l'exécution ; son rapport ultérieur ne prétend pas contenir son propre commit.

La fiche d'une graine conserve séparément provenance, co-construction et observations. Un échange d'adoption peut y être référencé ; cette référence ne transforme pas une instance non testée en méthode évaluée.
