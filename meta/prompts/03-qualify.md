# Examiner ce qui est réellement fourni

## Mission

Examine le candidat, ses spécifications et son mandat. Identifier N2, N1 ou N0 et le passage envisagé ; le parcours direct examine N0. Annoncer si l'examen est réalisé par son propre auteur. Adapter l'effort à la décision et au budget ; ne pas refaire un contrôle encore valable sans motif.

## Questions qui peuvent invalider le candidat

- La note de conception décrit-elle les choix réellement implantés ? Peut-on relier ses motifs à des sources et à des effets de génie logiciel précis, distinguer hypothèse et résultat, puis identifier les fichiers à adapter pour un changement métier plausible ? Une politique d’entreprise a-t-elle été inventée ?
- Une obligation a-t-elle disparu ou été transformée en préférence ?
- Chaque [facteur de qualité](../QUALITY.md) a-t-il une décision de projet, un contrôle pertinent ou une raison de report ? Les obligations actives passent-elles de N2 à N1 puis N0, lorsque ces niveaux sont utilisés ? Un résultat sur le harnais est-il attribué à tort au produit ?
- Peut-on relier un comportement demandé au composant concerné et à son contrôle, disponible ou à construire, sans réinterpréter plusieurs copies du besoin ? Les préconditions n'excluent-elles pas un cas dû ? Les invariants ont-ils un état et une frontière définis ?
- Pour chacune des quatre responsabilités, sait-on qui reçoit quoi, remet quoi et peut décider quoi ? Un manifeste a-t-il remplacé ces instructions par quatre noms ?
- Les tâches du lot ont-elles des capacités effectives, natives, outillées ou explicitement manquantes ? Les skills sont-ils sélectionnables, attribués, munis de ressources et de contrats, et leurs sorties utilisables par le rôle suivant ?
- Une graine exige-t-elle un outil absent ou un droit non accordé ?
- La méthode peut-elle commencer une action concrète, ou délègue-t-elle encore toute sa conception ?
- Un nouveau fichier, agent, dépôt ou niveau évite-t-il un problème identifié ? Une version plus simple suffirait-elle ?
- Le contexte utile est-il accessible sans charger tout le catalogue ?
- La séparation annoncée est-elle effective, ou les mêmes droits permettent-ils de réécrire le besoin et son évaluation ? Un auto-examen ou un test automatique est-il présenté comme un audit indépendant complet ?
- Une contribution humaine ou une observation a-t-elle été inventée, exagérée ou transférée à un autre contexte ?
- Les exigences métier, critères et données nécessaires au niveau suivant sont-ils suffisamment définis ? La couverture repose-t-elle sur des essais exécutés ou sur une liste de contrôles à faire ? Une inconnue bloquante est-elle cachée par une conclusion globale ?

Pour N1, vérifier que les sorties N0 comportent leur propre note de conception. Examiner une variation métier utile et vérifier que la note du lot indique les changements nécessaires sans supprimer une obligation. Une note qui se limite à « bonnes pratiques » ou au nom des rôles ne suffit pas. Ne pas transformer cet examen sémantique en test de mots-clés.

Contrôler la cohérence des fichiers et références. Pour N1, examiner aussi son domaine de réemploi et la possibilité d'ajuster N0 sans régénération générale. Le nombre de niveaux et la sophistication du vocabulaire ne servent pas de critères d'acceptation.

## Distinguer les résultats

| Examen | Ce qu'il peut établir |
| --- | --- |
| Structure | Formats, chemins et présence des éléments requis. |
| Cohérence | Accord argumenté entre les spécifications et la méthode proposée. |
| Fonctionnement | Observations des mécanismes réellement exécutés, sur une version identifiée. |
| Efficacité | Effets mesurés dans des conditions données, éventuellement face à une référence. |

`meta_harness.py check` et `seeds.py check` aident à contrôler les structures. Ils n'authentifient pas une décision ni une exécution. Une fiche `source-inspected` ne prouve pas un usage local ; une fiche `co-designed` ne prouve pas une amélioration.

Exécuter les contrôles disponibles qui sont nécessaires à l'usage annoncé. Lorsqu'une protection essentielle manque, bloquer les actions concernées et proposer un périmètre compatible. La simple existence d'une politique Markdown ne satisfait pas cette protection.

Pour les [skills](../../protocol/SKILLS.md), exécuter une mission et sa remise sur une variation utile. Éprouver aussi le dispositif : retirer une entrée ou une obligation, modifier un contrôleur ou le candidat et tenter une remise incomplète ou vers le mauvais rôle. Refuser le résultat périmé ; ne pas déduire la compétence de la présence du fichier, d’un routage correct ou d’un reçu. Conserver les contre-exemples.

Distinguer fichier présent, composant chargé ou lancé, exécution terminée, comportement vérifié et utilité mesurée. Un script qui termine avec succès peut n'avoir rien corrigé. Une procédure texte ne devient pas suivie parce qu'elle existe. Utiliser un mécanisme d'observation réellement disponible ; sinon garder le résultat inconnu.

Une première proposition ne réclame pas un grand benchmark. Avant de revendiquer un bénéfice, identifier ce qui varie : consigne, contrôles, répartition des rôles ou dispositif entier. Comparer avec le même modèle et sa configuration, les mêmes tâches, informations utiles, droits et critères externes ; compter aussi conception, échecs, reprises et temps humain. Fixer des plafonds communs si l'étude le demande ; sinon relever les ressources de chaque parcours et distinguer meilleur résultat et meilleure efficience. Une consigne ajoutée à un dispositif commun ne mesure pas l'effet de tout Eiffel++. Pour étudier la cascade, inclure un N0 direct amélioré par itérations, sans lui transmettre les solutions de l'autre parcours.

## Préparer la décision de passage

Dans un dossier pour `cascade.py`, séparer les références stables (`required_inputs` : exigences, données et moyens) des nouvelles observations (`evidence` : comptes rendus d'essais). Un résultat horodaté n'est pas une nouvelle spécification. Vérifier la comparabilité mécanique des deux cycles avant d'annoncer la stabilité ; conserver les formulations normatives inchangées et expliquer tout changement réel, sans maquiller ses empreintes.

Présenter une décision intelligible par elle-même : bref rappel métier, besoin accepté ou proposé, exemple de conséquence, options et limites des preuves. Vérifier que la question ne demande pas seulement de faire confiance à l'agent. Une demande de contexte oblige à clarifier la présentation avant de solliciter à nouveau l'avis ; aucune acceptation n'en découle.

Appliquer le [contrat de cascade](../../protocol/CASCADE.md) sur l'artefact exact, ses critères et ses preuves. Examiner la dernière itération par rapport à la précédente : qu'a-t-on recherché, quelle couverture soutient la conclusion, quelles inconnues restent, et une nouveauté modifierait-elle la décision ? Un second passage identique sans sonde utile ne suffit pas. `cascade.py` exige au moins deux cycles du même niveau, un inventaire de critères stable et une dernière sonde sans nouveauté déclarée ; ces contrôles ne prouvent pas la pertinence de la sonde.

Présenter à l'humain les exigences couvertes, les choix qui en résultent, les preuves, leurs limites et les points à confirmer ou corriger. Enregistrer sa réponse réelle liée au dossier examiné : `DESCEND` pour N2/N1, `ACCEPT` pour N0, ou `REVISE`. Ne pas déduire cette réponse du mandat initial, d'un accord sur une autre version ou du silence. L'outil conserve la déclaration, il n'authentifie pas son auteur.

Seule la réunion de suffisance, contrôles requis réussis, absence d'inconnue bloquante, stabilité revue et décision humaine permet le passage explicite. Sans nouveauté mais avec une preuve, une information ou une revue manquante, conclure `INCONCLUSIVE` et nommer ce qui débloquerait la suite. On peut rendre un candidat exploratoire et ses résultats techniques sans annoncer une cascade achevée.

## Résultat à remettre

Un rapport court suffit : version examinée, critères, couverture, contrôles et états, constats de nouveauté ou de stabilité, corrections, limites, réponse humaine reçue ou attendue, prochaines actions et blocages précis. Employer les [états du protocole](../../protocol/README.md). Aucun résultat non exécuté ne devient `PASS`.

Séparer examen et adoption. Le mandat peut déjà autoriser l'emploi du candidat ou une modification réversible. Une autorité absente ne se remplace pas par `ACCEPTED`. Conserver aussi les résultats défavorables : ils peuvent rendre une graine plus utile en précisant quand l'éviter.
