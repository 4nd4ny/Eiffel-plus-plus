---
protocol_version: "0.2.0"
status: PROPOSED
---

# Prompt de génération et d'adaptation du harnais — {{PROJECT_NAME}}

Ce fichier remplace le formulaire d'expérience isolé de la version 0.1.0. Il est un point d'entrée vers un **ensemble de prompts de génération**, utilisable à l'étape zéro puis lorsqu'une adaptation est justifiée. Il n'impose pas de lancer une expérience avant chaque tâche.

## Mission à donner à l'agent

Tu dois concevoir la manière de produire le logiciel de ce projet. Utilise l'intention, les impératifs, les ressources, les préférences et le mandat disponibles. Génère une méthode propre à cette situation ; ne te contente pas de remplir une procédure fixe ou de choisir un profil prédéfini.

Distingue les trois niveaux : N2 est le patron Eiffel++, N1 est un ensemble de prompts spécialisés capables de générer et réviser la méthode, N0 est le harnais opérationnel réparti entre gouvernance, STBL, audit et produit. Le logiciel final est produit par N0.

## Choisir le bon point d'entrée

- **N1 n'existe pas :** appliquer le [patron N2](../../../meta/START.md), en commençant par [caractériser la situation](../../../meta/prompts/01-characterize.md), puis [générer N1](../../../meta/prompts/02-generate-meta-harness.md). Exécuter ensuite les prompts produits pour générer N0.
- **N1 existe, N0 manque :** charger le profil et le point d'entrée du manifeste `meta-harness.json` ; produire le harnais opérationnel demandé par ce générateur.
- **N0 existe :** examiner l'écart observé avec le prompt d'adaptation de N1. Utiliser [l'adaptation générique](../../../meta/prompts/04-adapt.md) seulement comme appui ou si N1 ne couvre plus la situation.

Charger les références détaillées au besoin. Une version fonctionnelle de N0 doit pouvoir travailler sans relire le patron N2 à chaque tâche.

## Informations à exploiter

Retrouver le besoin, les fonctionnalités indispensables ou négociables, les délais, les ressources disponibles, le coût acceptable et la charge de supervision humaine souhaitée. Identifier les sources et conserver les inconnues. Poser une question seulement si sa réponse peut changer matériellement la méthode ou résoudre un conflit bloquant. Continuer les travaux indépendants et les choix réversibles couverts par le mandat.

Construire ou mettre à jour le profil selon le [tétraèdre](../../../meta/TETRAHEDRON.md). Les poids expriment des préférences ; ils ne décrivent pas des performances et n'accordent pas de permissions. Une pondération proposée reste `PROPOSED` tant que sa source ne permet pas de la tenir pour acceptée.

## Travail génératif

1. Déduire les décisions de méthode qui comptent réellement pour ce projet : granularité des besoins, outils, contexte, délégation, contrôles, intégration, reprise et mémoire éventuelle.
2. Pour chacune, relier le choix à une obligation, une préférence, une capacité disponible ou une hypothèse. Produire une nouvelle procédure lorsque les composants existants ne conviennent pas.
3. Omettre les rôles actifs, fichiers et mécanismes inutiles à l'exécution tout en conservant les quatre responsabilités et leurs frontières d'autorité.
4. Définir un budget de conception, une condition d'arrêt et les événements qui justifieraient une adaptation. Ne pas poursuivre la recherche d'une méthode parfaite.
5. Générer les prompts ou fichiers du niveau demandé, avec leurs contrats d'entrée et de sortie. Qualifier la sortie à l'aide du [prompt d'examen](../../../meta/prompts/03-qualify.md).

## Quand une expérience est utile

Une incertitude sur l'effet d'un mécanisme peut justifier une comparaison bornée. Fixer alors l'hypothèse, les tâches, les garanties, le budget et le critère de décision avant les essais. Comparer une variante crédible ; conserver les échecs et distinguer les cas de réglage des cas de confirmation. Mesurer les quatre axes et le coût de l'expérience elle-même.

Pour une décision réversible de faible impact, un contrôle de cohérence et les premières observations du travail peuvent suffire. Une obligation non compensable exige son contrôle indépendamment de la préférence pour le coût ou la rapidité. Les essais non exécutés restent `NOT_RUN`.

## Sortie attendue

Produire N1 et/ou N0 selon la situation, les raisons de conception, les hypothèses, les limites de capacités, les conditions d'adaptation et le plus petit prochain travail autorisé. Une révision précise aussi les résultats devenus périmés et le retour possible.

Le [contrat de génération](../../../meta/CONTRACT.md) et le [protocole commun](../../../protocol/README.md) s'appliquent. Les modifications hors mandat deviennent des propositions adressées à l'autorité compétente. Une délégation déjà valable n'est pas redemandée.
