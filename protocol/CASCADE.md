# Cascade et boucles d'amélioration

Ce parcours spécifie progressivement **N2 : principes → N1 : méthode → N0 : harnais utilisable**. Chaque niveau contient sa propre boucle IA + essais + humain. Descendre est une décision sur une version qualifiée, pas le simple fait de produire un fichier. Le parcours **N0 direct, amélioré par itérations** reste disponible et sert de comparateur.

La cascade est utile lorsque séparer les principes, les choix réemployables et les instructions d'exécution permet de localiser les corrections. Ce bénéfice reste une hypothèse à mesurer. Un niveau qui ne porte aucune décision distincte peut être omis dans le parcours direct ; le nombre de niveaux n'est pas un critère de qualité.

## Ce que chaque niveau doit résoudre

| Niveau examiné | Question avant de poursuivre | Remise |
| --- | --- | --- |
| N2 — principes | Comprend-on le besoin métier, les obligations, les droits et les qualités à préserver pour choisir une méthode ? | Références, exigences, critères de suffisance et principes applicables à N1. |
| N1 — méthode | La méthode précise-t-elle les tâches, responsabilités, capacités, informations et contrôles nécessaires pour fabriquer N0 ? | GENERATE/CHECK/ADAPT, contrats de sortie, rôles, skills utiles et règles d'adaptation. |
| N0 — usage | Les instructions permettent-elles de réaliser le lot autorisé, de contrôler les remises et de traiter les échecs ? | Harnais, scripts et skills exécutables dans le contexte, avec preuves situées et limites. |

À chaque niveau, livrer les instructions, scripts éventuels et [justification de conception](DESIGN.md) dans la même version. Préciser ce qui est établi, supposé ou encore absent. N2 ne peut pas inventer une politique d'entreprise ; N1 ne peut pas promettre une capacité indisponible ; N0 ne peut pas transformer un test de structure en validation du produit.

## Boucle au sein d'un niveau

1. **Fixer l'examen.** Identifier les exigences applicables, leurs sources, les critères de suffisance, les situations et contre-exemples à examiner, les moyens disponibles et la personne compétente pour la décision. Définir ce qui constituerait une nouveauté pertinente avant de regarder le dernier résultat.
2. **Éprouver une version.** Utiliser un cas réel autorisé ou une sonde isolée du niveau suivant. Conserver l'artefact, les entrées, les contrôles et les résultats réellement obtenus. Une sonde ne vaut pas autorisation de descendre.
3. **Analyser avec l'humain.** Distinguer observation et explication ; montrer les conséquences métier et poser les questions dont la réponse changerait la méthode. L'humain peut corriger l'exigence, donner un contre-exemple ou confirmer la suffisance du périmètre présenté.
4. **Réviser et vérifier.** Formuler une hypothèse, faire le plus petit changement utile, reprendre les contrôles touchés et comparer à la version précédente. Mettre à jour les motifs affectés ; conserver aussi les régressions et les résultats sans différence.

Cette boucle s'inspire de l'apprentissage expérientiel de Kolb ; elle n'est ni une équivalence entre cognition humaine et LLM ni une preuve de convergence. Une répétition du même essai sans nouvelle couverture n'est pas une confirmation indépendante.

Chaque passage conserve un dossier court : **observation → hypothèse → changement ou maintien → preuves → décision humaine → justification et suite**. Les références vers les fichiers et résultats suffisent ; ne pas transcrire une chaîne de pensée interne. Le [guide d'historique](../docs/HISTORY.md) explique sa conservation dans Git.

## Contrat de passage

Le dossier de passage lie les éléments suivants à une version identifiable. Les champs des outils sont décrits dans leur guide ; ce tableau exprime les obligations, pas un format JSON concurrent.

| Élément | Condition à examiner |
| --- | --- |
| Artefact et parent | Révision Git réelle ou instantané immuable, chemins et empreintes ; pour N1/N0, référence de la version supérieure ayant autorisé la descente. |
| Besoin et critères | Exigences métier et de méthode applicables, sources et décisions ; critères définis avant la conclusion, changements explicitement autorisés. |
| Couverture | Pour chaque critère, preuve et état du contrôle exécuté ; cas limites pertinents et limites de portée. Un contrôle prévu reste `NOT_RUN`. |
| Informations et capacités | Données, outils, compétences et droits requis pour le niveau suivant disponibles ; inconnues et conséquences conservées. Aucune inconnue bloquante ne peut être masquée par un score global. |
| Stabilité | Dernière revue comparée aux observations précédentes : ce qui a été recherché, couverture ajoutée ou réexaminée et absence de nouveauté qui changerait la décision. |
| Revue humaine | Réponse effective, auteur compétent, portée et référence de la décision, liée aux empreintes de l'artefact, des critères et du dossier examiné. Le mandat de concevoir ne vaut pas acceptation du candidat. |

La descente exige ensemble : **suffisance étayée + contrôles requis réussis + absence d'inconnue bloquante + stabilité revue + accord humain portant sur ce dossier**. L'accord peut être recueilli en une seule revue de plusieurs exigences ; il n'impose pas une confirmation de chaque fichier. Une délégation déjà donnée autorise les actions qu'elle couvre, mais ne fournit pas une réponse future à une question métier encore ouverte.

**Rendre la revue compréhensible sans retrouver toute la conversation.** Rappeler le but du produit, ses utilisateurs et les exigences métier sources. Expliquer le choix à faire avec un exemple d'usage, ses conséquences, les alternatives et ce que les tests permettront réellement de conclure. Distinguer correction d'un besoin accepté et renforcement proposé. Donner les liens pour approfondir, sans faire de leur lecture la condition implicite pour comprendre la question. Une demande de contexte supplémentaire appelle une meilleure présentation et garde la porte ouverte ; elle n'est ni un accord ni un rejet du besoin. Ce dossier doit rester proportionné à la décision.

Le dernier constat « rien de nouveau » est recevable seulement si les critères prévus ont été couverts, si les inconnues ont été examinées et si une revue humaine réelle confirme la suffisance de cette version. Il ne signifie ni certitude absolue ni épuisement de toutes les améliorations possibles. **Le silence humain, une réponse générique, un budget épuisé ou deux textes identiques ne ferment pas le passage.**

### Contrôle du dossier

`tools/cascade.py` matérialise ce passage : `start` choisit `cascade` ou `direct` ; `cycle` copie un dossier contenant `cycle.json`, les artefacts et les preuves ; `review` lie une réponse humaine à l'empreinte du cycle. `gate` examine l'état sans descendre ; `advance` effectue la descente ou la clôture seulement si le passage est satisfait. `reopen` rouvre un niveau et invalide ses descendants. Le [guide des outils](https://github.com/4nd4ny/Eiffel-plus-plus/blob/main/tools/README.md) précise les commandes.

Le cycle contient le niveau et son but, les états des critères, les chemins de preuves, la couverture exigences/critères, les entrées requises avec leurs sources, les inconnues bloquantes, l'observation, l'hypothèse, le changement, les nouveautés, la sonde de stabilité et les limites. Une entrée exclue doit avoir une justification consultable ; `EXCLUDED` ne permet pas de supprimer arbitrairement une obligation.

Le contrôle requiert au moins deux cycles au même niveau, un inventaire de critères inchangé, tous les critères à `PASS`, aucune entrée requise `MISSING` ni inconnue bloquante, puis une dernière liste de nouveautés vide et une sonde de stabilité renseignée. La revue porte sur ce dernier cycle : `DESCEND` pour N2/N1, `ACCEPT` pour N0, ou `REVISE` pour reprendre le travail. Le journal conserve les empreintes et l'ordre des événements. Ces conditions mécaniques ne vérifient pas à elles seules la sincérité des déclarations, la qualité des preuves ou l'exhaustivité des exigences métier.

| Situation | Suite |
| --- | --- |
| Une observation, un essai ou l'humain révèle une correction utile | Réviser au niveau qui possède la décision ; reprendre les contrôles affectés. |
| Aucune nouveauté, mais besoin incomplet, preuve manquante ou revue absente | `INCONCLUSIVE` : consigner l'impasse et l'information nécessaire ; continuer seulement les travaux indépendants autorisés. |
| Un critère obligatoire échoue | Conserver `FAIL` et corriger ou faire réexaminer le besoin par son autorité ; pas de descente. |
| Tous les éléments du passage sont réunis | Autoriser la descente N2→N1 ou N1→N0 ; à N0, clore la qualification pour le périmètre examiné. |

L'avis d'audit emploie les [états du protocole](README.md). Une acceptation de risque ou un avis avec réserves ne transforme pas un contrôle en `PASS`. Le succès du vérificateur de dossier établit sa cohérence mécanique ; il ne prouve ni l'identité du signataire ni la vérité de l'avis métier. La clôture réclame les preuves **et** la décision humaine.

Un changement d'artefact, de critères ou de dépendance rend les preuves et décisions touchées périmées. Ne pas recalculer une empreinte pour faire apparaître une ancienne approbation comme nouvelle. Si N0 révèle une erreur de principe, rouvrir N2 ou N1 et réexaminer les descendants concernés. La cascade ordonne la descente, elle n'interdit pas ce retour.

## Comparer les deux parcours

Pour comparer cascade et N0 direct, fixer le même modèle et sa configuration, les mêmes tâches, sources disponibles, droits et critères externes. Séparer les travaux et ne pas donner au second candidat les réponses du premier. Les deux parcours bénéficient d'essais et d'une revue humaine ; consigner les questions, réponses et différences d'exposition réellement reçues.

Le budget peut être identique ou libre selon la question étudiée. Sans plafond commun, rapporter le coût total et les ressources de chaque parcours ; un meilleur score après davantage de travail ne démontre pas une meilleure efficience. Compter conception, génération, essais, corrections, temps écoulé et attention humaine. Une mesure inaccessible reste inconnue. Distinguer contrôles du harnais, qualité du code produit et adéquation métier ; réserver si possible des tâches à l'évaluation finale.

Sans revue humaine des versions produites, on peut comparer des candidats exploratoires et leurs contrôles techniques, mais pas annoncer une cascade hybride achevée. Le succès sur un projet ne prouve pas la supériorité générale des trois niveaux.

## Améliorer Eiffel++ avec ses propres résultats

Une observation N0 peut suggérer une règle N1 ; plusieurs contextes peuvent motiver une révision N2. À chaque remontée, conserver provenance, contre-exemples et limites, puis réévaluer le transfert. La répétition d'une préférence ne la transforme pas en obligation universelle.

Appliquer la même boucle à Eiffel++ : besoin de méthode → changement de prompt ou d'outil → essais → revue humaine → décision versionnée. L'acceptation d'un correctif Eiffel++ ne valide pas automatiquement les harnais qu'il générera.

La mémoire de projet reste privée par défaut. Une contribution publique est un artefact distinct, sélectionné, relu et explicitement autorisé ; elle n'embarque pas automatiquement le dépôt, les échanges, données ou résultats du client. Voir [HISTORY.md](../docs/HISTORY.md).
