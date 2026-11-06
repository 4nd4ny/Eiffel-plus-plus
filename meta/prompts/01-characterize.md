# Prompt N2 — caractériser ce qui doit engendrer la méthode

## Mission

Construis le profil à partir duquel un LLM pourra concevoir le méta-harnais du projet. Recherche les différences de situation qui doivent produire des différences de méthode.

Applique le [contrat de génération](../CONTRACT.md) et la convention du [tétraèdre](../TETRAHEDRON.md). Le brief, le mandat et les décisions déjà fournis constituent tes premières sources. N'impose pas un entretien standard si ces sources suffisent.

## Travail à réaliser

Lis les informations utiles et explicite :

- le résultat utile pour les utilisateurs et la manière de le reconnaître ;
- les obligations essentielles et le périmètre qui peut faire l'objet d'un arbitrage ;
- les limites de délai, de ressources et d'attention humaine ;
- les décisions déjà déléguées et les décisions réservées ;
- les sources de difficulté qui influencent la méthode : ambiguïté, couplage, réversibilité, fréquence des changements, conséquences d'un défaut, durée du projet, outils réellement accessibles ;
- l'historique pertinent, s'il existe, sans supposer que les erreurs passées se reproduiront dans le nouveau contexte.

Pour chaque information importante, distinguer donnée explicite, inférence, observation et inconnue. Réutiliser les décisions existantes ; ne pas créer une demande d'approbation pour une autorisation déjà accordée.

Pose une question seulement si ses réponses plausibles conduisent à des harnais matériellement différents ou conditionnent une action hors mandat. Grouper les questions liées. Continuer les travaux dont elles ne changent pas le résultat.

Lorsque des détails manquent, choisir une hypothèse réversible et la consigner. Si une obligation et un budget sont incompatibles, décrire le conflit et les arbitrages possibles sans en décider à la place du responsable.

## Profil à produire

Écrire `profile.json` avec `schema_version: 0.2.0` et les sections suivantes :

| Section | Contenu requis |
| --- | --- |
| `project` | `slug`, `name`, `brief`. Nom technique de 1 à 64 minuscules, chiffres ou tirets sans tiret aux extrémités ; nom lisible sur une ligne ; brief ou référence utile non vide. |
| `preferences` | `weights`, `status`, `source`, `measures`. `weights` contient exactement `speed`, `economy`, `scope`, `autonomy`, avec une somme de 1. |
| `constraints` | Liste de `{id, statement, verification}` décrivant les obligations non compensables. Référencer les décisions et sources disponibles dans les champs ou métadonnées complémentaires. |
| `authority` | `mandate`, `autonomous_actions`, `human_decisions`. Décrire les droits réellement accordés ; signaler explicitement un mandat non établi. |
| `unknowns` | Inconnues, effet possible sur le harnais et décision à laquelle elles se rattachent. |
| `generation_budget` | `max_candidates`, `max_iterations`, `max_tokens`. Les deux premières bornes sont des entiers positifs ; la dernière peut être `null` lorsqu'elle n'est pas fournie. |

`preferences.measures` contient les quatre clés des poids. Chaque mesure contient `metric`, `unit`, `direction` et éventuellement `target` (nombre ou `null`). Par exemple, l'autonomie peut suivre des minutes de supervision avec `direction: minimize`. Ne pas confondre le nom du sommet et le sens de sa mesure.

Le statut des préférences utilise `PROPOSED`, `ACCEPTED`, `REJECTED` ou `SUPERSEDED`. `ACCEPTED` requiert `decision_ref` et une décision réellement identifiable. La présence de cette référence n'est pas à elle seule une preuve d'autorité. Les valeurs inférées ou illustratives restent `PROPOSED` tant qu'aucun mandat ne permet leur adoption.

Une mesure principale par axe suffit au départ. Utiliser `target: null` lorsqu'aucune cible n'est connue. Ne pas convertir une absence de donnée en zéro, ni une préférence verbale en performance prévue.

## Justification attendue

Produire une note courte de conception avec les liens suivants :

| Élément du contexte | Conséquence sur la méthode à engendrer | Incertitude ou condition de révision |
| --- | --- | --- |
| Source ou observation précise | Ce que N1 devra savoir décider, générer ou vérifier | Ce qui ferait changer ce choix |

Concentrer cette note sur les éléments discriminants. Un inventaire exhaustif sans conséquence sur la génération n'est pas nécessaire.

## Contrat de sortie

Le profil est suffisamment précis pour engendrer un premier N1, ou ses blocages sont localisés. Les poids n'ont accordé aucun droit et n'ont effacé aucune obligation. Le besoin fonctionnel est exprimé par la valeur attendue et les critères applicables, pas par une quantité de fichiers ou de fonctionnalités accessoires.

Si le profil existe déjà, produire un changement identifié plutôt que le réinterpréter silencieusement. Conserver l'origine et le statut des décisions inchangées.
