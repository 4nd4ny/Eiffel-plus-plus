# Outils locaux d'Eiffel++ 0.2.0

Les programmes utilisent la bibliothèque standard de Python. Ils n'appellent pas les modèles, n'accèdent pas aux comptes de forge et ne configurent pas de permissions distantes.

## Préparer l'étape zéro

`meta_harness.py prepare --brief BRIEF.md --profile PROFILE.json --output NOUVEAU_DOSSIER` assemble les entrées et les prompts N2 dans un paquet utilisable par un agent. Il valide le profil et conserve les sources nécessaires. Le paquet préparé n'est pas un harnais synthétisé : la génération de N1 puis de N0 se fait en exécutant les prompts avec un LLM.

## Vérifier une sortie N1 ou N0

`meta_harness.py check DOSSIER` détecte un manifeste `meta-harness.json` ou `harness.json`, contrôle les champs requis, le profil, les poids du tétraèdre, les chemins et les fichiers attendus. Les liens symboliques et chemins sortant du paquet sont refusés dans les périmètres copiés. Une référence descriptive au générateur n'est pas suivie automatiquement.

Les trois [schémas JSON](../meta/schemas/) documentent les échanges. Le validateur Python implémente des vérifications explicites pour ces contrats ; il n'est pas un moteur général JSON Schema. Ses contrôles structurels ne prouvent ni l'authenticité du mandat ni l'adéquation de la méthode au besoin.

## Matérialiser le harnais généré

`meta_harness.py materialize HARNAIS_N0 --meta-harness GENERATEUR_N1 --output NOUVEAU_DOSSIER --git-init` produit quatre dossiers autonomes à partir des fichiers N0, et non d'une sélection de recettes génériques. Il copie un instantané du protocole, enregistre les sources et conserve N1 dans la gouvernance. Le profil de N1 doit être identique à celui de N0 en contenu JSON.

L'option `--meta-harness` est facultative. Si elle est omise, le registre signale `generator_snapshot_present: false` ; aucune capacité d'adaptation autonome n'est revendiquée. Si elle est fournie, le chemin est un argument explicite de l'opérateur, jamais une adresse chargée sur instruction d'un fichier externe.

Les empreintes sont des identifiants de contenu, pas des signatures ou des décisions. Les quatre `_eiffel/project.json` restent `UNBOUND`. Un contrôle réussi conserve le statut déclaré du paquet ; il ne l'adopte pas.

La gouvernance reçoit également le patron N2 courant dans `_eiffel/meta`, avec ses empreintes et le rôle `available-for-regeneration`. Cela rend le retour vers N2 possible après export. Cet instantané ne prouve pas la filiation réelle du N1 reçu ; la référence déclarée et la provenance observée restent distinctes.

## Copier les composants génériques

`instantiate.py` reste disponible pour l'ancien parcours. Il remplace les variables du projet, rend locaux les liens au protocole et au patron, copie le protocole dans chaque dépôt et le patron N2 uniquement dans la gouvernance. Les métadonnées indiquent `generation_mode: generic-components`.

Cette instanciation ne réalise pas la synthèse contextuelle. Le point d'entrée `templates/EXPERIMENT.md` permet ensuite d'appliquer le patron.

## Publication locale sans écrasement

Les outils exigent une destination nouvelle, extérieure au catalogue. La préparation se fait dans un répertoire temporaire dédié, puis la destination est créée exclusivement. Aucune destination préexistante n'est remplacée. Les copies ne constituent pas une transaction distribuée entre quatre dépôts ; une interruption système pendant la publication peut laisser une nouvelle destination partielle à examiner.

`--git-init` crée quatre racines locales sur `main`, sans commit et sans remote. Aucun paramètre Git global n'est modifié.

## Contrôle du catalogue

`check_catalog.py` vérifie les liens locaux vers des fichiers, les blocs de code, les sections des quatre patrons de responsabilité, les entrées génériques, les variables reconnues et les sorties illustratives lorsque leurs manifestes sont présents. Il ne vérifie pas les ancres des titres, la disponibilité des URL externes, le YAML libre ou le sens des contrats.

Les tests couvrent les frontières des outils : destinations, chemins, poids, copies, métadonnées, instantanés et indépendance des racines Git. Le [rapport de validation](../docs/VALIDATION.md) décrit les résultats réellement exécutés.

## Exécution ultérieure

Un moteur d'agents exécute les prompts. Un environnement de contrôle applique les droits et vérifications requis par le harnais généré. Ces fonctions restent distinctes des outils de fichiers fournis ici. Voir le [modèle de confiance](../protocol/TRUST.md) et le [guide de déploiement](../docs/DEPLOYMENT.md).
