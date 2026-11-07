# Adapter, essayer et conserver

À partir de 0.4.0, les paquets peuvent décrire des composants spécialisés et joindre une expérience. Ces champs sont facultatifs : une méthode courte qui fonctionne ne réclame pas une nouvelle procédure. Les fichiers 0.2.0 et 0.3.0 restent lisibles ; il n'est pas nécessaire de réécrire les captures historiques.

## Partir d'un problème observé

Conserver l'observation initiale et la version de référence, puis distinguer l'hypothèse explicative de ce qui est établi. Chaque adaptation annonce l'effet attendu. Comparer sur des entrées et des moyens comparables ; conserver les échecs et les résultats nuls. Une répétition réussie n'établit pas à elle seule la causalité.

## Choisir la forme du composant

Une règle courte commune peut rester dans l'entrée N0. Une procédure spécialisée dispose d'un déclencheur et d'un chemin consultable. Une opération déterministe répétitive peut devenir un script. L'exemple `examples/observed-adaptation/` du catalogue illustre ces choix sans prétendre les avoir évalués.

Le tableau optionnel `components` du manifeste contient pour chaque élément `id`, `kind` (`procedure` ou `script`), `path`, `trigger`, `inputs`, `outputs`, `dependencies` et `limitations`. La première version de l'outillage prend en charge les scripts Python ; les autres langages peuvent rester des ressources sans qualification automatique. Les dépendances désignent des fichiers locaux embarqués, pas des commandes à télécharger.

`check` vérifie les identifiants, chemins et dépendances. Il n'exécute rien et ne prétend pas que l'agent a chargé ou suivi la procédure. Le contenu du composant reste soumis au mandat ; sa présence n'accorde aucun droit.

## Conserver l'expérience avec le paquet

Le champ optionnel `experience` du manifeste désigne un fichier JSON au format `1.0`, distinct de la version du protocole. Le schéma `meta/schemas/experience.schema.json` du catalogue et l'exemple montrent : problème et preuve locale, hypothèse, effet attendu, conditions d'emploi et d'évitement, référence, essais, coûts et décision.

Les références d'observation sont des chemins locaux conservés par la capture. Leur présence et leur empreinte ne prouvent pas la vérité du récit. Les coûts inconnus sont `null`. Une décision retenue exige un essai déclaré `PASS` et référencé, mais le contrôleur n'authentifie pas ce résultat. Une conclusion insuffisante reste `INCONCLUSIVE`. Les états des essais conservent le sens du protocole.

Une capture emporte naturellement composants, expérience et pièces locales, avec l'empreinte existante du paquet. Garder les résultats cachés d'un benchmark dans un registre d'audit séparé. Avant partage, examiner les données privées, les licences et la portée de chaque observation. Aucune publication n'est automatique.

## Réemployer sans accumuler

Repartir du socle adapté au nouveau projet. Consulter quelques graines pertinentes et réexaminer leurs faits, dépendances et contre-indications. Séparer une connaissance métier réutilisable d'un chemin, d'une personne ou d'une hypothèse propre à l'ancien travail. Retirer ce qui n'apporte rien.

Compter la conception, les exécutions, les reprises et la réflexion. Les mécanismes s'inspirent de Harness² ; ses résultats ne sont pas des mesures d'Eiffel++. Source : [Harness²](https://github.com/google-research/harness2/tree/6868817518876de8fd170c6a8354daca273b6191).

En 0.5.0, le type `skill` ajoute les capacités attribuées, ports et destinataires décrits dans [SKILLS.md](SKILLS.md). Une procédure existante peut rester une procédure ; la conversion exige une méthode et une remise réellement utilisables.
