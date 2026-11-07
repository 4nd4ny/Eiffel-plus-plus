# Filtrer un tableau local — exemple fictif

Le produit reçoit un CSV UTF-8 avec une colonne category et un fichier JSON portant une catégorie. Il rend les lignes correspondantes avec le même en-tête, le même ordre, les doublons et les valeurs préservés. Une catégorie absente donne un en-tête seul. Un CSV irrégulier, une colonne category manquante ou des règles invalides sont refusés. Aucun original n’est écrasé.

Deux lots récurrents justifient N1 : produire puis examiner un résultat ; examiner un résultat déjà fourni. Le second lot n’a pas besoin du skill de production. Gouvernance coordonne et conserve la référence de mission, STBL décrit la catégorie demandée, Produit remet un candidat et Audit examine la transformation. Ces rôles sont logiques ; cet exemple ne crée pas d’agents indépendants.
