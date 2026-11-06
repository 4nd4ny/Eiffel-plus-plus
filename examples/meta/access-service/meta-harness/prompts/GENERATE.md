# Générer la méthode du service d'autorisations

Statut de cet exemple : PROPOSED. Qualifications et performances : NOT_RUN.

Tu es chargé de synthétiser le **harnais N0** qui permettra de développer ce service avec peu d'attention humaine, tout en préservant les obligations d'isolation. Reçois `profile.json`, `GENERATION_CONTRACT.md`, les besoins métier, les décisions de politique et les capacités de l'environnement. Génère une méthode et ses prompts adaptés ; les quatre noms de rôles ne prescrivent ni quatre agents permanents ni une succession de réunions.

## Modéliser le problème de travail

Établis les frontières de confiance : origine de l'identité, rattachement à l'organisation, stockage des permissions, validation des ressources, exécution des contrôles et autorité de livraison. Pour chacune, indique la source et l'incertitude.

Sépare les questions de politique des décisions techniques. La matrice des rôles, les exceptions entre organisations et les délais de révocation demandent des décisions métier lorsqu'elles manquent. Le langage, la structure des modules et les stratégies de test peuvent relever d'un mandat technique. Ne bloque pas les travaux indépendants d'une réponse absente.

Déduis des propriétés vérifiables : accès prévu autorisé, accès étranger refusé, contexte non falsifiable par un simple paramètre, refus en cas de politique indéterminée, résultats rattachés au candidat exact. Les cas autorisés comptent autant que les interdictions.

## Inventer le workflow approprié

Synthétise les règles du N0 à partir de ces propriétés et des outils disponibles :

1. Établis une interface de décision et une matrice de politique avant de paralléliser des parties qui en dépendent.
2. Choisis la répartition du travail selon les interfaces stables et les capacités. Justifie toute délégation par une tâche indépendante, une information supplémentaire ou un gain attendu.
3. Définis comment un exécuteur indépendant applique les contrôles au candidat exact. Décris les droits à configurer ; n'en présume pas l'existence.
4. Autorise des boucles de correction sans nouvelle intervention humaine quand le mandat, la politique et les oracles sont inchangés.
5. Définis des événements précis de remontée humaine : décision métier absente, élargissement de droits, réserve hors délégation, conflit de sources ou livraison hors mandat.
6. Choisis une mémoire utile aux évolutions répétées. Relie les connaissances aux versions de politique ; invalide celles dont les hypothèses ont changé. Une synthèse ne doit pas élargir l'audience de ses sources.

Lis les poids et leur source dans le profil courant. Une priorité donnée aux fonctions et à l'autonomie peut conduire à investir dans des contrôles exécutables et des diagnostics utilisables par les agents. Si un profil révisé privilégie fortement le délai, cherche plutôt une livraison plus étroite dans la politique acceptée et une réutilisation des contrôles valides. Si les moyens de parallélisation sont absents ou coûteux, synthétise un circuit séquentiel. Ces choix restent des hypothèses d'efficacité ; aucune moyenne pondérée ne compense un défaut d'isolation.

Pour les parties inconnues de l'environnement, produis des interfaces substituables ou une qualification à effectuer. Les tests sur doubles et données synthétiques n'établissent pas à eux seuls la validité de l'intégration réelle.

## Produire un N0 exploitable

Écris `harness.json`, une copie cohérente du `profile.json`, puis `governance/`, `stbl/`, `audit/` et `product/`, chacun avec `AGENTS.md` et `README.md`.

Les fichiers doivent donner aux rôles les contrats et informations indispensables : périmètres d'écriture, sources de politique, conditions de candidature, type de preuves attendu, traitement des contre-exemples, chemins de reprise et conditions d'adaptation. Choisis les autres documents seulement lorsqu'ils servent une décision ou une exécution.

Pour chaque règle du harnais, explique quelle exigence, préférence ou capacité l'a motivée. Décris ce qui reste non implémenté. N'annonce aucun score d'autonomie, coût ou gain de qualité non mesuré.

Une seule méthode plausible peut suffire. Si une incertitude déterminante oppose des organisations, propose d'autres candidats dans la limite max_candidates du profil et une qualification limitée à cette différence. Respecte également max_iterations et max_tokens lorsqu'il est renseigné ; ne recopie pas les limites d'une version antérieure du profil.

## CHECK — qualifier le harnais avant adoption

Cherche une manière pour un producteur de faire accepter un candidat sans satisfaire l'isolation, de falsifier une origine de politique ou de réutiliser un résultat périmé. Cherche également les fausses escalades qui solliciteraient l'humain pour des choix techniques déjà autorisés.

Remets les corrections du harnais, les essais à exécuter et les questions restant ouvertes. Examine une variation du profil ou des capacités : les règles qui dépendent de cette variation doivent être recomposées ; les obligations stables restent identiques. Le manifeste N0 reste `PROPOSED` sans décision authentifiable applicable. Les contrôles non exécutés sont `NOT_RUN` ; la préparation d'un bon examen n'est pas la réussite du produit à cet examen.
