# Validation de la première édition

Date : **6 novembre 2026**. Périmètre : catalogue Eiffel++ 0.1.0, modèles Markdown et outils locaux d'instanciation. Il ne s'agit pas de l'audit d'un logiciel métier ni d'une certification indépendante.

## Contrôles exécutés

| Contrôle | Résultat observé | Limites |
| --- | --- | --- |
| `python3 tools/check_catalog.py` | `PASS` | Liens locaux, structure, blocs de code, fichiers d'entrée et variables ; pas les URL externes ni le sens des contrats. |
| `python3 -m unittest discover -s tests -v` | `PASS` — six tests | Comportements décrits ci-dessous ; pas l'intégration à une forge distante. |
| Revue croisée des modèles | Corrections intégrées | Revue par agents ; elle ne constitue pas une expertise indépendante au sens statistique ou organisationnel. |

Les six tests vérifient : quatre modèles autonomes avec liens résolus et instantanés cohérents ; refus d'écraser une destination ; refus de suivre un lien symbolique de destination ; refus de noms techniques invalides ; refus d'un nom lisible multiligne ; création de quatre racines Git sans commits ni remotes préexistants.

## Corrections issues de la revue

- Les questions STBL disposent d'un cycle `OPEN`, `ANSWERED`, `SUPERSEDED` distinct de leur caractère bloquant.
- Les arbitrages métier relèvent du PO ou de son délégataire et sont enregistrés dans STBL ; la gouvernance porte méthode, capacités et délégations.
- Les références de dépôts encore non résolues ne sont pas présentées comme des liens locaux valides.
- Le plan d'audit est commité avant la résolution de son SHA dans un manifeste distinct ; le rapport n'inclut pas son propre commit.

## Non établi dans cette édition

L'efficacité économique des métapatrons n'a pas été mesurée sur un ensemble de projets. Aucune protection distante, aucun runner indépendant, aucun moteur de politique, aucun audit de sécurité d'application et aucune preuve de code métier ne sont installés ou exécutés par les outils fournis. Leur déploiement et leur validation font partie de la réutilisation du catalogue.

Les commandes ci-dessus permettent de reproduire les contrôles sur la version téléchargée. Le commit contenant ce document identifie le contenu validé sans créer d'autoréférence dans le fichier.
