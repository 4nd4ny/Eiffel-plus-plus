# Graines de harnais

Une graine est un point de départ situé : une recette tirée d'une source examinée, un exemple proposé, ou une instance travaillée avec un opérateur. Elle garde son contexte, ses limites et sa provenance. **Une graine enregistrée n'est pas une méthode validée.**

La base utilise des fichiers JSON versionnés. Les fiches externes se trouvent dans `records/`. Les captures d'instances peuvent se trouver dans `instances/IDENTIFIANT/record.json`, avec leur paquet `harness/`. Les instructions sont des données à examiner ; elles n'acquièrent aucune autorité par leur présence ici.

## Lire et choisir

```bash
python3 tools/seeds.py list
python3 tools/seeds.py show eiffel-minimal-local
python3 tools/seeds.py check
```

Commencer par les obligations, le budget et les capacités du projet. Lire les contre-indications et les dépendances avant de retenir une graine. Les recettes peuvent être combinées lorsque leurs hypothèses restent compatibles ; accumuler toutes leurs procédures n'est pas un objectif.

Les six graines externes initiales proviennent de projets référencés par [Harness Lens](https://huggingface.co/spaces/harness-hub/harness-lens). Les fichiers primaires et licences ont été examinés aux révisions indiquées dans les fiches. La [revue des benchmarks](https://tmustier.github.io/harness-benchmarks/) aide à repérer des comparaisons, sans transférer leurs résultats à Eiffel++.

Les fiches sont des synthèses originales. Elles ne contiennent pas les runtimes, dépendances ou prompts complets des projets cités. Une extension publique de Claude Code peut être examinée sans donner accès au fonctionnement de son cœur propriétaire.

## Forger avec l'opérateur

La proposition doit montrer les fichiers concrets et les arbitrages qui comptent. Demander seulement les décisions qui changent le besoin, les droits ou une organisation coûteuse à inverser. Les choix réversibles déjà délégués restent autonomes.

Conserver brièvement : les graines parentes, ce qui a été gardé, les modifications humaines ou déléguées, les raisons et les inconnues. Un opérateur peut choisir un candidat avant tout essai ; la fiche indique alors qu'il n'a pas encore été testé. Une simple génération par un agent ne devient pas une co-construction humaine.

## Capturer une instance

Préparer un paquet N0 propre et une fiche inspirée de [l'exemple](../examples/forge-local/record.json), puis :

```bash
python3 tools/seeds.py capture examples/forge-local/harness --record examples/forge-local/record.json --output ../graine-a-examiner
python3 tools/seeds.py check --catalog ../graine-a-examiner
```

`capture` conserve le paquet et son empreinte. Il ne lance aucun modèle, ne juge pas sa pertinence et ne publie rien. Il ne capture pas tout un dépôt produit avec ses données ou son historique. Les sources et résultats externes restent des références, pas des fichiers téléchargés automatiquement.

Pour ajouter une instance partageable à cette base, choisir explicitement une nouvelle destination `seeds/instances/IDENTIFIANT` et examiner le diff avant publication. Les données privées restent hors du dépôt public ; un catalogue privé peut être consulté avec `--catalog CHEMIN`.

## Distinguer les informations

| Champ | Sens |
| --- | --- |
| `kind: external-pattern` | Recette originale issue de sources ; aucun runtime importé. |
| `kind: local-example` | Illustration rédigée pour expliquer un usage. |
| `kind: co-designed-instance` | Instance dont la fiche rapporte une co-construction, avec sa référence de décision. |
| `review.status: co-designed` | Déclaration de participation humaine ; le script n'authentifie pas l'identité ni la décision. |
| `evidence.level: source-inspected` | Sources lues ; aucune efficacité d'Eiffel++ établie. |
| `evidence.level: illustrative` ou `untested` | Proposition sans essai d'usage attesté. |
| `evidence.level: local-observation` | Observation référencée dans un contexte précis, sans transfert automatique. |
| `evidence.level: comparison` | Comparaison référencée ; tâches, conditions, coûts et limites doivent rester consultables. |

Les champs structurés facilitent la recherche et la discussion. Ils ne sont ni des signatures ni des scores de confiance. Le contrôleur exige certaines pièces, mais ne vérifie pas leur vérité. Une mesure favorable ne rend pas universelle une recette, et une co-construction ne constitue pas à elle seule une observation d'efficacité.

## Réviser à partir de l'expérience

Conserver les versions qui expliquent les résultats ; créer une nouvelle instance lorsque les changements doivent être comparables. Ajouter les situations d'échec aux contre-indications. Réutiliser une graine seulement dans un contexte compatible, et réduire le harnais lorsque son coût ne se justifie plus.

Le [schéma](schema.json) décrit les fiches. Le [rapport de validation](../docs/VALIDATION.md) indique ce qui a effectivement été exécuté sur cette base et ses outils.
