---
name: check-rows
description: Examiner un CSV filtré par comparaison avec sa source et ses règles ; à utiliser après réception d’un candidat identifié.
---

Reçois source, rules et candidate. Lis le [contrat commun](../../SPEC.md) et vérifie la validité de la mission avec l’empreinte conservée. Si candidat, règles ou contrôles ont changé, le constat est STALE ; le coordinateur doit examiner le changement avant de préparer une nouvelle mission.

Depuis la mission, exécute `python3 -B resources/skills/check-rows/scripts/run.py inputs/source inputs/rules inputs/candidate CHEMIN_RAPPORT`. La sortie 0 signifie que les cas examinés satisfont le contrat, 1 une non-conformité du candidat, 2 une impossibilité de conclure. Le rapport explicite les critères. Ne corrige ni candidat ni contrôleur pendant cet examen.

Remets le port report à Gouvernance, y compris les échecs et limites. Une remise complète n’est pas une décision d’adoption. Source, règles et candidat restent inchangés ; une entrée indisponible ou invalide donne UNKNOWN. Cet oracle CSV doit lui-même être qualifié par des contre-exemples avant un usage au-delà de l’exemple.
