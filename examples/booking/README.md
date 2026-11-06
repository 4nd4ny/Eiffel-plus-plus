# Exemple fictif — inscription à un atelier

**Illustration de la méthode, sans logiciel construit, décision client réelle ni audit exécuté.** Tous les identifiants appartiennent à ce scénario fictif. Les contrôles restent `NOT_RUN`.

## Parcours des quatre dépôts

1. La gouvernance prépare [un mandat d'exploration](01-mandate.md).
2. STBL décrit [le besoin](02-stbl.md), recherche [une question discriminante](03-question-decision.md) et propose [un contrat](04-contract.md).
3. Le produit reçoit [un ordre de travail](05-work-order.md).
4. L'audit prépare [les contrôles et les contre-exemples](06-audit.md).

## Ce que l'exemple rend visible

Deux demandes concurrentes peuvent consommer la dernière place si l'implémentation sépare lecture et réservation sans opération atomique appropriée. Une implémentation qui refuse tout évite aussi la survente : il faut donc une obligation positive de succès. Une réponse perdue après enregistrement doit pouvoir être rejouée sans nouvel effet métier.

Les trois défauts potentiels ont des sources différentes : composition/concurrence, contrat incomplet, comportement distribué. Ils ne sont pas résolus par une simple multiplication de tests provenant tous de la même lecture du code.

## Fin de l'illustration

Le scénario s'arrête au plan d'examen. Aucune référence Git fictive ni aucun verdict favorable n'est fourni. Dans un projet réel, le PO doit accepter les décisions, l'agent doit produire le candidat et l'exécuteur doit recueillir les résultats avant toute acceptation.
