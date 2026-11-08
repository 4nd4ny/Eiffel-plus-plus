# Vérifications d'Eiffel++ 0.3.0

Complément du 8 novembre 2026 : la [comparaison locale cascade/direct](../history/eiffel-0.7.0/APPLICATION-ICO.md) rapporte seize réalisations sur un périmètre borné. Le rapport daté ci-dessous conserve son périmètre historique ; cette observation ne valide pas la méthode en production.

Date : **6 novembre 2026**. Périmètre : documents du catalogue, formats JSON, outils locaux, exemples et base de graines. **La méthode reste un prototype non évalué sur la production de logiciels réels.**

## Résultats exécutés

| Contrôle | Résultat observé | Portée |
| --- | --- | --- |
| `python3 tools/check_catalog.py` | **PASS**, 97 fichiers Markdown | Liens locaux, blocs de code, sections, variables, schémas lisibles, paquets illustratifs et graines publiques. |
| `python3 -m unittest discover -s tests -v` | **PASS**, 27 tests | Sept tests des composants génériques, treize tests de préparation/matérialisation et sept tests de graines. |
| Catalogue public | **PASS**, 9 fiches | Huit recettes externes, dont les deux recettes ICO autorisées à la publication, et un exemple local ; aucune observation de production déclarée. |
| Parcours CLI de `forge-local` | **PASS** | Contrôle N0, matérialisation avec un seul Git, aucun remote, conservation des trois fichiers de travail, absence de copie automatique de N2. |
| Préparation avec deux graines | **PASS** | Deux fiches sélectionnées copiées, aucun artefact de graine chargé, liens locaux du paquet exporté valides. |
| Capture de `forge-local` puis contrôle | **PASS** | Empreinte vérifiée ; statuts `unreviewed` et `illustrative`, observations vides, inchangés. |
| Séparation public/privé | **PASS dans les cas testés** | Catalogue privé explicite lisible, rejet de ses déclarations privées sous contrôle public. Aucun détecteur de secrets n'est revendiqué. |
| Relecture indépendante des nouveaux chemins de copie | Aucun blocage établi dans le périmètre relu | Revue par un autre agent, sans mesure d'indépendance statistique ni certification. |

Les essais de matérialisation, de préparation et de capture ont utilisé des destinations temporaires nouvelles. Le logiciel CSV de l'exemple n'a pas été implémenté ; ses contrôles métier restent `NOT_RUN`.

## Frontières couvertes par les tests

- Les profils 0.3.0 acceptent des priorités verbales ; les poids restent vérifiés lorsqu'ils sont fournis. Les anciens profils 0.2.0 gardent leurs exigences.
- Une responsabilité n'impose pas un dépôt : le mode `single-repo` regroupe les quatre responsabilités, le mode `four-repos` conserve quatre racines distinctes.
- Les scripts copiés restent exécutables. Les permissions ordinaires sont conservées, les bits spéciaux supprimés.
- Les destinations préexistantes, les chemins sortants, les recouvrements et les liens symboliques sont refusés dans les cas examinés. Une course simulée à la création ne provoque pas d'écrasement.
- Une capture conserve les déclarations, vérifie l'identité du paquet et détecte un changement des octets ou du caractère exécutable. Son empreinte est portable avec Git et ne couvre pas toutes les permissions.
- Une co-construction déclarée exige une référence de décision ; une observation ou comparaison exige une référence de résultat. Leur existence dans la fiche ne les authentifie pas.
- Une recette publique peut conserver une provenance privée. La préparation respecte le statut du contenu sélectionné, conserve la provenance et ne publie pas automatiquement le brief ou le profil.
- La sélection à l'étape zéro copie uniquement les fiches demandées. Les sources externes ne sont pas téléchargées, exécutées ou investies d'une autorité.
- Les références de générateurs restent descriptives ; un instantané N1 doit être fourni explicitement et partager le profil de N0.
- Structure, adoption, autorité et résultats restent distincts. Les outils n'élèvent aucun statut par le seul succès d'une copie.

## Hypothèses encore ouvertes

Réutiliser une graine pourrait réduire l'effort de conception ; cela pourrait aussi importer des hypothèses inutiles. La co-construction pourrait améliorer l'adéquation au besoin ; elle peut également ajouter du temps humain. Une mémoire d'instances pourrait faciliter les prochains projets ; elle peut accumuler des habitudes devenues inadaptées.

Ces possibilités ne sont pas départagées par les tests ci-dessus. Aucune réduction de coût, accélération, qualité supérieure, autonomie accrue ou généralisation interprojets n'est mesurée. Les graines externes correspondent à des sources inspectées ; leur adaptation Eiffel++ n'a pas été exécutée sur un corpus de tâches. L'exemple local reste une illustration, sans adoption humaine inventée.

La prochaine observation utile vient d'un lot réel : retenir une graine, noter les adaptations de l'opérateur, exécuter le travail, enregistrer les résultats et les difficultés. Une affirmation comparative demandera une référence de comparaison et des conditions consultables. Le format de capture permet cette collecte ; il ne produit pas à lui seul les résultats.

## Reproduire et situer cette version

Les commandes de contrôle figurent ci-dessus. Le [démarrage](QUICKSTART.md) et le [guide des outils](../tools/README.md) décrivent les parcours exécutables. Python 3.10 ou plus récent suffit ; Git est requis pour `--git-init`.

Le commit contenant ce document identifie les fichiers livrés sans inscrire son propre identifiant. Le [rapport 0.2.0](https://github.com/4nd4ny/Eiffel-plus-plus/blob/v0.2.0/docs/VALIDATION.md) reste dans l'historique avec ses 16 tests ; il ne décrit pas les choix de la version courante.
