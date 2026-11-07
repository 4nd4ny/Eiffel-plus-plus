# Qualité du logiciel : repères de Meyer

Référence : Bertrand Meyer, *Object-Oriented Software Construction*, 2e édition, chapitre 1, §1.1–1.2, pages 3–16 : dix facteurs développés puis quatre complémentaires. [Page de l'auteur](https://bertrandmeyer.com/oosc2/) ; [édition officielle](https://smarties-press.com/books/oosc2/). Les questions ci-dessous sont une transposition pour Eiffel++.

| Repère | Sens du facteur | Question à résoudre pour le produit |
| --- | --- | --- |
| Q01 Correction | Respect de la spécification. | Quel contrat relie entrées, résultats, effets et contrôle ? |
| Q02 Robustesse | Réaction appropriée aux situations anormales. | Quelles défaillances explorer ? Quels diagnostics, arrêts ou reprises protégeront les données ? |
| Q03 Extensibilité | Facilité d'adaptation aux changements du besoin. | Quel changement plausible doit rester local ? Quelle interface évite de le propager partout ? |
| Q04 Réutilisabilité | Emploi de composants dans d'autres applications. | Quel composant et quel contrat pourraient être réemployés ? Quel couplage l'empêcherait ? |
| Q05 Compatibilité | Facilité de combinaison des composants. | Quels formats, API, versions et échanges doivent rester compatibles ? |
| Q06 Efficience | Sobriété des ressources à l'exécution. | Quelle charge, quel matériel, quelles mesures de temps, mémoire ou trafic sont pertinents ? |
| Q07 Portabilité | Facilité de transfert entre environnements. | Quelles plateformes sont visées, quelles dépendances les limitent, où les vérifier ? |
| Q08 Facilité d'usage | Facilité d'apprentissage et d'utilisation. | Quel parcours, quel utilisateur, quel retour d'erreur examiner concrètement ? |
| Q09 Fonctionnalité | Étendue des possibilités offertes. | Quels usages livrer, différer ou exclure, selon la référence du besoin ? |
| Q10 Ponctualité | Disponibilité au moment utile. | Quelle échéance de livraison est connue ? Quel incrément utile peut y répondre ? |
| Q11 Vérifiabilité | Facilité de contrôle et de diagnostic. | Quels oracles, données, observations et moyens permettent de détecter puis localiser un écart ? |
| Q12 Intégrité | Protection contre les accès et modifications non autorisés. | Quelles données, identités, frontières et permissions protéger dans le logiciel ? |
| Q13 Réparabilité | Facilité de correction des défauts. | Comment reproduire un écart, isoler sa cause, corriger et prévenir sa réapparition ? |
| Q14 Économie | Réalisation dans le budget attribué. | Quel coût total de production, contrôle et reprise compter ? Quel budget est effectivement accordé ? |

Correction et robustesse contribuent à la fiabilité. Lisibilité et modularité sont des moyens internes au service des qualités externes. La documentation sert notamment usage, évolution et réemploi ; son volume n'est pas une qualité supplémentaire.

## Emploi dans la génération

Au cadrage, examiner les quatorze facteurs une fois. Pour chacun, retenir une exigence ou préférence sourcée et son moyen d'examen, ou expliquer pourquoi il ne change pas le lot. Une inconnue reste à qualifier ; « hors lot » ne supprime pas une obligation du projet. Ne fabriquer ni seuil, ni priorité, ni résultat. Un moyen indisponible reste indiqué.

Cette revue peut tenir dans le besoin existant : aucun fichier, agent, test ou score par facteur n'est imposé. N1 conserve les décisions de projet et leurs déclencheurs ; N0 charge seulement ce qui concerne le lot et conserve les références nécessaires à sa reprise. Un changement de périmètre réexamine les facteurs affectés.

Examiner le **logiciel produit** : réutiliser une graine ne démontre pas la réutilisabilité du code, limiter les tokens ne mesure pas son efficience, réduire les questions à l'opérateur ne prouve pas sa facilité d'usage. Les erreurs désormais décrites dans le contrat relèvent aussi de la correction. Les priorités et coûts de la méthode restent distincts ; aucun gain ne compense une obligation non satisfaite.
