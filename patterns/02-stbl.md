# Métapatron 02 — Besoin explicite et décisions traçables

Version : **0.2.0** · Rôle : **stbl**

## Intention

Transformer la demande du client en exigences compréhensibles, réfutables et reliées à leur source. Produire une **spécification technique des besoins logiciels (STBL)** qui permette au dépôt produit d'implémenter et au dépôt audit de juger le même comportement attendu.

La STBL décrit les résultats attendus et leurs contraintes. Elle ne devient pas une copie de l'implémentation, ni un ensemble d'exemples présentés comme une définition complète du besoin.

## Contexte et forces

- Le client exprime des intentions, des exemples et des contraintes parfois contradictoires.
- L'agent sait formaliser rapidement, mais peut transformer une hypothèse plausible en fausse exigence.
- Une spécification exhaustive écrite avant toute exploration coûte cher et vieillit vite.
- Une règle trop faible peut accepter un programme inutile ; une règle trop forte peut rendre tout programme impossible.
- Les questions au Product Owner (PO) sont précieuses lorsqu'elles départagent des comportements observables. Les choix techniques réversibles peuvent souvent avancer sous mandat.

## Structure

Le dépôt `stbl` contient un index `STBL.md` et cinq types de fiches :

| Fiche | Fonction |
| --- | --- |
| `REQ-0001` | Besoin, source, domaine, résultats attendus, exclusions, critères observables. |
| `Q-0001` | Ambiguïté, options concrètes, conséquences et décision attendue. |
| `DEC-0001` | Décision attribuable au PO ou à son délégataire, avec mandat et source consultable. |
| `CTR-0001` | Préconditions, postconditions, invariants, effets autorisés et obligations de progrès. |
| `CHG-0001` | Changement sémantique et conséquences sur les artefacts déjà acceptés. |

Chaque révision livrée est identifiable. Les exigences, décisions, contrats et références externes forment un graphe léger ; les index sont des vues de navigation, pas une seconde définition du besoin.

## Contrat

**Préconditions**

- Le mandat de spécification et les règles applicables du dépôt `governance` sont identifiés.
- Les sources client sont accessibles ou leur absence est déclarée.
- Une base existante, si elle existe, est désignée par une révision précise.

**Postconditions**

- Chaque exigence retenue possède une source ou une décision justifiant son ajout.
- Chaque comportement obligatoire a un moyen d'observation et une catégorie de validation.
- Les ambiguïtés restantes ont un propriétaire, un impact et un traitement explicites.
- Le dépôt produit et le dépôt audit reçoivent la même révision de référence.

**Invariants**

- Aucun agent ne fabrique une acceptation du PO.
- Une exigence acceptée ne peut être affaiblie pour faciliter un test ou une preuve.
- Un changement de besoin est distinct d'un changement de code et suit une fiche `CHG`.
- Les garanties sont conditionnelles à des hypothèses visibles ; une entrée métier ordinaire ne devient pas artificiellement une précondition impossible.
- Les refus et interdictions ne remplacent pas les obligations positives : le système doit aussi rendre le service demandé et, lorsque c'est requis, terminer ou progresser.
- Une référence de décision permet son contrôle ; sa présence ne prouve pas à elle seule son authenticité.

## Heuristiques de décision

1. Formaliser d'abord les comportements à fort impact : droits, données, argent, persistance, concurrence et engagements externes.
2. Pour chaque règle, chercher un succès attendu et un échec attendu. Vérifier qu'une implémentation qui refuse tout ne satisfait pas le besoin.
3. Écrire les critères non fonctionnels avec unité, seuil, population, environnement et protocole de mesure. « Rapide » ou « sécurisé » ne suffit pas.
4. Classer une ambiguïté **bloquante** si les options changent une obligation métier, un droit, un coût significatif ou un résultat d'acceptation. Sinon, la traiter sous un mandat déjà accepté et en enregistrer l'hypothèse.
5. Distinguer contradiction, oubli et préférence. Une contradiction se résout ; un oubli se rend visible ; une préférence peut rester ouverte.
6. Réutiliser les règles et preuves inchangées. Réexaminer les éléments affectés par une révision, sans relire systématiquement tout le projet.

## Protocole de coopération

Le dépôt `governance` fournit les politiques et délégations. `stbl` publie une révision contenant le périmètre accepté, les propositions encore ouvertes et les décisions correspondantes. `product` signale les impossibilités et les questions découvertes pendant l'implémentation. `audit` apporte des constats identifiés, qui peuvent contester la précision, la cohérence ou la testabilité du besoin.

Un constat ne change pas automatiquement l'exigence. `stbl` le transforme, selon le cas, en clarification, question au PO ou proposition de changement. Le PO décide des arbitrages qui dépassent le mandat. Les révisions remplacées restent retrouvables. Les échanges suivent le [protocole commun](../protocol/README.md).

## Arrêt et escalade

Suspendre uniquement la partie dépendante lorsque la source est introuvable, que deux obligations se contredisent, qu'une décision indispensable manque ou que l'autorité du décideur ne peut pas être établie. Continuer les travaux indépendants.

Une escalade contient une question courte, deux ou trois options, leurs conséquences, la recommandation de l'agent et la liste précise des travaux bloqués. Le silence ne vaut pas acceptation, sauf règle explicite déjà acceptée et applicable au cas présent.

## Antipatrons

- Générer les exigences depuis le code puis déclarer celui-ci conforme.
- Remplacer une règle générale par quelques exemples heureux.
- Rédiger une longue STBL dont aucune phrase n'a de critère observable.
- Déclarer toutes les questions bloquantes, ou les résoudre toutes silencieusement.
- Ajouter des préconditions pour exclure les contre-exemples gênants.
- Supprimer une propriété de progrès au motif que les invariants de sécurité passent.
- Copier des données client confidentielles dans un dépôt public pour faciliter la traçabilité.

## Indicateurs

Suivre le nombre d'exigences acceptées avec source, décision et critère observable ; le nombre et l'âge des questions bloquantes ; les changements de besoin après acceptation ; les constats d'audit liés à une ambiguïté ; le coût de clarification par exigence.

Ces indicateurs servent à localiser les lacunes. Un taux de liens de 100 % ne démontre ni complétude du besoin ni justesse de l'interprétation.

## Variantes

- **Petit produit** : garder les fiches courtes et grouper les règles proches ; conserver les identifiants stables.
- **Domaine critique** : renforcer les contrats, les modèles d'états et les méthodes de preuve sur les obligations choisies.
- **Existant peu documenté** : commencer par des comportements observés, explicitement non assimilés au besoin accepté, puis faire arbitrer les écarts.
- **Interface exploratoire** : faire décider des parcours représentatifs et critères d'usage ; garder visibles les appréciations qui exigent une observation humaine.
