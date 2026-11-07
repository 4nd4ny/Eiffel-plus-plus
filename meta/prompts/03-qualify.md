# Examiner ce qui est réellement fourni

## Mission

Examine le candidat, ses spécifications et son mandat. Identifier N0, ou N1 lorsqu'un générateur spécialisé existe. Annoncer si l'examen est réalisé par son propre auteur. Adapter l'effort à la décision et au budget ; ne pas refaire un contrôle encore valable sans motif.

## Questions qui peuvent invalider le candidat

- Une obligation a-t-elle disparu ou été transformée en préférence ?
- Une graine exige-t-elle un outil absent ou un droit non accordé ?
- La méthode peut-elle commencer une action concrète, ou délègue-t-elle encore toute sa conception ?
- Un nouveau fichier, agent, dépôt ou niveau évite-t-il un problème identifié ? Une version plus simple suffirait-elle ?
- Le contexte utile est-il accessible sans charger tout le catalogue ?
- La séparation annoncée est-elle effective, ou les mêmes droits permettent-ils de réécrire le besoin et son évaluation ?
- Une contribution humaine ou une observation a-t-elle été inventée, exagérée ou transférée à un autre contexte ?

Contrôler la cohérence des fichiers et références. Pour N1, examiner aussi son domaine de réemploi et la possibilité d'ajuster N0 sans régénération générale. Le nombre de niveaux et la sophistication du vocabulaire ne servent pas de critères d'acceptation.

## Distinguer les résultats

| Examen | Ce qu'il peut établir |
| --- | --- |
| Structure | Formats, chemins et présence des éléments requis. |
| Cohérence | Accord argumenté entre les spécifications et la méthode proposée. |
| Fonctionnement | Observations des mécanismes réellement exécutés, sur une version identifiée. |
| Efficacité | Effets mesurés dans des conditions données, éventuellement face à une référence. |

`meta_harness.py check` et `seeds.py check` aident à contrôler les structures. Ils n'authentifient pas une décision ni une exécution. Une fiche `source-inspected` ne prouve pas un usage local ; une fiche `co-designed` ne prouve pas une amélioration.

Exécuter les contrôles disponibles qui sont nécessaires à l'usage annoncé. Lorsqu'une protection essentielle manque, bloquer les actions concernées et proposer un périmètre compatible. La simple existence d'une politique Markdown ne satisfait pas cette protection.

Distinguer fichier présent, composant chargé ou lancé, exécution terminée, comportement vérifié et utilité mesurée. Un script qui termine avec succès peut n'avoir rien corrigé. Une procédure texte ne devient pas suivie parce qu'elle existe. Utiliser un mécanisme d'observation réellement disponible ; sinon garder le résultat inconnu.

Une première proposition ne réclame pas un grand benchmark. Avant de revendiquer un bénéfice, comparer à une organisation crédible avec les mêmes informations et moyens ; compter aussi conception, échecs, reprises et temps humain. Pour étudier N1, inclure une génération directe de N0 comme alternative.

## Résultat à remettre

Un rapport court suffit : version examinée, contrôles et états, constats, corrections, limites, prochaines actions possibles et blocages précis. Employer les [états du protocole](../../protocol/README.md). Aucun résultat non exécuté ne devient `PASS`.

Séparer examen et adoption. Le mandat peut déjà autoriser l'emploi du candidat ou une modification réversible. Une autorité absente ne se remplace pas par `ACCEPTED`. Conserver aussi les résultats défavorables : ils peuvent rendre une graine plus utile en précisant quand l'éviter.
