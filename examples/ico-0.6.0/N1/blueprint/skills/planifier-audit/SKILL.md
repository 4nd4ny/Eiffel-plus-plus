---
name: planifier-audit
description: "Avant la modification ou lorsque le périmètre de vérification change."
---
# planifier-audit

Préconditions : lot autorisé et entrées `contract` lisibles ; respecter le contrat commun. Lire seulement la tranche utile de ROUTAGE et les facteurs affectés de QUALITE.

Choisir les oracles à partir du contrat ; associer chaque critère à un cas nominal et à une erreur pertinente. Vérifier les dépendances disponibles. Éprouver un défaut connu et un résultat illisible : un checker qui affiche PASS sans exercer le code est invalide. Décrire les commandes, la couverture et les exclusions ; figer check.py et toutes ses ressources avec le contrat lors de open. Un changement du plan impose un nouveau lot, sans effacer les essais précédents.

Postcondition : remettre `plan` à `governance, product`, avec les limites et preuves réelles. Les fichiers sont des ports de mission ; une copie de code qu’ils désignent doit aussi être vérifiée par l’atelier. Vérifier la mission avec son empreinte initiale avant la remise. Un changement du contexte rend la mission périmée ; aucune compétence ne crée une autorisation ou une garantie d’indépendance.
