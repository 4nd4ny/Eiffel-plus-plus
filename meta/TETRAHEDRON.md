# Priorités, plafonds et tétraèdre facultatif

Les arbitrages portent sur le délai, les ressources, les fonctionnalités utiles et l'attention humaine. Ils ne définissent pas à eux seuls la qualité du logiciel. Les comportements obligatoires, la sécurité ou la fidélité des données restent des exigences lorsque le projet les impose.

Les [quatorze repères de qualité](QUALITY.md) complètent ce cadrage. L'efficience du produit diffère du coût de l'agent ; sa facilité d'usage diffère de l'autonomie de production. Ne pas réduire ces facteurs aux quatre axes du tétraèdre.

## Commencer par les décisions concrètes

Des priorités ordonnées et des limites peuvent suffire. Par exemple : livrer un premier usage local, préserver les données, limiter la supervision et différer les options. Ne pas convertir automatiquement ces phrases en coefficients.

Fragment illustratif de `preferences` :

```json
{
  "priorities": [
    "Livrer d'abord l'import et le filtre locaux.",
    "Limiter les interruptions humaines aux ambiguïtés métier.",
    "Ajouter l'export seulement si le budget restant le permet."
  ],
  "status": "PROPOSED",
  "source": "Exemple fictif, sans décision de client."
}
```

Les limites non compensables figurent dans les contraintes ou le budget. Un statut `ACCEPTED` renvoie à une décision identifiable ; une inférence reste annoncée comme telle.

## Quatre axes possibles de mesure

| Clé | Ce qu'on peut observer |
| --- | --- |
| `speed` | Délai jusqu'à l'acceptation, attentes et reprises comprises. |
| `economy` | Coût des modèles, outils et calcul, y compris conception du harnais et tentatives échouées. |
| `scope` | Valeur des comportements effectivement acceptés dans le périmètre retenu. |
| `autonomy` | Temps humain actif, interruptions et corrections nécessaires. |

`preferences.measures` est facultatif et peut commencer par les axes utiles à la décision. Une mesure indique `metric`, `unit`, `direction` et éventuellement `target`. Une cible n'est pas une observation.

L'attention humaine peut être monétisée dans un coût total, à condition de rendre le recouvrement explicite. Une conversation qui clarifie le besoin peut produire de la valeur ; le silence d'un agent n'est pas en soi un gain d'autonomie. Les permissions restent définies par le mandat.

## Utiliser des poids seulement s'ils aident

`preferences.weights` est facultatif. Lorsqu'il est utilisé, il contient `speed`, `economy`, `scope`, `autonomy` ; les quatre nombres sont finis, positifs ou nuls, de somme 1. Leur barycentre représente une répartition de préférences.

Le tétraèdre ne représente pas les performances réalisables. Une variante peut améliorer plusieurs axes ensemble. Deux projets au même barycentre peuvent appeler des méthodes différentes selon leurs risques, outils et conditions de réemploi.

Avant de calculer un score, définir les échelles et les garder fixes pendant la comparaison. Sans mesures comparables, présenter les attentes et les compromis en langage clair. Aucun score élevé ne compense une obligation non satisfaite ni ne démontre un optimum.
