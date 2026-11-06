# Développement et vérification — {{PROJECT_NAME}}

Version : **0.1.0**. Projet : `{{PROJECT_SLUG}}`.

Ce document contient les commandes et conditions réelles du dépôt produit (`{{PRODUCT_REPO}}`). Les champs à renseigner ne sont pas des commandes exécutables. Les échanges suivent le [protocole commun](../../protocol/README.md).

## Environnement reproductible

Décrire les versions de langage et d'outils, les fichiers de verrouillage, les services nécessaires, la configuration de test et les jeux de données autorisés. Donner les noms des secrets nécessaires et leur mode d'injection, jamais leur valeur.

| Opération | Commande ou procédure réelle | Conditions nécessaires |
| --- | --- | --- |
| Préparer l'environnement | À renseigner | À renseigner |
| Construire | À renseigner | À renseigner |
| Exécuter les contrôles rapides | À renseigner | À renseigner |
| Exécuter les tests d'intégration | À renseigner | À renseigner |
| Démarrer le produit | À renseigner | À renseigner |
| Récupérer les journaux | À renseigner | À renseigner |

Un environnement préexistant doit être vérifié avant de s'appuyer sur son état. Ne pas supposer qu'un service, processus ou fichier temporaire d'une session antérieure existe encore.

## Boucle de travail

1. Identifier le mandat, le candidat de départ et les références de gouvernance (`{{GOVERNANCE_REPO}}`) et de STBL (`{{STBL_REPO}}`).
2. Inspecter les dépendances utiles et établir l'état initial nécessaire à l'interprétation des résultats.
3. Choisir un lot comportemental cohérent ; produire ou corriger le candidat.
4. Exécuter les contrôles rapides et les obligations pertinentes ; exploiter le diagnostic ou le contre-exemple retourné.
5. Élargir la vérification quand l'impact, une dépendance dynamique ou une interaction ne peut pas être exclu de manière fiable.
6. Remettre le candidat exact, ses résultats et ses limites à l'audit (`{{AUDIT_REPO}}`).
7. Vérifier l'état fusionné avec les contrôles requis avant de le considérer couvert par une acceptation.

L'ordre de travail peut prévoir des tests préalables, une recherche de contre-exemples, une comparaison d'implémentations ou une preuve ciblée. Aucune de ces techniques n'est une cérémonie obligatoire pour chaque édition. La taille des lots et la profondeur des contrôles s'ajustent au risque et au retour obtenu.

## Résultats des contrôles

| État | Sens opérationnel |
| --- | --- |
| `NOT_RUN` | Le contrôle n'a pas été exécuté pour le candidat concerné |
| `PASS` | Le contrôle a conclu positivement dans ses conditions et sa portée annoncées |
| `FAIL` | Le contrôle a constaté une violation de l'attente contrôlée |
| `UNKNOWN` | Le contrôle ne permet pas de conclure, notamment à cause d'une interruption, d'une panne ou d'une sortie ambiguë |
| `STALE` | Un ancien résultat ne s'applique plus au candidat ou aux conditions présents |

Un dépassement de délai signifie `FAIL` si le délai est précisément l'exigence contrôlée et si l'observation est valide. S'il empêche seulement le contrôle de se terminer, il signifie `UNKNOWN`. Un code de sortie non nul ne permet pas, à lui seul, de distinguer défaut produit et panne d'infrastructure.

Pour chaque élément de vérification, conserver l'objet exact, les références de contrats et de tests, la commande exécutée, les paramètres utiles, les versions de l'environnement, l'issue observée et le lien vers le journal. Les mesures annoncées doivent être calculables à partir des résultats conservés.

## Portée des vérifications

- Les tests techniques du produit donnent un retour rapide et peuvent enrichir le dossier de vérification.
- Les contrôles d'acceptation et verdicts de l'audit restent sous l'autorité de l'audit.
- Une preuve doit nommer la propriété et ses hypothèses ; une recherche bornée doit indiquer ses bornes.
- Une couverture de code n'est ni un taux de satisfaction des besoins ni une preuve d'absence de défauts.
- La cohérence de contrats locaux ne dispense pas des contrôles d'intégration, des effets externes et de l'environnement d'utilisation.

## Réutilisation des résultats et caches

La clé d'un résultat réutilisé doit couvrir toutes les entrées qui influencent ce résultat : code ou artefact vérifié, contrats, tests, configuration, dépendances, outils, données et environnement pertinents. Conserver la provenance du résultat antérieur et la justification de son applicabilité.

Si l'ensemble de ces dépendances n'est pas maîtrisé, ne pas réutiliser le résultat comme une preuve actuelle. Les appels externes, l'heure, le hasard et la concurrence demandent des conditions explicites ; une répétition empirique ne devient pas une garantie déterministe.

La sélection de tests peut être accélérée par un graphe de dépendances ou une analyse d'impact fiable. Une estimation par l'agent est une aide, pas une preuve de non-impact. Les barrières d'intégration et d'acceptation prévues par la politique restent applicables.

## Identité du candidat et fusion

Les runners vérifient un commit candidat déjà créé et publient leurs résultats pour ce commit ou pour l'artefact précisément construit à partir de lui. Ils enregistrent les conditions de construction nécessaires. Un rapport ne doit pas contenir un hash futur supposé.

L'enveloppe identifie `governance_commit`, `stbl_commit`, `audit_commit` et `product_commit`. `audit_commit` fige le plan et les oracles avant leur exécution. Le commit contenant ensuite un rapport est référencé comme `report_commit` dans un reçu ou une enveloppe extérieure ; il ne remplace aucune des quatre références d'entrée et ne doit pas créer d'auto-référence dans le rapport.

Après fusion, le résultat peut différer de chacune des branches vérifiées. Exécuter les contrôles d'intégration et d'acceptation requis sur cette nouvelle identité. Une reprise de résultats locaux exige une justification explicite de leur applicabilité ; elle n'accorde pas à elle seule un verdict au système fusionné.

## Échec, contestation et reprise

Un échec de produit appelle une correction ou une contestation argumentée de l'attente. Une panne d'infrastructure appelle une réparation ou un signalement de l'environnement. Garder ces deux cas distincts dans le rapport.

Ne pas masquer des contrôles, modifier une attente protégée ou réduire le périmètre annoncé pour obtenir un résultat positif. Transmettre une question ou un constat avec les références du [protocole](../../protocol/README.md). Respecter le budget du mandat et arrêter les tentatives qui n'ajoutent plus d'information.
