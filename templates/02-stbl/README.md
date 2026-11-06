# {{PROJECT_NAME}} — Besoins et décisions

Harnais Eiffel++ **0.3.0** · Projet : `{{PROJECT_SLUG}}` · Rôle : `stbl`

Composant optionnel pour une implantation en dépôts séparés. Ce dépôt porte la spécification technique des besoins logiciels (STBL), les questions au Product Owner (PO) et les décisions métier. Les quatre responsabilités peuvent partager une racine Git ; adapter alors leurs références et leurs droits.

## Dépôts partenaires

| Rôle | Dépôt | Responsabilité |
| --- | --- | --- |
| Gouvernance | {{GOVERNANCE_REPO}} | Méthode, politiques et délégations. |
| STBL | {{STBL_REPO}} | Besoins, contrats et arbitrages métier. |
| Audit | {{AUDIT_REPO}} | Évaluation indépendante et constats. |
| Produit | {{PRODUCT_REPO}} | Code, tests de développement et artefacts exécutables. |

Le [protocole commun](../../protocol/README.md) définit les échanges entre ces dépôts. Consulter [AGENTS.md](AGENTS.md) avant de travailler et [STBL.md](STBL.md) pour connaître la base courante.

## Démarrer

1. Renseigner dans `STBL.md` le périmètre, les sources et le mandat. Ne pas déclarer une exigence acceptée pendant cette initialisation.
2. Copier les modèles utiles dans `requirements/`, `questions/`, `decisions/`, `contracts/` ou `changes/`. Attribuer à chaque fiche le prochain identifiant libre de son type ; le numéro du modèle est illustratif.
3. Relier chaque exigence à sa source, puis préciser résultats positifs, refus attendus, effets autorisés et critères de validation.
4. Enregistrer les décisions du PO à partir d'une source consultable et du mandat applicable. Une proposition de l'agent conserve `PROPOSED`.
5. Publier une révision de référence et transmettre ses références exactes aux dépôts produit et audit.

## Modèles

| Modèle | À utiliser pour |
| --- | --- |
| [REQUIREMENT.md](templates/REQUIREMENT.md) | Décrire un besoin et son domaine d'application. |
| [QUESTION.md](templates/QUESTION.md) | Faire arbitrer une ambiguïté concrète. |
| [DECISION.md](templates/DECISION.md) | Enregistrer une décision et sa provenance. |
| [CONTRACT.md](templates/CONTRACT.md) | Définir les obligations d'une opération ou d'un composant. |
| [CHANGE.md](templates/CHANGE.md) | Faire évoluer une signification déjà acceptée. |

Les sources confidentielles peuvent être référencées sans être copiées. Conserver ici les éléments nécessaires à l'analyse et autorisés à être publiés ; indiquer comment un lecteur habilité peut consulter la source.

## Conditions de livraison d'une base

Une base exploitable distingue les exigences acceptées des propositions, désigne les décisions correspondantes et explicite les questions qui empêchent certains travaux. Chaque exigence obligatoire possède un moyen de validation ; chaque limite non résolue est visible.

Les liens de traçabilité facilitent le contrôle. Ils ne certifient pas automatiquement l'authenticité des décisions, la qualité du produit ou la complétude des besoins.
