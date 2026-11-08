# Une cascade vérifiable, sur un exemple fictif

Ce démonstrateur teste les portes N2 → N1 → N0. Ses réponses humaines sont des **fixtures synthétiques**, explicitement marquées ; il ne démontre aucun apprentissage ni bénéfice LLM.

Depuis la racine du dépôt, choisir une destination neuve :

```sh
python3 -B examples/cascade-0.7.0/demo.py /chemin/autorise/demo-cascade
python3 -B tools/cascade.py verify /chemin/autorise/demo-cascade/journal
```

Chaque niveau conserve deux cycles, puis constate `INCONCLUSIVE` faute de revue. La fixture ajoute une décision simulée, obtient `READY` et vérifie le passage. N0 clôt le périmètre. Les empreintes lient les pièces ; un `PASS` déclaré n'est pas un résultat d'exécution authentifié.

Dans un vrai projet, remplacer les fixtures par les artefacts, essais et réponses effectivement obtenus. Garder l'empreinte finale hors du journal pour détecter aussi une troncature de son histoire. Le journal peut être suivi dans un dépôt Git local ou privé ; aucun dépôt distant n'est créé automatiquement.

Voir le [contrat de cascade](../../protocol/CASCADE.md), les [commandes](../../tools/README.md) et le [guide de conservation et partage](../../docs/HISTORY.md).
