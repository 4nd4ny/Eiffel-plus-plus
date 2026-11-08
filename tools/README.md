# Outils locaux d'Eiffel++ 0.8.0

Ces programmes utilisent la bibliothèque standard de Python. Ils préparent et copient des fichiers, contrôlent leur structure et conservent leur provenance. Le choix de la méthode et sa mise en œuvre relèvent de l'opérateur, des agents et de l'environnement du projet.

## Réviser la mémoire et préparer un contexte neuf

`memory.py` fournit un magasin local et un contrôle de remise pour macOS/Linux. Son [contrat](../protocol/MEMORY.md) décrit les entrées, droits, exclusions et limites ; l'[exemple Python](../examples/memory-0.8.0/demo.py) montre le cycle complet. Aucun modèle ni processus de consolidation n'est lancé implicitement.

```sh
python3 -B tools/memory.py init MAGASIN projet policy.json
python3 -B tools/memory.py propose MAGASIN worker changement.json --output proposition.json
python3 -B tools/memory.py apply MAGASIN proposition.json EMPREINTE_RETOURNEE worker
python3 -B tools/memory.py prepare MAGASIN PAQUET_NEUF --scope lot --bindings versions.json --task-file tache.txt
python3 -B tools/memory.py request MAGASIN PAQUET_NEUF --scope lot --bindings versions.json --task-file tache.txt --packet-sha256 EMPREINTE_DU_RECU
```

`policy.json` contient les listes `maintainers` et `writers`. `changement.json` contient `reason` et `operations` ; leurs formats sont illustrés par le démonstrateur. `propose` écrit une proposition neuve hors magasin et retourne l'empreinte de son JSON canonique ; il ne l'applique pas. `apply` vérifie cette empreinte, la révision de départ et les droits de l'acteur fourni par l'hôte. Les erreurs sortent avec un code non nul. `inspect --expected-revision`, `select` et `recall ID` permettent de vérifier une ancre et consulter l'état applicable.

Conserver les ancres hors des remises. Transmettre seulement les messages rendus par `request`, sans historique ajouté. L'hôte doit authentifier l'acteur, protéger le magasin, fournir les versions réellement courantes et assurer le démarrage dans un contexte neuf ; le CLI ne configure pas ces protections. Les notes retirées restent dans l'histoire privée, qui ne doit pas être montée comme instructions chez le réalisateur.

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

`prepare` assemble le besoin, le profil et les prompts de conception. `--mode cascade` demande N2 → N1 → N0 ; `--mode direct` demande un N0 itératif. Sans cette option, le point d'entrée conserve le choix du mandat au lieu d'imposer un parcours. `--seed ID` est répétable ; `--catalog DOSSIER` choisit leur base. Seules les fiches sélectionnées sont copiées dans `context/seeds/`, sans leurs artefacts ou dépendances. `preparation.json` indique `requested_mode`, `seed_artifacts_loaded: false` et un statut de publication prudent. Les documents d'historique et de références sont également copiés et identifiés par empreinte ; leurs liens vers les ressources non embarquées renvoient au catalogue public. Sans graine sélectionnée, un index vide explique comment en choisir.

La visibilité de la source et celle de la fiche restent distinctes : une recette autorisée à la publication peut provenir d'un dépôt privé. Pour les seules fiches copiées, `publication.status` et `contains_private_material` déterminent si la préparation doit être marquée privée. Sinon elle reste `unreviewed`, car la publication des graines n'autorise pas celle du brief et du profil. Ce contrôle conserve les déclarations ; il n'authentifie pas l'autorisation et ne lit pas la source privée.

Le paquet obtenu est une entrée pour un agent, pas un harnais déjà produit. L'agent suit le parcours demandé dans des dossiers distincts. La préparation ne crée pas un journal de cycles ni une décision de passage ; utiliser le mécanisme explicite ci-dessous pour la cascade.

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

## Préparer une mission de skill et sa remise

Les paquets 0.5.0 déclarent leurs [capacités](../protocol/SKILLS.md). `list PAQUET --role ROLE` présente les compétences attribuées sans charger leurs instructions complètes. Une capacité native ou indisponible reste visible ; elle ne devient pas un skill fictif.

```bash
python3 tools/skills.py list HARNAIS_N0 --role audit
python3 tools/skills.py prepare HARNAIS_N0 --role audit --skill COMPETENCE --input candidate=FICHIER --output MISSION_NEUVE
python3 tools/skills.py verify MISSION --order-sha256 EMPREINTE_CONSERVEE
python3 tools/skills.py handoff MISSION --order-sha256 EMPREINTE_CONSERVEE --to governance --artifact report=RAPPORT --output REMISE_NEUVE
```

Les ports varient avec le skill ; fournir exactement les entrées/sorties déclarées. `prepare` renvoie l'empreinte de mission que l'appelant doit conserver. Les outils n'exécutent ni le skill ni son code : un acteur autorisé lit ses préconditions, accomplit le travail et examine les postconditions. Une identité périmée interdit la remise ; une remise enregistrée ne certifie pas son contenu. Pour les commandes complètes et les scripts réellement testés, voir [l'exemple CSV](../examples/skill-handoff/README.md).

## Conserver la justification de conception

Les paquets N1 et N0 0.6.0 et 0.7.0 exigent `design_rationale`, chemin vers un document Markdown non vide et distinct des instructions exécutées. `check` expose son chemin et son empreinte avec une revue NOT_RUN. `materialize` conserve la note et indique sa localisation dans `_eiffel/project.json` ; en quatre dépôts, elle doit appartenir à une racine de rôle. Le N1 explicitement fourni est conservé avec sa propre note. Les captures incluent ces documents sans changement.

Les missions de skill rendent la note N0 consultable et la lient à leur empreinte. Les versions historiques 0.2.0–0.5.0 restent lisibles sans note inventée ; une note explicitement référencée est contrôlée. La pertinence des arguments et l’adaptation métier demandent la revue décrite dans [DESIGN.md](../protocol/DESIGN.md).

## Conserver les cycles et contrôler un passage

Le [contrat de cascade](../protocol/CASCADE.md) définit la suffisance attendue. `cascade.py` conserve un journal local de déclarations et de pièces, sans appeler de modèle, lancer les tests cités ou obtenir lui-même une réponse humaine. Un dossier de cycle contient `cycle.json` et ses artefacts/preuves réguliers, sans lien symbolique ni chemin sortant.

| Champ de `cycle.json` | Contenu |
| --- | --- |
| `level`, `purpose` | Niveau entier 2, 1 ou 0 et but de l'itération. |
| `criteria` | Objet non vide : identifiant de critère → `PASS`, `FAIL` ou `UNKNOWN`. |
| `evidence` | Chemins relatifs de pièces existantes et non vides. Leur présence ne prouve pas leur conclusion. |
| `coverage` | Liste de `{requirement, criterion}` ; chaque critère déclaré doit être relié à une exigence. |
| `required_inputs` | Liste de `{id, status}` : `AVAILABLE` exige `source` vers une pièce ; `EXCLUDED` exige `reason` ; `MISSING` empêche le passage. |
| `observation`, `hypothesis`, `change` | Textes non vides distinguant constat, explication proposée et modification ou maintien. |
| `novelty`, `blocking_unknowns`, `limits` | Listes de textes ; une liste vide indique l'absence déclarée, pas une preuve automatique. |
| `stability_probe` | Examen effectué pour rechercher une nouveauté pertinente ; texte vide autorisé au premier cycle, insuffisant pour passer. |

Depuis la racine du catalogue, avec des destinations nouvelles et des dossiers de cycles réellement préparés :

```bash
python3 tools/cascade.py start JOURNAL_NEUF --mode cascade
python3 tools/cascade.py cycle JOURNAL_NEUF DOSSIER_CYCLE
python3 tools/cascade.py gate JOURNAL_NEUF
```

`direct` démarre à N0 ; `cascade` démarre à N2. `cycle` copie les pièces, conserve leurs empreintes et renvoie notamment `event_sha256`. Répéter avec une nouvelle itération et ses preuves. Le passage exige les deux derniers cycles du niveau actif à critères tous `PASS`, avec le même inventaire ; le dernier ne déclare aucune nouveauté ni inconnue bloquante et renseigne sa sonde de stabilité. Aucune entrée requise ne doit manquer.

Le contrôle compare aussi `purpose`, la couverture, les entrées requises avec leurs empreintes et modes, et `limits`. **`required_inputs` contient les références stables du besoin et des moyens ; les nouveaux résultats d'essai vont dans `evidence`.** Placer un compte rendu horodaté dans les entrées rendrait chaque nouvelle mesure incomparable à la précédente. Référencer le contrat normatif inchangé plutôt qu'une synthèse reformulée à chaque cycle. Les artefacts produits et les observations peuvent évoluer ; leur dossier est réexaminé. Une exigence réellement modifiée impose un nouveau cycle comparable, sans la déplacer artificiellement dans les preuves pour contourner le contrôle. La comparaison est littérale : conserver le texte des limites lorsqu'il n'a pas changé de sens.

Présenter ce dernier dossier à l'humain compétent. Après sa réponse effective, conserver son texte et utiliser l'empreinte renvoyée pour ce cycle :

```bash
python3 tools/cascade.py review JOURNAL EMPREINTE_CYCLE DESCEND IDENTITE_DECLAREE REPONSE.md
python3 tools/cascade.py gate JOURNAL
python3 tools/cascade.py advance JOURNAL
```

La décision est `DESCEND` pour N2/N1, `ACCEPT` pour N0, ou `REVISE`. `gate` retourne `READY` ou `INCONCLUSIVE` avec ses motifs ; il ne change pas de niveau. `advance` exige `READY`, puis descend ou clôt N0. Ces verdicts de dossier ne sont ni un test métier ni une authentification du signataire. Une demande générale de travail ou le silence ne remplit pas `REPONSE.md`.

```bash
python3 tools/cascade.py verify JOURNAL --expected-head EMPREINTE_CONSERVEE_HORS_DU_JOURNAL
python3 tools/cascade.py reopen JOURNAL 1 "Observation nouvelle affectant la méthode"
```

`verify` examine les empreintes et les pièces ; l'ancre externe est facultative, mais permet de détecter une histoire entièrement réécrite ou tronquée par rapport à la référence conservée. Sans cette ancre, une chaîne cohérente n'est pas une preuve d'inaltérabilité. `reopen` conserve les événements et commence une nouvelle époque au niveau courant ou à un ancêtre ; les passages de ce niveau et de ses descendants sont invalidés. En mode direct, seul N0 peut être rouvert. Le journal ne crée ni commit, ni dépôt distant, ni publication réseau. Conserver les décisions utiles dans Git selon [HISTORY.md](../docs/HISTORY.md).

## Exporter une contribution revue

Préparer séparément un dossier contenant exactement les fichiers partageables, sans journal privé ni histoire Git. Le fichier JSON de revue comprend `publication: "public"`, `contains_private_material: false`, les textes `authorization_ref`, `reviewer`, `license`, `scope`, puis `files` : objet chemin relatif → `{sha256, mode}` décrivant les octets et permissions ordinaires de chaque fichier relu.

```bash
python3 tools/cascade.py export DOSSIER_PUBLIC_PREPARE REVUE_PUBLICATION.json EXPORT_NEUF
```

L'export refuse une divergence avec les empreintes revues et ajoute `PUBLICATION.json`. Il conserve une déclaration d'autorisation, sans détecteur exhaustif de secrets ni authentification de la revue. Il ne pousse rien sur GitHub. Toute publication ultérieure doit rester dans l'autorisation portant sur ce contenu exact ; le retrait d'un fichier du dernier commit ne purge pas une histoire privée.
