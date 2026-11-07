# Pourquoi ce harnais pour le lot CSV

Ce lot fictif demande une production suivie d'un examen. Le [contrat](SPEC.md) fait foi pour la transformation ; le [profil](profile.json) borne les moyens et les décisions. Le [manifeste](harness.json) et le [point d'entrée](AGENTS.md) portent les choix ci-dessous. Le générateur N1 peut aussi produire un lot d'examen seul ; ce n'est pas le mode retenu ici.

## Décisions du lot

| Décision | Motif, alternative et contrepartie | Réalisation et contrôle |
| --- | --- | --- |
| Charger filter-rows pour Produit et check-rows pour Audit | Il faut créer puis vérifier un résultat. Un audit seul ne remplirait pas le besoin de production ; une procédure unique réduirait la coordination mais mêlerait les deux opérations. | Deux composants dans harness.json, scripts et contrats dans skills/. Examiner lignes exactes, doublons, ordre et résultat vide. |
| Préserver source et règles, produire une sortie neuve | Garder la référence rend le défaut reproductible et évite de perdre les données d'entrée. Réécrire la source économiserait un fichier mais supprimerait cette garantie. | Les scripts utilisent une sortie exclusive ; les missions conservent les entrées et leurs empreintes. Une entrée invalide ne devient pas un succès. |
| Cumuler les quatre responsabilités dans un acteur | Le périmètre local n'exige pas ici de séparation d'identités. Ce choix limite la coordination mais l'examen reste celui du producteur. | AGENTS.md décrit les remises ; aucun auditeur indépendant ni droit système distinct n'est annoncé. |
| Distinguer la remise du verdict | Un fichier présent peut contenir un constat incomplet ou erroné. Le destinataire doit examiner ses postconditions. | L'outil conserve les pièces avec semantic_status NOT_RUN ; Gouvernance lit les résultats avant de décider la suite. |

## Ce que l'humain peut adapter

Pour une autre catégorie, changer les règles d'entrée et préparer de nouvelles missions ; le contrat de sélection reste le même. Pour examiner un résultat déjà fourni, retirer `filter-rows` des composants et son attribution dans `capabilities`, conserver `check-rows`, adapter AGENTS.md et cette note : Produit reçoit alors le candidat sans le corriger. Les obligations du contrat restent dues.

Un changement de colonnes, d'encodage ou de sélection affecte SPEC.md, les deux scripts et les contrôles, pas seulement la formulation du prompt. Un besoin d'audit indépendant affecte les rôles et les moyens d'exécution ; changer le nom du rôle ne suffit pas. Une exigence de gros volumes appelle des mesures et une révision de la lecture en mémoire. Une politique d'entreprise concernant données, droits ou déploiement doit entrer dans le profil et les instructions concernées, sous l'autorité qui peut la définir ; aucune n'est inventée ici.

## Portée des résultats

Les tests du catalogue exercent le format CSV, les remises et des altérations de mission. Ils ne valident pas la signification métier de chaque ligne, un déploiement d'entreprise ou une amélioration des résultats d'un LLM. La vérification d'empreintes suppose une référence conservée par l'appelant ; elle ne protège pas contre la réécriture de toutes les références par un même acteur.

Lors d'une révision, expliquer le déclencheur et le compromis affecté, modifier les fichiers correspondants, puis reprendre les contrôles utiles. Conserver les anciennes décisions dans l'historique. Cette note explique le lot ; elle n'ajoute aucune permission ni exception à SPEC.md.
