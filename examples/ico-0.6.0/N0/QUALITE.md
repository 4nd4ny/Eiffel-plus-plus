# Qualités du logiciel et décisions du projet

Transposition des quatorze facteurs de Meyer retenus par `meta/QUALITY.md` d’Eiffel++. Les facteurs concernent le produit, pas seulement la documentation du harnais.

| Facteur | Décision | Contrôle ou limite |
| --- | --- | --- |
| Q01 Correction | Relier chaque résultat dû à un oracle ; distinguer obligation et renforcement. | Contrat du lot et tests nominaux/erreurs. |
| Q02 Robustesse | Entrée invalide, dépendance absente et reprise ne doivent pas détruire la référence. | Cas anormaux et restauration sur copie. |
| Q03 Extensibilité | Localiser un nouveau format ou fournisseur derrière son interface. | Revue des dépendances du changement ; aucun gain observé ici. |
| Q04 Réutilisabilité | Séparer transformation pure et effets afin de réemployer les composants du produit. | Tests hors UI ; réemploi du harnais ne prouve pas celui du produit. |
| Q05 Compatibilité | Conserver les contrats persistants et les API ; migration explicite si nécessaire. | Fixtures de format et consommateurs concernés. |
| Q06 Efficience | Mesurer la charge du produit lorsqu’un lot modifie recherche/indexation/UI. | Seuil métier à reprendre des sources du lot ; aucun benchmark produit ici. |
| Q07 Portabilité | Identifier Node, Python, navigateur et mécanismes propres à la plateforme. | Diagnostic local observé ; autres plateformes non exercées. |
| Q08 Facilité d’usage | Vérifier parcours, erreurs, sources et accessibilité sur des écrans réels. | Suite navigateur et revue utilisateur indisponibles dans le présent essai. |
| Q09 Fonctionnalité | Conserver une carte des usages ; le diagnostic de deux modules ne définit pas tout ICO. | ROUTAGE et périmètre/exclusions du lot. |
| Q10 Ponctualité | Livrer un incrément utile ; aucune date métier fournie. | Deux cycles puis bilan ; échéance à décider si nécessaire. |
| Q11 Vérifiabilité | Garder des oracles falsifiables, critères complets, candidats et contrôles identifiés. | Défaut injecté, passations et détection STALE. |
| Q12 Intégrité | Conserver données, clés, originaux et choix explicite des sorties réseau. | Travail sur copie sans comptes ; aucune certification de sécurité. |
| Q13 Réparabilité | Reproduire un écart avant de modifier, garder le cas qui le détecte. | Candidat complet, référence conservée, correction ciblée. |
| Q14 Économie | Compter génération, essais et reprises ; budget monétaire non fourni. | Durées locales mesurées ; coût modèle de conception inconnu, pas de faux zéro. |

Pour un lot Import : Q01, Q02, Q05, Q11, Q12, Q13 sont actifs ; Q03/Q04 si une interface change. Pour un lot Interface : Q01, Q02, Q08, Q09, Q11 et Q12 deviennent actifs ; les sondes URL/citations seules sont insuffisantes. Les autres décisions restent consultables, sans quatorze listes obligatoires à chaque agent.
