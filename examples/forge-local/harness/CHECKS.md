# Contrôles proposés

**État initial de tous les contrôles : NOT_RUN.** Aucun test du logiciel futur n'est livré ou exécuté avec cet exemple.

| Contrat de SPEC.md | Observation à obtenir |
| --- | --- |
| REQ-0001 — filtrage et comptage | Un jeu mêlant deux catégories, des doublons et des champs cités donne la sous-séquence attendue, dans le même ordre, et son compte exact. |
| REQ-0001 — valeurs et effets | Accents, chaînes numériques et champs vides conservés ; `L` identique avant et après l'opération interne. |
| REQ-0003 — résultat vide valide | Résultat vide, compte nul, absence d'erreur. |
| REQ-0003 — entrée invalide | Fichier inaccessible, colonne absente et CSV malformé produisent un diagnostic explicite. |
| REQ-0002 — fichier source intact | Empreinte du fichier avant et après les scénarios identique. |
| REQ-0002 — traitement local | Examiner le code et les dépendances ; si une garantie réseau forte est requise, observer l'exécution avec un dispositif adapté. L'absence de `curl` dans le texte ne suffit pas. |

Le producteur écrit des tests comportementaux, par exemple avec `unittest`, et exécute la commande effectivement disponible. `python3 -m unittest discover -s tests -v` est un moyen proposé une fois ces tests créés ; il ne constitue pas une preuve actuelle.

Éprouver aussi l'oracle : une version qui renvoie toujours zéro doit échouer sur le jeu comportant des lignes correspondantes. Conserver les résultats attachés au candidat exact. Pour l'usage, l'opérateur vérifie que la sortie obtenue répond à son besoin ; un test vert ne démontre pas ce choix métier.

Une révision de périmètre rend périmés les contrôles concernés. L'examen dans le même environnement et par la même identité reste déclaré comme tel.
