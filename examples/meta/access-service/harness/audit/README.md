# Plan d'audit proposé

Tous les examens sont NOT_RUN ; aucun résultat de sécurité n'est revendiqué.

| Obligation | Cas à exécuter |
| --- | --- |
| Cas autorisés | Matrice de politique acceptée : vérifier que chaque autorisation prévue produit bien le service demandé. |
| Isolation | Sujet de l'organisation A et ressource de B ; substitution d'identifiant de ressource ou d'organisation dans la requête. |
| Origine fiable | Identité ou contexte fourni par l'appelant en contradiction avec la source de confiance. |
| Refus explicite | Permission absente, action inconnue, politique indéterminée et entrées nécessaires manquantes. |
| Révocation | Cas conformes à la garantie temporelle décidée ; tant qu'elle manque, l'obligation concernée reste indéterminée. |
| Validité du verdict | Changement du candidat ou de la politique après examen, ancien rapport présenté comme actuel, résultat sans exécution. |

## Moyens et limites

Les jeux synthétiques et doubles peuvent qualifier des propriétés locales. Examiner ensuite les frontières réellement intégrées au fournisseur d'identité, au stockage et à l'exécuteur. Ne pas attribuer au système complet un résultat établi seulement sur une fonction isolée.

Le producteur peut fournir des tests techniques, mais les attentes indépendantes et leur version restent sous l'autorité d'audit. Si une injection de défaut n'est pas détectée par le contrôle prévu, revoir le contrôle avant d'en tirer une assurance.

L'absence de défaut observé ne suffit pas à conclure quand une obligation requise manque. Voir les [instructions d'audit](AGENTS.md) et, après matérialisation, les états dans `_eiffel/protocol/`.
