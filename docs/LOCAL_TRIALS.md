# Observer une activation et conserver une référence valide

`tools/trials.py` fournit des essais locaux explicites sur copies. Il ne lance aucun LLM, ne choisit pas une procédure à sa place et ne constitue pas un environnement de confinement. L'appelant autorise le script ou le vérificateur passé à la commande. Pour du code non fiable, l'isolation des fichiers et du réseau appartient à l'environnement d'exécution. Python 3.10+ et POSIX sont requis pour ces commandes ; les anciens outils restent utilisables séparément.

## Observer un composant

```bash
python3 tools/trials.py probe examples/observed-adaptation/harness --component csv-check --arg fixtures/good.csv --output generated/probe-good
python3 tools/trials.py check-probe examples/observed-adaptation/harness generated/probe-good
```

Le contrôleur copie le paquet vers une destination nouvelle, puis un lanceur Python lit et compile les octets du composant. Il transmet leur empreinte au parent par un canal distinct de la sortie du script, ferme ce canal puis exécute le code. Le reçu conserve trois informations distinctes :

| Champ | Portée |
| --- | --- |
| `activation_status` | `PASS` si le lanceur a signalé la lecture et la compilation des octets attendus ; `UNKNOWN` sinon. Sans reçu, `check-probe` renvoie `NOT_RUN`. Un paquet modifié devient `STALE`. |
| `execution.status` | `PASS` si le processus termine avec le code zéro ; `FAIL` sur code non nul ; `UNKNOWN` sur délai dépassé ou lancement impossible. |
| `behavior_status` | Toujours `NOT_RUN` dans ce reçu : le comportement attendu doit être contrôlé séparément. |

Une procédure textuelle est refusée par `probe` : aucun événement de lecture d'un fichier ne démontre que le LLM l'a suivi. Un adaptateur instrumenté spécifique serait nécessaire pour observer son chargement ; l'obéissance et l'efficacité resteraient des questions distinctes.

Un script qui annonce PASS dans sa sortie ne peut pas produire à lui seul le signal d'activation du lanceur. Il peut toutefois terminer avec succès sans accomplir le travail : le contrôle comportemental reste indispensable. Les reçus ne sont ni signés ni résistants à un opérateur qui réécrirait toutes les preuves. Les copies évitent la modification accidentelle du paquet source ; elles ne restreignent pas les autres droits d'un programme exécuté.

## Évaluer des artefacts avec le même contrôle

```bash
python3 tools/trials.py evaluate ARTEFACT_REFERENCE --checker VERIFIER.py --output generated/reference
python3 tools/trials.py evaluate ARTEFACT_CANDIDAT --checker VERIFIER.py --output generated/candidat
python3 tools/trials.py select --baseline generated/reference --candidate generated/candidat --output generated/choix
```

Le vérificateur reçoit le chemin de la copie de l'artefact comme premier argument. Il doit terminer avec code zéro et écrire un seul objet JSON : `{"criteria":{"format":"PASS","invariant":"PASS"},"score":1}`. Chaque critère déclaré est obligatoire ; `FAIL` et `UNKNOWN` sont admis comme résultats, mais ne rendent pas la sortie sélectionnable. Le score est un nombre fini positif ou nul, à maximiser. L'exécuteur conserve stdout, stderr, durée, statut de fin et empreintes.

Le vérificateur doit être autonome ou vérifier explicitement l'identité de ses dépendances. L'outil lie automatiquement son fichier principal, pas l'intégralité d'un environnement externe. Il ne doit pas modifier l'artefact : une modification détectée pendant l'évaluation rend le résultat `STALE`. Une panne ou une réponse non interprétable reste `UNKNOWN`, sans score inventé.

Le sélecteur vérifie l'identité des artefacts et du vérificateur, ainsi que la cohérence du résultat avec la sortie conservée. Tous les reçus doivent utiliser le même vérificateur ; les sorties admissibles doivent partager les mêmes critères. Un reçu périmé ou corrompu interrompt la sélection et doit être remplacé par une nouvelle évaluation. Cette vérification de cohérence ne remplace pas des droits indépendants sur les preuves.

## Décider sans dégrader silencieusement

Parmi les sorties admissibles, choisir le score maximal ; à égalité, garder la référence. Il n'y a pas d'arbitrage implicite entre une qualité et un coût inconnus. Si la référence échoue, elle ne sert pas de repli. Si rien n'est admissible, le résultat est `INCONCLUSIVE` et aucun artefact n'est remis. Sinon, le résultat est `KEEP_BASE` ou `ADOPT`, avec copie exacte de l'artefact évalué. La sélection ne compose jamais une sortie inédite.

Une référence peut donc être conservée quand une adaptation échoue ou n'améliore pas le résultat, et une adaptation peut être retenue quand elle apporte un gain vérifié. Le besoin et les critères applicables doivent être fixés en dehors du pouvoir de modification du candidat.

## Résultats et limites

Les [vérifications 0.4.0](VALIDATION_0_4.md) donnent les cas exécutés et leurs limites. Il s'agit de mécanismes logiciels qualifiés localement, pas d'un gain général établi sur les performances d'un modèle. Leur coût d'intégration, de vérification et de maintenance doit rester dans le bilan de la méthode.
