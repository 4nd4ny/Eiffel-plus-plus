# Passer des documents à un harnais effectif

Ce guide décrit les mécanismes à installer. Leur présence dans le catalogue ne signifie pas qu'ils sont activés sur un compte ou un projet.

## Déployer le résultat de l'étape zéro

N2 produit un méta-harnais N1, puis N1 produit le harnais N0. Déployer les mécanismes retenus dans N0 et leurs dépendances, sans installer toutes les options du catalogue. Les obligations restent explicites ; les moyens, la cadence des contrôles et l'organisation des agents proviennent du contexte.

Conserver le profil, le générateur N1, les raisons de conception et les versions utilisées. `meta_harness.py materialize --meta-harness` archive le générateur dans la gouvernance, ainsi que le patron N2 disponible pour les futures régénérations ; il ne configure pas le moteur d'agents, ses permissions ou son intégration continue. La copie N2 n'est pas une preuve qu'elle a produit le N1 fourni. Le résultat structurel du script reste distinct d'une qualification opérationnelle.

Définir les capacités nécessaires à N0, vérifier leur disponibilité et signaler les écarts avant d'annoncer une garantie. Une adaptation de N0 peut être automatisée dans un mandat existant ; une modification du besoin ou de l'autorité suit sa voie de décision. Prévoir une transition de versions qui n'applique pas rétroactivement de nouvelles règles à un ancien rapport.

## Dépôts et identités

Créer les quatre dépôts avec une visibilité choisie selon leur contenu. La publicité du catalogue n'autorise pas la publication de besoins client, de données ou de vulnérabilités. Associer des identités aux rôles et limiter chaque capacité au mandat.

Pour une indépendance forte, le producteur ne dispose pas de l'écriture sur les branches normatives des trois autres dépôts. L'auditeur lit le produit à une référence exacte et conserve ses résultats via un canal dont le candidat n'a pas les clés.

## Sur GitHub

Les mécanismes suivants sont des moyens possibles, à configurer selon les capacités du compte et la politique du projet :

- Protections de branches ou règles de dépôt imposant les revues et contrôles requis.
- Responsables de fichiers via `CODEOWNERS`, avec **exigence effective de leur revue** lorsque nécessaire.
- Invalidation des approbations lorsque le candidat change, ou contrôle équivalent de la version finalement examinée.
- Identification et limitation des possibilités de contournement administratif.
- Contrôles exécutés par une application ou une infrastructure identifiée, à droits restreints.

Un fichier `CODEOWNERS` seul ne bloque pas une fusion. Les administrateurs configurent les revues requises. La disponibilité et les options dépendent de la forge et de son offre ; vérifier la documentation lors du déploiement : [code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners), [branches protégées](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

## Exécution et acceptation

Construire un exécuteur qui reçoit une enveloppe de candidat, vérifie les références dans les dépôts concernés, prépare l'environnement isolé, exécute les contrôles et émet les résultats. Garder la politique de décision et les secrets du contrôleur hors du périmètre modifiable ou exécutable par le candidat.

Les dépendances et scripts de construction sont aussi du code à examiner. Exécuter le candidat avec les capacités minimales nécessaires. Les contrôles ayant besoin de services externes utilisent un environnement de test autorisé et identifié ; une indisponibilité devient `UNKNOWN`.

Le mécanisme d'acceptation vérifie les liens aux exigences et aux éléments probants. Il refuse les références absentes, résultats périmés, obligations requises non couvertes et signatures d'identités inconnues. Une signature n'est utile que si son auteur et la chaîne de confiance sont réellement contrôlés.

## Contrôler le harnais lui-même

Avant de s'y fier, injecter des défauts de contrôle : un test ignoré, un rapport ancien, un candidat modifié après audit, un résultat sans exécution, une précondition devenue trop restrictive, une identité sans mandat et un timeout du prouveur. Vérifier que la livraison normale est bloquée et que le diagnostic permet de corriger le problème.

Ces expériences sont nécessaires au futur moteur ; les scripts du catalogue n'implémentent pas ce moteur et ne prétendent pas les avoir réalisées.

## Exploitation et maintenance

Définir la rétention des résultats, les sauvegardes, la gestion des accès et les observations en usage. Un incident peut révéler une exigence oubliée : créer une question ou un changement STBL, puis les contrôles correspondants. Conserver la version des règles applicable à chaque livraison.
