# Deux objets à spécifier

Exemple fictif, PROPOSED ; les préférences ci-dessous ne sont pas une décision d'un client.

## Besoin du logiciel

- REQ-0001 : lire localement un CSV avec en-tête contenant `categorie`, filtrer sur une valeur demandée et restituer les lignes retenues ainsi que leur nombre. Pour l'opération interne `filtrer(L, c)`, l'appelant fournit des lignes décodées avec `categorie` et une catégorie texte `c`. Le fournisseur restitue exactement la sous-séquence des lignes où `categorie = c`, dans l'ordre initial, avec leurs doublons et valeurs textuelles ; le compte égale sa longueur. `L` reste inchangé.
- REQ-0002 : ne pas modifier le fichier source et ne pas envoyer de données sur le réseau.
- REQ-0003 : signaler un fichier illisible, un en-tête sans `categorie` ou un CSV malformé. Une entrée valide sans ligne retenue donne un résultat vide et un compte nul.

La lecture CSV établit les préconditions de l'opération interne ou produit le diagnostic de REQ-0003 ; ces préconditions ne dispensent pas la CLI de traiter une entrée invalide. Aucun objet persistant n'est spécifié ici : il n'y a pas d'invariant de classe à inventer. La forme de sortie CLI reste à proposer. Une interface web, un export modifiant le format ou une interprétation des quantités changerait le périmètre.

## Spécification de la méthode

Privilégier une première réalisation utilisable, peu de préparation et peu d'interruptions. La répartition proposée dans AGENTS.md conserve les quatre responsabilités dans un dépôt et assume un auto-examen. Elle ne conviendrait pas à un mandat exigeant un audit indépendant. N1 n'est pas nécessaire pour ce lot.

Capacités attendues : Python, accès à un répertoire temporaire et exécution des tests. Si elles manquent, déclarer le manque et adapter les moyens. Aucun outil externe n'est installé uniquement pour imiter une graine.

Budget proposé de conception : un candidat initial et au plus une révision de méthode avant essai. Après l'essai, relever les minutes humaines, le délai et les coûts accessibles ; aucun objectif chiffré n'est inventé comme préférence acquise.

## Choix de graines

`mini-swe-loop` inspire la boucle action, observation et correction ; `codex-scoped-instructions` inspire le chargement des seules consignes utiles. Les runtimes de ces projets ne sont pas repris. Le parallèle, la mémoire durable et une chaîne N1 sont écartés faute de réemploi identifié dans ce besoin bref.
