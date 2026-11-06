# Deux objets à spécifier

Exemple fictif, PROPOSED ; les préférences ci-dessous ne sont pas une décision d'un client.

## Besoin du logiciel

- REQ-0001 : lire localement un CSV avec en-tête contenant `categorie`, filtrer sur une valeur demandée et restituer les lignes retenues ainsi que leur nombre. Comparaison exacte des catégories ; les autres valeurs sont conservées comme textes, y compris les doublons.
- REQ-0002 : ne pas modifier le fichier source et ne pas envoyer de données sur le réseau.
- REQ-0003 : signaler un fichier illisible, un en-tête sans `categorie` ou un CSV malformé. Une entrée valide sans ligne retenue donne un résultat vide et un compte nul.

La forme exacte de la sortie CLI peut être proposée à l'opérateur avant de devenir un engagement. Une interface web, un export modifiant le format ou une interprétation des quantités serait un changement de périmètre.

## Spécification de la méthode

Privilégier une première réalisation utilisable, peu de préparation et peu d'interruptions. Un dépôt et un agent principal suffisent comme hypothèse de départ. N1 et les pondérations chiffrées ne sont pas nécessaires pour ce lot.

Capacités attendues : Python, accès à un répertoire temporaire et exécution des tests. Si elles manquent, déclarer le manque et adapter les moyens. Aucun outil externe n'est installé uniquement pour imiter une graine.

Budget proposé de conception : un candidat initial et au plus une révision de méthode avant essai. Après l'essai, relever les minutes humaines, le délai et les coûts accessibles ; aucun objectif chiffré n'est inventé comme préférence acquise.

## Choix de graines

`mini-swe-loop` inspire la boucle action, observation et correction ; `codex-scoped-instructions` inspire le chargement des seules consignes utiles. Les runtimes de ces projets ne sont pas repris. Le parallèle, la mémoire durable et une chaîne N1 sont écartés faute de réemploi identifié dans ce besoin bref.
