# Conserver l'expérience sans publier le projet

Git conserve l'histoire des versions ; les décisions expliquent ce qui a été retenu et pourquoi. Cette mémoire sert à reprendre le travail, contester une conclusion et améliorer une méthode. Elle ne demande ni transcription intégrale des conversations ni journal de raisonnement interne.

Depuis 0.8.0, le [contexte actif](../protocol/MEMORY.md) est reconstruit séparément de cette histoire. Une note retirée reste explicable sans être réinjectée ; la recherche normale applique sa validité actuelle. Une correction explicite invalide immédiatement les remises concernées. Les sources historiques et leurs droits restent conservés ; le prompt de consolidation prépare une proposition distincte de son application.

## Un historique utile au projet

Conserver dans un dépôt privé ou local, selon les droits du projet :

- le besoin et les critères applicables, avec leurs versions ;
- les instructions, rôles, skills, scripts et notes de conception de chaque niveau utilisé ;
- les observations, hypothèses, changements ou maintiens, preuves et limites de chaque itération utile ;
- les réponses humaines réellement reçues, leur portée, les décisions de passage et les inconnues restantes ;
- les échecs et décisions remplacées, reliés aux versions qui les rendent interprétables.

Réutiliser les documents existants. Une table de décisions et des références vers les résultats peuvent suffire ; ne pas créer un journal par rôle ou par appel de modèle. Les résultats volumineux peuvent rester dans un stockage contrôlé : conserver leur empreinte, leur emplacement autorisé et leur portée, sans prétendre qu'une référence inaccessible permet une reproduction publique.

Figer le candidat et les entrées avant l'essai. Le rapport identifie cette version ; un commit ultérieur peut enregistrer le rapport et la décision. Ne pas chercher à inclure dans un fichier le hash du commit qui le contient. Une correction de conclusion ajoute un lien vers la décision remplacée, au lieu de faire disparaître l'erreur historique.

Un commit constate un contenu, pas une acceptation. Un nom d'auteur ou un champ `decision_ref` n'authentifie pas la personne. L'accord humain doit correspondre au dossier effectivement présenté, selon le [contrat de passage](../protocol/CASCADE.md). L'autorisation de travailler ou de pousser des correctifs publics ne vaut pas validation métier des harnais générés.

## Vérifier une reprise par Git

En 0.7.0, le journal lie aussi les permissions complètes des pièces. Un essai synthétique a montré une limite : un journal dont les objets sont en lecture seule (`0444`) reste valide après le commit local, mais devient `STALE` après clone, qui les restitue en `0644`. Les contenus et la chaîne étaient identiques ; le témoin créé en `0644` restait valide. `core.fileMode=false` ne change pas la vérification d'Eiffel++.

Pour une histoire neuve destinée à Git, choisir des permissions compatibles avant d'enregistrer les cycles et vérifier une reprise réelle avant de revendiquer sa portabilité. Figer un candidat par une empreinte et un commit n'impose pas de rendre ses fichiers non modifiables au niveau du système.

Pour une histoire existante, garder l'ancre externe. Sur une copie dédiée, vérifier inventaire, contenus et identité de la chaîne avant de rétablir uniquement les permissions consignées, puis relancer `verify` avec cette même ancre. Ne pas réécrire les événements ou recalculer leurs empreintes pour effacer l'écart. La restauration ponctuelle a réussi dans l'essai ; aucun outil automatique de récupération n'est fourni. Un contenu différent reste une altération à examiner.

## Du projet à la communauté

La conservation privée et le partage public sont deux décisions différentes. Aucun générateur n'ajoute automatiquement un dépôt distant ni ne pousse des traces client.

Avant une contribution publique : sélectionner une recette, un harnais ou une leçon ; vérifier droits, licence et confidentialité ; retirer les éléments privés ; relire le contenu exact et obtenir l'autorisation qui le couvre. Préparer l'export dans une histoire distincte, sans reprendre les commits privés : supprimer un fichier dans le dernier commit ne le retire pas des commits précédents. Une anonymisation ou une reformulation ne garantit pas l'absence d'information confidentielle.

La contribution indique le contexte partageable, le problème, le changement, les observations disponibles, les limites, les contre-indications et les conditions de réemploi. Une preuve privée peut être signalée comme non publiable ; elle ne devient pas une preuve vérifiable par la communauté. Un extrait approuvé n'autorise pas la publication de sa source entière.

## De l'expérience à une nouvelle règle

Une expérience locale propose une amélioration ; elle ne l'impose pas au catalogue. Examiner si elle appartient à N0, N1 ou N2, puis éprouver ses effets sur des contextes pertinents, dont un cas qui pourrait l'invalider. Conserver la référence de départ comme option et mesurer aussi les régressions et le coût de la règle.

Une modification d'Eiffel++ suit le même processus : proposition sourcée, correctif, contrôles, revue, décision et version. Cette boucle permet d'améliorer le processus d'amélioration sans présenter une accumulation de textes ou de commits comme un progrès.

Les filiations conceptuelles sont recensées dans [REFERENCES.md](REFERENCES.md). Les [fiches de graines](https://github.com/4nd4ny/Eiffel-plus-plus/blob/main/seeds/README.md) restent le format de capture d'instances réutilisables ; ce guide explique leur histoire, pas un second catalogue.
