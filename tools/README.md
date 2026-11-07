# Outils locaux d'Eiffel++ 0.4.0

Ces programmes utilisent la bibliothèque standard de Python. Ils préparent et copient des fichiers, contrôlent leur structure et conservent leur provenance. Le choix de la méthode et sa mise en œuvre relèvent de l'opérateur, des agents et de l'environnement du projet.

## Consulter les graines

```bash
python3 tools/seeds.py list
python3 tools/seeds.py show mini-swe-loop
python3 tools/seeds.py check
```

Les fiches sont des données : sources, contexte d'usage, contre-indications, recette proposée et observations éventuelles. Aucun code, prompt distant ou runtime n'est téléchargé ou exécuté. La présence d'une référence de décision ou de mesure ne prouve pas sa vérité.

Un catalogue privé extérieur au dépôt est accessible avec `--catalog DOSSIER`. `check --catalog DOSSIER --public` applique les conditions déclaratives de publication publique à ce dossier. Les fiches déclarées privées ou non revues pour publication sont refusées dans le catalogue public ; ce contrôle ne recherche pas les secrets dans les contenus.

## Préparer une proposition

```bash
python3 tools/meta_harness.py prepare --brief BRIEF.md --profile PROFILE.json --seed mini-swe-loop --seed codex-scoped-instructions --output NOUVEAU_DOSSIER
```

`prepare` assemble le besoin, le profil et les prompts de conception. `--seed ID` est répétable ; `--catalog DOSSIER` choisit leur base. Seules les fiches sélectionnées sont copiées dans `context/seeds/`, sans leurs artefacts ou dépendances. `preparation.json` indique `seed_artifacts_loaded: false` et conserve un statut de publication prudent. Sans graine sélectionnée, un index vide explique comment en choisir.

La visibilité de la source et celle de la fiche restent distinctes : une recette autorisée à la publication peut provenir d'un dépôt privé. Pour les seules fiches copiées, `publication.status` et `contains_private_material` déterminent si la préparation doit être marquée privée. Sinon elle reste `unreviewed`, car la publication des graines n'autorise pas celle du brief et du profil. Ce contrôle conserve les déclarations ; il n'authentifie pas l'autorisation et ne lit pas la source privée.

Le paquet obtenu est une entrée pour un agent, pas un harnais déjà produit. L'agent peut proposer directement N0 dans un dossier distinct ; un générateur N1 n'est utile que si le réemploi le justifie.

## Contrôler un paquet N0 ou N1

```bash
python3 tools/meta_harness.py check DOSSIER
```

Le manifeste `harness.json` ou `meta-harness.json` détermine les contrôles. En 0.3.0, le profil peut exprimer des priorités rédigées sans pondération numérique. Si des poids sont fournis, ils sont contrôlés. Les paquets historiques 0.2.0 restent lisibles avec leurs exigences.

Les [schémas JSON](../meta/schemas/) décrivent les formats. Le contrôleur Python réalise des vérifications explicites ; il n'est pas un moteur général JSON Schema. Il refuse les chemins sortants et les liens symboliques dans les périmètres copiés. Les références descriptives ne sont pas suivies automatiquement.

Un résultat structurel `PASS` ne décide ni de la pertinence du harnais, ni de son adoption, ni de la réalité d'une autorisation humaine.

## Matérialiser le harnais choisi

```bash
python3 tools/meta_harness.py materialize HARNAIS_N0 --output NOUVEAU_DOSSIER --git-init
```

Avec `layout: single-repo`, le résultat contient un dossier `<slug>` et un seul Git. Les responsabilités peuvent partager des fichiers. Le parcours court n'embarque pas automatiquement le patron N2.

Avec `layout: four-repos` — également utilisé par les anciens manifestes sans `layout` — les quatre dossiers restent distincts. Ce parcours copie le protocole dans chaque rôle et conserve les ressources de régénération N2 dans la gouvernance.

`--meta-harness GENERATEUR_N1` permet de conserver un générateur explicite ; son profil doit être identique à celui de N0. S'il est absent, les métadonnées le disent. Un instantané disponible ne prouve pas une filiation historique.

Les fichiers conservent leurs permissions ordinaires, dont le caractère exécutable. Les bits spéciaux setuid, setgid et sticky sont éliminés. `--git-init` initialise les racines locales sur `main`, sans commit ni remote, et ne change aucune configuration Git globale. Les liaisons restent `UNBOUND` et le statut déclaré n'est jamais promu par la copie.

## Capturer l'instance travaillée

```bash
python3 tools/seeds.py capture HARNAIS_N0 --record NOTE.json --output NOUVELLE_INSTANCE
python3 tools/seeds.py check --catalog NOUVELLE_INSTANCE
```

La capture attend le paquet N0 propre, avant matérialisation : pas de `.git`, de `_eiffel`, d'historique ni de données produit. Elle copie ce paquet dans `harness/` et la fiche dans `record.json`. L'empreinte couvre les chemins, les octets et le caractère exécutable, pour rester portable avec Git.

Les champs de provenance, de participation humaine et d'observation sont conservés tels qu'ils sont déclarés. La capture ne transforme pas un exemple en instance co-construite, ni une observation locale en preuve d'efficacité. Les parents absents du catalogue consulté sont signalés sans interdire une filiation entre catalogues.

## Ancien parcours de composants

`instantiate.py` reste disponible pour copier les quatre ensembles génériques. Il remplace les variables, rend leurs liens locaux et indique `generation_mode: generic-components`. Il ne choisit pas une méthode adaptée au projet. Le point d'entrée `templates/EXPERIMENT.md` invite ensuite à forger, essayer et capturer une organisation proportionnée.

## Destinations et portée des contrôles

Les outils exigent une destination nouvelle et refusent l'écrasement des sources. La préparation se fait dans un dossier temporaire, puis la destination est créée exclusivement. Une interruption système peut laisser une destination nouvelle partielle : ce n'est pas une transaction distribuée entre dépôts.

`check_catalog.py` contrôle les liens locaux vers les fichiers, les blocs de code, les sections attendues, les variables, les paquets illustratifs et les graines publiques. Il ne contrôle pas les ancres des titres, la disponibilité des URL externes, les licences à lui seul, le YAML libre ou la vérité des textes.

Le [rapport de validation](../docs/VALIDATION.md) distingue les résultats exécutés sur les outils et l'absence d'évaluation de la méthode. Un exécuteur existant peut utiliser les prompts ; Eiffel++ ne fournit pas de moteur d'agents, de sélecteur optimal, de déploiement des permissions ou de certification du logiciel produit.

## Composants et expériences optionnels

Depuis 0.4.0, `meta_harness.py check` vérifie aussi les champs `components` et `experience` lorsqu’ils sont présents. `capture` les conserve avec leurs fichiers, sans exécution et sans promotion du niveau de preuve. Voir [contrats et limites](../protocol/ADAPTATION.md). Les paquets 0.2.0 et 0.3.0 ainsi que les anciennes graines restent lisibles ; les empreintes historiques ne sont pas recalculées pour changer leur version.

## Essais explicites et sélection

`trials.py probe` lance un composant Python déclaré sur une copie ; `check-probe` vérifie la validité actuelle de ce reçu. `evaluate` exécute le vérificateur Python fourni explicitement, puis `select` choisit une sortie admissible en conservant la référence à égalité. Ces commandes exécutent du code autorisé, contrairement à `check` et `capture` ; elles ne fournissent pas de confinement. Voir [formats, commandes et limites](../docs/LOCAL_TRIALS.md).
