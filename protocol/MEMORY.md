# Réviser la mémoire et reconstruire le contexte — 0.8.0

Une mémoire conserve des informations ; son chargement ne leur donne aucune autorité supplémentaire. L'oubli opérationnel consiste à retirer une consigne de l'usage courant tout en conservant son origine et la décision qui explique son retrait. Une exigence applicable ne disparaît pas parce qu'elle est ancienne ou rarement consultée.

## Contrat

- **Entrées de l'hôte :** identité de l'acteur, sources, tâche courante, portée, versions pertinentes (`bindings`) et heure fiable. Les références déclarées ne prouvent ni l'identité d'un humain ni la vérité d'une proposition.
- **Mémoire :** sources conservées et notes de nature `requirement`, `observation`, `hypothesis` ou `choice`. Une note cite exactement sa source ; une interprétation nouvelle possède sa propre source d'agent. Elle garde sa portée, ses dépendances et ses conditions de réexamen. Hypothèses et choix exigent une échéance ou une version de référence.
- **Révision :** une proposition est distincte de son application. Chaque application conserve son proposant, son exécutant déclaré, ses opérations, son motif et ses empreintes. Une note n'est pas réécrite : retirer puis créer une nouvelle note. Un identifiant retiré ne se réactive jamais.
- **Sélection :** toutes les exigences applicables sont conservées. Une hypothèse expirée, une note retirée, contestée, hors portée, liée à une ancienne version ou dépendante d'une note invalide est exclue. Une exigence contestée ou devenue incertaine bloque le contexte concerné ; elle n'est pas discrètement effacée. Son retrait exige une décision de son mainteneur, avec une source humaine ou documentaire.
- **Remise :** reconstruire le contexte, conserver son empreinte hors du paquet remis, puis le revérifier juste avant l'appel. Une exigence manquante, une mémoire modifiée, une échéance atteinte ou un historique ajouté invalide la remise.

La répétition, la fréquence de consultation, une synthèse et la descente N2 → N1 → N0 ne changent pas la nature d'une note. Les notes dérivées référencent leurs parents. Une exigence ne peut dépendre d'une hypothèse. Un résultat de test favorable ne transforme pas une hypothèse en besoin métier.

## Mécanisme disponible

Le module [memory.py](https://github.com/4nd4ny/Eiffel-plus-plus/blob/main/tools/memory.py) fournit `init`, `propose`, `apply`, `inspect`, `select`, `recall`, `prepare` et `launch_request` (commande `request`). Python standard, macOS/Linux, aucun service externe ni appel de modèle. L'[exemple exécutable](https://github.com/4nd4ny/Eiffel-plus-plus/tree/main/examples/memory-0.8.0) illustre l'usage avec des sources fictives.

Le magasin garde un journal dans `ledger.json`. Les transitions sont rejouées et contrôlées à la lecture ; une ancre de révision extérieure permet de détecter un retour à une ancienne version. Un verrou `flock` englobe la comparaison de révision et le remplacement atomique du fichier : deux écritures fondées sur la même version ne peuvent réussir toutes deux. Le verrou reste un fichier stable, sans verrou actif après fermeture du processus. Git conserve les étapes du travail, sans rendre une affirmation vraie.

`prepare` crée un nouveau paquet avec `request.json`, `CONTEXT.md` et `receipt.json`. Le reçu indique les exigences et les exclusions par identifiant, sans recopier les consignes écartées. `launch_request` reconstruit les attentes depuis le magasin courant et retourne deux messages neufs. `recall` applique le même filtre : retrouver l'identifiant d'une ancienne consigne ne réactive pas son contenu.

L'hôte transmet seulement la requête retournée, avec ses instructions système réellement applicables. Il ne rajoute ni ancien fil, ni résumé opaque, ni magasin brut. Les modèles ne reçoivent pas le journal de mémoire comme instructions. Les archives nécessaires à une enquête sont des pièces historiques traitées séparément ; leur contenu n'est pas automatiquement chargé dans le prochain contexte.

## Frontière d'exécution

La gouvernance configure l'hôte, les identités et les reprises. STBL conserve les sources du besoin et porte les arbitrages d'exigences. Le produit écrit ses observations et hypothèses dans son mandat. L'audit examine les propositions, les exigences perdues et les textes réellement remis. Ces responsabilités peuvent être cumulées, avec cette limite déclarée ; aucun nouvel agent obligatoire n'est ajouté.

Les mainteneurs déclarés peuvent enregistrer des sources humaines/documentaires et arbitrer les exigences. Les rédacteurs peuvent conserver leurs observations, hypothèses et choix, retirer leurs propres notes et contester une note. Ils peuvent proposer une modification plus large, mais pas l'appliquer au-delà de ces droits. Les changements métier suivent l'autorité existante ; aucune revue humaine supplémentaire n'est imposée pour une opération déjà déléguée.

Une proposition rédigée par un agent ne peut enregistrer une nouvelle source `human` ou `document`, même si un mainteneur accepte globalement cette proposition. L'hôte doit enregistrer séparément la source réellement reçue ; une adoption conserve l'origine de ce qui a été proposé. L'identité du proposant, comme celle de l'exécutant, doit être imposée par l'hôte.

**Le CLI ne constitue pas une authentification ni une séparation de droits système.** L'hôte doit imposer l'identité, garder magasin, politique et ancres hors de l'écriture des exécutants, et exposer seulement les opérations autorisées. Une personne pouvant éditer le magasin et remplacer son ancre peut fabriquer une autre histoire. Une politique Markdown ne remplace pas cette frontière. Les fichiers locaux et `flock` ne promettent pas de concurrence distribuée entre machines synchronisées par cloud.

Les versions et la portée doivent venir de l'état réellement applicable, pas d'un choix du réalisateur pour éviter un contrôle. Les conditions métier ne sont pas déduites automatiquement de la prose. Un texte source exact peut encore être faux ou malveillant ; sa conformité lexicale ne démontre pas son sens ni son autorité. Les copies sans dépendance déclarée et les contradictions sémantiques non signalées demandent une revue.

Retirer un fichier n'efface pas un texte déjà envoyé à un fournisseur de modèle. Le contrôleur produit une requête neuve ; l'adaptateur doit réellement démarrer sans l'ancien historique. Une tâche en cours n'est pas annulée automatiquement par une modification ultérieure du magasin : revalider aux reprises et avant les actions qui en dépendent. Aucun effacement interne au modèle, ordonnanceur, service de « rêve » ou adaptateur fournisseur n'est fourni.

## Consolidation et niveaux

Le [prompt de révision](https://github.com/4nd4ny/Eiffel-plus-plus/blob/main/meta/prompts/05-revise-memory.md) examine un lot borné de sources et prépare des propositions sans les appliquer. Une correction explicite est traitée immédiatement ; elle n'attend pas une consolidation périodique. La fréquence sert à prioriser, jamais à voter la vérité. Chaque copie d'une même erreur garde la même origine.

N2 conserve ces invariants. N1 précise les sources, portées, versions, acteurs et moyens de reprise disponibles dans le projet. N0 donne la commande de préparation et de revalidation de son contexte, ainsi que la limite de l'adaptateur réellement utilisé. L'absence de contrôle effectif de l'historique reste une capacité manquante ; une promesse d'oubli dans un prompt ne la remplace pas.

Éprouver au minimum retrait, échéance, changement de portée/version, propagation aux descendants, maintien d'une exigence rarement utilisée, contestation d'une exigence, refus d'une ancienne remise et conflit d'écriture. Distinguer ces contrôles du comportement d'un LLM et de la qualité du produit réalisé.
