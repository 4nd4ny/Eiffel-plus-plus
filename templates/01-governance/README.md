# {{PROJECT_NAME}} — Gouvernance

Ce dépôt définit le harnais et la méthode de {{PROJECT_NAME}}. Il est référencé par {{STBL_REPO}}, {{AUDIT_REPO}} et {{PRODUCT_REPO}} à une version exacte.

Lire [AGENTS.md](AGENTS.md), le [protocole](../../protocol/README.md), puis [POLICY.md](POLICY.md), [ROLES.md](ROLES.md) et [WORKFLOW.md](WORKFLOW.md).

## Mise en service

0. À partir du [patron Eiffel++](../../meta/START.md), générer N1 puis N0 pour le contexte du projet. Ce dossier générique est une bibliothèque de composants. Conserver le générateur et le profil retenus ; utiliser les fichiers nécessaires à la méthode synthétisée.

1. Identifier les responsables et les règles de délégation.
2. Définir les contrôles requis par type d'exigence et les capacités réellement disponibles.
3. Remplir [un mandat](templates/MANDATE.md), sans attribuer de droits non accordés.
4. Installer les protections d'accès et de CI ; conserver la preuve de configuration.
5. Adopter un commit du protocole et en communiquer les références aux trois autres dépôts.
6. Observer le premier lot, puis déclencher si nécessaire [une proposition](templates/POLICY_CHANGE.md) et le [prompt de génération/adaptation](templates/EXPERIMENT.md).

Les formulaires sont des modèles. Une case à remplir ou une valeur proposée n'est pas une décision effective.
