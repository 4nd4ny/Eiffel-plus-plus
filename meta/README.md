# Concevoir la méthode depuis les spécifications

Eiffel++ 0.4.0 est un **prototype de conception et de réutilisation de harnais**. Les outils vérifient des fichiers ; aucun gain de qualité, de coût, de délai ou d'autonomie n'est établi pour la méthode proposée.

## Deux objets à spécifier

Le besoin du **produit** décrit les comportements utiles et les contraintes des utilisateurs. Le besoin de la **méthode** décrit comment travailler dans les moyens disponibles : décisions, coordination, sources de contexte, vérification, budget, reprise et limites d'autonomie.

Eiffel++ emploie ici *Specification Driven Development* pour faire découler la méthode de ces spécifications. Leur précision doit servir une décision ou un contrôle ; elle n'impose ni une rédaction exhaustive avant tout essai ni un format unique.

La [revue qualité](QUALITY.md) examine les quatorze facteurs de Meyer au cadrage, puis transmet leurs conséquences pertinentes au lot. Elle complète les arbitrages de méthode sans imposer quatorze agents, tests ou objectifs.

Le contrat du comportement relie les exigences, le code et les contrôles : préconditions, postconditions, effets et invariants pertinents décrivent ce que doit faire le composant. Les contrats entre responsabilités organisent les remises et les décisions ; leurs règles Markdown ne deviennent pas des assertions exécutables. [CONTRACT.md](CONTRACT.md) définit ces deux usages pour la conception du harnais.

## Réemploi et co-construction

Donner [START.md](START.md) à un agent avec un brief. Le parcours est : spécifier ce qui change la méthode, chercher une graine, proposer N0, le forger avec l'opérateur, puis observer son usage et conserver l'instance choisie.

La [base de graines](../seeds/README.md) contient des fiches de provenance et, pour les instances capturées, un instantané du harnais. Un mécanisme décrit dans un projet externe peut inspirer une proposition sans être installé. Une instance co-construite peut rester non testée ; une observation favorable ne démontre pas son transfert à un autre projet.

Dans un paquet exporté, cet index peut ne présenter que les fiches sélectionnées, ou renvoyer au catalogue public. Il ne signifie pas que toute la base ou les artefacts des graines ont été chargés.

Le générateur peut réemployer sans modifier, paramétrer, composer ou inventer. Les critères de choix sont la compatibilité avec les spécifications, les capacités réellement disponibles et le coût complet attendu. La popularité d'une graine et le nombre de ses fonctions ne suffisent pas.

## Les niveaux restent disponibles

| Objet | Quand l'utiliser |
| --- | --- |
| **N0 : harnais du projet** | Instructions et contrôles concrets nécessaires au travail. La génération directe depuis le brief et les graines est le parcours court. |
| **N1 : générateur spécialisé** | Plusieurs phases, équipes ou situations récurrentes justifient des règles de génération et d'adaptation réutilisables. Son coût doit être explicité. |
| **N2 : patron Eiffel++** | Ces prompts génériques aident à concevoir N0 ou, si utile, N1. Ils n'ont pas à être rechargés pendant chaque tâche. |

Les quatre responsabilités — gouvernance, STBL, audit et produit — restent identifiables avec leurs entrées, remises et droits. Leur répartition entre agents dépend du travail et de l'indépendance nécessaires. La minimalité conserve ces obligations et retire les répétitions ; elle ne privilégie pas par principe un ou quatre agents.

## Les quatre prompts

| Prompt | Travail |
| --- | --- |
| [01-characterize.md](prompts/01-characterize.md) | Décrire les spécifications, priorités, plafonds, capacités et questions qui influencent la méthode. |
| [02-generate-meta-harness.md](prompts/02-generate-meta-harness.md) | Choisir des graines et forger N0 ; produire N1 seulement si son réemploi le justifie. |
| [03-qualify.md](prompts/03-qualify.md) | Examiner la cohérence, la capacité d'exécution et les résultats effectivement disponibles. |
| [04-adapt.md](prompts/04-adapt.md) | Modifier la partie concernée, puis capturer une instance avec sa provenance et ses limites. |

## Outils de fichiers

Depuis la racine du catalogue :

```bash
python3 tools/seeds.py list
python3 tools/meta_harness.py prepare --brief briefing.md --profile profile.json --output ../etape-zero
```

Ajouter `--seed ID` pour chaque fiche choisie et `--catalog DOSSIER` pour une autre base locale. `prepare` conserve les fiches sélectionnées dans `context/seeds/`, sans charger leurs artefacts ou runtimes. Sans sélection, le paquet le signale ; il ne prétend pas réutiliser une graine.

`prepare` assemble les entrées ; l'agent écrit ensuite N0 dans un dossier distinct. Les chemins ci-dessous désignent ce paquet effectivement produit :

```bash
python3 tools/meta_harness.py check ../mon-harnais
python3 tools/meta_harness.py materialize ../mon-harnais --output ../projet --git-init
```

`--meta-harness CHEMIN_N1` peut être ajouté si un N1 existe. Le mode `single-repo` matérialise un seul dépôt ; `four-repos` conserve le parcours à quatre racines. Le [guide des outils](https://github.com/4nd4ny/Eiffel-plus-plus/blob/main/tools/README.md) décrit leurs formats et limites ; il n'est pas nécessairement copié avec le paquet.

La préparation, le contrôle structurel et la copie ne lancent pas de modèle, n'installent pas les contrôles prescrits et ne décident pas de l'adoption. L'archive d'une source disponible n'est pas une preuve qu'elle a engendré historiquement le candidat.
