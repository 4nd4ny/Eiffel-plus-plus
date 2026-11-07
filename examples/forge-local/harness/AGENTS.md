# Harnais local proposé

Statut : PROPOSED. Exemple fictif ; aucun essai logiciel exécuté. Lire [SPEC.md](SPEC.md), puis les seuls critères utiles de [CHECKS.md](CHECKS.md).

## Responsabilités proposées

| Rôle et acteur | Entrées → remise | Décisions et limites |
| --- | --- | --- |
| Gouvernance : opérateur ou délégataire | Mandat et moyens → périmètre, budget, délégations. | Décide dans son mandat ; ne réécrit pas un constat. |
| STBL : agent, sous mandat | Demande et décisions → contrat dans SPEC.md. | Propose les ambiguïtés ; ne change pas seul le besoin accepté. |
| Produit : agent | Contrat et mandat → code identifié et résultats techniques. | Choisit l'implémentation ; ne change pas les critères pour réussir. |
| Audit : même agent dans cette proposition | Contrat, candidat et CHECKS.md → constats et limites. | Examine sans corriger le candidat pendant le contrôle ; ne décide pas de l'acceptation métier. |

Ce cumul est un auto-examen, sans séparation de droits. Une indépendance requise appelle une autre organisation et des protections effectives. Les noms de rôles n'en fournissent aucune. Cette proposition n'accorde pas de mandat réel.

## Action et remise

Dans le mandat adopté, vérifier Python et les moyens de test, puis réaliser le contrat de SPEC.md avec les contrôles de CHECKS.md. Choisir librement les techniques utiles ; ne recopier ni le besoin ni les critères. Une ambiguïté métier hors délégation suspend seulement le travail qui en dépend.

Après modification, exécuter les contrôles pertinents ; conserver version, commande et résultat. Corriger un écart dans un nouveau candidat, sans changer le critère pour obtenir un succès. Après deux reprises sans information nouvelle, signaler le blocage et les parties utilisables.

Remettre le candidat, les résultats et les limites. Si une reprise est utile, ajouter la prochaine action et les décisions ouvertes. Conserver les adaptations avec leur raison et les observations disponibles, y compris les échecs.
