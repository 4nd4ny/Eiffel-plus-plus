# Passer des documents à un harnais effectif

Ce guide décrit les mécanismes à installer. Leur présence dans le catalogue ne signifie pas qu'ils sont activés sur un compte ou un projet.

## Déployer le résultat de l'étape zéro

Le harnais N0 peut être forgé directement à partir des spécifications et de graines, ou produit par un générateur N1 lorsque son réemploi le justifie. Déployer les seuls mécanismes retenus et leurs dépendances. Les obligations restent explicites ; les moyens, la cadence des contrôles et l'organisation proviennent du contexte.

Conserver le profil, les graines, les raisons de conception et les versions utiles. N1 n'est archivé que s'il est fourni. Le parcours `single-repo` ne recopie pas automatiquement tout N2. Les outils de fichiers ne configurent pas le moteur d'agents, ses permissions ou son intégration continue. Un instantané disponible n'établit pas une filiation de génération ; un contrôle structurel ne constitue pas une qualification opérationnelle.

Définir les capacités nécessaires à N0, vérifier leur disponibilité et signaler les écarts avant d'annoncer une garantie. Une adaptation de N0 peut être automatisée dans un mandat existant ; une modification du besoin ou de l'autorité suit sa voie de décision. Prévoir une transition de versions qui n'applique pas rétroactivement de nouvelles règles à un ancien rapport.

## Dépôts et identités

Choisir une ou plusieurs racines Git selon les besoins d'accès, de confidentialité et de coordination. Les quatre responsabilités peuvent partager des fichiers ; leur cumul doit rester visible. La publicité du catalogue n'autorise pas la publication de besoins client, de données ou de vulnérabilités. Associer les identités et capacités au mandat réellement reçu.

Pour une indépendance forte, le producteur ne dispose pas de l'écriture sur les sources normatives et les résultats qui le jugent. L'auditeur lit le produit à une référence exacte et conserve ses résultats via un canal dont le candidat n'a pas les clés. Un dépôt unique avec la même identité partout ne fournit pas cette indépendance par la seule séparation de dossiers.

## Sur GitHub

Les mécanismes suivants sont des moyens possibles, à configurer selon les capacités du compte et la politique du projet :

- Protections de branches ou règles de dépôt imposant les revues et contrôles requis.
- Responsables de fichiers via `CODEOWNERS`, avec **exigence effective de leur revue** lorsque nécessaire.
- Invalidation des approbations lorsque le candidat change, ou contrôle équivalent de la version finalement examinée.
- Identification et limitation des possibilités de contournement administratif.
- Contrôles exécutés par une application ou une infrastructure identifiée, à droits restreints.

Un fichier `CODEOWNERS` seul ne bloque pas une fusion. Les administrateurs configurent les revues requises. La disponibilité et les options dépendent de la forge et de son offre ; vérifier la documentation lors du déploiement : [code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners), [branches protégées](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

## Exécution et acceptation

Utiliser d'abord les moyens de contrôle disponibles. Lorsqu'une acceptation automatique est requise, l'exécuteur doit vérifier les références, préparer l'environnement approprié, exécuter les contrôles et émettre les résultats. Construire un nouveau moteur seulement si les moyens existants ne conviennent pas. Garder la politique de décision et les secrets du contrôleur hors du périmètre modifiable ou exécutable par le candidat.

Les dépendances et scripts de construction sont aussi du code à examiner. Exécuter le candidat avec les capacités minimales nécessaires. Les contrôles ayant besoin de services externes utilisent un environnement de test autorisé et identifié ; une indisponibilité devient `UNKNOWN`.

Le mécanisme d'acceptation vérifie les liens aux exigences et aux éléments probants. Il refuse les références absentes, résultats périmés, obligations requises non couvertes et signatures d'identités inconnues. Une signature n'est utile que si son auteur et la chaîne de confiance sont réellement contrôlés.

## Contrôler le harnais lui-même

Avant de s'y fier, injecter des défauts de contrôle : un test ignoré, un rapport ancien, un candidat modifié après audit, un résultat sans exécution, une précondition devenue trop restrictive, une identité sans mandat et un timeout du prouveur. Vérifier que la livraison normale est bloquée et que le diagnostic permet de corriger le problème.

Choisir les expériences qui correspondent aux garanties revendiquées. Les scripts du catalogue n'implémentent pas ce moteur et ne prétendent pas avoir réalisé ces expériences sur un logiciel métier.

## Exploitation et maintenance

Définir la rétention des résultats, les sauvegardes, la gestion des accès et les observations en usage. Un incident peut révéler une exigence oubliée : créer une question ou un changement STBL, puis les contrôles correspondants. Conserver la version des règles applicable à chaque livraison.
