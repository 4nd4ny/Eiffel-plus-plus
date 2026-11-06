# CTR-0001 — Contrat d'une opération ou d'un composant

Modèle Eiffel++ **0.3.0**. Identifiant illustratif · Statut de décision : `PROPOSED`.

| Champ | Valeur initiale |
| --- | --- |
| Exigences sources | À renseigner avec leurs révisions. |
| Décision applicable | Aucune. |
| Opération / composant / frontière | À renseigner. |
| État observé et abstractions | À renseigner : état avant, état après, unités et égalités utilisées. |
| Hypothèses d'environnement | À renseigner ; distinguer ce qui est contrôlé de ce qui est supposé. |

## Préconditions

Décrire les obligations du demandeur et le domaine d'appel valide. Préciser qui vérifie les entrées externes. Ne pas utiliser une précondition pour supprimer une obligation de refus propre ou un cas métier normalement autorisé.

## Postconditions et effets

- Résultat positif garanti lorsque les conditions de succès sont réunies.
- Relation entre état avant et état après.
- Données et effets externes autorisés à changer ; éléments qui doivent rester inchangés.
- Erreurs admises, résultat observable et état laissé après échec.
- Atomicité, reprise et idempotence lorsque nécessaires.

## Invariants et progrès

Énoncer les propriétés de cohérence et les points où elles doivent tenir. Ajouter les obligations temporelles pertinentes : réponse, terminaison, absence de famine ou progression sous des hypothèses explicites. Un invariant de sécurité ne démontre pas à lui seul le progrès.

## Vérifiabilité et absence de vacuité

| Obligation | Moyen de validation envisagé | Hypothèses / limites | Résultat actuel |
| --- | --- | --- | --- |
| À renseigner. | Assertion, test de propriétés, modèle, preuve ou inspection. | À renseigner. | `NOT_RUN` |

Vérifier que le domaine admet un cas valide, qu'un comportement utile est exigé et qu'un contre-exemple significatif serait rejeté. Chercher des préconditions contradictoires et des postconditions triviales. Les résultats de cette analyse sont des éléments d'assurance limités, pas une preuve de complétude du besoin.

Si une formalisation exécutable est produite, indiquer sa notation, sa révision et son lien avec cette fiche. Toute différence de sens suit une fiche `CHG`. Une preuve de conformité à ce contrat ne valide pas automatiquement le choix du contrat par le client.

Voir le [protocole commun](../../../protocol/README.md).
