# Pourquoi le patron Eiffel++ est conçu ainsi

Cette note décrit les choix du N2 actuel. Les [exigences de conception](CONTRACT.md), les [repères de qualité](QUALITY.md) et les [règles de travail](../protocol/README.md) font référence. Eiffel++ est un prototype : ses outils ont des tests, son efficacité sur la production de logiciels par des LLM reste à établir. Aucun contexte d'entreprise particulier n'est présumé.

## Décisions et compromis

En 0.8.0, la reprise de contexte distingue l'histoire conservée et les consignes encore applicables. Le [contrat de mémoire](../protocol/MEMORY.md) préfère une sélection reconstruite, des sources exactes et des transitions contrôlées à un résumé cumulatif libre. Une exigence incertaine bloque la seule portée concernée ; une hypothèse périmée en est retirée. Ce choix évite une suppression silencieuse d'obligation, au prix d'un réexamen quand les versions changent. Le traitement sémantique reste une proposition d'agent et l'authentification une responsabilité de l'hôte. Le contrôleur ne sait pas effacer un historique déjà envoyé à un modèle.

| Choix | Motif de génie logiciel et contrepartie | Conséquence observable |
| --- | --- | --- |
| Séparer besoin, réalisation, examen et gouvernance sans imposer quatre processus | Limiter les confusions d'autorité tout en permettant une organisation proportionnée. Un même acteur réduit la coordination mais perd l'indépendance de l'examen. | Les prompts font préciser les remises et droits effectifs ; le nombre de rôles ne prouve pas la séparation. |
| Garder N0 direct et proposer la cascade N2 principes → N1 méthode → N0 usage | Le parcours direct évite une abstraction sans usage. La cascade localise les décisions réemployables, mais coûte davantage et peut propager une mauvaise hypothèse. | Le mandat choisit le parcours ; une comparaison mesure leurs résultats et leurs coûts, sans avantage présumé des trois niveaux. |
| Itérer avec IA, essais et humain dans chaque niveau | Les tests confrontent les mécanismes aux cas exécutés ; l'humain précise le besoin et juge sa suffisance. Ces deux apports ne se remplacent pas. | Une descente lie artefact, critères, couverture, inconnues, stabilité et décision humaine ; une impasse reste inconclusive. |
| Séparer stabilité et acceptation | L'absence de nouveauté peut provenir d'un manque d'information. Elle ne prouve pas que la méthode satisfait le besoin. | La dernière revue examine une couverture définie ; silence, répétition et épuisement de ressources ne ferment pas un passage. |
| Réemployer des skills à contrat plutôt qu'accumuler des consignes permanentes | Rendre une opération identifiable, testable et réutilisable ; préserver les entrées, sorties et effets dus. Leur sélection et leurs dépendances ont un coût. | Capacité reliée à une tâche ; scripts testés quand disponibles ; moyen manquant déclaré. |
| Distinguer contrôles structurels, comportements observés et adoption | Une interface valide n'établit pas la correction métier. Cette séparation conserve les inconnues mais oblige à lire la portée des résultats. | `check` ne décide pas de la pertinence du harnais ; les remises ne deviennent pas des verdicts. |
| Livrer une note avec chaque paquet | Permettre la critique et l'évolution de la méthode sans dépendre de la conversation d'origine. La documentation peut dériver : sa cohérence doit être revue. | `design_rationale` est conservé avec le paquet ; la note décrit les choix effectifs et leurs conditions de révision. |
| Conserver les décisions dans Git et sélectionner les contributions publiques | Reprendre une expérience exige son contexte et ses limites. Publier l'histoire privée exposerait aussi les données supprimées des derniers fichiers. | Historique privé par défaut ; export distinct relu et autorisé ; transfert vers N1/N2 soumis à de nouveaux essais. |

## Adapter le patron à une entreprise

Les exigences métier entrent dans le brief, les sources de référence et le profil ; elles ne sont pas remplacées par les préférences du patron. Une exigence d'examen indépendant affecte les responsabilités, les identités et les moyens de contrôle. Un changement de formats, de charge ou de plateformes affecte les contrats, les compétences et leur qualification. Une politique de données ou de déploiement affecte le mandat, les outils disponibles et les décisions réservées.

Le générateur doit nommer les fichiers et contrôles précis de son projet dans la note du niveau produit. La présente liste indique des familles de changements, pas des politiques d'entreprise ni des seuils acceptés. Les [prompts de caractérisation](prompts/01-characterize.md) et d'[adaptation](prompts/04-adapt.md) organisent cet examen.

Une autre méthode peut mieux convenir. Aucun nombre de fichiers, d'agents ou de mots ne sert d'objectif de conception. Les gains attendus restent des hypothèses tant qu'une comparaison pertinente ne les établit pas.

Le [contrat de cascade](../protocol/CASCADE.md) et le [guide d'historique](../docs/HISTORY.md) détaillent ces choix. Kolb inspire la boucle d'expérience et de révision ; Harness² inspire l'usage d'observations pour adapter le harnais ; l'Experience Factory fournit un précédent de capitalisation en génie logiciel humain. Ces filiations documentées dans les [références](../docs/REFERENCES.md) ne démontrent pas la supériorité de cette combinaison. Eiffel++ s'applique le même examen : un correctif de son protocole doit être testé et revu avant d'être présenté comme un progrès.
