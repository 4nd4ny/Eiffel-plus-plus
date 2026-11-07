# Capacités et remises — 0.5.0

Un rôle porte une responsabilité et des décisions. Une capacité décrit le travail qu'il doit savoir accomplir. Un skill fournit une méthode réutilisable pour une capacité précise. Aucun de ces éléments n'accorde de permissions ni ne prouve une compétence acquise.

## Transmission N2 → N1 → N0

N2 part des opérations du projet : cadrer un lot, concevoir une interface, reproduire un défaut, qualifier un contrôle, examiner un candidat. Il associe chaque opération à une responsabilité et détermine le moyen nécessaire. Un intitulé tel que « expert backend » ne précise ni opération ni résultat.

N1, lorsqu'il est utile, conserve les méthodes réutilisables, leurs conditions d'emploi et la façon de les adapter au lot. Ses fonctions GENERATE, CHECK et ADAPT sélectionnent, éprouvent et révisent ces capacités. Il contient les skills réellement réemployables, pas des fichiers vides à compléter dans N0. Une compétence métier non disponible reste signalée.

N0 attribue les tâches du lot et contient les skills choisis avec leurs ressources locales. Un rôle peut utiliser plusieurs skills ; plusieurs rôles peuvent partager un skill sans partager leurs droits. Aucun skill par rôle n'est imposé. Une capacité native suffit lorsque les instructions existantes donnent déjà une méthode adaptée ; sa justification référence cette méthode. Une méthode encore à écrire reste indisponible.

## Déclaration dans les manifestes N1 et N0

En 0.5.0, `capabilities` couvre les quatre responsabilités. Chaque entrée contient `role`, `task` et exactement un moyen :

- `skill` : identifiant d'un composant `kind: skill` présent dans le paquet ;
- `native` : méthode déjà disponible et raison pour laquelle une compétence supplémentaire est inutile ;
- `unavailable` : moyen manquant et conséquence sur le travail possible.

Les tâches sont celles du périmètre annoncé. CHECK examine leur couverture du besoin ; le programme contrôle références et formes, pas l'exhaustivité métier. Les paquets historiques restent lisibles sous leurs versions. Réviser un paquet en 0.5.0 exige un examen explicite des capacités, pas l'ajout automatique de quatre descriptions génériques.

Un composant `skill` réemploie `id`, `path`, `trigger`, `inputs`, `outputs`, `dependencies`, `limitations`. Il ajoute `handoff_to`, liste des responsabilités destinataires possibles. Les entrées et sorties sont des ports nommés, par exemple `candidate` ou `report`, liés à des fichiers lors d'une mission. Les ressources nécessaires à la méthode, y compris contrat et contrôles, figurent dans `dependencies`. Le contrôleur ne déduit pas les imports d'un script ni les dépendances d'une phrase.

Le fichier `<id>/SKILL.md` comporte un en-tête `name` et `description`, puis une méthode : déclencheur, préconditions, postconditions, effets autorisés, invariants pertinents, erreurs/arrêt et remise attendue. Aucun découpage fixe de rubriques n'est exigé. Référencer le besoin au lieu de le recopier. Joindre un script quand une opération déterministe gagne à être exécutée de façon reproductible.

Cette organisation suit le [format Agent Skills](https://agentskills.io/specification). Le lecteur Python Eiffel++ prend en charge `name` et `description` monolignes, en texte YAML simple ou chaîne JSON entre guillemets ; il ne prétend pas implémenter tout YAML ni configurer la découverte automatique d'un hôte. Un skill existant avec un en-tête plus complexe demande une adaptation explicite de ces deux champs. Les métadonnées additionnelles ne donnent aucun droit à l'outil.

## Orchestration locale disponible

`tools/skills.py` fournit quatre opérations sans appeler de modèle ni lancer le code d'un skill :

1. `list` montre les capacités d'un rôle et les noms, descriptions et déclencheurs utiles, sans injecter tous les corps de skills.
2. `prepare` vérifie l'attribution du skill au rôle et la présence exacte des entrées. Il prépare une mission avec les seules instructions et ressources déclarées, et copie les entrées. Il renvoie `order_sha256` : le coordinateur conserve cette référence hors de l'espace de travail du producteur lorsque la séparation est requise.
3. `verify --order-sha256 SHA` compare mission, contrôles, plan de capacités et entrées aux octets figés. Un changement produit `STALE`. Le coordinateur utilise la référence conservée lors de la préparation, jamais une empreinte recalculée pour faire accepter un changement.
4. `handoff --order-sha256 SHA` refuse une mission périmée, un mauvais destinataire ou des sorties absentes/surnuméraires. Il conserve les pièces pour le destinataire ; `semantic_status` reste `NOT_RUN`.

Ces commandes utilisent le paquet N0 source. Les sorties de `materialize`, contenant les métadonnées réservées `_eiffel`, ne sont pas directement des entrées de ces outils ; conserver le paquet source identifié. Les quatre racines d'un paquet `four-repos` peuvent être examinées ensemble avant matérialisation. Une mission regroupe les seules ressources nécessaires sans installer de droits distants.

Les scripts ou agents effectuent ensuite le travail sous le mandat existant. Le destinataire contrôle les postconditions avant d'accepter la remise. Une sortie JSON contenant le mot PASS ne constitue pas automatiquement une preuve ; les reçus mécaniques et l'évaluation sémantique restent distincts. Les reprises conservent le budget du lot. Le coordinateur ne parallélise que les tâches aux écritures disjointes et aux entrées disponibles ; aucun ordonnanceur ou agent fictif n'est lancé par ce protocole.

La protection repose sur la référence de mission conservée par l'appelant et sur la déclaration complète des dépendances. Elle détecte les altérations examinées ; elle n'authentifie pas une personne et n'empêche pas un acteur ayant tous les droits de réécrire simultanément les références de confiance. Le confinement et l'indépendance, s'ils sont requis, restent à mettre en place.

## Qualification utile

Tester un chemin normal et une variation de lot. Puis chercher les omissions : compétence absente, entrée manquante, mauvais destinataire, sortie incomplète, contrôle altéré, obligation retirée, candidat modifié après préparation. Vérifier qu'une dépendance indisponible ne devient pas PASS. Préserver la qualification des contrôles et la sélection d'une référence valide lorsqu'une décision de livraison les exige ; un skill ne les remplace pas.

L'exemple [CSV avec remises](https://github.com/4nd4ny/Eiffel-plus-plus/tree/main/examples/skill-handoff) exerce deux compétences et une remise Produit → Audit → Gouvernance. Les tests portent sur ce mécanisme local et ces opérations déterministes ; ils ne démontrent ni une orchestration autonome de plusieurs LLM ni un gain de qualité du code qu'ils écriraient.
