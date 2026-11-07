# Pourquoi le patron Eiffel++ est conçu ainsi

Cette note décrit les choix du N2 actuel. Les [exigences de conception](CONTRACT.md), les [repères de qualité](QUALITY.md) et les [règles de travail](../protocol/README.md) font référence. Eiffel++ est un prototype : ses outils ont des tests, son efficacité sur la production de logiciels par des LLM reste à établir. Aucun contexte d'entreprise particulier n'est présumé.

## Décisions et compromis

| Choix | Motif de génie logiciel et contrepartie | Conséquence observable |
| --- | --- | --- |
| Séparer besoin, réalisation, examen et gouvernance sans imposer quatre processus | Limiter les confusions d'autorité tout en permettant une organisation proportionnée. Un même acteur réduit la coordination mais perd l'indépendance de l'examen. | Les prompts font préciser les remises et droits effectifs ; le nombre de rôles ne prouve pas la séparation. |
| Produire N0 directement, ajouter N1 si le réemploi le justifie | Éviter un générateur sans usage ; isoler dans N1 les choix stables entre plusieurs lots. N1 coûte à concevoir et peut figer de mauvaises hypothèses. | Le prompt de génération doit comparer ce besoin de réemploi au parcours direct. |
| Réemployer des skills à contrat plutôt qu'accumuler des consignes permanentes | Rendre une opération identifiable, testable et réutilisable ; préserver les entrées, sorties et effets dus. Leur sélection et leurs dépendances ont un coût. | Capacité reliée à une tâche ; scripts testés quand disponibles ; moyen manquant déclaré. |
| Distinguer contrôles structurels, comportements observés et adoption | Une interface valide n'établit pas la correction métier. Cette séparation conserve les inconnues mais oblige à lire la portée des résultats. | `check` ne décide pas de la pertinence du harnais ; les remises ne deviennent pas des verdicts. |
| Livrer une note avec chaque paquet | Permettre la critique et l'évolution de la méthode sans dépendre de la conversation d'origine. La documentation peut dériver : sa cohérence doit être revue. | `design_rationale` est conservé avec le paquet ; la note décrit les choix effectifs et leurs conditions de révision. |

## Adapter le patron à une entreprise

Les exigences métier entrent dans le brief, les sources de référence et le profil ; elles ne sont pas remplacées par les préférences du patron. Une exigence d'examen indépendant affecte les responsabilités, les identités et les moyens de contrôle. Un changement de formats, de charge ou de plateformes affecte les contrats, les compétences et leur qualification. Une politique de données ou de déploiement affecte le mandat, les outils disponibles et les décisions réservées.

Le générateur doit nommer les fichiers et contrôles précis de son projet dans la note du niveau produit. La présente liste indique des familles de changements, pas des politiques d'entreprise ni des seuils acceptés. Les [prompts de caractérisation](prompts/01-characterize.md) et d'[adaptation](prompts/04-adapt.md) organisent cet examen.

Une autre méthode peut mieux convenir. Aucun nombre de fichiers, d'agents ou de mots ne sert d'objectif de conception. Les gains attendus restent des hypothèses tant qu'une comparaison pertinente ne les établit pas.
