---
name: verifier-candidat
description: "Lorsqu’un candidat complet et son empreinte ont été remis."
---
# verifier-candidat

Préconditions : lot autorisé et entrées `candidate, rationale` lisibles ; respecter le contrat commun. Lire seulement la tranche utile de ROUTAGE et les facteurs affectés de QUALITE.

Recevoir l’empreinte externe du candidat et du lot ; vérifier la copie complète avec verify. Évaluer référence et candidat avec les mêmes contrôles via evaluate. Examiner le comportement et les exclusions, pas seulement le reçu. Une obligation FAIL refuse le candidat ; une exécution illisible ou une capacité absente reste UNKNOWN/NOT_RUN ; STALE invalide les preuves concernées. Conserver sorties brutes et temps dans le périmètre autorisé. Ne pas réparer pendant cet examen.

Postcondition : remettre `report` à `governance`, avec les limites et preuves réelles. Les fichiers sont des ports de mission ; une copie de code qu’ils désignent doit aussi être vérifiée par l’atelier. Vérifier la mission avec son empreinte initiale avant la remise. Un changement du contexte rend la mission périmée ; aucune compétence ne crée une autorisation ou une garantie d’indépendance.
