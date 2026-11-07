# Choisir des graines et forger le harnais

## Mission

Produis N0 à partir du besoin, du mandat et des ressources disponibles. Utilise le [cadre de conception](../CONTRACT.md). La sortie attendue est une méthode utilisable dans son périmètre, avec ses limites ; N1 est une option de réemploi, pas une étape obligatoire.

## Choisir un point de départ

Lire l'index de la [base de graines](../../seeds/README.md), puis les fiches dont le contexte paraît pertinent. Vérifier les sources et révisions consultées, les capacités requises, les cas déconseillés et le niveau d'observation disponible.

Choisir un candidat principal ; ajouter une alternative seulement si elle permet de trancher un compromis matériel. Examiner une organisation plus simple qui conserve les mêmes obligations, moyens de contrôle et exigences d'indépendance.

Réemployer, paramétrer, composer ou inventer selon le besoin. Une graine peut convenir sans changement. La ressemblance textuelle, la popularité et le nombre d'agents ne prouvent pas l'adéquation. Une recette issue d'un runtime ne fournit pas automatiquement ses outils ou sa mémoire.

## Forger avec l'opérateur

Présenter un candidat concret : prochaine action, répartition du travail, sources à charger, contrôles, arrêts et décisions réservées. Expliquer brièvement ce qui est repris, supprimé, adapté ou ajouté, et son coût attendu. Ne pas fabriquer un gain chiffré.

Rendre visibles les choix sur lesquels une contribution humaine changerait la méthode. Intégrer les réponses et corrections effectivement reçues. Les choix déjà autorisés peuvent être exécutés sans nouvelle approbation ; la co-construction ne devient pas une validation systématique de chaque fichier.

Conserver la référence des arbitrages. Un candidat automatique ne devient pas « co-construit » du seul fait qu'un champ le dit. Une préférence exprimée par l'opérateur ne démontre pas que le harnais fonctionne mieux.

## Produire N0

Un point d'entrée doit permettre de commencer le lot autorisé : contrat de référence, périmètre de modification, contrôle associé et condition de remise. Laisser le choix d'implémentation au produit. Référencer les obligations existantes au lieu de les recopier dans chaque consigne. Les moyens encore à construire restent explicites ; ne pas renvoyer toute la conception au prochain agent.

Traduire la revue [qualité](../QUALITY.md) en obligations et contrôles pertinents pour le lot. Conserver les limites et les décisions de report ; ne pas charger chaque agent d'une liste générique de quatorze injonctions. Une qualité examinée au cadrage n'est pas une qualité démontrée du logiciel.

Pour un problème identifié, préférer une procédure spécialisée avec déclencheur ou un auxiliaire déterministe à l'accumulation de consignes permanentes. Les champs facultatifs `components` et `experience` décrits dans [l'adaptation observée](../../protocol/ADAPTATION.md) permettent de conserver les dépendances, limites et observations. Ne pas inventer une expérience pour compléter le paquet.

Rendre concrets les échanges des quatre responsabilités : acteur effectif, entrées, remise, droits et indépendance. Une table courte peut suffire. Choisir le nombre d'agents selon ces exigences ; déclarer les cumuls et l'auto-examen lorsque le producteur examine son candidat. Une vérification automatique n'assure que la part de l'audit qu'elle couvre. Retirer une consigne redondante sans retirer le contrat qu'elle servait.

Les responsabilités peuvent partager les mêmes fichiers et le même dépôt. Le manifeste référence ces instructions, il ne les remplace pas. Pour le mode léger, il peut prendre cette forme illustrative :

```json
{
  "schema_version": "0.4.0",
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

Les fichiers indiqués doivent exister et contenir les instructions ou références correspondantes. Quatre chemins valides, même identiques, ne prouvent pas que les responsabilités sont organisées. Adapter les noms au résultat ; trois fichiers ne sont pas un objectif. Copier le profil utilisé et renseigner les sources réellement employées.

Le mode `four-repos` utilise `repositories` vers quatre dossiers distincts, chacun avec `AGENTS.md` et `README.md`, selon le [schéma N0](../schemas/project-harness.schema.json). Le choisir lorsque les exigences de séparation ou l'organisation le justifient. Les droits effectifs restent à configurer et à vérifier.

Tous les chemins internes sont relatifs, sans traversée ni lien symbolique. `.git` et `_eiffel` sont réservés aux outils. Examiner le résultat avec [03-qualify.md](03-qualify.md).

## Produire N1 seulement si son réemploi est utile

Nommer les situations répétées que N1 devra couvrir et la difficulté qu'il évitera. Si la raison se réduit à « respecter trois niveaux », produire N0 directement.

N1 fournit les fonctions GENERATE, CHECK et ADAPT, réunies ou séparées selon le besoin. Elles conservent les contrats du comportement et des responsabilités, leur domaine de validité et les règles d'arrêt ; elles indiquent ce qui ferait changer leur implantation. Une stabilité justifiée reste possible.

N1 conserve aussi le traitement des quatorze facteurs pour ce projet. GENERATE sélectionne leurs conséquences pour le lot, CHECK recherche les obligations perdues et ADAPT réexamine les facteurs touchés. Vérifier cette transmission sur des situations différentes ; ne pas confondre présence des noms et consignes utilisables.

Écrire le profil, les instructions, une spécification de sortie et un manifeste de cette forme :

```json
{
  "schema_version": "0.4.0",
  "kind": "meta-harness",
  "level": 1,
  "status": "PROPOSED",
  "profile": "profile.json",
  "entrypoint": "GENERATE.md",
  "prompts": ["GENERATE.md"],
  "output_contract": "SPEC.md",
  "source_pattern": "Eiffel++ 0.4.0 ; graines réellement utilisées à préciser"
}
```

Le fichier unique peut inclure les trois fonctions. Le nom machine `output_contract` désigne la spécification attendue, sans lui attribuer une preuve exécutable.

Examiner une variation pertinente du contexte : quelle décision changerait, et pourquoi ? Cette réflexion reste un examen argumenté. La capacité d'adaptation sera observée seulement lorsque N1 sera exécuté sur des situations distinctes. Appliquer ensuite son point d'entrée pour produire N0, dans le budget commun.
