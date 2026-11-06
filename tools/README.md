# Outils locaux

Les deux programmes utilisent seulement la bibliothèque standard de Python. Ils n'accèdent pas au réseau, aux comptes GitHub ou aux modèles d'IA.

## Instanciation

`instantiate.py` crée les quatre modèles dans un **nouveau** dossier extérieur au catalogue. Il remplace les six variables documentées, rend locaux les liens vers le protocole et copie les fichiers de ce protocole. Chaque dépôt reçoit un inventaire d'empreintes dans `_eiffel/project.json` et une copie de la licence des templates dans `_eiffel/LICENSE`.

Les empreintes identifient les contenus source. Elles ne sont ni des signatures ni une preuve de provenance. Les identifiants de commit sont laissés vides (`UNBOUND`) ; les futurs mainteneurs doivent les résoudre et adopter les versions appropriées.

`--git-init` initialise quatre dépôts locaux distincts sur `main`, sans commit et sans remote. Aucun paramètre Git global n'est modifié. Si le transfert final est interrompu par le système, le dossier nouvellement créé peut être partiel ; aucun dossier préexistant n'est remplacé. Examiner cette nouvelle destination avant de relancer avec une autre destination.

## Contrôle structurel

`check_catalog.py` vérifie les liens locaux vers des fichiers, les blocs de code, les sections des quatre patrons, les fichiers d'entrée et les variables reconnues. Il ne vérifie pas les ancres de titres, la disponibilité des URL externes, le YAML, le sens des contrats ou la validité des preuves.

Les tests couvrent la création de quatre dépôts autonomes, la résolution des liens, le remplacement des variables, la conservation des instantanés, le refus d'écraser une destination et le refus d'un nom permettant de sortir du périmètre attendu.

## Hors périmètre de cette version

Pas d'ordonnanceur d'agents, pas de moteur de politique, pas de vérification distante d'identité ou de SHA, pas de runner de sécurité. Ces mécanismes doivent être intégrés et vérifiés séparément selon le [modèle de confiance](../protocol/TRUST.md).
