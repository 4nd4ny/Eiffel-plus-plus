# Contrat de travail

Le contrat comportemental du lot fait foi : entrées valides, erreurs dues, sorties, effets autorisés et invariants. Référencer l’exigence d’origine ; ne pas remplacer le besoin par l’état actuel du code. Un renforcement proposé peut échouer sans devenir une régression sur les obligations acceptées.

Préconditions de l’atelier : Python et runtime Eiffel++ 0.6.0 ou 0.7.0 ; sources régulières sans liens, hors dépendances installées et données personnelles ; vérificateur local explicitement autorisé. Les arbres d’entrée doivent être distincts des nouvelles destinations. Préparer un export propre si le dépôt comporte `.git`, `_eiffel` ou des liens ; ne pas supprimer ces éléments dans l’original.

Invariants du lot : référence complète, consignes, compétences, justification, contrôles et contrat restent identiques à leur empreinte initiale. Le dossier `work` est seul mutable. Un candidat est une copie complète, avec empreinte conservée séparément. Les artefacts d’essai sont écrits hors du lot. Les vérifications encadrent l’exécution ; toute dérive invalide le résultat.

Postconditions d’une évaluation : inventaire des critères exactement égal au contrat ; résultats PASS/FAIL/UNKNOWN ; durée et sortie du processus conservées. Un score ne compense jamais un critère obligatoire en échec. Le vérificateur doit être éprouvé sur un défaut connu : un programme qui imprime PASS n’est pas un oracle valable.

Une sélection exige la même fermeture de contrôles pour référence et candidats. Égalité : KEEP_BASE ; aucun résultat admissible : INCONCLUSIVE. L’artefact sélectionné contient tous les fichiers de la copie de code, mais la portée du verdict demeure celle du contrat. Les dépendances installées, l’environnement réel, les données et le déploiement ne sont pas compris dans cette copie.

Ces mécanismes détectent des modifications entre observations. Ils ne confinent pas un programme hostile, n’authentifient pas les personnes et ne protègent pas contre un acteur capable de réécrire toutes les références externes. Aucun script ne lance de modèle, n’accède à des identifiants ou ne déploie le produit.
