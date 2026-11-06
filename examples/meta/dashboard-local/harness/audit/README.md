# Plan de contrôle proposé

Tous les contrôles sont NOT_RUN. Ce tableau décrit l'examen à réaliser, pas ses résultats.

| Propriété | Contrôle prévu | Limite à déclarer |
| --- | --- | --- |
| Fidélité de l'import | Jeux avec accents, virgules citées, fichier vide et champs malformés ; comparaison aux lignes attendues. | Format exact et cas indéterminés à rattacher aux décisions STBL. |
| Filtre et compteur | Comparaison à une sélection de référence pour catégorie présente, absente et ensemble complet. | Exécuter dans l'environnement de livraison. |
| Fichier inchangé | Empreinte de l'entrée avant et après les scénarios. | Une empreinte seule ne vérifie pas l'absence de transfert. |
| Fonctionnement local | Examen des dépendances et observation des accès réseau. | Une observation bornée ne prouve pas tous les comportements possibles. |
| Cellules comme données | Valeurs contenant du balisage ou du texte ressemblant à du code. | Vérifier l'affichage et l'absence d'exécution dans le navigateur retenu. |

Les contrôles doivent produire un résultat pour le candidat identifié et être protégés selon le mandat adopté. Un test ignoré, un résultat ancien ou une commande seulement décrite ne satisfait aucune obligation.

En cas d'échec, transmettre entrée, comportement attendu et comportement observé. Conserver la possibilité d'un critère erroné sans modifier ce critère à la place du responsable compétent.

Voir les [instructions d'audit](AGENTS.md). Après matérialisation, appliquer les états et références de `_eiffel/protocol/`.
