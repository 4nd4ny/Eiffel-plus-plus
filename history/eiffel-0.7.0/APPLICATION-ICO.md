# Première application : la revue a changé le processus

État au 8 novembre 2026 : **comparaison inachevée**, périmètre soumis à une revue humaine contextualisée. Aucun avantage de la cascade sur N0 direct n'est établi.

La préparation utilise deux constructeurs à contexte neuf, avec le même modèle hérité et aucun changement de configuration demandé. Le service ne fournit pas ici son identifiant résolu, les tokens ou la facturation : ces mesures restent inconnues. Aucun plafond commun n'est imposé. Les preuves détaillées et le code du projet restent dans un dépôt local privé, sans distant ; ce document est une synthèse partageable.

## Observations qui ont changé une décision

| Observation réelle | Suite observée | Ce qu'elle établit |
| --- | --- | --- |
| Un contrôleur visible référençait un runtime situé dans le dossier réservé à l'évaluateur. | Le runtime générique a été rendu accessible aux deux bras, sans exposer les oracles. | Le contrôle des entrées peut détecter une dépendance incohérente avant réalisation. |
| Les sessions employaient des versions de Node différentes malgré une commande identique. | Le binaire et son empreinte ont été fixés pour les deux bras ; la référence a été réévaluée. | La commande seule ne suffit pas à identifier l'environnement. |
| L'humain ne pouvait pas juger les trois corrections sans rappel du cahier des charges. | Le contexte produit et les conséquences ont été présentés ; les prompts Eiffel++ ont été corrigés. | Une revue humaine doit être compréhensible sans dépendre de la mémoire de la conversation. |
| Trois corrections de modules couvrent peu les interactions essentielles du produit. | Un parcours import → recherche → réponse sourcée ou abstention, avec contrôle des sorties réseau, a été proposé. | Le périmètre des essais conditionne la portée d'une conclusion sur le harnais. La proposition reste ouverte. |

## Ce qui a réellement été exécuté

Le bras cascade conserve deux dossiers N2, des sondes et une porte `INCONCLUSIVE`. Aucun N1 ni N0 n'a été généré dans ce bras sans la décision requise. Le retour humain est réel ; il demande une clarification, pas une acceptation.

Le bras direct conserve ses versions N0 et un pilote de correction d'URL. Ce pilote réussit les 4 contrôles visibles et les 98 vérifications complémentaires écrites par l'exécutant ; seul le module autorisé a changé. Ces compléments sont un auto-contrôle, pas une évaluation indépendante. Les cas réservés n'ont pas été exécutés sur ce pilote. La durée observée est de 362,914 secondes, dont 23,554 de correction et 0,599 de tests instrumentés ; le reste comprend lecture, analyse, préparation et rédaction des preuves. Ces mesures ne suffisent pas à comparer les parcours.

Une sonde de faisabilité du parcours élargi a exercé les vraies fonctions d'import et de réponse avec un fournisseur fictif, sans installation : sortie d'import attendue, citation et abstention sur ensemble vide. La recherche, la CLI et la suite complète n'ont pas été exécutées, faute de dépendances dans la copie. Le journal réseau vide de cette sonde ne prouve pas une absence générale de sorties réseau. Aucun résultat n'est attribué à un harnais pour cette sonde.

## Conclusion bornée

Le mécanisme a permis de conserver un désaccord de compréhension et d'empêcher une descente prématurée. C'est un résultat sur le processus de revue. La qualité comparative du code, le temps total des deux approches et leur coût monétaire restent **inconnus** tant que le périmètre, les passages et les réalisations comparables ne sont pas terminés.

Les [commits de développement](README.md) et le [contrat de cascade](../../protocol/CASCADE.md) rendent ces choix réexaminables. Cette expérience propose des précautions réutilisables ; elle ne démontre pas une supériorité générale de trois niveaux.
