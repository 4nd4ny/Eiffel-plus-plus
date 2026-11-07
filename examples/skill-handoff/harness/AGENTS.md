# Lot CSV

La [note de conception](DESIGN.md) explique ce lot et les changements à prévoir selon le besoin métier ; la consulter pour comprendre ou adapter la méthode. SPEC.md reste le contrat.

Lire SPEC.md et choisir la capacité de la tâche dans harness.json ; skills.py list peut en présenter l’index par rôle. Les rôles partagent ici un acteur : auto-examen, sans indépendance organisationnelle. Écrire seulement dans le lot autorisé.

STBL fixe rules selon le besoin. Gouvernance prépare la mission Produit, conserve son order_sha256 et identifie son destinataire Audit. Produit lit filter-rows, exécute l’opération et remet candidate. Gouvernance prépare ensuite la mission Audit à partir de la même source, des mêmes règles et du candidat remis. Audit lit check-rows et remet report, sans corriger le candidat. Gouvernance examine les constats et décide la suite dans le mandat.

Pour chaque mission, le rôle lit le skill choisi et ses préconditions avant l’action ; l’environnement doit fournir Eiffel++ 0.6.0 et Python 3. Préparer par `python3 CHEMIN_EIFFEL/tools/skills.py prepare CHEMIN_N0 --role product --skill filter-rows --input source=SOURCE --input rules=RULES --output MISSION_NEUVE`. Conserver l’empreinte renvoyée ; remettre par `python3 CHEMIN_EIFFEL/tools/skills.py handoff MISSION --order-sha256 EMPREINTE_CONSERVEE --to audit --artifact candidate=CANDIDAT --output REMISE_NEUVE`. Audit utilise check-rows avec les ports source, rules, candidate, puis remet report à governance. Un résultat non exécuté reste NOT_RUN. Une mission STALE ne permet pas de remettre une preuve actuelle. Une nouvelle qualification doit expliquer le changement, pas seulement recalculer les empreintes. Une reprise ne recrée pas le budget.

Produit peut changer son nouveau fichier de sortie ; source, règles, contrat et contrôles restent hors de cette correction. Audit évalue sans modifier les entrées. Une remise n’accorde aucun droit de livraison. Après une correction sans information nouvelle, arrêter le lot et conserver la limite.

Lors d’une modification du produit, documenter ses décisions de conception réellement affectées dans la documentation existante ; distinguer ces motifs de ceux du harnais. Une livraison qui modifie la méthode met aussi sa note à jour.
