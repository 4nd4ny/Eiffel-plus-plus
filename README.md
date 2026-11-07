# Eiffel++

**Forger avec un humain une manière de travailler adaptée au projet, à partir de graines réutilisables.**

Version **0.5.0 — prototype non évalué en production de logiciels**. Les outils de fichiers sont testables ; l'utilité de la méthode, les économies et la qualité des logiciels produits restent à mesurer. Les exemples ne sont pas des expériences réussies.

## L'idée

Partir du besoin, des contraintes et du budget. Examiner quelques harnais existants. En reprendre ce qui convient, modifier une proposition concrète avec l'opérateur, l'essayer, puis conserver l'instance et les observations qui pourront servir au projet suivant.

Une graine peut être une petite recette extraite d'un projet public ou un harnais complet co-construit dans un contexte donné. Son origine ne garantit pas qu'elle conviendra ailleurs. Eiffel++ autorise le réemploi inchangé, la composition, l'invention lorsque nécessaire, et la décision de ne pas ajouter de procédure.

**Intention de conception : privilégier le harnais minimal suffisant.** Relier les comportements attendus, le code et leurs contrôles ; conserver les quatre responsabilités, leurs échanges et leurs limites d'autorité. Choisir leur répartition entre agents selon le besoin et l'indépendance requise. Retirer les répétitions et les étapes sans effet utile. La minimalité n'est ni un objectif de longueur ni un nombre imposé d'agents. La valeur reste à observer : qualité, reprises humaines, temps et coût total, face à une référence explicite.

Le point d'entrée est [meta/START.md](meta/START.md). La [base de graines](seeds/README.md) et le [démarrage](docs/QUICKSTART.md) permettent de commencer sans lire tout le catalogue.

## Specification Driven Development : préciser l'objet

| Objet | Ce que l'on explicite |
| --- | --- |
| Besoin du logiciel | Utilisateurs, comportements attendus, obligations et critères d'acceptation. |
| Spécification de la méthode | Capacités disponibles, répartition du travail, autonomie accordée, budgets, contrôles nécessaires et conditions d'arrêt. |
| Harnais utilisable, ou N0 | Instructions concrètes et mécanismes réellement disponibles pour travailler selon cette spécification. |

Le SDD désigne ici une démarche de conception guidée par ces spécifications. Ce terme n'annonce ni une norme nouvelle, ni une preuve formelle. Les préconditions, postconditions et invariants du développement par contrat restent utiles au niveau du logiciel lorsque le contexte le justifie. Une phrase contractuelle dans un Markdown ne fait pas respecter une règle.

## Le parcours courant

1. **Décrire ce qui compte.** Réutiliser le brief et les décisions existantes. Des priorités verbales, des limites de coût et des obligations suffisent ; les pondérations numériques sont facultatives.
2. **Choisir un point de départ.** Examiner une ou deux graines pertinentes, leurs limites et les outils qu'elles supposent. Donner la raison du choix et ce qui ne sera pas repris.
3. **Forger une proposition concrète.** Produire directement N0 lorsqu'il suffit. L'opérateur corrige les arbitrages importants ; les choix réversibles déjà délégués restent autonomes. Un document court ou une seule racine Git peut suffire.
4. **Essayer puis capitaliser.** Exécuter un petit travail réel, conserver les coûts et les échecs observés. Capturer une version réutilisable avec sa provenance et ses limites. Une co-construction humaine et une efficacité mesurée sont deux informations différentes.

L'absence d'essai n'interdit pas d'enregistrer une proposition. Elle interdit de la présenter comme une méthode éprouvée.

## Adapter à partir des observations

Une adaptation part d'un problème référencé, d'une hypothèse et d'un effet attendu. Préférer une procédure spécialisée consultée au besoin ou un auxiliaire déterministe lorsqu'ils répondent au problème. Les composants et leurs dépendances peuvent être déclarés dans N0 ; une fiche d'expérience conserve conditions d'emploi, réussites, échecs, coûts inconnus et limites avec le paquet. Ces contrats sont facultatifs et ne déclenchent aucune exécution automatique.

Voir le [parcours d'adaptation observée](protocol/ADAPTATION.md) et son [exemple fictif](examples/observed-adaptation/README.md). Les captures historiques restent lisibles. Les outils vérifient les références et la cohérence des déclarations ; ils ne les authentifient pas.

Des [essais locaux explicites](docs/LOCAL_TRIALS.md) peuvent observer le lancement d'un composant Python et comparer des artefacts avec un vérificateur commun. Le sélecteur conserve une référence valide en l'absence de gain et refuse de remettre une sortie sans contrôle concluant. Ces mécanismes ont des [tests locaux](docs/VALIDATION_0_4.md), sans gain général de productivité revendiqué.

## Les niveaux et les responsabilités sont des moyens

N0 est le harnais de travail. **N1**, un générateur spécialisé de harnais, devient utile si sa réutilisation ou ses adaptations récurrentes le justifient. **N2**, le patron de conception, aide à produire directement N0 ou à concevoir N1. Une chaîne N2 → N1 → N0 reste possible ; elle n'est plus obligatoire.

Les responsabilités de gouvernance, de spécification du besoin (`stbl`), d'examen (`audit`) et de production restent identifiables. Elles peuvent partager des fichiers et une racine Git. Quatre dépôts séparés sont une option lorsque les droits, la confidentialité ou l'organisation le demandent. Une séparation de noms ne constitue pas une indépendance de contrôle.

Les [quatre patrons](patterns/01-governance.md) et les anciens [composants](templates/) sont des ressources facultatives. Les [exemples à trois niveaux](examples/meta/README.md) sont conservés pour illustrer ce parcours, avec leur statut non testé.

## Base de graines

La base est un ensemble de fiches JSON versionnées, lisibles par les humains et les agents. Aucun serveur de base de données ni recherche vectorielle n'est nécessaire pour ce premier catalogue.

Chaque fiche précise le contexte favorable, les contre-indications, les capacités requises, une recette courte, les questions à l'opérateur, les sources et la qualité des observations. Les graines externes sont des synthèses originales de mécanismes examinés, pas des copies de leurs runtimes ou de leurs prompts.

```bash
python3 tools/seeds.py list
python3 tools/seeds.py show eiffel-minimal-local
python3 tools/seeds.py check
```

La présence dans la base ne vaut ni recommandation universelle ni classement d'efficacité. Une instance co-construite conserve sa filiation et la référence de la décision humaine, sans transformer cette référence en identité authentifiée. Les contenus privés restent dans un catalogue privé choisi explicitement.

## Un exemple plus petit

L'[exemple local](examples/forge-local/README.md) contient un harnais direct, un profil sans poids numériques et une seule implantation Git :

```bash
python3 tools/meta_harness.py check examples/forge-local/harness
python3 tools/meta_harness.py materialize examples/forge-local/harness --output ../essai-eiffel --git-init
```

Les scripts vérifient et copient des fichiers. Ils n'appellent aucun modèle, n'exécutent pas le logiciel futur et ne configurent pas les permissions d'une forge. Pour conserver ensuite un harnais travaillé avec un opérateur, voir la commande `capture` dans le [guide des graines](seeds/README.md).

## Ce qui reste à démontrer

Le [rapport de validation](docs/VALIDATION.md) distingue les contrôles exécutés sur les outils des hypothèses de méthode. La comparaison utile oppose une méthode simple, une génération directe de N0 et, lorsque pertinent, la génération via N1, avec le coût de préparation inclus. Ni le nombre de fichiers ni le nombre de niveaux n'est une mesure de qualité.

```bash
python3 tools/check_catalog.py
python3 -m unittest discover -s tests -v
```

Le projet est indépendant, sans affiliation ni approbation de Bertrand Meyer. Licence MIT pour les textes et outils propres à Eiffel++ ; les sources externes gardent leurs licences. Voir les [références](docs/REFERENCES.md), les [contributions](CONTRIBUTING.md) et les [changements](CHANGELOG.md).

Les [capacités et skills 0.5.0](protocol/SKILLS.md) relient les tâches aux responsabilités et aux méthodes disponibles. N1 conserve les compétences réemployables ; N0 sélectionne celles du lot. L'[exemple CSV](examples/skill-handoff/README.md) exerce des missions et remises locales avec empreintes, sans lancer de modèles. Le [nouvel outil](tools/skills.py) contrôle attribution, pièces et péremption ; il ne juge pas la compétence d'un agent.
