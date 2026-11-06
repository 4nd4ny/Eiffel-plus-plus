# Contrat illustratif — CTR-0001

**Exemple fictif — `PROPOSED`, dépend de DEC-0001. Le texte ci-dessous n'est pas un programme vérifié.**

## Opération

`réserver(atelier, participant, clé, paramètres)` renvoie une confirmation stable, un refus de capacité ou une erreur définie. Les données invalides et identités non autorisées sont traitées à la frontière avec une réponse prévue ; elles ne sont pas simplement exclues de tous les tests.

## Préconditions et environnement

Le stockage fournit le mécanisme transactionnel utilisé et ses garanties sont explicites. L'atelier existe ; les entrées satisfont le schéma après validation de frontière. Les hypothèses nécessaires au progrès (disponibilité, terminaison des opérations) sont séparées des invariants de sûreté.

## Postconditions

Pour une nouvelle demande valide prenant effet lorsqu'une place est disponible, créer exactement une réservation active et sa réponse durable. Si la capacité est atteinte, refuser sans nouvel effet de réservation. Pour la répétition d'une demande déjà confirmée avec les mêmes paramètres, retourner la même réservation sans modifier le nombre de places consommées.

## Invariants

Nombre de réservations actives inférieur ou égal à la capacité. Une même clé dans son périmètre ne désigne pas deux réservations distinctes. L'identité renvoyée appartient au participant autorisé. Les effets sur d'autres ateliers sont interdits.

## Non-vacuité et périmètre

Une implémentation qui refuse tout échoue à la postcondition positive. Un contrat qui suppose une seule demande simultanée ne couvre pas REQ-0001. Une preuve sur un modèle de compteur doit être reliée à la transaction réelle avant d'étendre sa conclusion à l'application.
