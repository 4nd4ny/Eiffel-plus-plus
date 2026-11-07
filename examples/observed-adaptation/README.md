# Adapter à partir d'une observation

Exemple **fictif**, sans projet client et sans résultat d'efficacité. Le paquet [harness](harness/) contient une procédure CSV chargée selon un déclencheur, un petit auxiliaire Python et une fiche d'expérience `INCONCLUSIVE`. Les essais de cette fiche restent `NOT_RUN` ; les tests du catalogue ne les transforment pas en essais métier.

```bash
python3 tools/meta_harness.py check examples/observed-adaptation/harness
```

Le contrôleur vérifie les références et la cohérence des déclarations, sans exécuter l'auxiliaire. Le paquet peut être matérialisé et capturé avec les outils existants. Son script est illustratif : il ne prétend pas valider tout fichier CSV.
