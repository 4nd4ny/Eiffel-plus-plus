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
6. Après acceptation du périmètre élargi, le passage technique a refusé deux cycles annoncés stables : leurs résultats de sonde figuraient parmi les entrées stables, et des limites avaient été reformulées. Le guide et le prompt de qualification précisent désormais le classement exigences/moyens versus preuves. Un test vérifie positivement que de nouvelles observations peuvent satisfaire le même besoin. Les 116 tests du catalogue passent ; aucune règle du contrôleur n'a été assouplie pour obtenir ce résultat.
7. La revue d'auxiliaires générés pendant N1 a révélé des défauts dans le lien candidat/résultats et les remises effectives. Le prompt demande désormais de qualifier aussi le logiciel ajouté au harnais et d'en compter le coût. Après cette précision, le catalogue et les 116 tests passent, avec temporaires dans un chemin réel autorisé. Une première invocation utilisant le chemin temporaire macOS passant par le lien `/var` avait été refusée par les contrôles de chemins ; ce résultat d'environnement n'a pas été traité comme un succès ni résolu en relâchant ces contrôles.
8. Une reprise Git sur exemple synthétique a conservé les octets mais changé `0444` en `0644`, rendant le journal `STALE`. Le témoin en `0644` passait après clone ; restaurer uniquement les modes consignés dans une autre copie rétablissait le verdict avec l'ancre externe initiale. Le guide d'histoire documente cette limite et sa récupération manuelle ; les contrôles d'identité n'ont pas été affaiblis.

Ces constats documentent des décisions et des résultats observables, pas une transcription de raisonnement interne. Les commits suivants conservent les validations et résultats disponibles. La revue humaine d'acceptation de cette version reste distincte de l'autorisation de commit/push ; aucune réponse future n'est inventée.

Le [journal de cette auto-application](journal/session.json) conserve deux cycles liés à la révision `fe266c733463b43bfd7019438fc2d8d5f9b19eda` et aux résultats des 115 tests. Son [état de passage](GATE.json) est **INCONCLUSIVE** : les contrôles réussis ne remplacent pas l'avis humain absent. Cette limite est une observation réelle, distincte des réponses simulées du démonstrateur public. Vérification : `python3 -B tools/cascade.py verify history/eiffel-0.7.0/journal --expected-head 2d36d6afcb66e8905baba408d10f76335af6e9a2333267ef456291bb58279545`.

## Réemploi

Les contre-exemples sont réutilisables pour toute porte de génération. Une leçon issue d'ICO reste située dans cet essai et ne devient pas automatiquement un principe universel. Voir le [guide d'historique](../../docs/HISTORY.md) et la [cascade](../../protocol/CASCADE.md).

L'[application ICO en cours](APPLICATION-ICO.md) distingue les observations déjà obtenues, le pilote N0 direct et les décisions encore ouvertes. Le code et les preuves privées du projet ne sont pas publiés dans cet historique.
