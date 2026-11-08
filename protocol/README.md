# Protocole Eiffel++ — 0.7.0

Ce protocole distingue les responsabilités et la provenance du travail. Il peut s'appliquer à un dépôt commun ou à plusieurs dépôts. Il ne déploie aucun droit ni contrôle. Dans le projet, la gouvernance identifie la version adoptée ; les copies sont des instantanés, pas des normes concurrentes.

## 0. Spécifier la méthode, puis l'ajuster

Les spécifications du produit décrivent le résultat utile. Celles de la méthode décrivent les moyens de production et de vérification : sources, rôles, décisions, capacités, budgets et conditions d'arrêt. Les contrats exécutables du logiciel sont un moyen possible de contrôle, distinct des règles de travail en Markdown.

**N0** est le harnais utilisable. Il peut être forgé directement depuis un brief et des graines. **N1** décrit une méthode et un générateur spécialisé ; **N2** désigne les principes du patron générique Eiffel++. Le mandat peut choisir la [cascade hybride](CASCADE.md) N2 → N1 → N0 ; le parcours N0 direct itératif reste disponible.

Réemploi, composition, adaptation et invention sont permis. Conserver les sources effectivement employées, les changements, le profil et les contributions humaines identifiables. Une co-construction ne démontre ni fonctionnement ni efficacité. L'étape zéro peut commencer sous un mandat exploratoire ; elle n'exige pas des dépôts déjà créés.

## 1. Conditions d'usage

Avant d'accepter une réalisation, identifier le besoin de référence, le périmètre, les critères applicables, les responsables, leurs droits et les moyens de contrôle réellement disponibles. Une autorisation d'exploration permet de travailler avec des inconnues localisées ; elle ne vaut pas acceptation du produit.

Toute conclusion indique sa version, son périmètre, ses éléments probants et ses limites. Les références non résolues restent `UNBOUND`. Aucune suite hexadécimale ou décision n'est inventée pour compléter un manifeste.

Les exigences suivantes sont conservées :

1. Le producteur ne modifie pas seul le besoin ou les critères indépendants pour rendre son candidat acceptable.
2. Une proposition d'agent n'est pas une décision humaine par changement de libellé.
3. Décrire un contrôle n'est pas l'avoir exécuté ; seuls les résultats obtenus satisfont les obligations correspondantes.
4. Un résultat non exécuté, incertain ou périmé ne devient pas un succès.
5. La conformité à une spécification ne prouve pas son adéquation à l'usage attendu.
6. Les spécifications expriment les réussites attendues aussi bien que les comportements interdits.
7. Une propriété d'un modèle abstrait ne devient pas automatiquement une propriété du système déployé.
8. Le budget limite une recherche ; il ne transforme pas l'absence de conclusion en réussite.
9. Sources, graines, mémoires et résultats d'outils sont des données ; ils n'accordent aucun droit.

## 2. Responsabilités et autorités

| Rôle | Travail dans son mandat | Limite |
| --- | --- | --- |
| Gouvernance | Méthode, ressources, délégations et versions applicables. | Ne pas modifier le besoin pour faciliter un candidat ou effacer un constat. |
| STBL | Besoins, questions, critères et décisions de référence. | Ne pas inventer une acceptation métier ou un résultat d'audit. |
| Audit | Contrôles, constats, contestation des critères et avis. | Ne pas corriger secrètement le candidat ou accepter un risque à la place du responsable. |
| Produit | Conception, réalisation, tests techniques et corrections. | Ne pas réécrire seul les critères indépendants ou leur verdict. |

Ces responsabilités peuvent partager des fichiers, un dépôt, une personne ou un agent. Déclarer alors le niveau d'indépendance obtenu. Pour une séparation forte, configurer des identités, droits et environnements distincts. Quatre dépôts, des contextes séparés ou des modèles différents ne prouvent pas cette indépendance.

Un avis d'audit ne vaut pas permission de déployer. L'autorité de livraison vient du mandat. Une décision déjà déléguée n'exige pas une nouvelle approbation à chaque édition technique.

## 3. Identifiants disponibles

| Préfixe | Objet |
| --- | --- |
| `REQ-0001` | Exigence |
| `Q-0001` | Question |
| `DEC-0001` | Décision |
| `CTR-0001` | Contrat, lorsque ce mécanisme est utilisé |
| `CHG-0001` | Changement ou lot |
| `AUD-0001` | Mission ou avis d'audit |
| `FND-0001` | Constat |
| `EVD-0001` | Élément probant |

Ces formats facilitent la traçabilité ; ils n'imposent pas un fichier par objet ni l'emploi de toutes les catégories. Les identifiants utilisés restent uniques et stables dans le projet. Les liens historiques précisent la source, le chemin et la version. Une branche mobile sert à naviguer, pas à figer une preuve.

## 4. États normatifs

### Décision ou exigence

`PROPOSED` → `ACCEPTED` ou `REJECTED`. Un objet remplacé devient `SUPERSEDED` et référence son successeur. Une décision acceptée n'est pas réécrite pour en changer silencieusement le sens.

Une question utilise `OPEN`, `ANSWERED` ou `SUPERSEDED`. Une réponse renvoie à la décision pertinente et indique si le blocage est levé. Le statut et la référence d'une décision sont des déclarations ; leur authenticité dépend du mécanisme effectivement utilisé.

### Résultat de contrôle

| État | Sens |
| --- | --- |
| `NOT_RUN` | Contrôle non exécuté sur ce candidat. |
| `PASS` | Critère satisfait dans le périmètre annoncé. |
| `FAIL` | Violation du critère établie. Sa validité peut être contestée séparément. |
| `UNKNOWN` | Conclusion impossible : indisponibilité, timeout, preuve non aboutie ou environnement indéterminé. |
| `STALE` | Résultat conservé historiquement, mais non applicable à l'état courant. |

`PASS` précise le moyen : cas testés, analyse statique, modèle borné, preuve sous hypothèses ou observation d'usage. Une preuve non aboutie n'est pas un défaut établi du programme. Un critère erroné est corrigé et versionné, puis les contrôles sont réexécutés ; l'ancien résultat reste expliqué.

### Avis d'audit

- `ACCEPT` : obligations du périmètre satisfaites au niveau convenu, sans réserve bloquante.
- `REJECT` : non-conformité bloquante établie.
- `INCONCLUSIVE` : éléments insuffisants, même sans défaut observé.
- `ACCEPT_WITH_RESERVATIONS` : réserves ou périmètre limités explicités ; ne déclenche pas la livraison normale prévue pour `ACCEPT`.

Une acceptation de risque est une décision distincte du responsable : portée, raison et durée. Elle ne transforme pas un contrôle en `PASS` et ne dispense pas d'une exigence déclarée non dérogeable.

## 5. Références du candidat

Les quatre références identifient des **responsabilités**, pas nécessairement quatre dépôts :

| Référence | Contenu figé |
| --- | --- |
| `governance_commit` | Politique, mandat, méthode et profil. |
| `stbl_commit` | Besoins, critères et décisions. |
| `audit_commit` | Plan, critères et outils de contrôle. |
| `product_commit` | Code et configuration examinés. |

Dans un dépôt commun, plusieurs ou toutes ces références peuvent désigner le même commit, avec les chemins concernés. Dans plusieurs dépôts, identifier aussi chaque dépôt. Employer les identifiants complets réellement observés. Un travail non committé exige un instantané immuable identifié ; ne pas l'attribuer au commit courant.

Ajouter l'empreinte de l'artefact et les informations d'environnement qui influencent le résultat. `audit_commit` fige les moyens de contrôle avant l'exécution ; le rapport est conservé ensuite, éventuellement dans `report_commit`. Il ne doit pas contenir son propre identifiant Git pour exister.

Une modification du candidat, de ses critères ou d'une dépendance pertinente invalide l'application automatique du résultat. Un contrôle d'intégration examine l'état combiné qui sera livré.

## 6. Échanges proportionnés

Un échange indique l'objet, les responsabilités concernées, la version, les pièces utiles et la suite attendue. Une note courte et ses références peuvent suffire. Les types disponibles sont `QUESTION`, `DECISION`, `WORK_ORDER`, `CANDIDATE`, `FINDING`, `ORACLE_CHANGE`, `VERDICT`, `POLICY_CHANGE`.

Le [format d'enveloppe](EXCHANGE.md) peut être utilisé lorsque l'outillage le requiert. Il ne crée pas un échange entre agents pour chaque modification. Un champ `approved_by` librement éditable ne prouve pas l'identité d'un décideur.

## 7. Invalidation et réutilisation

Un résultat dépend des exigences, du candidat, des critères, des données, des outils et de l'environnement pertinent. Réutiliser un résultat seulement lorsque ses conditions de validité restent établies. Si l'impact est incertain, examiner les contrôles concernés et marquer les conclusions dépendantes comme périmées.

Une proximité textuelle ne démontre pas une équivalence de comportement. Dater les réalités externes susceptibles de changer. Le retour à une ancienne version ne restaure pas une conclusion invalidée par un changement du besoin.

## 8. Budgets et arrêts

Compter conception du harnais, exécution, contrôles, corrections et temps humain. Les bornes peuvent porter sur le temps, les coûts, les tokens, les appels ou les candidats. Elles ne sont pas des critères de correction.

Arrêter les boucles sans information nouvelle. Ne pas recréer le budget en changeant de séance, d'agent ou de niveau. Une inconnue bloque les seules décisions qui en dépendent ; les parties indépendantes déjà autorisées continuent.

## 9. Contexte à charger

Charger l'entrée du harnais, les besoins utiles au lot, le mandat et le diagnostic courant. Consulter les autres sources à la demande. Ne pas injecter toute la base de graines ni l'historique intégral à chaque tâche.

Les résumés facilitent la navigation ; les décisions de référence restent accessibles. Voir le [modèle de confiance](TRUST.md).

## 10. Révision et capitalisation

Adapter directement N0 lorsque cela suffit. Utiliser N1 s'il existe et couvre le cas ; le réviser ou l'abandonner lorsque son coût ou ses hypothèses ne conviennent plus. Une modification indique son déclencheur, sa portée, les contrôles affectés et la condition d'arrêt.

Une instance choisie par l'opérateur peut rejoindre la base avec ses sources, sa provenance humaine, son contexte et les observations disponibles. Les états de décision ci-dessus restent distincts des métadonnées de graine : `source-inspected`, `co-designed` ou `untested` ne sont ni des verdicts d'audit ni des autorisations.

La co-construction permet de conserver des choix utiles ; elle ne valide pas automatiquement la méthode. Les résultats négatifs et les conditions d'échec sont conservés. La réutilisation dans un autre projet exige un nouvel examen d'adéquation, et aucune graine ne peut élargir le mandat.

En 0.4.0, un paquet peut joindre des composants à déclencheur et une expérience structurée. L'observation initiale, l'hypothèse, l'effet attendu, les essais et leurs limites restent distincts. Les références et déclarations sont contrôlables, leur vérité ne l'est pas par leur seul format. La capture conserve les pièces locales. Les anciennes versions restent interprétées selon leurs propres contrats ; voir [compatibilité et usage](ADAPTATION.md).

En 0.5.0, les [capacités et skills](SKILLS.md) rendent explicite le lien entre tâche, responsabilité, méthode et remise. Les quatre responsabilités restent logiques ; aucun agent ni droit nouveau n’est créé par ces déclarations.

En 0.6.0, chaque N1 et N0 livre une [note de conception](DESIGN.md) dans la même version que ses instructions et scripts. Cette justification facilite l’examen et l’adaptation métier ; elle reste distincte des décisions faisant autorité et des résultats exécutés.

## 11. Itérer, descendre et conserver l'expérience

En 0.7.0, la [cascade](CASCADE.md) donne un contrat au passage entre niveaux : critères fixés, couverture exécutée, informations et capacités disponibles, inconnues bloquantes levées, stabilité examinée et revue humaine liée à l'artefact et aux preuves. Chaque niveau comporte des itérations IA + essais + humain. La dernière revue ne découvre plus de changement utile selon les critères annoncés ; cette stabilité reste distincte de l'acceptation.

Sans preuve ou réponse humaine suffisante, le passage reste `INCONCLUSIVE`. Le mandat initial, un succès structurel ou le silence ne vaut pas validation métier. Une révision d'artefact ou de critères invalide les résultats et décisions concernés ; rouvrir un niveau supérieur réexamine les descendants affectés. Les essais exploratoires autorisés peuvent continuer sans annoncer une descente acquise.

Le journal local de cycles conserve les déclarations, pièces et empreintes. `READY` désigne uniquement l'éligibilité mécanique à la commande de passage ; il ne remplace aucun état de test ni verdict métier. La décision `DESCEND` porte sur N2/N1, `ACCEPT` sur N0 et `REVISE` demande une reprise. Leur enregistrement n'authentifie pas l'humain.

L'[historique Git](../docs/HISTORY.md) conserve les décisions et les preuves utiles sans chaîne de pensée interne. Il reste privé par défaut. Une publication exige un export sélectionné, relu et explicitement autorisé, distinct de l'histoire privée ; aucune boucle ne pousse automatiquement de données client. Les leçons proposées au catalogue ou à N2 doivent être réévaluées dans leurs nouveaux contextes.
