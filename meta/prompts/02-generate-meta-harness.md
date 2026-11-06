# Choisir des graines et forger le harnais

## Mission

Produis N0 à partir du besoin, du mandat et des ressources disponibles. Utilise le [cadre de conception](../CONTRACT.md). La sortie attendue est une méthode utilisable dans son périmètre, avec ses limites ; N1 est une option de réemploi, pas une étape obligatoire.

## Choisir un point de départ

Lire l'index de la [base de graines](../../seeds/README.md), puis les fiches dont le contexte paraît pertinent. Vérifier les sources et révisions consultées, les capacités requises, les cas déconseillés et le niveau d'observation disponible.

Choisir un candidat principal ; ajouter une alternative seulement si elle permet de trancher un compromis matériel. Comparer aussi à une organisation simple : un producteur, les besoins utiles, des contrôles exécutables et une note de reprise si nécessaire.

Réemployer, paramétrer, composer ou inventer selon le besoin. Une graine peut convenir sans changement. La ressemblance textuelle, la popularité et le nombre d'agents ne prouvent pas l'adéquation. Une recette issue d'un runtime ne fournit pas automatiquement ses outils ou sa mémoire.

## Forger avec l'opérateur

Présenter un candidat concret : prochaine action, répartition du travail, sources à charger, contrôles, arrêts et décisions réservées. Expliquer brièvement ce qui est repris, supprimé, adapté ou ajouté, et son coût attendu. Ne pas fabriquer un gain chiffré.

Rendre visibles les choix sur lesquels une contribution humaine changerait la méthode. Intégrer les réponses et corrections effectivement reçues. Les choix déjà autorisés peuvent être exécutés sans nouvelle approbation ; la co-construction ne devient pas une validation systématique de chaque fichier.

Conserver la référence des arbitrages. Un candidat automatique ne devient pas « co-construit » du seul fait qu'un champ le dit. Une préférence exprimée par l'opérateur ne démontre pas que le harnais fonctionne mieux.

## Produire N0

Un point d'entrée court doit permettre de commencer le lot autorisé. Les procédures désignent des outils disponibles et des contrôles pertinents ; les moyens encore à construire restent explicites. Éviter de seulement renvoyer les décisions essentielles au prochain agent.

Distinguer les quatre responsabilités. Elles peuvent partager les mêmes fichiers et le même dépôt. Pour le mode léger, le manifeste peut prendre cette forme illustrative :

```json
{
  "schema_version": "0.3.0",
  "kind": "project-harness",
  "level": 0,
  "status": "PROPOSED",
  "profile": "profile.json",
  "generator": "Conception directe ; référence du brief et des graines à renseigner",
  "layout": "single-repo",
  "entrypoint": "AGENTS.md",
  "responsibilities": {
    "governance": "AGENTS.md",
    "stbl": "SPEC.md",
    "audit": "CHECKS.md",
    "product": "AGENTS.md"
  }
}
```

Les fichiers indiqués doivent exister. Adapter leurs noms au résultat ; trois fichiers ne sont pas un objectif. Copier le profil utilisé et remplacer la provenance descriptive par les sources réellement employées, sans inventer de filiation.

Le mode `four-repos` utilise `repositories` vers quatre dossiers distincts, chacun avec `AGENTS.md` et `README.md`, selon le [schéma N0](../schemas/project-harness.schema.json). Le choisir lorsque les exigences de séparation ou l'organisation le justifient. Les droits effectifs restent à configurer et à vérifier.

Tous les chemins internes sont relatifs, sans traversée ni lien symbolique. `.git` et `_eiffel` sont réservés aux outils. Examiner le résultat avec [03-qualify.md](03-qualify.md).

## Produire N1 seulement si son réemploi est utile

Nommer les situations répétées que N1 devra couvrir et la difficulté qu'il évitera. Si la raison se réduit à « respecter trois niveaux », produire N0 directement.

N1 fournit les fonctions GENERATE, CHECK et ADAPT, réunies ou séparées selon le besoin. Les instructions peuvent être reprises de graines existantes. Elles expliquent les indices qui changent la méthode, les invariants, le domaine de validité et les règles d'arrêt. Une stabilité justifiée reste possible.

Écrire le profil, les instructions, une spécification de sortie et un manifeste de cette forme :

```json
{
  "schema_version": "0.3.0",
  "kind": "meta-harness",
  "level": 1,
  "status": "PROPOSED",
  "profile": "profile.json",
  "entrypoint": "GENERATE.md",
  "prompts": ["GENERATE.md"],
  "output_contract": "SPEC.md",
  "source_pattern": "Eiffel++ 0.3.0 ; graines réellement utilisées à préciser"
}
```

Le fichier unique peut inclure les trois fonctions. Le nom machine `output_contract` désigne la spécification attendue, sans lui attribuer une preuve exécutable.

Examiner une variation pertinente du contexte : quelle décision changerait, et pourquoi ? Cette réflexion reste un examen argumenté. La capacité d'adaptation sera observée seulement lorsque N1 sera exécuté sur des situations distinctes. Appliquer ensuite son point d'entrée pour produire N0, dans le budget commun.
