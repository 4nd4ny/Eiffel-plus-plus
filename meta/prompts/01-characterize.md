# Décrire le besoin de produit et le besoin de méthode

## Mission

Extrais des sources disponibles ce qui doit changer la manière de travailler. Le brief, les décisions déjà données et le mandat sont les premières sources. Le [cadre de conception](../CONTRACT.md) et les [arbitrages](../TETRAHEDRON.md) aident à distinguer exigences, préférences et observations.

## Informations discriminantes

Décrire brièvement : le résultat utile et ses critères d'acceptation, les obligations, le périmètre négociable, les délais et ressources, l'attention humaine disponible, les droits, les outils réellement accessibles et les difficultés pertinentes. Préciser à quel objet chaque exigence s'applique : produit ou méthode. Référencer le contrat du comportement existant ; compléter seulement les préconditions, postconditions, effets, erreurs ou invariants pertinents encore ambigus. Ne pas inventer d'invariant pour remplir une rubrique.

Par exemple, « ne pas modifier le fichier source » concerne le produit ; « pouvoir reprendre après interruption » concerne la méthode. La seconde appelle un moyen de reprise proportionné, sans imposer une infrastructure de mémoire à tous les projets.

Distinguer ce que l'utilisateur a dit, ce que l'agent infère, ce qui a été observé et ce qui reste inconnu. Une question est utile si ses réponses changent une décision concrète ou une action réservée. Regrouper les questions liées et poursuivre les travaux indépendants. Ne pas demander des détails que la tâche n'oblige pas à interpréter.

Identifier qui porte gouvernance, STBL, produit et audit, les décisions déléguées et l'indépendance nécessaire. Un cumul est possible ; signaler les responsabilités non attribuées sans créer des agents par défaut. Ces choix alimentent les échanges définis dans le cadre de conception.

Examiner les quatorze [facteurs de qualité](../QUALITY.md) pour le logiciel : obligation ou préférence sourcée, moyen d'examen, inconnue ou raison de ne pas l'activer pour le lot. Conserver cette revue dans le besoin existant si possible. La qualité du harnais ne remplace pas celle du produit ; ne pas inventer quatorze objectifs chiffrés.

## Profil pour les outils de paquets

Le travail de compréhension peut commencer en Markdown. Pour employer les outils, écrire `profile.json` selon le [schéma](../schemas/profile.schema.json), version `0.3.0` :

| Section | Contenu |
| --- | --- |
| `project` | `slug`, `name`, `brief`. Slug de 1 à 64 minuscules, chiffres ou tirets sans tiret aux extrémités. |
| `preferences` | `status`, `source`, puis des `priorities` ordonnées ou des `weights` justifiés. `measures` est facultatif. |
| `constraints` | `{id, statement, verification}` pour les obligations ; la vérification décrit un moyen prévu, pas un résultat. |
| `authority` | `mandate`, `autonomous_actions`, `human_decisions` selon les droits effectivement accordés. |
| `unknowns` | Inconnues qui peuvent influencer le travail et leur effet possible. |
| `generation_budget` | `max_candidates`, `max_iterations`, `max_tokens`. Deux entiers positifs ; tokens peut être `null` si cette limite n'est pas connue. |

Les poids, s'ils existent, portent sur les quatre axes et totalisent 1. Les mesures ne sont renseignées que lorsqu'elles sont utiles ; chaque mesure indique `metric`, `unit`, `direction` et éventuellement `target`. Une absence de donnée n'est ni un zéro ni une performance prévue.

Les préférences inférées restent `PROPOSED`. `ACCEPTED` exige une décision identifiable et sa `decision_ref` ; ce champ ne l'authentifie pas. Une modification d'un profil existant conserve l'origine des décisions inchangées.

## Résultat court

Donner le profil et les conséquences pratiques : quelle information motive quel choix de méthode, et qu'est-ce qui ferait réviser ce choix ? Ces conséquences servent à chercher les graines compatibles. Décrire les conflits non résolus sans multiplier les formulaires ni inventer un arbitrage du responsable.
