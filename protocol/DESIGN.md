# Justifier la conception pour l'humain — 0.6.0

Chaque génération livre ses instructions, scripts et une note de conception dans la même version du paquet. La note explique les décisions qui changent la manière de produire ou de vérifier le logiciel. Elle fournit une synthèse argumentée à partir du besoin, des contraintes et des observations, utilisable sans relire la conversation de génération.

## À chaque niveau

- N2 → N1 : justifier le domaine du générateur, les compétences réemployées, les choix laissés aux lots et l'utilité de N1 face à une génération directe de N0.
- N1 → N0 : justifier les choix du lot concret, les adaptations et les limites ; ne pas recopier la justification générale de N1.
- N2 → N0 directement : fournir la même justification concrète, avec la raison de ce parcours.
- N0 → réalisation : demander une synthèse des décisions du produit réellement affectées par la livraison, dans sa documentation de conception existante lorsqu'elle convient. Aucun niveau supplémentaire ni journal exhaustif n'est imposé.

La note propre au patron N2 est `meta/DESIGN.md`. Chaque N1 et N0 0.6.0 référence sa note par `design_rationale`, généralement `DESIGN.md`. Elle est distincte des instructions exécutées et accessible depuis le point d'entrée. En `four-repos`, la placer dans une racine effectivement matérialisée, généralement `governance/DESIGN.md` ; les métadonnées indiquent aux autres rôles où la retrouver.

## Contenu qui permet de décider

Retenir les décisions importantes, sans quota de sections ou de pages. Pour chacune, rendre compréhensible le lien : **besoin ou contrainte → choix → conséquence dans les fichiers → contrôle et limite → condition de révision**.

La note rend visibles :

- le contexte métier connu, les sources qui font foi, les hypothèses et les décisions encore ouvertes ; aucune politique d'entreprise ne doit être inventée ;
- les motifs de génie logiciel pertinents : contrats, modularité, couplage, gestion des erreurs, vérifiabilité, capacité d'évolution ou autres qualités affectées ; expliquer l'effet concret au lieu d'énumérer les noms ;
- une alternative plausible lorsqu'un compromis réel existe, les raisons du choix dans ce contexte et son coût ou sa contrepartie ; ne pas inventer des alternatives artificielles ;
- ce que l'on a observé, ce que l'on attend seulement et ce que l'on ne sait pas ; ne pas convertir une intention de robustesse en garantie ;
- un mode d'emploi pour l'adaptation métier : quelle exigence nouvelle ferait revoir quoi, quels fichiers/rôles/skills/contrôles seraient touchés et de quelle décision ou information cela dépend.

Une note courte peut suffire. Référencer contrats, profils, sources et preuves au lieu de les dupliquer. Un titre de section rempli par des généralités ne justifie pas le harnais.

## Usage et révision

L'humain peut s'en servir pour contester les hypothèses, comparer les compromis et adapter le harnais à l'entreprise. La note est explicative : elle ne modifie ni le besoin, ni les permissions, ni les critères d'acceptation. Si elle contredit les instructions, résoudre l'écart avant d'utiliser la conclusion concernée. Les décisions déjà autorisées restent utilisables ; aucun nouveau passage systématique d'approbation n'est créé.

Rédiger la note avec les choix, puis la relire face aux fichiers effectivement livrés. Lors d'une adaptation, actualiser les seuls motifs affectés, conserver l'historique dans les versions ou décisions existantes et préciser les contrôles à reprendre. La note courante décrit la méthode courante ; un ancien argument ne devient pas une justification du nouveau paquet par simple copie.

## Vérification et conservation

Le contrôle mécanique exige un document Markdown non vide, référencé et distinct des instructions. Il expose son empreinte sans noter la qualité de ses arguments. La capture conserve la note ; la matérialisation conserve celle de N0 et le N1 explicitement fourni avec sa propre note. La préparation des missions rend la note N0 consultable et la lie à leur référence ; sa modification rend ces missions périmées. Les anciens paquets restent lisibles sans note inventée rétroactivement.

La revue humaine ou de l'agent doit examiner les sources, la correspondance aux fichiers et l'utilité des indications d'adaptation. Une présence structurelle PASS ne suffit pas. Un examen par l'auteur reste un auto-examen ; la note ne constitue ni une transcription du raisonnement interne d'un modèle ni une preuve d'aptitude au déploiement.
