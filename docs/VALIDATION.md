# Validation d'Eiffel++ 0.2.0

Date : **6 novembre 2026**. Périmètre : patron N2, prompts, exemples N1/N0, protocole, schémas et outils locaux. Cette validation ne constitue pas un audit de logiciel métier, une certification de sécurité ou une mesure de l'efficacité des harnais proposés.

## Contrôles exécutés

| Contrôle | Résultat observé | Portée |
| --- | --- | --- |
| `python3 tools/check_catalog.py` | **PASS**, 91 fichiers Markdown | Liens locaux, blocs de code, entrées, sections, variables, schémas JSON lisibles et structure des quatre paquets N1/N0 illustratifs. |
| `python3 -m unittest discover -s tests -v` | **PASS**, 16 tests | Six tests de l'instanciation générique et dix tests du nouvel outil de génération de paquets. |
| Paquets `dashboard-local` N1 et N0 | Structure **PASS** | Sémantique et autorité non attestées par le script : `NOT_RUN`. |
| Paquets `access-service` N1 et N0 | Structure **PASS** | Sémantique et autorité non attestées par le script : `NOT_RUN`. |
| Préparation et matérialisation des deux exemples | **PASS** | Deux entrées N2 préparées, huit dossiers de rôle matérialisés, fichiers spécifiques conservés et liens locaux valides. Essais réalisés dans des répertoires temporaires. |
| Revue des niveaux et de la générativité | Corrections intégrées | Revue argumentée par agents, distincte d'une validation expérimentale sur des projets externes. |

## Frontières testées dans les outils

- Les quatre rôles donnent quatre racines Git distinctes, sans commit ni remote inventé.
- L'instanciation générique conserve son comportement et ses liens, avec N2 copié uniquement dans la gouvernance.
- Les poids invalides, booléens, non finis, incomplets ou de somme incorrecte sont refusés ; aucune normalisation silencieuse ne modifie une préférence.
- Les dossiers et chemins dangereux, imbriqués ou symboliques sont refusés dans les cas testés.
- Une destination préexistante, y compris créée pendant la préparation, n'est pas écrasée.
- Les fichiers N0 sont copiés tels que fournis ; le profil et les sources nécessaires sont conservés.
- N1 peut être archivé dans la gouvernance ; ses profils doivent correspondre à N0. Les générateurs rejetés ou remplacés ne sont pas utilisés comme générateurs actifs.
- Une référence descriptive à `generator` n'est jamais suivie comme une instruction de lecture externe.
- Le N2 disponible est archivé comme ressource de régénération, sans affirmation d'une filiation historique non établie.
- Les métadonnées distinguent structure, sémantique, autorité et statut déclaré ; la matérialisation ne transforme pas une proposition en décision acceptée.
- La préparation reste explicitement une entrée : elle ne prétend pas avoir appelé un modèle ou généré N1/N0.

## Corrections de conception issues de la revue

1. Les trois niveaux sont distingués des quatre responsabilités : N2 génère N1, N1 génère N0, N0 produit le logiciel.
2. Les prompts N1 des exemples lisent le profil courant au lieu de recopier en dur leurs poids et budgets. Ils demandent des transformations de méthode lorsque le contexte pertinent change.
3. Une fonction de qualification peut être incluse dans un prompt ; trois fonctions ne rendent pas obligatoires trois fichiers ou trois agents.
4. N1 et N2 restent accessibles après export des quatre dépôts. La disponibilité d'un instantané n'est pas une preuve de sa participation passée à la génération.
5. Le budget est commun aux niveaux et aux délégations d'une étape zéro ; il n'est pas réinitialisé par un changement de contexte.
6. Le gabarit d'expérience devient un point d'entrée génératif. Les expériences comparatives sont proportionnées à une incertitude, au lieu d'être un préalable universel.
7. Les états du protocole et les limites des mandats sont conservés ; les adaptations déjà déléguées ne déclenchent pas de nouvelle approbation systématique.

## Ce qui n'est pas établi

Les exemples sont des instanciations illustratives rédigées pour le catalogue. Les tests ne démontrent pas qu'un LLM quelconque exécutera parfaitement les prompts sur un nouveau projet. Aucun gain chiffré, optimum, taux de généralisation ou niveau d'autonomie n'a été mesuré sur un corpus de projets.

Les outils locaux n'appellent pas de modèle et ne déploient pas les droits, contrôles, infrastructures d'audit ou protections distantes décrits dans les harnais. Ces mécanismes doivent être mis en œuvre dans l'environnement choisi. Les contrôles effectués sur le catalogue ne certifient pas les logiciels qui seront produits avec lui.

## Reproduction

Les deux commandes de contrôle figurent ci-dessus. Les commandes de préparation et matérialisation des exemples sont données dans le [démarrage](QUICKSTART.md) et les [exemples](../examples/meta/README.md). Utiliser une nouvelle destination extérieure au catalogue pour chaque essai.

Le commit contenant ce document identifie la version livrée sans inscrire son propre identifiant dans le fichier. L'historique Git conserve l'édition 0.1.0 et sa validation initiale de six tests.
