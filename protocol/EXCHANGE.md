# Enveloppe d'échange

Les métadonnées suivantes peuvent figurer dans le front matter d'un Markdown. Le YAML stocke l'information ; il ne rend pas les phrases exécutables et ne prouve ni l'identité de l'émetteur ni la véracité du contenu.

```yaml
protocol_version: "0.1.0"
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
contracts: [CTR-0001]
evidence: []
```

Cet exemple **ne peut pas être accepté** : les références sont non résolues et aucun élément probant n'est fourni. Les remplacer par des identifiants réellement observés ; ne jamais fabriquer des suites hexadécimales pour remplir les champs.

## Corps minimal

1. **Objet** : décision ou observation attendue, en une phrase.
2. **Périmètre** : comportements, chemins et environnements concernés ; exclusions.
3. **Changement** : ce qui diffère de la version de référence.
4. **Justification** : sources et raison du changement.
5. **Éléments probants** : liens exacts vers résultats complets ; aucun journal inutilement recopié.
6. **Inconnues** : questions, hypothèses et réserves restant à traiter.
7. **Suite attendue** : rôle responsable, action et condition d'arrêt.

## Élément probant minimal

Un `EVD` décrit le critère vérifié, le type de justification, l'identité exacte du candidat, l'outil et sa version, les commandes ou paramètres, le statut normalisé, les sorties conservées, la portée et les limites. Ajouter le digest de l'artefact construit et les informations de provenance émises par l'exécuteur.

Un identifiant de contrôle ou une déclaration `PASS` sans ces liens ne suffit pas à accepter le candidat. Les gros journaux peuvent être conservés dans un stockage d'artefacts avec empreinte, règles d'accès et durée de rétention ; Git garde les références et synthèses nécessaires.

## Concurrence et révisions

Avant d'appliquer une décision, vérifier sa version de départ. Si le dépôt cible a évolué, recalculer l'impact plutôt que d'écraser silencieusement le travail concurrent. Une modification qui change la signification d'une exigence produit un nouvel objet ou une nouvelle version, avec relation explicite vers l'ancien.

Pour les audits, l'enveloppe fige la révision des oracles avant le travail. Le compte rendu ultérieur ne doit pas créer une dépendance circulaire en prétendant contenir son propre commit.
