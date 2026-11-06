# Deux chaînes de génération illustratives

Ces exemples montrent ce que le [patron Eiffel++ N2](../../meta/START.md) peut produire : un **méta-harnais N1 composé de prompts spécialisés**, puis un **harnais N0 réparti entre quatre responsabilités**. Le logiciel final se situe après ces trois niveaux.

Les briefs, poids, cibles et mandats ci-dessous sont fictifs. Ils ne décrivent ni les préférences de Christian ni un projet client réel. Les fichiers sont des instanciations illustratives rédigées pour ce catalogue ; aucune exécution d'agent, qualification opérationnelle ou mesure de gain n'est attestée. Tous les paquets restent `PROPOSED` et leurs contrôles métier `NOT_RUN`.

| Projet | Particularités du besoin | Poids illustratifs vitesse / économie / fonctions / autonomie | Conséquence sur la méthode générée |
| --- | --- | --- | --- |
| [Tableau de bord local](dashboard-local/brief.md) | CSV non sensible, exécution locale, interface petite, horizon court | 0,45 / 0,30 / 0,15 / 0,10 | Un producteur, vérifications ciblées, contexte court, pas de consolidation périodique sans réemploi démontré. |
| [Service d'autorisations](access-service/brief.md) | Isolation entre organisations, décisions sensibles, évolutions répétées | 0,10 / 0,10 / 0,35 / 0,45 | Contrats d'accès explicites, vérification indépendante de l'isolation, correction autonome dans un mandat, remontée humaine des seuls arbitrages de politique. |

Ces conséquences proviennent aussi des contraintes et des capacités disponibles. Les poids ne sélectionnent pas automatiquement une recette. Une autre équipe, un autre environnement ou un besoin modifié doit pouvoir conduire le même N1 à produire une organisation différente.

## Lire une chaîne

Dans chaque projet :

- `brief.md` décrit le besoin fictif ; `profile.json` situe ses arbitrages et inconnues.
- `meta-harness/` contient le N1 : `GENERATE.md` synthétise une méthode, `ADAPT.md` la révise, `GENERATION_CONTRACT.md` borne ces opérations.
- `harness/` contient une sortie N0 plausible de ces prompts : quatre dossiers à matérialiser dans quatre dépôts. Ce sont des prompts de travail et leurs contrats, pas du code applicatif.
- Les copies de `profile.json` rendent chaque paquet autonome ; toute révision doit conserver la cohérence entre N1 et N0.

L'hypothèse illustrée par l'autonomie élevée du second cas est qu'une vérification explicite peut éviter beaucoup d'interruptions humaines. Cela ne constitue pas un résultat mesuré et ne donne aucun droit supplémentaire à l'agent.

## Vérifier et matérialiser un exemple

Depuis la racine du catalogue :

```bash
python3 tools/meta_harness.py check examples/meta/dashboard-local/meta-harness
python3 tools/meta_harness.py check examples/meta/dashboard-local/harness
python3 tools/meta_harness.py materialize examples/meta/dashboard-local/harness --meta-harness examples/meta/dashboard-local/meta-harness --output ../demo-dashboard --git-init
```

Remplacer les deux chemins `dashboard-local` par `access-service` pour l'autre chaîne. Chaque destination doit être nouvelle. L'outil contrôle la structure et copie les fichiers ; il ne lance pas les prompts, n'authentifie pas un mandat et ne valide pas le produit.

Après matérialisation, le N1 est conservé dans le dépôt governance, sous `_eiffel/meta-harness/`. Son prompt `prompts/ADAPT.md` peut donc proposer une nouvelle version N0 à partir d'observations réelles. Le patron N2 est conservé sous `_eiffel/meta/` : si le besoin sort du domaine du N1, son `START.md` sert à préparer une nouvelle spécialisation dans le mandat applicable. Le protocole commun est disponible dans chaque dépôt sous `_eiffel/protocol/`.

## Comparer sans fabriquer de résultats

Pour tester la générativité, modifier une donnée du brief et suivre le raisonnement du N1 : ajout d'un serveur partagé au premier cas, changement de politique d'accès au second. Demander un nouveau harnais et examiner les changements de contrats, de workflow et de frontières d'autorité.

Les poids décrivent des préférences ; les cibles sont des hypothèses de cadrage. Un score pondéré n'est calculable qu'après définition des mesures, normalisation justifiée et observations. Une obligation d'isolation ou de fidélité aux données reste obligatoire même si son poids d'arbitrage est faible.
