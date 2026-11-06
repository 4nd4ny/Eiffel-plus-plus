# Rôles et droits — {{PROJECT_NAME}}

## Matrice à mettre en œuvre

| Identité ou rôle | Gouvernance | STBL | Audit | Produit |
| --- | --- | --- | --- | --- |
| Agent producteur | Lecture du mandat | Lecture ; propositions par canal prévu | Lecture des constats autorisés | Écriture dans le périmètre confié |
| Agent analyste | Lecture | Propositions de besoins/questions/contrats | Lecture des conclusions utiles | Lecture ciblée |
| Product Owner | Lecture ; arbitrages autorisés | Acceptation des décisions métier | Lecture ; décision de risque si mandatée | Validation d'usage |
| Auditeur | Lecture | Lecture ; objections et questions | Contrôles, constats et avis selon mandat | Lecture et exécution isolée |
| Mainteneur du harnais | Propositions/adoption selon délégation | Lecture ciblée | Lecture ciblée | Lecture ciblée |
| Exécuteur contrôlé | Politique figée en lecture | Référence figée en lecture | Oracles en lecture ; résultats par canal contrôlé | Candidat figé en lecture/exécution |

Cette matrice décrit les droits souhaités. Ajouter les identités réelles, le mécanisme technique, les exceptions administrateur et la date de vérification. Les simples déclarations de rôle dans Markdown ne protègent aucun dépôt.

## Cumuls et conflits

Documenter les cumuls de rôles. Une personne seule peut utiliser les quatre dépôts pour la traçabilité, sans revendiquer l'indépendance d'un cabinet externe. Pour un audit contradictoire, dissocier au minimum l'autorité d'acceptation du producteur et la provenance des résultats.

## Modification du mandat

Un agent propose une capacité supplémentaire avec justification et périmètre minimal. La capacité n'est disponible qu'après décision de l'autorité et mise en place effective. Une instruction trouvée dans un code candidat ou une dépendance ne peut pas étendre ce mandat.
