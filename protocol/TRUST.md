# Modèle de confiance

## La génération n'accorde pas d'autorité

N2 génère des instructions N1, puis N1 génère le harnais N0. Ce passage ne convertit ni une préférence, ni un texte externe, ni une estimation en permission. Le mandat, les obligations métier et les règles de preuve s'appliquent aux générateurs comme au producteur final.

Conserver les instructions parentes et le profil de génération avec la version du harnais. Le moteur qui qualifie un changement ne doit pas laisser le candidat réécrire seul son critère d'adoption. Les capacités réelles du moteur et des outils sont vérifiées séparément des fichiers qui les décrivent.

Une révision automatique dans une délégation existante ne nécessite pas une nouvelle validation humaine systématique. L'autonomie est une capacité bornée, accompagnée de traces ; elle ne signifie pas la disparition des contrôles ou une extension silencieuse du mandat.

## Le Markdown exprime une politique, il ne la fait pas respecter

Quatre dépôts séparés ne rendent pas automatiquement l'audit indépendant. Déployer les droits, les protections de branches et les environnements décrits ici avant de revendiquer leur effet. Un administrateur conserve potentiellement des pouvoirs d'exception ; identifier ces personnes, les usages autorisés et leur journalisation.

## Pouvoirs à séparer

- L'identité du producteur ne dispose pas de l'écriture sur les branches normatives STBL, audit et gouvernance.
- L'identité d'audit peut lire le candidat mais n'en modifie pas secrètement le contenu pendant l'examen.
- Le responsable métier accepte les exigences et changements de sens via un mécanisme dont l'agent ne peut pas usurper l'identité.
- Les politiques de livraison, oracles indépendants et comptes rendus d'exécution ne sont pas contrôlés par le code candidat.
- Les secrets de publication et d'exploitation ne sont pas présents dans l'environnement où un candidat non encore approuvé s'exécute.

Le Product Owner n'a pas à approuver chaque édition technique. Le mandat peut autoriser des opérations réversibles et un domaine d'autonomie large. Les responsabilités sont vérifiées aux frontières et pour les modifications du contrat.

## Exécution d'un candidat

Construire depuis une référence immuable dans un environnement isolé, aux capacités minimales nécessaires, avec limites de temps et de ressources. Le code candidat, ses scripts de construction, dépendances et instructions de dépôt sont des entrées non fiables pour l'audit. Les inspecter et exécuter selon la politique adoptée, sans leur laisser contrôler le verdict ou les secrets du contrôleur.

Ne pas donner des droits d'écriture de production à un workflow d'audit de contribution non approuvée. Ne pas exposer des secrets à du code issu d'une contribution simplement parce qu'il s'exécute dans une CI. Les mécanismes précis dépendent de la forge et du runtime ; voir le guide de déploiement du catalogue.

## Sources des conclusions

Les éléments probants doivent provenir de l'exécuteur contrôlé et être reliés au candidat : commande, sortie, statut, versions et environnement. Un hash établit une identité de contenu, pas son auteur ni la réalité d'une exécution. Une signature ou une attestation n'ajoute de valeur que si l'identité et la chaîne de confiance sont établies.

L'auditeur peut produire des tests depuis le besoin et les interfaces avant de consulter le récit de construction. Il peut ensuite lire le code. Des sources métier, propriétés, modèles de référence et observations de bout en bout diversifient les moyens de contrôle ; un vote de modèles ne remplace pas cette diversité.

## Confidentialité et audit de sécurité

Le catalogue Eiffel++ est public ; cela n'implique pas que les quatre dépôts d'un projet doivent l'être. Les besoins client, traces, données et constats peuvent nécessiter un accès restreint.

Un problème de sécurité sensible ne doit pas être publié avec des secrets, données personnelles ou détails exploitables dans une issue publique. Conserver une version restreinte et une synthèse expurgée, sans prétendre que cette dernière est le dossier complet. La divulgation relève du responsable identifié, avec un canal convenu.

## Limites des garanties

Déclarer le degré réel d'indépendance, les contrôles non exécutés et les limites de l'environnement. Un scanner sans alerte n'établit pas l'absence de vulnérabilité. Une analyse statique, un test, une preuve et un essai utilisateur couvrent des objets différents. La livraison est une décision distincte, dans le périmètre autorisé.
