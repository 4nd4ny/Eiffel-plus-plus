# Contrat de génération N1 → N0 — service d'autorisations

Statut : PROPOSED. Origine : scénario fictif Eiffel++ 0.2.0. Validation opérationnelle : NOT_RUN.

## Entrées et préconditions

- Le profil explicite l'autonomie recherchée et les obligations non compensables.
- Les besoins et politiques disponibles ont une origine ; leurs lacunes sont conservées comme questions.
- L'inventaire des capacités distingue observations, hypothèses et moyens restant à configurer.
- La génération dispose d'un budget borné et d'un périmètre d'édition défini.

Une politique absente peut permettre de préparer un candidat de méthode et des interfaces synthétiques. Elle ne permet pas d'inventer une décision métier ou d'accepter le service.

## Postconditions attendues

Le N0 définit un chemin allant de la politique à un candidat, puis à une vérification indépendante. Il décrit les preuves correspondant à chaque obligation d'isolation et les cas positifs attendus. L'accès à une ressource ne dépend pas d'une simple déclaration non fiable de l'appelant.

Les boucles de correction technique peuvent se poursuivre sans intervention humaine dans le mandat. Les escalades portent sur des décisions précises ; une demande générale de revue à chaque étape n'est pas une stratégie d'autonomie.

Chaque règle générée est justifiée par une propriété à garantir, une préférence ou une capacité observée. Les copies de contexte sont limitées, les sources versionnées consultables, et l'oubli ou l'invalidation de la mémoire est prévu.

## Invariants

La politique acceptée et les droits ne changent pas pour améliorer un score. Le producteur ne peut modifier seul les oracles indépendants. Une erreur ou une inconnue d'authentification n'est pas convertie en permission. Aucun résultat non exécuté ou périmé ne valide un candidat.

Les quatre responsabilités restent identifiables même si le nombre d'agents varie. Une adaptation du harnais ne constitue ni une autorisation de déployer ni une extension du mandat. Les sources sensibles ne deviennent pas publiques par synthèse.

## Qualification

Examiner structure, cohérence du workflow, réalisabilité de l'isolation des outils et qualité des diagnostics. Prévoir des essais de substitution d'identifiants, politique absente, révocation et modification après audit.

Les résultats de ces essais doivent venir de l'environnement réel ou d'un modèle de test dont les limites sont annoncées. Le contrôle du paquet documentaire ne certifie ni la sécurité du futur service ni la validité d'une politique métier.
