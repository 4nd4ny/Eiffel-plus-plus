# Méthode proposée pour des évolutions autonomes

Origine : chaîne illustrative access-service, Eiffel++ 0.2.0. Décision d'adoption : PROPOSED. Qualifications : NOT_RUN.

## Organisation et justification

| Choix N0 | Raison |
| --- | --- |
| Politique et interface stabilisées avant partage du travail | Plusieurs composants doivent interpréter la même décision d'autorisation. |
| Contrôles indépendants exécutables | Les obligations d'isolation doivent rester vérifiables sans revue humaine de chaque correction. |
| Réalisation parallèle seulement sur interfaces stabilisées | Éviter que les agents construisent des hypothèses de politique incompatibles. |
| Mémoire des incidents avec versions de politique | Évolutions répétées ; les leçons peuvent devenir fausses après un changement de règle. |
| Remontées humaines définies par événements | Chercher l'autonomie dans un mandat, sans transformer chaque résultat en demande d'approbation. |

## Circuit d'un changement

STBL rend explicite le comportement demandé et ses décisions de politique. Audit définit l'examen correspondant. Produit propose un candidat et corrige les contre-exemples. L'exécuteur vérifie le candidat identifié. La décision de livraison suit la délégation établie, distincte d'un simple avis du modèle.

Une réalisation, une analyse de dépendances et une préparation de données synthétiques peuvent progresser en parallèle si leurs interfaces sont connues. L'identité d'un rôle ne se confond pas avec un agent permanent.

## Mise en service

Il reste à établir les identités techniques, droits, exécuteur, sources de politique et autorité de livraison. Ces éléments sont déclarés dans l'exemple, non installés. Une simulation sur doubles doit annoncer les intégrations qu'elle ne vérifie pas.

Les [instructions de gouvernance](AGENTS.md) sont le point d'entrée. Le N1 archivé sous `_eiffel/meta-harness/` sert aux adaptations après matérialisation ; les quatre dépôts sont reliés par des références de rôle et de version.
