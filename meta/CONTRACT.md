# Contrat de génération N2 → N1 → N0

Ce contrat porte sur la transformation d'un niveau en celui qu'il engendre. Il s'applique en complément du [protocole opérationnel](../protocol/README.md), dont il conserve les états et les frontières d'autorité.

## Préconditions

- La demande, ses sources et le périmètre autorisé sont identifiables, y compris si l'étape zéro est exploratoire.
- Les préférences connues sont distinguées des inférences. Les obligations non négociables et les questions ouvertes sont visibles.
- Les capacités du moteur d'exécution sont documentées à un niveau suffisant pour le harnais envisagé ; les capacités non confirmées restent inconnues.
- Le travail de génération possède une borne : nombre de candidats, de révisions, temps ou budget disponible.

Une information manquante n'est bloquante que pour les décisions qui en dépendent. Une première version peut porter des hypothèses provisoires et un périmètre limité.

## Postconditions N2 → N1

Le méta-harnais engendré fournit :

1. un profil du contexte et des arbitrages, avec leurs sources et incertitudes ;
2. des prompts spécialisés permettant d'engendrer N0, de l'examiner et de le réviser ;
3. des règles de synthèse expliquant comment les caractéristiques du projet changent la méthode, sans réduire cette adaptation à un choix de profil préétabli ;
4. un domaine de validité et des conditions signalant qu'une révision de N1 devient nécessaire ;
5. un contrat de sortie, un budget de génération et une règle d'arrêt ;
6. un manifeste dont les chemins désignent les fichiers réellement produits.

Un N1 ne se réduit pas à un harnais N0 assorti de l'instruction « adapte-toi ». Ses prompts doivent permettre de produire une autre méthode à partir d'un changement pertinent du contexte.

## Postconditions N1 → N0

Le harnais engendré fournit :

1. les quatre dépôts logiques `governance`, `stbl`, `audit`, `product`, chacun avec son entrée courte et ses instructions propres ;
2. les modalités concrètes de production, d'échange, de vérification et d'arrêt adaptées au projet ;
3. les actions déléguées, les décisions réservées et la manière de les distinguer ;
4. le mécanisme de sélection du contexte et, si nécessaire, de mémoire, avec leurs sources et leurs conditions de validité ;
5. la traçabilité des règles importantes vers les besoins, contraintes, préférences ou observations qui les motivent ;
6. les moyens de qualification disponibles, les observations réellement obtenues et les conditions d'activation encore ouvertes ;
7. son profil, son manifeste et la référence du N1 qui l'a engendré.

Les contrôles documentés sont distingués des contrôles configurés et des contrôles effectivement exécutés. Une description ne vaut pas installation. Les références non résolues ne sont pas remplacées par des identifiants fictifs.

## Invariants conservés entre niveaux

### Autorité

La génération ou l'adaptation n'étend pas les permissions. L'autonomie s'exerce dans une délégation identifiable. Le générateur peut proposer une révision du mandat ou des obligations ; l'autorité compétente décide selon la procédure applicable.

### Sens du besoin

Une optimisation de vitesse, de coût, de périmètre ou d'attention humaine ne modifie pas silencieusement le besoin accepté. Le harnais ne crée pas de préconditions artificielles qui excluraient des usages obligatoires pour paraître plus performant.

### Intégrité de l'acceptation

Le producteur ne peut réécrire seul le besoin, les oracles indépendants ni leur verdict. Une proposition de changement du contrôle suit une voie distincte ; elle ne fait pas disparaître le résultat historique.

### Honnêteté des résultats

Les observations, hypothèses, prévisions et décisions restent distinctes. Un résultat `NOT_RUN`, `UNKNOWN` ou `STALE` ne satisfait pas une obligation exigeant `PASS`. Les qualificatifs « optimal », « autonome » ou « vérifié » annoncent un périmètre et une justification précis.

### Conservation des contraintes

Le tétraèdre arbitre entre configurations admissibles. Une propriété non négociable n'est pas absorbée dans une moyenne compensable. Lorsque l'ensemble des contraintes paraît irréalisable, le générateur rend le conflit explicite.

### Traçabilité et révision bornée

Chaque harnais est lié à son générateur, à ses entrées et à une version. Une adaptation produit un changement identifiable et un examen d'impact. Les travaux en cours restent attachés au contrat sous lequel ils ont été engagés, sauf transition explicite.

### Statut des données

Une source externe, un souvenir ou une trace d'outil reste une donnée. Sa reformulation dans un prompt généré ne lui accorde pas l'autorité d'une décision. Les connaissances dérivées conservent les restrictions de leurs sources.

## Qualification et adoption

La qualification structurelle vérifie les formats, chemins et éléments requis. L'examen sémantique recherche les contradictions et l'adéquation des règles. La qualification opérationnelle observe les mécanismes effectivement exécutés. Une expérience comparative apprécie leur effet dans un domaine donné.

Ces qualifications peuvent être réalisées au niveau nécessaire à la décision courante. Elles ne sont pas toutes requises pour écrire un premier candidat. Leur résultat n'est jamais déduit du seul fait que le paquet a été généré ou matérialisé.

L'adoption dépend de l'autorité et du mandat déjà établis. Elle peut être automatique pour une adaptation déléguée ; elle exige une décision distincte lorsqu'elle change le besoin, les droits ou une obligation réservée. Un champ `ACCEPTED` est une déclaration à rattacher à cette décision, pas un mécanisme d'authentification.

## Fin de la récursion

N0 exécute le projet ; N1 réadapte N0 ; N2 peut réviser N1 lorsque son domaine de validité est dépassé. La profondeur s'arrête là. Un incident ne justifie pas à lui seul une régénération générale, et aucun niveau ne peut prolonger de lui-même son budget.
