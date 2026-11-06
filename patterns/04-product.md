# 04 — Le producteur sous contrat

Version du métapatron : **0.2.0**.

## Intention

Permettre à un agent de produire et de transformer du logiciel avec une grande liberté technique, dans un périmètre explicite, tout en soumettant son résultat à une acceptation qu'il ne contrôle pas. L'unité de travail est un changement accompagné d'éléments de vérification rattachés à des exigences et à des contrats versionnés.

Le producteur choisit comment implémenter, explorer, tester et corriger. Il ne décide pas seul de ce que le client aurait dû demander ni de ce qui constitue une preuve suffisante. Sa vitesse utile se mesure jusqu'à l'acceptation d'un résultat maintenable, pas au nombre de lignes générées.

## Contexte et forces

Ce patron convient à un dépôt de code séparé des dépôts de gouvernance, de spécification STBL et d'audit. Il s'applique aussi à un logiciel existant : l'état initial, ses défauts connus et ses contraintes deviennent des entrées explicites.

Les forces à équilibrer sont les suivantes :

- Un agent peut produire plusieurs solutions rapidement ; relire le contexte, intégrer les changements et vérifier les résultats reste coûteux.
- Un lot trop petit multiplie les échanges ; un lot trop grand masque les hypothèses et augmente les reprises.
- Des contrôles proches du code accélèrent la correction ; ils ne remplacent pas un oracle d'acceptation indépendant.
- Une abstraction facilite parfois l'évolution ; une généralisation spéculative crée de la dette sans répondre à un besoin.
- L'autonomie exige des interfaces stables, des retours exploitables et des limites connues. Une longue liste de consignes ne remplace pas ces moyens.

## Structure

Le dépôt produit contient le code, ses tests techniques, sa documentation d'exploitation, ses décisions locales et les références des éléments de vérification. Les gabarits correspondants figurent dans [templates/04-product](../templates/04-product/README.md).

| Élément | Responsabilité |
| --- | --- |
| Ordre de travail | Référencer les objectifs, les contrats applicables, les révisions et le périmètre autorisé |
| Agent producteur | Construire un candidat ; choisir des expériences utiles ; corriger les défauts ; signaler les contradictions |
| Outils déterministes | Compiler, analyser, exécuter, comparer et enregistrer leurs résultats |
| Dépôt STBL | Conserver les besoins, les décisions métier authentifiées, les spécifications et contrats de la version retenue |
| Dépôt d'audit | Contrôler le candidat selon sa politique et publier un verdict portant sur ce candidat |
| Gouvernance | Définir la méthode, les budgets, les autorités et les politiques applicables au mandat et à la mise en service |

La coopération suit le [protocole commun](../protocol/README.md). Un lien vers une branche mouvante ne suffit pas : chaque échange identifie le dépôt et la révision observée. La copie d'un contrat dans un contexte d'agent est une vue de travail ; elle ne devient pas une nouvelle source normative.

## Contrat

### Préconditions

Avant une modification destinée à être acceptée :

- Le changement possède un objectif, un périmètre d'écriture et les références nécessaires à son interprétation.
- Les révisions du produit, des spécifications et des contrats utilisés sont identifiées.
- Les ambiguïtés matérielles et les contraintes d'environnement sont déclarées. Une hypothèse non arbitrée n'est pas présentée comme une exigence.
- Les contrôles requis et l'autorité d'acceptation sont identifiables dans le mandat ou la politique applicable.

Une exploration peut commencer avec des inconnues si son mandat le permet. Elle produit alors un prototype ou une information à examiner, sans prétendre satisfaire un contrat encore indéterminé.

### Postconditions

À la remise d'un candidat :

- Son identité est vérifiable : commit exact et, si pertinent, empreinte de l'artefact construit.
- Le rapport relie les changements aux exigences, contrats et décisions concernés, sans revendiquer une couverture non vérifiée.
- Les résultats indiquent les commandes réellement exécutées, leur environnement pertinent, leurs sorties exploitables et leurs limites.
- Les défauts connus, contrôles non exécutés et incertitudes restantes sont visibles.
- La reprise du travail est possible à partir de l'état persistant, sans reconstruire toute la conversation.

### Invariants

1. Le producteur ne modifie pas les oracles protégés, les verdicts d'audit ni le statut attribué par le responsable produit pour faire accepter son code. Il peut proposer une correction ou une contestation argumentée.
2. Il peut ajouter et améliorer les tests techniques du produit. Une attente qui fait autorité ne change qu'au travers du protocole prévu ; un test gênant ne disparaît pas silencieusement.
3. Un résultat est attaché à son objet réel. Un test local ne prouve pas que l'état fusionné fonctionne ; une preuve de propriété ne démontre pas tous les besoins.
4. Les états des contrôles sont `NOT_RUN`, `PASS`, `FAIL`, `UNKNOWN`, `STALE`. Une interruption, une infrastructure indisponible ou une sortie ambiguë ne devient jamais `PASS`. Un ancien résultat devenu inapplicable devient `STALE`.
5. Une preuve conserve ses hypothèses, la propriété vérifiée, les versions des outils et les limites de son modèle. Une assertion exécutée sur quelques entrées reste un test.
6. Le code reste compréhensible, maintenable et conforme aux exigences de sécurité applicables. Une consommation réduite de tokens ne justifie pas une régression de ces qualités.

## Heuristiques de décision

**Choisir un lot cohérent.** Regrouper les modifications qui partagent une obligation comportementale et peuvent être évaluées ensemble. Réduire le lot si les contrats évoluent, si les échecs sont difficiles à localiser ou si l'intégration devient risquée. L'élargir lorsque les transformations sont homogènes et bien contrôlées.

**Exploiter le déterminisme.** Confier aux outils les tâches répétitives : formatage, compilation, recherche structurelle, calcul d'empreintes, comparaison de sorties et exécution des suites. Présenter à l'agent des diagnostics structurés et des extraits ciblés ; conserver les journaux complets accessibles.

**Faire varier les moyens de vérification.** Choisir selon le risque : exemples, propriétés, contre-exemples, tests de frontière, tests de concurrence, analyse statique ou preuve ciblée. La synthèse de plusieurs candidats est utile si elle réduit une incertitude réelle et reste dans le budget. Elle n'est pas obligatoire.

**Distinguer local et global.** Un contrat local solide permet de travailler en parallèle. La compatibilité des contrats, les migrations, les effets externes et les interactions restent à vérifier sur l'ensemble intégré.

**Réutiliser avec une clé complète.** Un cache de vérification dépend de l'objet vérifié, des contrats, des tests, de la configuration, des outils, des dépendances et des caractéristiques pertinentes de l'environnement. Une dépendance non maîtrisée interdit de considérer le cache comme une preuve actuelle. Une sélection de tests incertaine doit être élargie.

**Éviter les cérémonies.** Ne créer un ADR que pour une décision durable ; ne produire une passation que lorsqu'une reprise est nécessaire. Les huit fichiers du gabarit sont des supports, pas huit obligations documentaires à répéter pour chaque changement.

## Protocole de coopération

1. Recevoir un ordre de travail avec ses références, puis charger seulement le contexte nécessaire. Une information manquante se demande à son propriétaire sous une référence `Q-0001`, selon l'allocation prévue par le protocole.
2. Observer l'état initial utile et préparer une branche ou un espace de travail isolé. Ne pas attribuer à son changement un défaut déjà présent ; ne pas ignorer celui-ci s'il compromet la vérification.
3. Produire un candidat dans le mandat. Les contrats d'interface nécessaires aux travaux parallèles sont partagés avec leur révision ; tout changement d'interface est propagé aux travaux affectés.
4. Exécuter les contrôles choisis et requis. Les boucles de correction utilisent le défaut constaté ou un contre-exemple, sans reconstruire toute l'analyse à chaque tour.
5. Remettre le candidat exact et ses références `CHG-0001` et `EVD-0001` à l'audit. Le producteur distingue sa proposition de la décision du destinataire.
6. Traiter les constats `FND-0001`. Un désaccord sur l'oracle est documenté et transmis ; il ne se règle pas en affaiblissant le contrôle dans le dépôt produit.
7. Après fusion de changements concurrents, vérifier l'état réellement intégré et obtenir les résultats requis pour cette révision. Des rapports établis sur des branches isolées ne s'additionnent pas en acceptation globale.

Les identifiants cités ici illustrent leur format ; ils ne créent aucun enregistrement de projet. Les décisions utilisent `PROPOSED`, `ACCEPTED`, `REJECTED`, `SUPERSEDED`. Les verdicts d'audit reçus utilisent `ACCEPT`, `REJECT`, `INCONCLUSIVE`, `ACCEPT_WITH_RESERVATIONS`. Le dépôt produit les référence sans les réémettre à son nom.

L'enveloppe fige les quatre révisions `governance_commit`, `stbl_commit`, `audit_commit` et `product_commit`. Le plan et les oracles de `audit_commit` précèdent l'exécution ; le `report_commit` est ajouté à un reçu extérieur après enregistrement du rapport. Un verdict avec réserves ne constitue pas une autorisation automatique de livraison.

## Arrêt et escalade

Le travail courant peut continuer de façon autonome tant que les choix restent dans le mandat. Une demande d'arbitrage devient nécessaire lorsqu'une contradiction de besoins, une modification de contrat, une sortie du périmètre ou une limite d'autorité empêche de progresser correctement.

Le producteur s'arrête également lorsque le budget convenu est atteint ou que les tentatives n'apportent plus d'information. Il remet le dernier état reproductible, le constat minimal, les solutions déjà essayées et la question précise à trancher. Il ne transforme ni une limite de temps en succès ni une panne d'outil en défaut démontré du produit.

## Antipatrons

- Faire valider le même raisonnement par plusieurs agents puis appeler leur accord une preuve.
- Réécrire les tests d'acceptation, masquer un échec, désactiver une vérification ou changer un statut métier pour obtenir du vert.
- Généraliser toute l'architecture ou ajouter un framework pour une hypothèse future sans justification.
- Lire l'intégralité du dépôt et de l'historique à chaque reprise.
- Produire plusieurs branches incompatibles plus vite que l'intégration ne peut les absorber.
- Ajouter des tests qui répètent l'implémentation sans pouvoir distinguer un comportement correct d'un comportement fautif.
- Confondre une explication convaincante, une couverture de lignes et une preuve d'adéquation au besoin.

## Indicateurs

Mesurer le délai, le coût d'inférence et de calcul, ainsi que le temps humain jusqu'à l'acceptation d'un changement. Suivre aussi les défauts échappés, reprises après intégration, contrôles inutilisables, preuves périmées et violations de contrats.

Pour interpréter ces mesures, conserver la taille et la nature du changement, le risque, l'état initial et les obligations réellement contrôlées. Une réduction des tokens accompagnée de plus de défauts n'est pas une amélioration. La dette doit désigner un problème concret, ses effets et son traitement prévu ; un score abstrait ne suffit pas.

## Variantes

- **Correction limitée :** petit contexte, reproduction ciblée, modification étroite et contrôles de régression pertinents.
- **Transformation homogène :** génération ou réécriture par outil, lot plus large, invariants de transformation et vérification des usages.
- **Noyau critique :** contrats plus précis, analyse des hypothèses, preuve ciblée et contrôles d'intégration ; les garanties restent limitées à leur portée annoncée.
- **Exploration produit :** plusieurs prototypes possibles, résultats explicitement exploratoires, arbitrage du besoin avant revendication de conformité.
- **Logiciel existant peu documenté :** caractérisation de l'existant comme observation, sans transformer tous ses comportements historiques en exigences acceptées.
