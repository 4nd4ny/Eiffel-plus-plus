# Brief fictif — service d'autorisations entre organisations

Statut : PROPOSED. Source : exemple construit pour Eiffel++ 0.2.0. Aucun client réel ni mandat effectif.

Plusieurs organisations utilisent une même application. Le service doit décider si un sujet peut effectuer une action sur une ressource. Les organisations sont isolées ; un paramètre modifié par l'appelant ne doit pas suffire à changer de périmètre.

L'équipe veut faire évoluer les règles et l'implémentation avec peu d'interventions humaines. Cette autonomie recherchée repose sur des contrats de politique et des vérifications exécutables. Les décisions métier sur les rôles et exceptions restent identifiables.

Le méta-harnais doit découvrir les points encore inconnus : fournisseur d'identité, stockage, règles métier, délais de révocation et délégation de livraison. Il peut produire une première méthode pour des données synthétiques et des interfaces substituables ; il ne peut inventer une politique acceptée.

Un seul changement de code ne doit pas exiger quatre conversations humaines. La méthode peut autoriser des corrections automatiques tant que la politique adoptée, les droits et les contrôles restent inchangés. Le profil de préférences et ses cibles sont dans [profile.json](profile.json).

## Transformation à essayer

Introduire une exception métier autorisant certains opérateurs à agir pour plusieurs organisations. Le N1 doit faire expliciter l'autorité, les limites et les traces de cette exception, puis modifier les contrats et contrôles pertinents. Il ne peut supprimer l'isolation générale pour améliorer le taux de réussite.
