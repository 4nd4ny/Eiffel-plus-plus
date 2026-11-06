# Réalisation proposée du service

Ce dépôt recevra l'implémentation et ses vérifications techniques. Aucun logiciel n'est inclus et tous les résultats applicatifs sont NOT_RUN.

## Interfaces de travail

Décrire explicitement les limites entre établissement de l'identité, contexte d'organisation, lecture de politique et décision d'accès. Une interface permet de préparer les comportements sans prétendre que le fournisseur d'identité ou le stockage est déjà qualifié.

Une fois ces limites stabilisées, des tâches d'implémentation distinctes peuvent être parallélisées. Conserver les versions de politique et les contrats partagés ; intégrer et vérifier l'état combiné avant candidature.

## Correction et mémoire

Le diagnostic doit permettre de reproduire le refus erroné ou l'autorisation indue. Les tentatives infructueuses utiles peuvent être consignées avec leur cause supposée, leur source et les versions concernées. Une interprétation de politique proposée n'entre pas dans la mémoire comme une décision acceptée.

Lors d'un changement de politique, réexaminer les exemples, procédures et contrôles qui en dépendent. Le N1 d'adaptation est conservé dans le dépôt governance après matérialisation.

## Candidature

Fournir l'artefact exact, ses dépendances, les vérifications effectuées et les limites. Les résultats d'audit porteront sur cet état intégré. Une procédure de déploiement reste subordonnée au mandat applicable.

Voir les [instructions du produit](AGENTS.md).
