---
name: modifier-interface
description: "Quand le lot affecte un parcours, les sources affichées ou l’accessibilité."
---
# modifier-interface

Préconditions : lot autorisé et entrées `contract, plan` lisibles ; respecter le contrat commun. Lire seulement la tranche utile de ROUTAGE et les facteurs affectés de QUALITE.

Repérer le parcours dans web/src et sa source métier. Vérifier états chargement, vide, erreur et succès ; citations et données affichées doivent rester reliées à leur source. Conserver navigation clavier et comportement mobile. Utiliser les tests de composants puis le parcours navigateur prévu ; si le navigateur manque, remettre cette limite avec le candidat, sans remplacer le contrôle par les sondes du moteur. Figer le projet complet et expliquer le compromis UX, sans publier de données de test privées.

Postcondition : remettre `candidate, rationale` à `audit`, avec les limites et preuves réelles. Les fichiers sont des ports de mission ; une copie de code qu’ils désignent doit aussi être vérifiée par l’atelier. Vérifier la mission avec son empreinte initiale avant la remise. Un changement du contexte rend la mission périmée ; aucune compétence ne crée une autorisation ou une garantie d’indépendance.
