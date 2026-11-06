# 01 — Le cadre révisable

## Intention

Faire porter la discipline sur le mandat, les interfaces et les critères d'acceptation, en laissant aux agents une latitude de réalisation proportionnée aux garanties disponibles.

## Contexte et forces

Un processus très détaillé peut devenir plus coûteux que la tâche ; une autonomie sans mandat peut déplacer le besoin, modifier les contrôles ou multiplier les tentatives. Le modèle et les outils évoluent, tandis que les garanties attendues doivent rester explicites. Les budgets limitent la recherche sans définir la vérité.

## Structure

Le dépôt `governance` contient les règles communes, les responsabilités, les capacités accordées, les profils de vérification, les budgets et les expériences destinées à améliorer le harnais. Il référence les trois autres dépôts sans absorber leur contenu métier.

Fichiers : [README](../templates/01-governance/README.md), `AGENTS.md`, `POLICY.md`, `ROLES.md`, `WORKFLOW.md`, et formulaires de mandat, de modification de méthode et d'expérience.

## Contrat

### Préconditions

Le projet et les responsables sont identifiés ; les droits techniques correspondent au mandat ; les niveaux de garantie sont déterminés par catégorie de besoin. Les éléments encore non configurés restent indiqués comme tels.

### Postconditions

Chaque action déléguée a un périmètre ; chaque condition d'acceptation possède un responsable et un contrôle ; les décisions de méthode sont versionnées et mesurables.

### Invariants

La gouvernance ne réécrit pas une exigence pour faire passer du code. Une optimisation de coût ne dégrade pas implicitement les garanties. Le producteur ne contrôle pas seul l'exécuteur ou le verdict. Les décisions de méthode n'attribuent pas une autorité que les personnes n'ont pas accordée.

## Heuristiques de décision

- Choisir le plus petit dispositif qui satisfait les garanties requises.
- Mettre le calcul répétitif dans des programmes ordinaires ; réserver les modèles aux choix et interprétations.
- Agrandir un lot lorsque les obligations restent cohérentes et les reprises rares ; le réduire lorsque les échecs deviennent diffus.
- Paralléliser aux frontières de contrats stabilisées, dans la capacité d'intégration disponible.
- Ajouter un évaluateur spécialisé lorsqu'un angle mort est observé ; mesurer son apport par comparaison.
- Réexaminer le harnais après un changement de modèle, d'outil ou de domaine ; ne pas retirer un contrôle obligatoire sur la seule base d'un gain de score.

## Protocole de coopération

Un mandat transmet aux trois autres rôles le commit de gouvernance, les capacités, les obligations et le budget. Une modification de méthode passe par une proposition distincte avec impact sur les travaux en cours. Le [protocole commun](../protocol/README.md) définit les états et liens exacts.

## Arrêt et escalade

Budget atteint, absence de progrès informationnel, droits insuffisants ou contradiction de politique : suspendre le lot concerné avec diagnostic. Continuer les tâches indépendantes déjà autorisées. Une hausse de budget ou de capacité relève de l'autorité désignée.

## Antipatrons

Organigramme d'agents bavards ; prompt géant relu partout ; cérémonies simulées ; seuils de qualité abaissés en cours d'audit ; agents administrateurs des quatre dépôts ; mesure de productivité par lignes ou tokens isolés.

## Indicateurs

Coût et délai par comportement accepté, attention humaine, reprises, défauts échappés, contrôles réutilisés à bon droit, résultats inconclusifs, coût d'intégration. Comparer à périmètre et garanties constants.

## Variantes

Exploration limitée : résultats non livrables, hypothèses visibles. Standard : garanties ordinaires du projet. Renforcé : séparation d'identités et preuves ciblées supplémentaires. Les profils ne changent pas le sens des états ni le droit d'inventer une décision.
