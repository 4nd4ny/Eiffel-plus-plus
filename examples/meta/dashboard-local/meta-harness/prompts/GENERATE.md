# Générer la méthode du tableau de bord local

Statut de cet exemple : PROPOSED. Qualifications et performances : NOT_RUN.

Tu conçois le **harnais N0** permettant de réaliser le projet décrit dans `profile.json`. Tu reçois ce profil, `GENERATION_CONTRACT.md`, les besoins disponibles et un inventaire des capacités réellement accessibles. Produis des fichiers d'instructions utilisables par les futurs agents. Le profil situe les préférences ; il ne fournit pas à lui seul la méthode.

## Comprendre ce qui change la manière de travailler

Commence par les invariants du besoin : fichier local, données non sensibles, absence de réseau, valeurs préservées. Détermine quelles exigences peuvent être vérifiées automatiquement dans l'environnement disponible et quelles observations réclament une interaction humaine.

Les doublons d'id et quantités manquantes sont des questions métier. Regroupe-les si elles empêchent une décision utile ; continue les parties indépendantes. N'invente pas une réponse du PO. Le choix d'une bibliothèque ou de l'organisation des fichiers peut rester autonome dans le mandat.

Vérifie le navigateur et les moyens d'exécuter les tests avant de les imposer au producteur. Si une capacité manque, cherche une réalisation locale plus simple ou explicite la limite. Une commande plausible n'est pas un outil vérifié.

## Synthétiser une méthode proportionnée

À partir de ces observations, rédige les règles du futur harnais :

- Choisis le lot minimal qui produit une fonction utilisable et observable, puis les conditions d'ajout des options.
- Définis un circuit court entre exigence, candidat et contre-exemple. Un producteur peut suffire ; l'indépendance du contrôle doit être réalisée par les droits et l'exécuteur appropriés.
- Place dans le contexte initial seulement le mandat, les contrats du lot, l'index des sources et le diagnostic courant. Ouvre le reste à la demande.
- Déduis les cas de vérification du comportement du CSV et du besoin. Prévois la fidélité des données, l'absence de transfert et le diagnostic d'entrée invalide.
- Définis les décisions techniques autorisées, les questions réellement bloquantes et la manière de les regrouper.
- Choisis ce qui mérite une mémoire. Pour ce besoin bref, une note de reprise et les décisions canoniques peuvent suffire ; justifie tout mécanisme supplémentaire par son réemploi attendu.

Lis les poids du profil courant et leur source. Le profil illustré privilégie vitesse et économie ; un profil révisé peut justifier une autre organisation. Si l'attention humaine devient la contrainte principale, examine une automatisation supplémentaire du diagnostic et de la reprise. Si la valeur des fonctions optionnelles augmente, redéfinis les lots et leurs contrôles. Ni l'un ni l'autre n'autorise à omettre le traitement local ou la fidélité des données. Les cibles chiffrées restent des préférences, pas des observations.

Tu peux synthétiser une seule organisation si elle convient. Un autre candidat est utile seulement si une incertitude importante oppose des méthodes réellement différentes. Lis les limites dans generation_budget : max_candidates, max_iterations et max_tokens lorsqu'il est renseigné. N'ajoute pas un benchmark complet à cette génération par défaut.

## Émettre N0

Écris `harness.json`, une copie du `profile.json` utilisé, puis les dossiers `governance/`, `stbl/`, `audit/` et `product/`, avec chacun `AGENTS.md` et `README.md`.

Dans ces fichiers, rends explicites :

1. les instructions propres au rôle et à ce projet ;
2. les entrées nécessaires, sorties, conditions d'arrêt et droits ;
3. les critères qui établissent un résultat exploitable ;
4. la justification des règles par le besoin ou une capacité observée ;
5. les inconnues, la qualification restante et les conditions de révision.

Évite les instructions sans effet sur une décision. Ne recopie pas tout ce méta-harnais dans les quatre contextes.

Le manifeste respecte le contrat N0 Eiffel++ 0.2.0 : niveau 0, quatre dépôts, profil identifié et référence textuelle à ce N1. Conserve `PROPOSED` sauf décision authentifiable applicable ; aucune opération structurelle ne crée une acceptation. Les contrôles non exécutés restent `NOT_RUN`.

## CHECK — qualifier le harnais avant remise

Relis le harnais comme un agent qui dispose seulement de son point d'entrée. Peut-il réaliser un lot, obtenir les sources utiles, comprendre un échec et reprendre sans solliciter l'humain pour une décision déjà déléguée ? Une demande de vitesse a-t-elle conduit à cacher une exigence ?

Fournis une courte liste des obligations de déploiement encore non réalisées. Vérifie également une variation du profil : tes règles changent-elles lorsque l'arbitrage ou les capacités le justifient ? Si elles restent identiques, justifie cette stabilité par les obligations du besoin. Toute adaptation ultérieure repasse par `ADAPT.md` à partir de faits nouveaux.
