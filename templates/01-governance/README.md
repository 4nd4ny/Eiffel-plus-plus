# {{PROJECT_NAME}} — Gouvernance

Composant optionnel Eiffel++ **0.3.0** pour une implantation en dépôts séparés. Ce dépôt définit la méthode de {{PROJECT_NAME}} et les références de {{STBL_REPO}}, {{AUDIT_REPO}} et {{PRODUCT_REPO}}. Les quatre responsabilités peuvent aussi partager une racine Git ; adapter alors les références et les droits.

Lire [AGENTS.md](AGENTS.md), le [protocole](../../protocol/README.md), puis [POLICY.md](POLICY.md), [ROLES.md](ROLES.md) et [WORKFLOW.md](WORKFLOW.md).

## Mise en service

0. À partir du [patron Eiffel++](../../meta/START.md), forger N0 depuis les spécifications et les graines retenues. Ajouter N1 seulement si son réemploi le justifie. Conserver le profil et la provenance ; retenir uniquement les composants nécessaires.

1. Identifier les responsables et les règles de délégation.
2. Définir les contrôles requis par type d'exigence et les capacités réellement disponibles.
3. Remplir [un mandat](templates/MANDATE.md), sans attribuer de droits non accordés.
4. Installer les protections d'accès et de CI ; conserver la preuve de configuration.
5. Adopter un commit du protocole et en communiquer les références aux trois autres responsabilités.
6. Observer le premier lot, puis déclencher si nécessaire [une proposition](templates/POLICY_CHANGE.md) et le [prompt de génération/adaptation](templates/EXPERIMENT.md).

Les formulaires sont des modèles. Une case à remplir ou une valeur proposée n'est pas une décision effective.
