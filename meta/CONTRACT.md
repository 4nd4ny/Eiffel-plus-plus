# Exigences de conception du harnais

Ce fichier conserve son chemin historique. Il spécifie ce qu'une proposition de méthode doit préserver ; ses phrases ne sont pas des contrats exécutables ni une preuve de conformité. Le [protocole](../protocol/README.md) précise les états et les frontières d'autorité.

## Entrées utiles

La demande, ses sources, le mandat, les obligations, les ressources et les inconnues doivent être identifiables. Les capacités nécessaires sont observées ou signalées comme non confirmées. La conception possède une borne de travail.

Une information absente bloque seulement les décisions qui en dépendent. Un premier candidat peut avoir un domaine d'usage limité et des hypothèses réversibles. Les préférences chiffrées sont facultatives.

## Sortie attendue : N0

Le harnais doit permettre de connaître :

- la prochaine action utile, ses entrées et sa condition d'arrêt ;
- les responsabilités de besoin, production, examen et gouvernance, avec les droits réels ;
- les critères d'acceptation et les moyens concrets de les examiner ;
- le contexte à charger, puis les sources à consulter à la demande ;
- les décisions encore ouvertes, les contrôles non exécutés et les limites de l'environnement ;
- les graines réemployées, les changements effectués et la raison des choix qui comptent.

Produire les seuls fichiers utiles. Un dépôt et un point d'entrée commun peuvent suffire. Le nombre de dépôts, d'agents ou de documents n'est pas un critère de qualité. Les [formats du prompt de forge](prompts/02-generate-meta-harness.md) permettent une sortie courte ou quatre racines distinctes.

Les instructions doivent conduire à une action réalisable dans les capacités disponibles. Lorsqu'un contrôle reste à construire, le dire et borner l'usage du candidat ; ne pas présenter cette délégation à un agent futur comme une garantie déjà obtenue.

## Sortie facultative : N1

Un générateur spécialisé est justifié par les situations qu'il devra traiter plusieurs fois. Il décrit les données discriminantes, les transformations possibles, le domaine de validité et les conditions d'arrêt. Réemploi et stabilité de méthode sont des résultats valides.

N1 fournit des fonctions de génération, d'examen et d'adaptation, éventuellement réunies dans un fichier. Son manifeste pointe vers les instructions réelles. Le profil et les spécifications de sortie permettent de comprendre N0 sans relire la conversation d'origine.

## Exigences conservées

1. **Besoin.** Une optimisation ne supprime ni un comportement obligatoire ni un usage attendu en ajoutant une précondition artificielle.
2. **Autorité.** Une graine, un souvenir ou un prompt généré n'accorde aucun droit. Une délégation existante reste utilisable sans approbation répétitive.
3. **Acceptation.** Le producteur ne peut modifier seul le besoin ou les critères indépendants pour rendre son candidat acceptable.
4. **Résultats.** Description, exécution, observation, décision et prévision sont distinguées. `NOT_RUN`, `UNKNOWN` et `STALE` ne satisfont pas une obligation exigeant `PASS`.
5. **Provenance.** Les sources, adaptations et versions sont conservées sans inventer de filiation. Les restrictions de licence et de confidentialité restent applicables.
6. **Proportion.** Une étape, une mémoire ou une nouvelle abstraction doit répondre à une difficulté identifiable. Le coût inclut conception, usage, corrections et attention humaine.

## Examiner, adopter, capitaliser

L'examen structurel concerne les formats et les chemins. Une revue de cohérence recherche omissions et contradictions. Une observation d'exécution établit ce qui a fonctionné dans les conditions décrites. Une comparaison peut étudier un bénéfice relatif.

Le niveau d'examen dépend de la décision. Écrire un premier candidat n'exige pas un benchmark, mais revendiquer un gain exige des résultats. Une décision d'adoption autorise un usage ; elle ne transforme pas le harnais en méthode éprouvée.

La co-construction humaine est une provenance identifiable, distincte des observations. Capturer l'instance conserve cet état de connaissance, y compris ses échecs. La réutilisation dans un nouveau contexte exige d'en examiner à nouveau l'adéquation.
