---
name: specifier-contrat
description: "Quand un mandat doit devenir des comportements contrôlables."
---
# specifier-contrat

Préconditions : lot autorisé et entrées `mandate` lisibles ; respecter le contrat commun. Lire seulement la tranche utile de ROUTAGE et les facteurs affectés de QUALITE.

Lire la source métier de la tranche dans ROUTAGE. Écrire préconditions, postconditions, effets et invariants avec leur frontière ; ne pas exclure un cas dû par une précondition commode. Nommer les critères obligatoires, les renforcements proposés et les moyens manquants. Fournir aussi scope, score_meaning, authority, excluded dans contract.json. Un score ne compense jamais une obligation. Réexaminer seulement les facteurs QUALITE touchés.

Postcondition : remettre `contract` à `audit`, avec les limites et preuves réelles. Les fichiers sont des ports de mission ; une copie de code qu’ils désignent doit aussi être vérifiée par l’atelier. Vérifier la mission avec son empreinte initiale avant la remise. Un changement du contexte rend la mission périmée ; aucune compétence ne crée une autorisation ou une garantie d’indépendance.
