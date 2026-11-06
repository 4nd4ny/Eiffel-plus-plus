# Deux chaînes de génération illustratives

Ces illustrations héritées de **0.2.0** conservent leurs profils et manifestes N1/N0 dans cette version. Elles montrent un parcours facultatif : un méta-harnais N1 puis un harnais N0 réparti en quatre dépôts. Eiffel++ **0.3.0** permet de forger N0 directement, avec quatre responsabilités et une topologie adaptée ; voir le [petit exemple local](../forge-local/README.md).

Les briefs, poids, cibles et mandats ci-dessous sont fictifs. Ils ne décrivent ni les préférences de Christian ni un projet client réel. Les fichiers sont des instanciations illustratives rédigées pour ce catalogue ; aucune exécution d'agent, qualification opérationnelle ou mesure de gain n'est attestée. Tous les paquets restent `PROPOSED` et leurs contrôles métier `NOT_RUN`.

| Projet | Particularités du besoin | Poids illustratifs vitesse / économie / fonctions / autonomie | Conséquence sur la méthode générée |
| --- | --- | --- | --- |
| [Tableau de bord local](dashboard-local/brief.md) | CSV non sensible, exécution locale, interface petite, horizon court | 0,45 / 0,30 / 0,15 / 0,10 | Un producteur, vérifications ciblées, contexte court, pas de consolidation périodique sans réemploi démontré. |
| [Service d'autorisations](access-service/brief.md) | Isolation entre organisations, décisions sensibles, évolutions répétées | 0,10 / 0,10 / 0,35 / 0,45 | Contrats d'accès explicites, vérification indépendante de l'isolation, correction autonome dans un mandat, remontée humaine des seuls arbitrages de politique. |

Ces choix illustratifs dépendent aussi des contraintes et des capacités. Les poids ne sélectionnent pas automatiquement une recette. L’adaptation du même N1 à d’autres contextes reste une hypothèse à éprouver.

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

Dans ce parcours à quatre dépôts, la matérialisation conserve N1 sous `_eiffel/meta-harness/` dans governance, le patron courant sous `_eiffel/meta/` et le protocole sous `_eiffel/protocol/`. `prompts/ADAPT.md` peut servir à proposer une révision de N0 ; une conception directe reste possible. Ces copies ne démontrent aucune exécution des prompts ni compatibilité métier.

## Comparer sans fabriquer de résultats

Pour tester la générativité, modifier une donnée du brief et suivre le raisonnement du N1 : ajout d'un serveur partagé au premier cas, changement de politique d'accès au second. Demander un nouveau harnais et examiner les changements de contrats, de workflow et de frontières d'autorité.

Les poids décrivent des préférences ; les cibles sont des hypothèses de cadrage. Un score pondéré n'est calculable qu'après définition des mesures, normalisation justifiée et observations. Une obligation d'isolation ou de fidélité aux données reste obligatoire même si son poids d'arbitrage est faible.
