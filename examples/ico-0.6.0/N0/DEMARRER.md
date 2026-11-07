# Démarrer un lot

Depuis une console Python, les fonctions de `tools/workshop.py` sont également utilisables ; l’exemple exécutable `demo.py` à la racine de l’exemple public montre l’enchaînement complet. La copie privée inclut un lanceur prêt pour le diagnostic ICO.

```sh
python3 -B tools/workshop.py --eiffel "$EIFFEL" open --harness "$HARNAIS" --code "$SOURCE_PROPRE" --checker "$CONTROLES" --contract "$CONTRAT" --plan "$PLAN_AUDIT" --output "$LOT_NEUF"
python3 -B tools/workshop.py --eiffel "$EIFFEL" freeze --workspace "$LOT_NEUF" --anchor "$EMPREINTE_LOT" --output "$CANDIDAT_NEUF"
python3 -B tools/workshop.py --eiffel "$EIFFEL" evaluate --workspace "$LOT_NEUF" --anchor "$EMPREINTE_LOT" --output "$EVAL_REFERENCE"
python3 -B tools/workshop.py --eiffel "$EIFFEL" evaluate --workspace "$LOT_NEUF" --anchor "$EMPREINTE_LOT" --candidate "$CANDIDAT_NEUF" --candidate-anchor "$EMPREINTE_CANDIDAT" --output "$EVAL_CANDIDAT"
python3 -B tools/workshop.py --eiffel "$EIFFEL" compare --workspace "$LOT_NEUF" --anchor "$EMPREINTE_LOT" --evaluation "$EVAL_REFERENCE" "$SHA_EVAL_REFERENCE" --evaluation "$EVAL_CANDIDAT" "$SHA_EVAL_CANDIDAT" --output "$CHOIX_NEUF"
```

Conserver chaque empreinte retournée avant l’étape suivante. Modifier seulement `LOT_NEUF/work` entre ouverture et gel. Les chemins sont des paramètres explicites, jamais des chemins implicites vers un projet original. `check.py CODE` imprime un objet JSON avec `criteria` et `score` ; `contract.json` décrit `criteria`, `scope`, `score_meaning`, `authority`, `excluded`. Un code de sortie non nul ou une sortie illisible vaut UNKNOWN. Les vérificateurs sont des programmes autorisés, à examiner avant lancement.

Pour une mission, préparer chaque port déclaré sous forme de fichier, conserver `order_sha256`, lire le SKILL.md copié, appliquer sa méthode et remettre les ports attendus au rôle permis. Les commandes de `skills.py --help` appartiennent au runtime fourni. Les paramètres du lot et les justifications ne remplacent pas la lecture de la source métier.
