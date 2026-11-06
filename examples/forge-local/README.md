# Exemple : forger un petit harnais local

**Illustration non testée sur un logiciel métier, sans acceptation d'un opérateur inventée.** Cet exemple montre un N0 direct, trois documents de travail et une racine Git. Il remplace la chaîne de trois générations comme premier exemple du démarrage ; les exemples plus élaborés restent disponibles séparément.

Le besoin fictif est une petite commande locale qui filtre un fichier CSV par catégorie et compte les lignes retenues sans modifier l'entrée. La méthode retient une boucle courte, des instructions locales et des contrôles comportementaux. Les recettes `mini-swe-loop` et `codex-scoped-instructions` servent d'inspiration ; aucun runtime externe n'est installé.

- [AGENTS.md](harness/AGENTS.md) : répartition des responsabilités et prochaine action.
- [SPEC.md](harness/SPEC.md) : besoin du logiciel et spécification de la méthode, distingués.
- [CHECKS.md](harness/CHECKS.md) : critères concrets, moyens proposés et état non exécuté.
- [record.json](record.json) : fiche illustrative utilisable pour essayer `capture` ; elle ne rapporte aucune co-construction ou mesure fictive.

La première adaptation humaine peut porter sur la forme du résultat, le budget de reprise ou l'indépendance du contrôle. Elle doit être enregistrée pour ce qu'elle est : un choix situé. Un outil CLI et une interface web n'exigent pas exactement les mêmes moyens d'examen.

```bash
python3 tools/meta_harness.py check examples/forge-local/harness
python3 tools/meta_harness.py materialize examples/forge-local/harness --output ../essai-eiffel --git-init
```

Les commandes ci-dessus s'exécutent depuis la racine d'Eiffel++. Le harnais matérialisé reste à adopter et à essayer dans un mandat réel. Aucun logiciel CSV ni résultat d'audit applicatif n'est fourni dans cet exemple.
