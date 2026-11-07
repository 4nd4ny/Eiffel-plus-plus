# ICO — réalisation Eiffel++ 0.6.0

Exemple issu d’une régénération réelle : [N2 et ses entrées](N2/START.md) → [générateur N1](N1/GENERATE.md) → [harnais N0 complet](N0/AGENTS.md). Chaque niveau fournit sa justification. Quatre responsabilités, sept compétences disponibles, une copie de travail et un atelier qui fige le candidat complet. Un lot ne charge que les compétences utiles.

Le code ICO et ses données ne sont pas distribués. Les instructions et l’atelier sont ceux employés dans la réalisation privée. Le [cas fictif](fixtures/contract.json) permet d’exécuter publiquement le cycle sans le produit. Les [résultats et la comparaison](COMPARAISON.md) séparent ce qui a été observé sur ICO de cette démonstration. Voir le [périmètre de publication](PUBLICATION.md).

## Exécuter l’exemple

Python 3.10+ et environnement POSIX ; runtime Eiffel++ **0.6.0** de ce dépôt. Depuis la racine du dépôt, choisir des destinations nouvelles hors du dépôt de sources :

```sh
python3 -B examples/ico-0.6.0/demo.py --output "$SORTIE_NEUVE"
python3 -B examples/ico-0.6.0/N1/generate.py --mode import --output "$N0_IMPORT_NEUF"
python3 -B examples/ico-0.6.0/N1/generate.py --mode interface --output "$N0_INTERFACE_NEUF"
python3 -B tools/meta_harness.py check "$N0_IMPORT_NEUF"
python3 -B -m unittest discover -s tests -p test_ico_example.py -v
```

Le premier exemple améliore une fonction fictive, prépare six missions, consomme leurs remises, vérifie référence et candidat, puis sélectionne une copie complète. Il n’exécute aucun modèle. `ADOPT` désigne ici une sélection expérimentale sur des critères fictifs, sans adoption métier. Les autres commandes montrent que N1 retire une compétence inutile et conserve les capacités indisponibles.

Pour travailler sur son propre code, suivre [DEMARRER](N0/DEMARRER.md) : fournir un export propre, le contrat, le plan et un vérificateur autorisé. Garder les empreintes retournées séparément des dossiers qu’elles identifient. Un changement du besoin ou des contrôles ouvre un nouveau lot ; il ne suffit pas de recalculer l’empreinte.

## Ce que les mécanismes établissent

La référence, le contrat, le plan, les consignes, les compétences, les justifications et les dépendances du vérificateur sont liés au lot. Les candidats contiennent toute la copie de sources. Les critères de sortie doivent correspondre exactement au contrat. Égalité ou régression : référence conservée ; absence de résultat admissible : `INCONCLUSIVE`.

Les empreintes ne prouvent ni la pertinence d’un oracle, ni la compétence d’un modèle, ni l’indépendance des acteurs. Le même assistant a conçu et examiné cet exemple. Les processus locaux sont autorisés et bornés dans le temps ; le runtime public ne confine pas du code hostile. La campagne privée utilise en plus une garde macOS sans réseau et limitée à son dossier de sortie. Aucun compte ni identifiant de connexion n’est requis.

Les décisions de conception expliquent les compromis dans [N2](N2/DESIGN.md), [N1](N1/DESIGN.md) et [N0](N0/DESIGN.md). La bibliothèque `N1/blueprint` sert au générateur ; `N0` est la sortie livrée. Leur duplication rend chaque niveau utilisable séparément, au prix de fichiers supplémentaires.
