# Prompt N2 — adapter au bon niveau

## Mission

À partir d'un changement de contexte, d'une préférence révisée ou d'observations d'exécution, détermine quelle transformation est utile. Préserve le [contrat de génération](../CONTRACT.md) et les décisions déjà acceptées. Ne régénère que ce que le changement rend pertinent.

## Choisir le niveau de transformation

| Situation | Transformation à envisager |
| --- | --- |
| Un paramètre ou une procédure N0 change dans le domaine prévu par N1. | Appliquer le prompt ADAPT de N1 ; produire un changement local de N0. |
| Une nouvelle phase ou famille de tâches reste dans le domaine de N1 mais appelle une autre organisation. | Réappliquer GENERATE de N1 sur le profil et le contexte courants. |
| Le domaine, les contraintes structurantes ou les capacités disponibles dépassent les règles N1. | Utiliser N2 pour réviser les prompts N1, puis engendrer le N0 nécessaire. |
| Les besoins ou les droits doivent changer pour que l'adaptation soit possible. | Préparer une décision pour l'autorité compétente ; poursuivre les parties déjà autorisées. |

Une nouvelle préférence n'impose pas toujours de changer les prompts N1 : un générateur capable de la prendre en compte peut produire N0 directement. En revanche, sa version de profil et le paquet N0 matérialisé doivent rester cohérents.

Après matérialisation, le patron N2 disponible peut être retrouvé dans la gouvernance sous `_eiffel/meta/START.md`. Examiner son identité et sa compatibilité avant emploi. L'archive conserve une ressource de régénération ; elle ne prouve pas à elle seule que cette version a historiquement engendré N1.

## Exploiter l'expérience sans la transformer en obligation automatique

Commence par les nouveaux événements et les sources pertinentes. Distingue une observation d'une explication proposée. Plusieurs copies ou relances d'un même incident ne deviennent pas plusieurs confirmations indépendantes.

Cherche l'effet sur le besoin et les quatre axes du tétraèdre, ainsi que les risques de régression. Une erreur grave peut justifier un changement même si elle est rare. Une procédure récurrente peut être déplacée vers un programme ordinaire si cela simplifie le travail.

Les résultats historiques restent rattachés à leur version. Une nouvelle configuration n'hérite pas automatiquement de leur validité. Les données et conclusions restent dans le périmètre de confidentialité de leurs sources.

## Produire une adaptation identifiable

Décris le déclencheur, l'effet recherché, les fichiers concernés, les conditions de validité et ce qui pourrait justifier un retour. Donne la modification concrète lorsque le mandat l'autorise.

Si le profil change, conserver l'origine de la nouvelle préférence ou contrainte. Créer un état cohérent du paquet N1 avec ce profil avant de matérialiser N0 avec son générateur ; les prompts inchangés peuvent être réutilisés. Ne pas fusionner implicitement deux versions du profil.

Prévoir le devenir des travaux en cours : maintien sur l'ancienne version, migration explicitement autorisée ou nouvelle qualification. Ne pas déplacer les critères d'acceptation d'un candidat à son insu.

Les changements partagés doivent être publiés sur la révision attendue par un mécanisme d'écriture conditionnelle réellement disponible. Une instruction de calculer un hash ne constitue pas à elle seule cette protection. En cas de conflit, relire et réévaluer les conclusions concernées.

## Qualifier proportionnellement

Reprendre les contrôles affectés et examiner les conséquences sur les autres obligations. Une modification locale correctement délimitée ne nécessite pas de relancer tous les acteurs et de relire tout le projet.

Une expérience n'est ajoutée que si elle peut départager des options encore pertinentes. Garder ses coûts, échecs et incertitudes. En l'absence de mesures, décrire le bénéfice attendu comme une hypothèse et choisir un périmètre d'emploi compatible avec cette incertitude.

## Autorité, budget et arrêt

Adopter automatiquement les adaptations effectivement déléguées et suffisamment qualifiées pour leur usage. Préparer une décision distincte pour celles qui dépassent le mandat ; ne pas demander à nouveau une autorisation déjà acquise.

Respecter le budget restant et transmettre sa consommation entre niveaux. Une nouvelle séance, une délégation ou un retour à N2 ne recrée pas le budget initial. Arrêter les révisions sans information nouvelle. La profondeur reste bornée à N2 → N1 → N0. Une modification de N1 ne déclenche pas la création d'un niveau supplémentaire.

Le résultat final est une version applicable, une proposition encore ouverte ou un diagnostic d'incompatibilité. Aucun de ces états ne doit être rebaptisé « optimum » sans domaine et résultats permettant cette conclusion.
