# Contribuer

Préciser le problème traité, le comportement attendu et ce qui permettrait d'abandonner la proposition. Eiffel++ est un prototype non évalué en production ; ajouter des fichiers ou des niveaux ne constitue pas un progrès en soi.

## Modifier la méthode

Partir des spécifications du besoin et de la méthode. Préférer réemploi, adaptation ou composition avant invention. Justifier une procédure par un effet utile et un coût acceptable. Ne pas imposer quatre dépôts, un générateur N1 ou des pondérations à un projet qui n'en a pas besoin.

Les quatre patrons historiques conservent leur structure pour rester lisibles ; les harnais produits peuvent être beaucoup plus courts. Les responsabilités et les permissions restent explicites même lorsqu'elles partagent un fichier.

## Ajouter une graine

Suivre le [guide de la base](seeds/README.md). Relier toute synthèse externe à des fichiers et une révision réellement consultés ; conserver les licences et limitations. Ne pas recopier des prompts propriétaires ou des données privées.

Une instance co-construite indique les modifications décidées, leur origine, le contexte et les essais réellement effectués. Une référence déclarée n'authentifie pas la décision. L'absence de mesure est acceptable si elle reste visible. Conserver aussi les échecs et contre-indications.

## Modifier le protocole ou les outils

Documenter compatibilité et migration. Les anciens résultats restent interprétés selon leur version. Ne pas confondre validation de fichiers, cohérence de la méthode et efficacité observée.

```bash
python3 tools/check_catalog.py
python3 -m unittest discover -s tests -v
```

Ajouter un test lorsqu'il couvre un risque concret du code. Les règles en prose demandent une revue ou une observation adaptée, pas un test qui se contente de retrouver leurs mots.
