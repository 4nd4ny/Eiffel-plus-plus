# Besoin et contrats proposés

Statut de toutes les exigences ci-dessous : PROPOSED. Contrôles correspondants : NOT_RUN.

| Exigence | Comportement attendu |
| --- | --- |
| REQ-0001 | Ouvrir un CSV local sans transfert réseau et sans modifier le fichier source. |
| REQ-0002 | Afficher les valeurs, filtrer les lignes par catégorie et compter exactement les lignes retenues. |
| REQ-0003 | Signaler une entrée non prise en charge ; ne pas convertir silencieusement une donnée. |

## Contrat du lot initial

**Préconditions proposées :** fichier UTF-8 comportant id, nom, categorie et quantite ; format CSV effectivement pris en charge décrit dans la livraison.

**Postconditions :** pour une catégorie choisie, les lignes affichées sont exactement les lignes correspondantes ; le compteur indique leur nombre ; le fichier d'entrée garde les mêmes octets. Les champs restent des données, y compris lorsqu'ils ressemblent à du balisage.

**Invariants :** aucun transfert nécessaire au fonctionnement ; aucune décision implicite sur le sens d'une valeur ambiguë. Un échec d'import laisse l'utilisateur avec un diagnostic et la possibilité de choisir un autre fichier.

## Questions

- Q-0001, OPEN : que signifie un doublon d'id pour le métier ?
- Q-0002, OPEN : une quantité manquante est-elle autorisée et, si oui, comment l'afficher ?

Aucune réponse n'est inventée. En attendant, l'import peut diagnostiquer ces cas et les scénarios non ambigus restent spécifiables. Les préconditions ne doivent pas être renforcées pour exclure un fichier que le besoin réel exigerait d'accepter.

Les options sont examinées séparément selon leur valeur et le budget restant. Voir les [instructions STBL](AGENTS.md).
