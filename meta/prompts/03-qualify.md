# Prompt N2 — examiner un générateur ou un harnais candidat

## Mission

Examine le paquet annoncé, ses entrées et son mandat. Commence par identifier le niveau : N1 contient des prompts qui engendrent une méthode ; N0 contient la méthode opérationnelle du projet.

Utilise le [contrat de génération](../CONTRACT.md). Adapte la profondeur de l'examen à la décision actuelle et au budget. Ne répète pas les contrôles déjà valides sans motif d'invalidation. Annonce si l'examen est réalisé par le même agent que la génération.

## Examen commun

Vérifie que le paquet correspond au profil et au besoin fournis. Les choix importants doivent être reliés à une raison précise : contrainte, préférence, capacité ou observation. Les inconnues et les décisions non établies doivent rester identifiables.

Cherche notamment :

- une obligation perdue ou transformée en préférence négociable ;
- un élargissement de permissions présenté comme un gain d'autonomie ;
- une précondition qui exclurait un usage que le client attend ;
- une fonctionnalité disponible supposée activée sans observation ;
- une assertion d'efficacité sans mesure, ou une simulation décrite comme une exécution ;
- une source, un souvenir ou un exemple promu en autorité sans décision ;
- une procédure coûteuse dont aucune condition du projet ne justifie l'emploi.

Corrige les défauts réversibles dans le mandat. Un désaccord sur le besoin ou sur une autorité appelle une question ciblée au rôle compétent.

## Examen de N1

Lis effectivement les prompts de génération, de qualification et d'adaptation. Vérifie qu'ils contiennent les informations nécessaires à leur usage hors de la conversation d'origine.

Sur les variations pertinentes décrites par le concepteur, demande quels choix de méthode changeraient et pourquoi. Vérifie que les règles savent traiter une situation nouvelle dans leur domaine de validité, ou reconnaître qu'elle le dépasse. La présence des mots « adaptable » et « méta-harnais » ne suffit pas.

Vérifie les conditions de retour vers N2 et la borne de révision. Aucun prompt ne doit s'accorder la faculté de changer seul l'objectif, le mandat ou le contrôle qui permettra son adoption.

## Examen de N0

Vérifie que les quatre responsabilités et leur séparation existent dans les fichiers effectifs. Une entrée courte doit permettre à chaque acteur de connaître sa prochaine action, ses sources, son mandat et ses conditions d'arrêt.

Contrôle la cohérence des chemins, interfaces, états et références entre dépôts. Vérifie qu'un résultat attendu ne reste pas formulé comme une consigne vague alors qu'un contrôle ou une décision précise est nécessaire.

Identifie ce qui est documentaire, configuré et exécuté. Si une obligation nécessite une protection technique, préciser la capacité requise et ce qui a réellement été vérifié. L'absence de cette protection bloque les actions concernées ; elle n'empêche pas de livrer un candidat explicitement limité.

## Niveaux de qualification

| Niveau examiné | Ce que l'examen peut établir |
| --- | --- |
| Structure | Formats, chemins, fichiers et champs requis. |
| Cohérence | Accord entre besoin, profil, responsabilités et règles générées. |
| Fonctionnement | Observations d'exécution des mécanismes concernés. |
| Efficacité | Résultats mesurés sur les tâches et conditions annoncées. |

Le programme `tools/meta_harness.py check` aide au premier niveau. Il ne remplace pas les autres. Employer les niveaux nécessaires à la décision ; l'efficacité comparative n'est pas une précondition universelle pour produire un premier harnais.

## Résultat à écrire

Fournis un rapport court : objet et version examinés, niveau d'examen, contrôles et états, constats, corrections faites, limites, actions possibles dans le mandat et blocages restants.

Pour chaque contrôle, utiliser les états du protocole. Pour chaque résultat exécuté, conserver ses références. Une revue textuelle établit une conclusion de revue textuelle ; elle n'est pas une preuve d'exécution des mécanismes décrits.

Sépare la qualification de l'adoption. Une autorisation déjà accordée peut permettre l'adoption ou la matérialisation sans nouvelle demande. Une autorité manquante ne se remplace pas par une ligne `ACCEPTED` dans le manifeste.
