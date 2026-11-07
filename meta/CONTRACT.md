# Exigences de conception du harnais

Ce fichier conserve son chemin historique. Il spécifie ce qu'une proposition de méthode doit préserver ; ses phrases ne sont pas des contrats exécutables ni une preuve de conformité. Le [protocole](../protocol/README.md) précise les états et les frontières d'autorité.

## Entrées utiles

La demande, ses sources, le mandat, les obligations, les ressources et les inconnues doivent être identifiables. Les capacités nécessaires sont observées ou signalées comme non confirmées. La conception possède une borne de travail.

Une information absente bloque seulement les décisions qui en dépendent. Un premier candidat peut avoir un domaine d'usage limité et des hypothèses réversibles. Les préférences chiffrées sont facultatives.

## Sortie attendue : N0

Le point d'entrée indique la prochaine action autorisée, les sources utiles et l'arrêt. Le harnais relie le comportement attendu, sa réalisation et les contrôles qui l'examinent, avec leurs limites. Les décisions ouvertes, capacités manquantes et contrôles non exécutés restent visibles.

### Contrat du comportement

Référencer la spécification qui fait foi. Pour les opérations concernées, préciser les préconditions à la charge de l'appelant, les postconditions dues par le fournisseur, les erreurs attendues et les effets autorisés. Lorsqu'un invariant est pertinent, nommer l'état valide et les frontières auxquelles il doit tenir ; une règle générale de prudence ne suffit pas. Garder les entrées invalides à traiter dans le besoin, sans les exclure artificiellement par précondition.

Lier ces obligations au code et aux contrôles disponibles. Un test établit un résultat sur les cas exécutés ; une assertion écrite ou un contrat dans un prompt n'est pas une preuve. Conserver une référence commune plutôt que recopier le besoin dans chaque rôle. L'implémentation reste libre dans ce contrat.

Le contrat et ses contrôles prennent en compte les [facteurs de qualité du logiciel](QUALITY.md) pertinents, avec les raisons des reports et les inconnues. Le respect des contrats ne suffit pas à établir toutes les qualités d'usage, d'évolution ou d'exécution.

### Contrats entre responsabilités

Pour chaque responsabilité, désigner qui l'assume, ce qu'elle reçoit et remet, ses décisions autorisées et les protections réellement disponibles. Ces contrats de travail sont documentaires ; ils ne constituent pas des assertions du logiciel.

| Responsabilité | Entrées → remise attendue | Limite d'autorité |
| --- | --- | --- |
| Gouvernance | Mandat, ressources, constats → répartition, budget et décisions dans la délégation. | Ne réécrit ni le besoin ni un constat pour faciliter une livraison. |
| STBL | Demande, sources, décisions → contrat du comportement et critères de référence. | Ne fabrique ni acceptation métier ni résultat de contrôle. |
| Produit | Contrat et ordre de travail → candidat identifié, changements et résultats techniques. | Ne modifie pas seul les critères indépendants ni leur verdict. |
| Audit | Contrat, candidat et moyens de contrôle → constats, avis et limites. | Ne corrige pas le candidat pendant son examen et ne décide pas du besoin. |

Un acteur peut cumuler des responsabilités ; déclarer les cumuls et, si le producteur examine son propre candidat, l'auto-examen. Plusieurs agents ne prouvent pas leur indépendance. Un contrôle automatique peut assurer une partie de l'examen sans juger l'adéquation du besoin. Une séparation indispensable mais absente reste une limite, jamais un rôle fictif.

Produire les seuls fichiers utiles, avec les sources et raisons des adaptations. Un point d'entrée commun peut suffire si les échanges ci-dessus y sont concrets ; faire pointer quatre clés vers ce fichier ne le démontre pas. Les [formats du prompt de forge](prompts/02-generate-meta-harness.md) permettent une sortie courte ou quatre racines distinctes. La minimalité reste une intention de conception, sans quota de mots, fichiers ou agents.

Les instructions doivent conduire à une action réalisable dans les capacités disponibles. Lorsqu'un contrôle reste à construire, le dire et borner l'usage du candidat ; ne pas présenter cette délégation à un agent futur comme une garantie déjà obtenue.

## Justification destinée à l’humain

Chaque paquet N1 ou N0 est livré avec une [note de conception](../protocol/DESIGN.md), référencée par `design_rationale`, produite en même temps que ses instructions et scripts. Elle relie besoins et sources, décisions, compromis de génie logiciel, fichiers concernés, contrôles et limites. Elle indique comment adapter ces choix aux exigences de l’entreprise sans inventer ses politiques. N1 justifie la méthode réemployable ; N0 justifie les choix du lot. La note du patron lui-même se trouve dans [DESIGN.md](DESIGN.md).

La note est une synthèse des décisions et de leurs raisons vérifiables, pas une obligation de journal exhaustif. Une explication ne modifie ni les critères ni le mandat. La revue recherche les incohérences avec les fichiers livrés et les indications d’adaptation inutilisables ; le contrôle de présence ne les détecte pas à lui seul.

## Capacités mobilisables

Le [contrat des skills](../protocol/SKILLS.md) relie chaque tâche du lot à une responsabilité et à un moyen : méthode native suffisante, skill concret ou capacité manquante. Un skill reçoit des entrées, produit une remise et préserve les invariants pertinents sous ses préconditions. Ses ressources et son destinataire sont explicites. Les capacités déclarées ne deviennent démontrées qu’à la mesure des observations disponibles.

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
