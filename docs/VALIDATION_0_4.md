# Vérifications de l'intégration 0.4.0

7 novembre 2026. Périmètre : contrats optionnels de composants et d'expérience, lancement instrumenté de scripts Python, évaluation liée aux artefacts et sélection conservatrice. Les critères des deux derniers mécanismes ont été fixés avant le rejeu des six jeux de code.

## Résultats exécutés

| Contrôle | Résultat | Portée |
| --- | --- | --- |
| Catalogue et liens | PASS, 104 documents Markdown, 12 graines | Structure et cohérence des références, sans authenticité des déclarations. |
| Suite Python | PASS, 45 tests | 27 tests antérieurs, 7 tests de contrats et 11 tests de lancement/sélection. |
| Parcours CLI | PASS | Lancement d'un auxiliaire CSV, vérification de son reçu et sélection d'une référence valide. |
| Activation, six jeux de code | 12/12 cas conformes aux attentes | Pour chaque jeu : script appliquant une correction connue, puis script annonçant PASS sans modifier le code. |
| Sélection, six jeux de code | 24/24 cas conformes aux attentes | Régression, égalité, amélioration et absence de résultat admissible. |
| Sorties sélectionnées | 18/18 réévaluées avec succès, copies exactes | Les six cas sans résultat admissible ne produisent aucun artefact. |
| Rejeu des contrôles | 54 évaluations, 621 exécutions de critères | 69 critères distincts répartis sur les six jeux, répétés selon les scénarios. |
| Identité des sources de contrôle | PASS | Fichiers figés et code du contrôleur inchangés entre gel et vérification finale. |

Les six jeux sont des copies privées de modules TypeScript, JavaScript, PHP et Ruby, corrigés dans une expérience antérieure. Leurs sources et traces privées ne sont pas incorporées au catalogue public. Les tests unitaires publics reproduisent les mécanismes avec des fixtures autonomes. Le rapport détaillé de cette exécution est conservé dans l'espace local de l'opérateur.

## Ce que démontre le rejeu

Sans invocation, le reçu est NOT_RUN. Un script valide reçoit un accusé de lecture/compilation distinct de sa sortie, puis un statut de fin. L'auxiliaire sans effet est bien lancé, mais ses résultats échouent aux contrôles comportementaux : son message PASS ne devient pas une preuve d'utilité. Les tests négatifs couvrent aussi syntaxe invalide, exception, timeout et modification du paquet.

Dans les scénarios construits de régression, les sorties dégradées seules satisfont 28 des 69 critères. La référence conservée en satisfait 69/69. Cette différence est attendue par construction : elle prouve que la référence valide reste disponible et que le sélecteur ne livre pas la régression. Elle ne mesure pas la fréquence de régression d'un LLM ni un gain de 41 critères en usage courant.

Une référence invalide n'est jamais un repli admissible. Une égalité conserve la référence ; une adaptation valide peut remplacer une référence défaillante. Un reçu ou un artefact modifié est refusé. Une décision INCONCLUSIVE ne produit aucun artefact.

## Limites

Le lancement ne prouve pas l'obéissance d'un modèle. Les procédures textuelles ne sont pas qualifiées automatiquement. Le vérificateur doit être approprié, commun et autorisé ; ses dépendances doivent être figées explicitement si elles ne sont pas contenues dans son fichier. Les reçus ne sont pas signés et l'exécuteur local n'est pas un confinement hostile.

Le rejeu déterministe a duré 11.72 secondes, avec zéro appel de génération et zéro coût d'API pour ces essais. La conception du code, l'assistance dans la conversation, les vérifications unitaires et la maintenance ne sont pas comprises dans cette durée ou ce coût. Aucun gain global de productivité, de qualité des productions LLM ou d'économie n'est établi.

Les expériences de l'exemple N0 restent fictives et NOT_RUN. Les états d'un exemple ne sont pas promus par les tests du catalogue. Les anciens formats restent acceptés ; le [rapport historique 0.3.0](VALIDATION.md) conserve son périmètre.

## Reproduction publique

```bash
python3 tools/check_catalog.py
python3 -m unittest discover -s tests -v
```

Voir les [essais locaux](LOCAL_TRIALS.md) pour les commandes et les contrats. La suite publique couvre le fonctionnement des outils ; elle ne recrée pas les jeux privés ni les scores de la précédente expérience LLM.
