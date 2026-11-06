# Plan d'audit illustratif — AUD-0001

**Exemple fictif — tous les contrôles `NOT_RUN`. Aucun défaut n'a été observé dans un logiciel réel.**

## Candidat et avis

Références aux quatre dépôts : non résolues. Artefact : absent. Avis possible à ce stade : `INCONCLUSIVE`. Il ne s'agit pas d'un rejet d'une implémentation qui n'existe pas.

## Contre-exemples à rechercher

| Cas | Trace à provoquer | Critère | État |
| --- | --- | --- | --- |
| Dernière place | A et B lisent une place avant que l'un n'enregistre | Une seule confirmation, sans survente | `NOT_RUN` |
| Refus systématique | Demande valide, capacité libre, service disponible | Une confirmation doit pouvoir être obtenue | `NOT_RUN` |
| Réponse perdue | Enregistrement validé, réponse perdue, répétition | Même réservation, aucun effet supplémentaire | `NOT_RUN` |
| Clé réutilisée autrement | Même clé, autres paramètres | Erreur convenue, sans mutation silencieuse | `NOT_RUN` |
| Contrôle d'accès | Participant A tente de récupérer le résultat de B | Aucun accès non autorisé | `NOT_RUN` |
| Redémarrage | Confirmation puis redémarrage du service | Réservation encore présente selon le contrat de stockage | `NOT_RUN` |

## Moyens

Exemples métier, tests de transitions d'état, ordonnancement contrôlé des appels concurrents et intégration au stockage réel de test. Un modèle abstrait peut aider à explorer les séquences ; sa conclusion ne suffit pas à couvrir l'adaptateur de base de données.

## Qualité de l'oracle

Vérifier que les contrôles rejettent une implémentation qui refuse tout et une implémentation qui crée un doublon au réessai. Un résultat futur doit conserver la trace réelle, le candidat, l'environnement et la portée. Toute correction d'un critère erroné suit une proposition indépendante.
