# Vérifications de l'intégration 0.4.0

7 novembre 2026. Les trois premières améliorations demandées sont intégrées : adaptation liée à une observation, composants spécialisés et conservation des conditions d'emploi et d'échec.

## Contrôles exécutés

- `python3 tools/check_catalog.py` : PASS, 102 fichiers Markdown ; références locales, schémas, exemples et 12 graines cohérents.
- `python3 -m unittest discover -s tests -v` : PASS, 34 tests, dont sept nouveaux contrôles des composants et expériences.
- `git diff --check` : PASS.

Les nouveaux cas couvrent les dépendances manquantes ou sortantes, les identifiants répétés, les observations non résolues, l'adoption d'un essai non exécuté et les coûts absents ou invalides. Les parcours antérieurs continuent de passer, y compris la préparation, la capture et les exports avec liens locaux.

Les expériences de l'exemple sont fictives et restent NOT_RUN. Le validateur n'authentifie pas les récits. Aucun gain de qualité du code produit, de coût LLM ou de productivité n'est déduit de ces tests. Les mécanismes d'activation et de choix parmi les sorties sont examinés séparément avant intégration.

Le [rapport historique 0.3.0](VALIDATION.md) garde son périmètre. Les formats 0.2.0 et 0.3.0 restent acceptés selon leur contrat ; aucun résultat historique n'est promu ni réécrit.
