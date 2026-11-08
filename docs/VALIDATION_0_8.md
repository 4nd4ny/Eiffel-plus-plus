# Mémoire révisable — vérifications du 9 novembre 2026

Le mécanisme 0.8.0 a été exécuté localement. **149 tests du catalogue passent**, dont 33 tests de mémoire ; durée de la suite : 6,583 s. Le contrôle des documents, schémas, exemples et graines passe également. La première intégration avait détecté deux liens absents dans les copies autonomes ; leur correction conserve l'accès au prompt de révision sans supposer qu'il est embarqué avec chaque copie du protocole.

Les tests de mémoire couvrent conservation des exigences, échéances, portée, versions, dépendances, retrait définitif, contestation, provenance, identité déclarée, propositions séparées de l'application, ancre de remise et concurrence réelle entre deux processus. Une approbation globale ne permet pas à une proposition d'agent de fabriquer une source humaine/documentaire. L'exemple public est aussi exécuté ; les décisions de ces tests sont fictives.

## Application locale à ICO

Les quatre contrats documentaires existants ont servi de références, avec une contrainte explicite de répertoire. Chaque contexte conserve le contrat du lot et cette contrainte : cinq entrées d'exigence distinctes, dont deux applicables par lot. Trois reprises sur chacun des quatre lots donnent **12 contextes contrôlés et 24 présences d'exigences vérifiées**. Une observation valide reste également présente.

Sept notes sont écartées dans chaque contexte : un ancien constat réel devenu inapplicable et six perturbations synthétiques couvrant échéance, version, portée, retrait et deux niveaux de dérivation. Quatre témoins non filtrés échouent sur le même contrôleur. Les anciennes remises, l'omission d'un contrat, l'ajout d'historique et une tentative de retrait d'exigence sont refusés. Une exigence contestée bloque son lot sans être supprimée ; les autres lots restent accessibles.

**57 vérifications passent** dans cet essai déterministe, en 1,262 s pour son exécution finale. Ces vérifications comprennent des répétitions et ne constituent pas 57 scénarios indépendants. Les empreintes de 1 279 fichiers de référence sont inchangées ; l'ancien journal N0 reste clôturé dans son périmètre initial. La première exécution avait aussi passé ; la seconde utilise le contrôleur renforcé sur la provenance des propositions.

Le code ICO, les contrats complets, le magasin, les scénarios détaillés et les preuves restent privés dans 99. Eiffel. Ce document ne publie que le résultat agrégé autorisé ; il n'est pas une reproduction autonome de l'essai privé. L'[exemple fictif public](../examples/memory-0.8.0/README.md) et [les tests génériques](../tests/test_memory.py) permettent de reproduire les propriétés du contrôleur sans ICO.

## Ce qui est établi et ce qui reste à éprouver

Le consommateur ICO est un processus Python qui examine les messages préparés, **pas un LLM**. L'essai établit la sélection, la conservation et le refus de remises sur les cas connus. Il ne mesure ni l'obéissance d'un modèle, ni la qualité du code généré, ni la détection autonome des contradictions sémantiques. Aucun appel API de modèle n'a été effectué par cet essai ; les coûts de conception ne sont pas mesurés.

L'hôte doit encore imposer les identités et les droits, fournir les bonnes versions et transmettre la requête sans ancien historique. Un magasin partagé avec des droits d'écriture non contrôlés, un adaptateur réinjectant un résumé ancien ou une source correctement citée mais fausse restent hors garantie. Voir le [contrat et les limites d'exécution](../protocol/MEMORY.md).
