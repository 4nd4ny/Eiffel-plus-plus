---
name: filter-rows
description: Filtrer un CSV local par catégorie en préservant les lignes et la source ; à utiliser pour produire un nouveau candidat.
---

Reçois les ports source et rules de la mission Produit. Le [contrat commun](../../SPEC.md) fixe le résultat ; un fichier invalide appelle un refus explicite, pas une précondition qui le ferait disparaître.

Python 3 et une destination neuve sont nécessaires. Depuis la racine de mission, exécute `python3 -B resources/skills/filter-rows/scripts/run.py inputs/source inputs/rules CHEMIN_CANDIDAT`. Le script refuse d’écraser une sortie. Conserve source, règles et contrôles ; ne modifie pas les assertions pour réussir.

Une sortie 0 établit la production du fichier, pas son acceptation. En erreur, conserver le diagnostic et arrêter cette production ; pas de remise d’un fichier partiel. Sinon, transmettre le port candidate à Audit avec l’empreinte de mission conservée par le coordinateur. Le destinataire examinera le résultat sous les mêmes règles. L’absence de sorties ne permet pas de relancer indéfiniment le lot.
