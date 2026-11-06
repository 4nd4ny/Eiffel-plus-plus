# Prompt N2 — engendrer un méta-harnais spécialisé

## Mission

À partir du profil, du brief et des sources disponibles, écris **le générateur N1 qui saura produire le harnais N0 du projet**. Tu conçois des prompts exécutables par un LLM, avec leur contrat et leurs règles de décision.

Respecte le [contrat de génération](../CONTRACT.md). Les anciens patrons du catalogue et les mécanismes externes sont des composants possibles. Tu peux inventer une méthode adaptée lorsque le contexte le justifie.

## Concevoir les règles de synthèse

Détermine d'abord les décisions de méthode qui dépendent réellement de ce projet. Pour chacune, explique quels indices N1 doit lire et quelle transformation ces indices peuvent provoquer.

Ces décisions peuvent concerner la granularité du travail, le parallélisme, la coordination, les questions au PO, la sélection des sources, la vérification, la mémoire, les budgets, l'arrêt ou la récupération après une interruption. Ne reproduis pas systématiquement toute cette liste dans N0.

Formule des règles capables de créer une organisation différente lorsque le besoin change. Par exemple, un contexte où les interfaces sont stabilisées peut autoriser une production parallèle ; une incertitude métier sur l'interface peut déplacer le travail vers une clarification et un prototype ciblé. Les conditions doivent provenir du projet et non d'une règle universelle imposant un nombre d'agents.

Le résultat de cette conception doit distinguer :

- les invariants qui traversent toutes les générations ;
- les caractéristiques du projet qui déterminent les choix de méthode ;
- les transformations que N1 peut produire dans son mandat ;
- les situations qui dépassent son domaine de validité.

## Écrire les prompts N1

Le paquet contient au moins les trois fonctions ci-dessous. Leurs fichiers doivent être réellement rédigés pour ce contexte. Ils doivent rester utilisables sans relire toute la conversation qui les a engendrés.

### GENERATE — produire N0

Ce prompt reçoit le profil courant, les besoins disponibles, la phase ou famille de tâches et les capacités d'exécution connues. Il doit :

1. repérer les informations encore nécessaires aux seules décisions concernées ;
2. dériver une manière de travailler cohérente avec les obligations et le tétraèdre ;
3. engendrer les instructions courtes et les procédures nécessaires aux quatre responsabilités ;
4. choisir quels actes sont délégués, quels événements demandent une décision et quels contrôles sont mécaniques, en conservant le mandat ;
5. définir les sources à charger, les mémoires éventuellement utiles et les règles d'invalidation ;
6. fournir la première action exécutable du projet, les conditions d'arrêt et le retour d'information attendu ;
7. écrire `harness.json`, le profil utilisé et les fichiers effectifs des quatre dépôts.

Une contrainte essentielle doit conduire à un contrôle, une décision compétente ou une condition d'activation explicite. Un contrôle technique prévu mais non configuré reste présenté comme tel.

### CHECK — qualifier N0

Ce prompt reçoit le candidat N0 et ses entrées. Il recherche les omissions et contradictions, vérifie la justification des choix, puis exécute ou demande les contrôles nécessaires au niveau de qualification annoncé.

Il doit distinguer structure, cohérence sémantique, capacité opérationnelle et efficacité observée. Il ne doit pas déclarer un succès sur la seule présence d'un fichier de politique. Il conserve la possibilité de conclure `UNKNOWN` ou `NOT_RUN` pour un contrôle non établi.

Il précise également ce qui permet de commencer utilement dans le mandat existant et ce qui bloque une action particulière. Une qualification proportionnée remplace un passage systématique par toutes les analyses concevables.

### ADAPT — réengendrer la partie nécessaire

Ce prompt reçoit les observations, changements de besoin ou de préférence et le harnais actif. Il décide si le contexte demande un ajustement local de N0, une nouvelle génération N0, ou un retour N2 pour modifier les règles N1 elles-mêmes.

Il doit préserver les obligations et les permissions, limiter le changement à son domaine d'impact, conserver les références et indiquer les contrôles à reprendre. Son déclenchement et son coût font partie du harnais ; il n'analyse pas automatiquement toute l'histoire après chaque action.

## Contrat de sortie propre à N1

Écrire `GENERATION_CONTRACT.md` contenant les obligations que les prompts viennent d'incorporer : entrées, sorties N0, invariants, critères de cohérence, conditions d'activation, domaine de validité, budget et règle d'arrêt. Y conserver les invariants applicables sans dépendre d'un chemin extérieur qui disparaîtrait lors de l'export.

Le fichier explique aussi comment une règle N0 se rattache à une source du besoin, une contrainte ou une préférence. La traçabilité peut prendre la forme d'un tableau court ; elle n'exige pas un graphe ni une nouvelle base de données.

Copier le profil courant dans `profile.json`. Ne pas utiliser des versions différentes du profil pour concevoir N1 et matérialiser son N0 sans créer une révision identifiée.

Écrire un manifeste N1 de cette forme, adapté aux noms réellement produits :

```json
{
  "schema_version": "0.2.0",
  "kind": "meta-harness",
  "level": 1,
  "status": "PROPOSED",
  "profile": "profile.json",
  "entrypoint": "prompts/GENERATE.md",
  "prompts": ["prompts/GENERATE.md", "prompts/CHECK.md", "prompts/ADAPT.md"],
  "output_contract": "GENERATION_CONTRACT.md",
  "source_pattern": "Eiffel++ 0.2.0"
}
```

Le manifeste N0 devra utiliser `kind: project-harness`, `level: 0`, référencer son profil et son `generator`, et mapper `repositories` vers les quatre dossiers distincts `governance`, `stbl`, `audit`, `product`. Chaque dossier contient `AGENTS.md`, `README.md` et les seules procédures nécessaires. Les chemins internes sont relatifs, sans traversée de répertoire ni lien symbolique. `.git` et `_eiffel` sont réservés à la matérialisation.

## Vérifier la capacité de généralisation

Sur un exemple bref, explique ce que tes prompts feraient si une préférence importante changeait, puis si une contrainte discriminante changeait. Les réponses doivent désigner des modifications de méthode et les invariants conservés. Il s'agit d'un examen argumenté, pas d'un résultat de benchmark.

Si seul un coefficient change sans effet possible sur la méthode, ou si tous les projets conduisent aux mêmes instructions, revois le générateur. Si la situation justifie une stabilité de méthode, donne cette raison plutôt que fabriquer une différence.

Remets le paquet N1 et son domaine de validité. L'application de son point d'entrée produit ensuite N0 ; ne présente pas la seule écriture de N1 comme la génération du harnais opérationnel.
