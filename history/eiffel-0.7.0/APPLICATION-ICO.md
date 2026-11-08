# Première application : la revue a changé le processus

État au 8 novembre 2026 : **comparaison inachevée**. Après la revue contextualisée décrite ci-dessous, l'humain a accepté d'ajouter le parcours complet aux trois corrections. Aucun avantage de la cascade sur N0 direct n'est établi.

La préparation utilise deux constructeurs à contexte neuf, avec le même modèle hérité et aucun changement de configuration demandé. Le service ne fournit pas ici son identifiant résolu, les tokens ou la facturation : ces mesures restent inconnues. Aucun plafond commun n'est imposé. Les preuves détaillées et le code du projet restent dans un dépôt local privé, sans distant ; ce document est une synthèse partageable.

## Observations initiales qui ont changé une décision

| Observation réelle | Suite observée | Ce qu'elle établit |
| --- | --- | --- |
| Un contrôleur visible référençait un runtime situé dans le dossier réservé à l'évaluateur. | Le runtime générique a été rendu accessible aux deux bras, sans exposer les oracles. | Le contrôle des entrées peut détecter une dépendance incohérente avant réalisation. |
| Les sessions employaient des versions de Node différentes malgré une commande identique. | Le binaire et son empreinte ont été fixés pour les deux bras ; la référence a été réévaluée. | La commande seule ne suffit pas à identifier l'environnement. |
| L'humain ne pouvait pas juger les trois corrections sans rappel du cahier des charges. | Le contexte produit et les conséquences ont été présentés ; les prompts Eiffel++ ont été corrigés. | Une revue humaine doit être compréhensible sans dépendre de la mémoire de la conversation. |
| Trois corrections de modules couvrent peu les interactions essentielles du produit. | Un parcours import → recherche → réponse sourcée ou abstention, avec contrôle des sorties réseau, a été proposé. | Le périmètre des essais conditionne la portée d'une conclusion sur le harnais. La proposition reste ouverte. |

## Ce qui avait été exécuté au premier arrêt

Le bras cascade conserve deux dossiers N2, des sondes et une porte `INCONCLUSIVE`. Aucun N1 ni N0 n'a été généré dans ce bras sans la décision requise. Le retour humain est réel ; il demande une clarification, pas une acceptation.

Le bras direct conserve ses versions N0 et un pilote de correction d'URL. Ce pilote réussit les 4 contrôles visibles et les 98 vérifications complémentaires écrites par l'exécutant ; seul le module autorisé a changé. Ces compléments sont un auto-contrôle, pas une évaluation indépendante. Les cas réservés n'ont pas été exécutés sur ce pilote. La durée observée est de 362,914 secondes, dont 23,554 de correction et 0,599 de tests instrumentés ; le reste comprend lecture, analyse, préparation et rédaction des preuves. Ces mesures ne suffisent pas à comparer les parcours.

Une sonde de faisabilité du parcours élargi a exercé les vraies fonctions d'import et de réponse avec un fournisseur fictif, sans installation : sortie d'import attendue, citation et abstention sur ensemble vide. La recherche, la CLI et la suite complète n'ont pas été exécutées, faute de dépendances dans la copie. Le journal réseau vide de cette sonde ne prouve pas une absence générale de sorties réseau. Aucun résultat n'est attribué à un harnais pour cette sonde.

Le pilote employait N0 v3. Son retour a produit v4, qui précise les chemins des copies et l'environnement commun. V4 n'a pas encore fait l'objet d'une nouvelle réalisation : les résultats de v3 ne sont pas présentés comme des résultats d'exécution de v4.

## Conclusion bornée

Le mécanisme a permis de conserver un désaccord de compréhension et d'empêcher une descente prématurée. C'est un résultat sur le processus de revue. La qualité comparative du code, le temps total des deux approches et leur coût monétaire restent **inconnus** tant que le périmètre, les passages et les réalisations comparables ne sont pas terminés.

Les [commits de développement](README.md) et le [contrat de cascade](../../protocol/CASCADE.md) rendent ces choix réexaminables. Cette expérience propose des précautions réutilisables ; elle ne démontre pas une supériorité générale de trois niveaux.

## Reprise après la décision humaine

L'opérateur a choisi d'ajouter le parcours complet. Le quatrième lot fait produire une suite d'intégration du produit existant ; il ne lui ajoute pas de fonctionnalité. Les cinq obligations couvrent import réel, recherche dans la mémoire produite, réponse liée aux sources, abstention par le vrai parcours et contrôle des tentatives réseau. Les modèles déterministes bornent la portée à l'assemblage logiciel.

Les dépendances verrouillées ont été installées dans une copie, sans scripts d'installation, poids de modèle ni navigateur. Les 78 contrôles existants sélectionnés passent. Un lancement externe a vérifié les sources TypeScript, les variables attendues et le refus d'écrire dans le produit. La protection système permet la boucle locale et refuse une connexion extérieure.

L'évaluateur réservé du lot a été qualifié : une suite de référence passe sur le produit et sur un changement sans effet ; quatre régressions comportementales et une tentative réseau injectée sont détectées. Ce résultat qualifie l'instrument de comparaison, pas un harnais candidat. Les solutions et cas réservés restent hors du contexte des constructeurs et des exécutants.

Un contrôle de passage réel a ensuite révélé une mauvaise séparation entre entrées stables et observations nouvelles. Les dossiers sont repris avec leurs anciennes versions conservées ; les [instructions de qualification](../../meta/prompts/03-qualify.md) et le [guide du contrôleur](../../tools/README.md) ont été précisés. Les coûts de ces reprises appartiennent au parcours cascade et ne doivent pas être effacés du bilan.

Deux nouveaux cycles comparables ont ensuite permis le passage N2 → N1. Le reçu distingue l'accord humain sur le périmètre de l'examen technique du coordinateur ; il ne prétend pas que l'humain a lu des pièces produites après sa réponse. La méthode N1 est en préparation et reste à soumettre à la revue prévue.

Le bras direct a conservé six versions N0. Son second pilote, avec v6, a produit une suite du parcours complet : les cinq obligations sont étayées, les six tests comptés par Node (dont le parent) passent sans saut, et le produit est préservé. Sa durée observée est de 608,070 secondes, dont 1,516 seconde pour le lancement réussi avec compilation et tests. Les cas réservés n'ont pas été exécutés sur ce candidat. V6 a été maintenu après examen de ce retour.

Une reprise de lancement a aussi révélé une erreur du mandat commun : une destination de preuves déjà créée ne doit pas être réutilisée. La consigne commune exige désormais une destination neuve à chaque tentative et la conservation des anciennes traces. Ce défaut de coordination n'est pas attribué au harnais v6, qui exigeait déjà une destination neuve.

Le plan final prévoit quatre lots, deux répétitions par lot et par bras, soit seize réalisations à contexte neuf après gel des deux N0. Il sépare qualité des correctifs et capacité de la suite d'intégration à détecter des régressions. Aucune de ces réalisations finales n'a encore été exécutée ; les pilotes et sondes ne les remplacent pas.
