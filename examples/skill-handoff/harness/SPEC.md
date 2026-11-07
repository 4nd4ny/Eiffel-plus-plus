# Contrat commun CSV

Entrées : source CSV UTF-8 à virgules, en-tête unique incluant category, lignes de même longueur ; rules JSON avec category de type chaîne. Le producteur refuse les fichiers irréguliers et les règles invalides. La sortie contient exactement les lignes dont category égale la catégorie demandée, dans l’ordre initial, avec doublons, en-tête et valeurs conservés. Zéro ligne retenue est valide. Préserver les fichiers source et règles ; écrire dans une destination neuve.

L’audit compare séparément source et candidat sous les mêmes règles. Son rapport doit distinguer source valide et résultat conforme ; une erreur d’environnement ne prouve pas une violation du produit. Les empreintes de mission protègent l’applicabilité des constats, pas la justesse de l’oracle. Aucune décision de livraison n’est implicite.
