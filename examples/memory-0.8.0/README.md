# Oubli opérationnel : exemple fictif exécutable

Le [démonstrateur](demo.py) conserve une exigence rare et une consigne de pilote. Il prépare un contexte, retire la consigne du pilote, constate le refus de l'ancienne remise, puis produit un contexte neuf qui conserve l'exigence. Les sources et acteurs sont synthétiques ; aucun avis humain réel, modèle, déploiement ou gain de productivité n'est simulé comme résultat acquis.

Depuis le dépôt, avec une destination neuve :

```sh
python3 -B examples/memory-0.8.0/demo.py /chemin/autorise/essai-neuf
```

Le résultat comprend la mémoire privée de démonstration, les deux remises et `result.json`. Le programme refuse une destination préexistante. Les tests du catalogue exercent aussi les conflits entre processus, les modifications d'autorité, l'expiration et la perte d'exigences. Voir le [contrat](../../protocol/MEMORY.md).

## Formats et intégration

Une politique déclare `maintainers` et `writers`. L'hôte impose l'identité de l'appelant ; les noms passés au CLI ne l'authentifient pas. Le magasin et les ancres doivent rester hors de l'écriture des réalisateurs. `source` conserve l'origine, la référence et le texte fourni ; `remember` en extrait une citation exacte. Une interprétation de l'agent est enregistrée dans une source `agent`, jamais sous le nom d'un humain.

Les opérations `retire`, `challenge` et `resolve` citent leur source et leur justification. Les hypothèses/choix ont une échéance `expires_at` ou des versions `basis`. Les exigences n'expirent pas par ancienneté. `depends_on` relie les dérivations et propage leur invalidation. La liste `scope` nomme les travaux couverts ; `*` couvre tout le projet.

`propose` produit un objet sans l'appliquer. L'empreinte est SHA-256 de sa représentation JSON canonique (`meta.canonical`) ; l'appelant conserve cette empreinte séparément et l'utilise avec `apply`. Le CLI `propose --output` écrit cette représentation et retourne son empreinte. Ne pas confondre un brouillon proposé et une décision de son mainteneur.

`prepare` reçoit le travail courant et ses versions depuis l'hôte. `launch_request` compare le paquet à la mémoire au moment de l'appel et retourne uniquement les messages à transmettre dans un contexte neuf. La sélection inclut toutes les exigences applicables, sans recherche par popularité ou troncature. Les autres notes gardent leur nature visible. Un adaptateur ne doit pas joindre l'ancien historique à ces messages. Le démonstrateur vérifie ces données ; il ne prouve pas l'obéissance d'un LLM.

## Choix de conception

Un journal local, des citations exactes et des transitions vérifiées suffisent ici pour rendre les erreurs reproductibles. Les sources conservées évitent qu'une correction efface son origine ; les empreintes externes détectent les remises périmées. Le retrait opère dans la sélection, sans supprimer l'histoire. Le verrou et le remplacement atomique couvrent les écrivains locaux qui utilisent cet outil, pas une synchronisation distribuée.

L'interprétation sémantique demeure une activité de revue. Un agent peut proposer une consolidation avec le [prompt dédié](../../meta/prompts/05-revise-memory.md) ; l'outil n'appelle aucun modèle ni service et ne prétend pas identifier tout seul les fausses croyances. Le mécanisme est indépendant de la cascade et réutilisable avec un N0 direct.
