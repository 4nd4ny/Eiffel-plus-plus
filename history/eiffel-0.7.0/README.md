# Eiffel++ appliqué à sa propre évolution

Cette version répond au besoin de combiner trois niveaux de spécification avec des cycles IA–tests–humain au sein de chacun. Le mandat autorise les correctifs, les essais et leur publication ; il ne constitue pas une acceptation des futurs résultats métier.

## Décisions de conception

| Observation | Changement vérifiable | Motif et limite |
| --- | --- | --- |
| Une cascade de textes peut progresser sans retour d'expérience. | Ajouter des cycles liés aux artefacts et preuves, puis une porte avant chaque descente. | Les résultats doivent changer une décision ; la présence d'un fichier ne prouve pas son utilité. |
| L'absence de nouveauté peut cacher un besoin inconnu. | Refuser le passage en présence de critères inconnus, de données manquantes ou sans revue humaine. | La suffisance métier reste une appréciation humaine informée. |
| Une approbation peut viser une version dépassée. | Lier la réponse au dernier cycle ; réouvrir et conserver les décisions remplacées. | Une empreinte n'authentifie pas l'auteur. |
| La mémoire des projets pourrait divulguer leur contenu. | Séparer histoire privée et export public préparé, revu par empreinte. | L'outil ne peut pas garantir automatiquement l'absence de secrets. |
| Le nombre de niveaux pourrait être pris pour une qualité. | Conserver le mode N0 direct itératif comme comparateur. | Le bénéfice de la cascade doit être mesuré, pas présumé. |

## Événements de développement observés

1. Les prompts N2 et le contrat de cascade ont été rédigés ; les responsabilités du journal ont été précisées avant l'implémentation.
2. Une revue distincte a écrit les contre-exemples de test : silence humain, avis périmé, données absentes, critères déplacés, pièces altérées et troncature.
3. Le premier essai a révélé une mauvaise utilisation d'un utilitaire de chemins ; elle a été corrigée. L'essai suivant a révélé un désaccord de test sur N0 : `advance` doit clôturer N0, puis exiger une réouverture pour reprendre. Le test a été corrigé pour ce contrat explicite.
4. La revue a demandé de comparer aussi les besoins, les entrées et leurs empreintes entre cycles. Garder les mêmes noms de critères ne suffit pas à établir la stabilité.
5. Lors de l'application réelle, l'opérateur a demandé le rappel du cahier des charges avant de répondre à la question de passage. Le protocole et les prompts ont été corrigés : la revue explique désormais les usages, les conséquences et la portée des essais. Cette contribution humaine a changé la méthode ; elle n'a pas validé le périmètre proposé.

Ces constats documentent des décisions et des résultats observables, pas une transcription de raisonnement interne. Les commits suivants conservent les validations et résultats disponibles. La revue humaine d'acceptation de cette version reste distincte de l'autorisation de commit/push ; aucune réponse future n'est inventée.

## Réemploi

Les contre-exemples sont réutilisables pour toute porte de génération. Une leçon issue d'ICO reste située dans cet essai et ne devient pas automatiquement un principe universel. Voir le [guide d'historique](../../docs/HISTORY.md) et la [cascade](../../protocol/CASCADE.md).
