# Ordonnancement — {{PROJECT_NAME}}

## Étape zéro : générer la méthode

Le [patron N2](../../meta/START.md) produit les prompts spécialisés N1, puis N1 produit le harnais opérationnel N0. Conserver le profil du projet, les impératifs, les capacités disponibles, les références de génération et les conditions de révision dans la gouvernance. Utiliser `templates/EXPERIMENT.md` comme point d'entrée de génération ou d'adaptation.

La boucle ci-dessous est un composant de référence. N1 peut en regrouper les opérations, en automatiser les contrôles ou concevoir une autre organisation préservant les obligations. Ne pas en déduire un nombre imposé d'agents ou de conversations.

## Boucle générale

1. Sélectionner des obligations dont le besoin et les interfaces sont suffisamment déterminés.
2. Donner au producteur un contexte ciblé, les références exactes et un mandat.
3. Laisser produire un candidat cohérent ; exécuter les contrôles techniques utiles sans conversation superflue.
4. Soumettre le candidat figé au dépôt audit avec le quadruplet de références.
5. Retourner les contre-exemples minimisés et les inconnues.
6. Corriger le code ou ouvrir, par une voie distincte, une contestation du besoin/de l'oracle.
7. Examiner l'état intégré et l'artefact qui sera livré ; accepter selon la politique active.

Ce sont des conditions de circulation de l'information, pas sept cérémonies imposées. Des étapes peuvent être regroupées et des tâches indépendantes exécutées en parallèle.

## Taille des lots

Regrouper le travail partageant une intention et des invariants. Découper quand les erreurs deviennent difficiles à localiser. Ne pas compter les lignes comme mesure principale du risque. Conserver de petites boucles lorsque l'incertitude ou la fragilité du domaine les justifie.

## Parallélisme

Figer les interfaces utiles et répartir les domaines d'écriture. Limiter le travail simultané à la capacité de contrôle et d'intégration. Des changements sans conflit textuel peuvent être incompatibles sémantiquement. Les cycles de dépendances sont traités comme des ensembles cohérents.

## Invalidations

Déduire l'impact de liens versionnés, puis élargir si les dépendances sont incertaines. Une nouvelle configuration, migration, dépendance ou hypothèse externe peut invalider une conclusion. Les sélections de tests incomplètes servent au diagnostic rapide ; elles ne dispensent pas des contrôles requis avant livraison.

## Conditions d'arrêt

Arrêter le lot quand les critères sont satisfaits, qu'un budget est atteint, qu'une décision dépasse le mandat ou que les tentatives n'apportent plus d'information. Dans les trois derniers cas, produire un diagnostic sans déclarer le travail terminé. Continuer les lots indépendants autorisés.
