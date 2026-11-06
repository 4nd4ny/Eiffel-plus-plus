# Charte du cabinet — {{PROJECT_NAME}}

Version du métapatron : **0.3.0**. Document de départ à compléter ; aucun mandat n'est présumé accepté.

## Mandat

| Élément | Valeur à établir |
|---|---|
| Projet | {{PROJECT_NAME}} (`{{PROJECT_SLUG}}`) |
| Source du mandat et responsable | Non renseignés |
| Décision d'autorisation | Non renseignée ; état initial `PROPOSED` |
| Dépôt gouvernance | {{GOVERNANCE_REPO}} |
| Dépôt STBL | {{STBL_REPO}} |
| Dépôt audit | {{AUDIT_REPO}} |
| Dépôt produit | {{PRODUCT_REPO}} |
| Objectifs et périmètre | Non renseignés |
| Exclusions et conséquences | Non renseignées |
| Accès et environnements autorisés | Non renseignés |
| Budget et conditions d'arrêt | Non renseignés |
| Destinataire du verdict | Non renseigné |

Le mandat précise quels contrôles peuvent être exécutés sans nouvelle intervention, quels environnements peuvent être utilisés et quelles décisions restent réservées. Les délégations existantes sont réutilisées ; leur absence n'est pas comblée par une hypothèse silencieuse.

## Responsabilités

- **Gouvernance** : méthode, capacités, politique d'acceptation et délégations ; désignation des autorités compétentes pour les réserves et la livraison.
- **STBL** : provenance des besoins, contrats et critères métier ; enregistrement des arbitrages du Product Owner ou de son délégataire sur le sens métier.
- **Produit** : candidat reproductible, informations de construction et correctifs.
- **Audit** : enquête contradictoire, contrôles, constats sourcés et verdict à portée définie.

Les réserves et la livraison relèvent des autorités désignées dans le mandat. Une décision qui change le sens métier revient au Product Owner ou à son délégataire et doit être enregistrée dans le STBL ; une politique de gouvernance ne remplace pas cette acceptation.

Le cabinet est indépendant dans ses pouvoirs et dans la collecte de ses résultats. Il n'est pas présenté comme un organisme accrédité. Si une même personne ou un même modèle remplit plusieurs rôles, le dossier expose cette limite et les protections effectives.

## Garanties à configurer

Documenter l'état réel de chaque protection : responsable, configuration vérifiable et élément de preuve. Une case non renseignée ne signifie pas qu'elle existe.

| Protection | État initial |
|---|---|
| Politique d'acceptation protégée contre l'auteur du candidat | `NOT_RUN` |
| Oracles qualifiés et sélecteurs de contrôles protégés | `NOT_RUN` |
| Exécuteur et collecte de résultats hors écriture auteur | `NOT_RUN` |
| Construction et exécution du candidat isolées | `NOT_RUN` |
| Secrets et identifiants séparés du code évalué | `NOT_RUN` |
| Publication des preuves sensibles maîtrisée | `NOT_RUN` |

## Périmètre des affirmations

Une campagne examine les versions des quatre responsabilités et un candidat précis ; les références peuvent partager un dépôt Git et un commit. Les preuves, tests, scans, inspections et validations client conservent chacun leur portée. Le verdict ne promet ni absence universelle de bug ni sécurité absolue, et ne se transmet pas automatiquement à la production ou à une autre configuration.

## Publication

Définir les destinataires de chaque catégorie de source et de preuve avant diffusion. Un dépôt public ne doit recevoir aucun secret, donnée personnelle ou document client non autorisé. Les résultats sensibles restent dans l'emplacement autorisé ; leur référence publique doit permettre aux personnes habilitées d'établir la provenance sans divulguer le contenu.

Les demandes de dérogation et les changements de mandat suivent le [protocole commun](../../protocol/README.md) avec une décision versionnée. Un contrôle qualifié n'est jamais affaibli uniquement pour obtenir un verdict favorable.
