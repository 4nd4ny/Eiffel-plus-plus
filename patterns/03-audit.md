# Métapatron 03 — Cabinet d'audit indépendant

Version du métapatron : **0.3.0**.

## Intention

Évaluer un candidat logiciel à partir de besoins et de critères dont son auteur ne maîtrise pas le verdict. Le cabinet recherche les défauts, les écarts au besoin client, les risques de sécurité et les lacunes de qualité ; il rapporte aussi ce qu'il n'a pas pu établir.

« Cabinet » désigne une séparation fonctionnelle du travail et des pouvoirs. Ce patron ne crée ni organisme accrédité ni certification. Un agent critique est un moyen d'enquête ; une conclusion doit être soutenue par des observations, des contrôles exécutés ou une décision humaine identifiée.

## Contexte et forces

- La gouvernance fixe la méthode, les capacités, les délégations et les règles d'acceptation.
- La responsabilité STBL porte les besoins, contrats et critères auxquels comparer le produit, ainsi que les arbitrages métier du Product Owner ou de son délégataire.
- La responsabilité produit conserve le candidat et sa construction.
- La responsabilité audit maintient des plans, oracles, constats et résultats séparés.
- Le générateur et l'auditeur peuvent partager un modèle et donc des erreurs. Une conversation séparée améliore la contradiction sans démontrer l'indépendance de leurs jugements.
- Une suite verte peut manquer un besoin ; un modèle formel correct peut mal représenter l'implémentation ; un scanner peut manquer une vulnérabilité. La portée de chaque résultat doit rester visible.
- La répétition intégrale de tous les contrôles coûte cher. Leur réutilisation n'est sûre que si les entrées et hypothèses pertinentes sont maîtrisées.

## Structure

Le cabinet utilise un mandat, une politique d'audit, un plan adapté au risque et un registre de constats. L'exécuteur de contrôles et la politique d'acceptation sont protégés contre les modifications du constructeur du produit. Cette protection doit être configurée dans l'hébergement, les permissions et la CI ; un fichier Markdown ne l'applique pas.

Dans ce composant optionnel, chaque campagne possède un identifiant `AUD-0001` et **quatre références logiques** : `governance_commit`, `stbl_commit`, `audit_commit`, `product_commit`. Elles peuvent partager un dépôt Git et un commit ; chacune conserve son adresse et son SHA complet. La topologie ne démontre pas l’indépendance du contrôle. `audit_commit` désigne le plan, les politiques et les oracles utilisés avant l'exécution ; les résultats sont ajoutés ensuite dans `report_commit`, identifié par le commit contenant le rapport. Cette convention évite de prétendre qu'un rapport contient son propre SHA.

Cette liaison inclut également les critères applicables, la recette de construction, l'empreinte de l'artefact candidat, l'environnement de construction et l'environnement de contrôle. L'identité du code seul ne suffit pas à identifier un binaire ou une configuration déployée. Un arbre modifié ne peut pas être présenté comme le commit déclaré. Le manifeste de liaison est figé séparément et son empreinte est conservée dans les preuves qui le référencent, sans s'inclure elle-même.

L'auditeur lit les sources métier et le produit. Il peut produire ses propres scénarios et examiner ceux de l'auteur. Il ne doit pas dériver toutes les réponses attendues de l'implémentation à contrôler.

## Contrat

### Préconditions

- Le mandat identifie le périmètre, les accès autorisés, les exclusions et le destinataire du verdict.
- Les quatre références logiques sont résolues en SHA complets, éventuellement identiques ; une branche mobile n’est pas une référence de campagne.
- Les besoins et critères sont traçables à leurs sources et leur état de décision est connu.
- Le candidat est identifié, et l'exécuteur dispose d'un environnement isolé approprié. Les scripts de construction, dépendances et fixtures sont traités comme du code non fiable.
- La politique d'acceptation et les oracles qualifiés sont accessibles à l'auditeur et protégés contre leur affaiblissement par l'auteur.

Une précondition manquante conduit à un verdict `INCONCLUSIVE`, avec la demande précise permettant de poursuivre. Elle ne se transforme pas en hypothèse silencieuse.

### Postconditions

- Chaque constat `FND-0001` indique une source, un impact, un moyen de reproduction ou la raison de son indétermination.
- Chaque élément `EVD-0001` renvoie à un résultat capturé, au candidat concerné, aux outils, aux hypothèses et à sa portée.
- Le verdict associe chaque critère obligatoire à un résultat utilisable et énumère les limites restantes.
- Aucun résultat périmé, absent ou indéterminé n'est présenté comme une réussite.
- Les informations destinées à un dépôt public ont été revues pour retirer secrets et données non publiables, tout en conservant une provenance vérifiable dans l'emplacement autorisé.

### Invariants

- L'auteur du produit ne peut pas s'auto-attribuer un verdict d'audit accepté.
- Un contrôle qualifié n'est jamais affaibli uniquement pour faire passer le candidat.
- Un changement de besoin ou d'oracle suit une décision distincte, versionnée et sourcée ; les résultats affectés deviennent `STALE`.
- Les résultats de vérification sont `NOT_RUN`, `PASS`, `FAIL`, `UNKNOWN` ou `STALE`. Les décisions sont `PROPOSED`, `ACCEPTED`, `REJECTED` ou `SUPERSEDED`.
- Un échec de preuve ou un délai de vérificateur n'est pas à lui seul un contre-exemple du programme ; sa conclusion peut être `UNKNOWN`.
- Une preuve porte uniquement sur son énoncé, son modèle et ses hypothèses. Une réussite aux tests porte sur les cas et conditions exécutés.

## Heuristiques de décision

Commencer par les contrôles qui départagent le candidat au meilleur coût : identité et construction, typage et analyses, propriétés métier, intégration, parcours utilisateur, puis investigations ciblées selon le risque. Cet ordre reste adaptable ; une règle métier critique peut justifier immédiatement une analyse plus profonde.

Chercher les comportements qui satisfont formellement une règle tout en trahissant le besoin. Par exemple, refuser toutes les réservations prévient la survente mais ne rend pas le service demandé. Vérifier les scénarios de réussite, les invariants, les erreurs et les garanties de progrès nécessaires.

La sécurité combine notamment modèle de menaces, frontières de confiance, permissions, entrées non fiables, dépendances et comportements observés. Un rapport de scanner contribue au dossier ; son absence d'alerte ne démontre pas la sécurité.

Réutiliser une observation seulement lorsque son identité et toutes ses dépendances pertinentes sont inchangées. Si l'analyse d'impact ne couvre pas la configuration, les données, les migrations, les services externes ou les dépendances dynamiques, invalider plus largement. Une sélection ciblée de tests dont la complétude n'est pas établie nécessite un contrôle plus large à l'intégration.

## Protocole de coopération

Appliquer le [protocole commun](../protocol/README.md). Le produit remet un candidat identifié ; le STBL fournit les critères et les questions `Q-0001`. La gouvernance arbitre la méthode, les capacités et les délégations ; le Product Owner ou son délégataire tranche les questions métier, avec une décision `DEC-0001` enregistrée dans le STBL. L'audit publie des constats et des preuves, puis un verdict.

Un correctif `CHG-0001` donne lieu à un nouveau candidat. L'auditeur contrôle la correction du constat et les obligations affectées, y compris la composition avec les autres changements. Le plan n'exige pas une nouvelle discussion entre agents pour chaque contrôle déterministe.

Une erreur supposée de test passe par une proposition de changement d'oracle. Le diagnostic distingue défaut du produit, défaut du besoin, défaut de l'oracle et défaut de l'environnement ; il ne choisit pas arbitrairement celui qui permet d'obtenir du vert.

## Arrêt et escalade

Les verdicts sont `ACCEPT`, `REJECT`, `INCONCLUSIVE` et `ACCEPT_WITH_RESERVATIONS`.

- `ACCEPT` : tous les critères obligatoires du périmètre disposent de résultats valides et aucun constat bloquant n'est ouvert. La livraison relève de l'autorité désignée dans le mandat, selon la politique de gouvernance.
- `REJECT` : une violation établie bloque l'acceptation selon la politique applicable.
- `INCONCLUSIVE` : une information, un accès, une exécution ou un résultat obligatoire manque. Ce verdict arrête automatiquement le passage vers l'acceptation ; il ne signifie pas que le produit est défectueux.
- `ACCEPT_WITH_RESERVATIONS` : les critères obligatoires sont satisfaits, mais des limites ou risques non bloquants demandent une décision explicite. Ce verdict n'autorise jamais une livraison automatique.

Arrêter également les boucles de réparation qui répètent le même contre-exemple sans progrès, dépassent le budget convenu ou nécessitent une décision métier non déléguée. Fournir une question et les éléments permettant d'y répondre, pas une demande de permission générale.

## Antipatrons

- Prendre le nombre d'agents convaincus pour une preuve.
- Accorder `PASS` parce que l'auteur affirme avoir exécuté les tests.
- Exécuter le script de construction d'un candidat avec les secrets ou privilèges de l'auditeur.
- Conserver le même verdict après modification d'un besoin, d'un oracle ou du candidat.
- Confondre « aucun défaut trouvé » et « absence de défaut ».
- Cacher un contrôle obligatoire `UNKNOWN` derrière une réserve non bloquante.
- Publier des journaux bruts contenant des données client, jetons, identifiants ou charges sensibles.
- Déclarer l'indépendance de la CI alors que l'auteur peut modifier son exécuteur, ses sélecteurs de tests ou sa politique d'acceptation.

## Indicateurs

Suivre le coût et le délai par obligation examinée, les défauts échappés à l'audit, les faux rejets, les résultats indéterminés, la part de résultats réutilisés avec une liaison valide et les écarts de besoin découverts après acceptation. Ne pas récompenser le volume de constats, de tokens ou de tests.

## Variantes

- **Audit léger** : changement limité, contrôles rapides et parcours pertinent ; mêmes règles d'identité et de verdict.
- **Audit renforcé** : concurrence, permissions, transactions ou migrations ; tests d'intégration et propriétés spécifiques.
- **Noyau vérifié** : preuve de propriétés critiques avec hypothèses et lien vers l'implémentation explicités ; contrôle du reste du système maintenu.
- **Audit de besoins** : recherche de contradictions et de critères insuffisants avant réalisation ; aucune conclusion sur un produit qui n'a pas été examiné.

Le [métapatron instanciable](../templates/03-audit/README.md) fournit les documents de départ. Aucun de ces documents ne constitue un résultat d'audit préexistant.
