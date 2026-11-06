# Méthode proposée pour une livraison locale courte

Origine : chaîne illustrative dashboard-local, Eiffel++ 0.2.0. Décision d'adoption : PROPOSED. Résultats réels : NOT_RUN.

## Choix et raisons

| Choix N0 | Raison |
| --- | --- |
| Un producteur, un lot actif | Petite surface fonctionnelle ; privilégier vitesse et économie. |
| Contrôles ciblés fournis à un exécuteur indépendant | Préserver la fidélité et le fonctionnement local sans revue humaine de chaque édition. |
| Questions regroupées sur les cas indéterminés | Les doublons et valeurs manquantes changent le sens métier ; les choix de fichiers ne le changent pas. |
| Note de reprise et références canoniques | Horizon bref ; aucune utilité mesurée d'une consolidation périodique. |

## Circulation du travail

STBL précise le lot obligatoire et les questions restantes. Le produit réalise un candidat identifiable. L'audit examine les comportements requis sur ce candidat et renvoie des contre-exemples. Le produit peut corriger dans son mandat sans nouvelle cérémonie. La livraison suit l'autorité effectivement établie.

Une question ne bloque que les comportements qui dépendent de sa réponse. Une cible indicative de quatre heures n'autorise pas une acceptation fictive si le lot reste incomplet.

## Mise en service restant à effectuer

Identifier le mandat et les versions des sources, vérifier les outils locaux, protéger les contrôles indépendants, puis qualifier leur exécution. Le paquet documentaire n'installe aucun mécanisme d'isolation.

Les [instructions du rôle](AGENTS.md) constituent son point d'entrée. Pour une évolution de méthode, utiliser le N1 archivé après matérialisation dans `_eiffel/meta-harness/`. Les résultats ou décisions d'autres rôles se citent par rôle, chemin et version ; aucun lien vers un dossier voisin n'est requis.
