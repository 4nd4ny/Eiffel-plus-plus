# {{PROJECT_NAME}} — Dépôt produit

Version du gabarit Eiffel++ : **0.2.0**. Identifiant de projet : `{{PROJECT_SLUG}}`.

Ce dépôt contient le logiciel et les moyens techniques de le construire, de le vérifier et de l'exploiter. L'agent producteur dispose de liberté sur l'implémentation dans le mandat reçu. Les besoins, contrats normatifs et verdicts conservent leurs autorités respectives.

| Dépôt | Rôle dans la coopération |
| --- | --- |
| Gouvernance (`{{GOVERNANCE_REPO}}`) | Méthode, budgets, autorités et politique d'acceptation |
| STBL (`{{STBL_REPO}}`) | Besoins, décisions métier authentifiées, spécifications et contrats applicables |
| Audit (`{{AUDIT_REPO}}`) | Contrôles indépendants et verdicts sur les candidats |
| Produit (`{{PRODUCT_REPO}}`) | Code, tests techniques, construction et exploitation |

Le [protocole commun](../../protocol/README.md) définit les échanges et identifiants. Toute référence utilisée pour décider ou vérifier doit désigner une révision précise. Les chemins du protocole sont réécrits lors de l'instanciation des dépôts.

## Documents utiles

- [AGENTS.md](AGENTS.md) : mandat et règles de travail de l'agent producteur.
- [ARCHITECTURE.md](ARCHITECTURE.md) : responsabilités, interfaces et décisions établies.
- [DEVELOPMENT.md](DEVELOPMENT.md) : environnement, contrôles et gestion des résultats.
- [Ordre de travail](templates/WORK_ORDER.md), [rapport de changement](templates/CHANGE_REPORT.md), [passation](templates/HANDOFF.md) et [ADR](templates/ADR.md) : supports à copier uniquement lorsqu'ils sont utiles.

## Première utilisation

Renseigner les commandes réelles et les éléments d'architecture observés. Référencer les exigences et contrats retenus, puis préparer un premier ordre de travail borné. Les champs non renseignés restent des inconnues : ce gabarit ne fournit ni implémentation, ni architecture acquise, ni preuve d'acceptation.

Dans le catalogue Eiffel++, ces fichiers sont des données à instancier. Le fichier `AGENTS.md` de ce répertoire vise le futur dépôt produit, pas le développement du catalogue.
