# Cabinet d'audit — {{PROJECT_NAME}}

Version du métapatron : **0.2.0**. Projet : `{{PROJECT_SLUG}}`.

Ce dépôt organise un cabinet d'audit fonctionnel indépendant pour le projet. Il aide à examiner bugs, sécurité, qualité et adéquation aux besoins du client. Il ne constitue ni une accréditation ni une certification.

## Les quatre dépôts

| Responsabilité | Dépôt |
|---|---|
| Gouvernance : méthode, capacités et délégations | {{GOVERNANCE_REPO}} |
| STBL : besoins, critères et décisions métier | {{STBL_REPO}} |
| Plans, oracles et résultats d'audit | {{AUDIT_REPO}} |
| Produit et candidats | {{PRODUCT_REPO}} |

Lire le [protocole commun](../../protocol/README.md), la [charte](AUDIT_CHARTER.md), la [politique](POLICY.md) et les [instructions d'agent](AGENTS.md).

## Démarrer une campagne

1. Définir le mandat, les délégations existantes et le périmètre autorisé dans la charte.
2. Configurer effectivement les permissions, branches protégées et exécuteurs isolés. Les textes de ce dépôt ne les activent pas.
3. Copier le [plan](templates/AUDIT_PLAN.md) dans un dossier de campagne portant un nouvel identifiant `AUD-0001`.
4. Figer le plan et les oracles dans `audit_commit`, puis résoudre le quadruplet des dépôts dans un manifeste distinct. Identifier l'artefact candidat, sa construction et les environnements de contrôle ; le plan ne contient pas son propre SHA.
5. Effectuer les contrôles utiles, consigner les [preuves](templates/EVIDENCE.md) et les [constats](templates/FINDING.md), puis préparer un [verdict](templates/VERDICT.md).

Les identifiants présents dans les modèles sont illustratifs : réserver des identifiants uniques selon le protocole. Les champs `null` ne sont pas des données acquises. Aucun modèle ne représente une campagne exécutée.

## Documents disponibles

| Document | Usage |
|---|---|
| [AUDIT_PLAN](templates/AUDIT_PLAN.md) | Périmètre, liaison des versions et contrôles requis |
| [THREAT_MODEL](templates/THREAT_MODEL.md) | Menaces, frontières de confiance et hypothèses |
| [FINDING](templates/FINDING.md) | Défaut observé, impact et reproduction |
| [EVIDENCE](templates/EVIDENCE.md) | Résultat capturé avec portée et provenance |
| [ORACLE_CHANGE](templates/ORACLE_CHANGE.md) | Correction justifiée d'un critère ou d'un oracle |
| [VERDICT](templates/VERDICT.md) | Conclusion liée au candidat exact |

## Publication et limites

Ce dépôt peut être public. Garder secrets, données personnelles, sources client non publiables et preuves sensibles dans leur emplacement autorisé. Publier des extraits expurgés et des références vérifiables ; décrire toute limite d'accès qui affecte le verdict. Une empreinte ne remplace pas un droit d'accès ni l'examen du contenu.

`audit_commit` dans la liaison d'une campagne désigne la version du plan, des politiques et des oracles utilisée avant exécution. Les résultats sont ajoutés ensuite dans un `report_commit`, retrouvé par le commit contenant le rapport. Le rapport n'inscrit pas son propre SHA. Le [format des échanges](../../protocol/EXCHANGE.md) fixe les noms des quatre références ; le [modèle de confiance](../../protocol/TRUST.md) précise leur portée.

`INCONCLUSIVE` bloque automatiquement l'acceptation. `ACCEPT_WITH_RESERVATIONS` exige une décision explicite de l'autorité désignée dans le mandat et n'autorise pas une livraison automatique. Toute modification du sens métier relève du Product Owner ou de son délégataire, via le STBL. Une conclusion ne s'étend jamais à une version ultérieure du produit sans réévaluation.
