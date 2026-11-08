# Choisir des graines et forger le harnais

## Mission

Produis le niveau autorisé à partir du besoin, du mandat et des ressources disponibles. Utilise le [cadre de conception](../CONTRACT.md). La sortie attendue est une méthode utilisable dans son périmètre, avec ses limites. Le parcours direct produit N0 ; la [cascade](../../protocol/CASCADE.md) stabilise N2, puis N1, puis N0 avec une boucle IA + essais + humain dans chacun.

En cascade, examiner le dossier de passage du niveau supérieur avant de produire son descendant adopté : exigences et critères identifiés, preuves, données et capacités disponibles, inconnues, stabilité et accord humain liés à la version. Des sondes isolées peuvent éprouver le niveau courant ; les nommer comme telles, sans fabriquer une autorisation de descente. Une absence de nouveauté avec une exigence manquante reste inconclusive.

## Choisir un point de départ

Lire l'index de la [base de graines](../../seeds/README.md), puis les fiches dont le contexte paraît pertinent. Vérifier les sources et révisions consultées, les capacités requises, les cas déconseillés et le niveau d'observation disponible.

Choisir un candidat principal ; ajouter une alternative seulement si elle permet de trancher un compromis matériel. Examiner une organisation plus simple qui conserve les mêmes obligations, moyens de contrôle et exigences d'indépendance.

Réemployer, paramétrer, composer ou inventer selon le besoin. Une graine peut convenir sans changement. La ressemblance textuelle, la popularité et le nombre d'agents ne prouvent pas l'adéquation. Une recette issue d'un runtime ne fournit pas automatiquement ses outils ou sa mémoire.

## Forger avec l'opérateur

Présenter un candidat concret : prochaine action, répartition du travail, sources à charger, contrôles, arrêts et décisions réservées. Expliquer brièvement ce qui est repris, supprimé, adapté ou ajouté, et son coût attendu. Ne pas fabriquer un gain chiffré.

Rendre visibles les choix sur lesquels une contribution humaine changerait la méthode. Intégrer les réponses et corrections effectivement reçues. Les choix déjà autorisés peuvent être exécutés sans nouvelle approbation ; la co-construction ne devient pas une validation systématique de chaque fichier.

Conserver la référence des arbitrages. Un candidat automatique ne devient pas « co-construit » du seul fait qu'un champ le dit. Une préférence exprimée par l'opérateur ne démontre pas que le harnais fonctionne mieux.

Enregistrer l'observation qui motive le candidat, l'hypothèse, le changement ou maintien, puis les preuves et la décision effectivement reçue. Conserver ces éléments avec les versions concernées dans l'[historique privé du projet](../../docs/HISTORY.md). Une synthèse de décisions suffit ; ne pas produire un journal de raisonnement interne ni publier automatiquement les échanges humains.

## Livrer la justification avec la génération

Pour chaque paquet produit, rédiger sa [note de conception](../../protocol/DESIGN.md) avec les instructions et scripts, puis référencer son chemin dans `design_rationale`. Rendre la note accessible depuis le point d’entrée. Partir des choix réellement retenus et de leurs sources, sans reconstituer un journal de délibération. Relier les décisions importantes aux qualités de génie logiciel qu’elles servent, à une alternative pertinente, aux contreparties et aux observations disponibles.

Donner à l’humain des points d’adaptation concrets : si telle exigence métier change, quels contrats, fichiers, rôles, skills et contrôles revoir, et quelle décision ou information est nécessaire ? Conserver les inconnues ; ne pas inventer de politique d’entreprise ou présenter un bénéfice attendu comme mesuré. N1 explique ce qui est stable et paramétrable ; N0 explique le lot effectivement livré. Une reprise de N0 met à jour ses motifs affectés au lieu de recopier ceux de N1.

## Produire N0

Un point d'entrée doit permettre de commencer le lot autorisé : contrat de référence, périmètre de modification, contrôle associé et condition de remise. Laisser le choix d'implémentation au produit. Référencer les obligations existantes au lieu de les recopier dans chaque consigne. Les moyens encore à construire restent explicites ; ne pas renvoyer toute la conception au prochain agent.

Traduire la revue [qualité](../QUALITY.md) en obligations et contrôles pertinents pour le lot. Conserver les limites et les décisions de report ; ne pas charger chaque agent d'une liste générique de quatorze injonctions. Une qualité examinée au cadrage n'est pas une qualité démontrée du logiciel.

Pour un problème identifié, préférer une procédure spécialisée avec déclencheur ou un auxiliaire déterministe à l'accumulation de consignes permanentes. Les champs facultatifs `components` et `experience` décrits dans [l'adaptation observée](../../protocol/ADAPTATION.md) permettent de conserver les dépendances, limites et observations. Ne pas inventer une expérience pour compléter le paquet.

Relier les tâches aux [capacités et skills](../../protocol/SKILLS.md). Le manifeste 0.8.0 contient `capabilities` pour les quatre responsabilités : une tâche et son skill concret, sa méthode native justifiée ou le moyen manquant. Réemployer un skill adéquat avant d’en écrire un. Livrer chaque skill utile avec sa méthode, ses contrats, ses ressources, ses ports d’entrée/sortie et ses destinataires ; la présence de SKILL.md seule ne satisfait pas ce besoin. Les scripts rendent les opérations déterministes vérifiables ; les instructions ne prouvent pas leur exécution.

Dans le point d’entrée, expliquer comment choisir la compétence, préparer ses entrées, examiner sa remise et poursuivre ou arrêter. Pour les missions instrumentées, le coordinateur conserve l’empreinte renvoyée par `skills.py prepare` et la transmet à verify/handoff. Une modification du plan ou des contrôles impose une nouvelle qualification ; ne pas recalculer l’empreinte pour faire disparaître STALE. Ne lancer ni quatre processus par défaut ni des boucles réinitialisant le budget.

Rendre concrets les échanges des quatre responsabilités : acteur effectif, entrées, remise, droits et indépendance. Une table courte peut suffire. Choisir le nombre d'agents selon ces exigences ; déclarer les cumuls et l'auto-examen lorsque le producteur examine son candidat. Une vérification automatique n'assure que la part de l'audit qu'elle couvre. Retirer une consigne redondante sans retirer le contrat qu'elle servait.

Les responsabilités peuvent partager les mêmes fichiers et le même dépôt. Le manifeste référence ces instructions, il ne les remplace pas. Pour le mode léger, il peut prendre cette forme illustrative :

```json
{
  "schema_version": "0.8.0",
  "kind": "project-harness",
  "level": 0,
  "status": "PROPOSED",
  "profile": "profile.json",
  "design_rationale": "DESIGN.md",
  "generator": "Conception directe ; référence du brief et des graines à renseigner",
  "layout": "single-repo",
  "entrypoint": "AGENTS.md",
  "responsibilities": {
    "governance": "AGENTS.md",
    "stbl": "SPEC.md",
    "audit": "CHECKS.md",
    "product": "AGENTS.md"
  },
  "capabilities": [
    {"role": "governance", "task": "Répartir le lot et décider la remise", "native": "Mandat et passation décrits dans AGENTS.md."},
    {"role": "stbl", "task": "Définir le comportement du lot", "native": "Contrat déjà explicite dans SPEC.md."},
    {"role": "audit", "task": "Examiner le candidat", "native": "Contrôles du lot décrits dans CHECKS.md."},
    {"role": "product", "task": "Réaliser la modification ciblée", "native": "Méthode disponible dans AGENTS.md pour ce lot simple."}
  ]
}
```

La note `DESIGN.md` de cet exemple de format reste à rédiger selon les décisions réelles ; aucun argument générique prérempli ne la remplace. En `four-repos`, placer la note dans une racine copiée, par exemple `governance/DESIGN.md`.

Les fichiers indiqués doivent exister et contenir les instructions ou références correspondantes. Quatre chemins valides, même identiques, ne prouvent pas que les responsabilités sont organisées. Adapter les noms au résultat ; trois fichiers ne sont pas un objectif. Copier le profil utilisé et renseigner les sources réellement employées.

Le mode `four-repos` utilise `repositories` vers quatre dossiers distincts, chacun avec `AGENTS.md` et `README.md`, selon le [schéma N0](../schemas/project-harness.schema.json). Le choisir lorsque les exigences de séparation ou l'organisation le justifient. Les droits effectifs restent à configurer et à vérifier.

Tous les chemins internes sont relatifs, sans traversée ni lien symbolique. `.git` et `_eiffel` sont réservés aux outils. Examiner le résultat avec [03-qualify.md](03-qualify.md).

## Contexte des reprises

Pour les reprises de contexte, transmettre le [contrat de mémoire](../../protocol/MEMORY.md) au niveau produit. N1 précise sources, natures, portées, dépendances, versions pertinentes et acteurs autorisés. GENERATE fournit à N0 la préparation/revalidation du contexte et l'adaptateur réellement disponible ; CHECK éprouve retrait d'une consigne et maintien d'une exigence ; ADAPT conserve la provenance et réexamine les descendants. N0 nomme ses commandes concrètes, l'emplacement privé du magasin et les ancres conservées par l'hôte. Si l'hôte ne peut empêcher la réinjection de l'ancien historique, déclarer cette capacité manquante. Ne pas embarquer le journal brut comme instructions ni ajouter cette infrastructure à un lot qui ne réutilise aucune mémoire.

## Produire N1 lorsque le parcours le demande

Nommer les situations répétées que N1 devra couvrir et la difficulté qu'il évitera. Si une cascade a été explicitement choisie, rendre ces décisions de méthode distinctes des principes N2 et des opérations N0 ; comparer leur utilité au parcours direct. Hors de ce mandat, si la raison se réduit à « respecter trois niveaux », produire N0 directement.

N1 demande explicitement à GENERATE de livrer la note N0, à CHECK de confronter ses motifs aux fichiers et au besoin, et à ADAPT de réviser les décisions affectées par les changements métier. Les productions de code sous N0 documentent aussi leurs décisions de conception utiles dans les documents du produit.

N1 fournit les fonctions GENERATE, CHECK et ADAPT, réunies ou séparées selon le besoin. Elles conservent les contrats du comportement et des responsabilités, leur domaine de validité et les règles d'arrêt ; elles indiquent ce qui ferait changer leur implantation. Une stabilité justifiée reste possible.

En cascade, GENERATE exige le passage valide avant la descente et livre avec N0 ses critères, rôles, skills et motifs. CHECK éprouve la suffisance, les remises, les inconnues et la stabilité sur une version précise, puis prépare la revue humaine. ADAPT rattache une correction au niveau qui la possède, invalide les résultats affectés et conserve l'historique. Le prompt ne peut ni se donner lui-même l'accord métier ni fermer le passage par une mention `PASS`.

N1 conserve une bibliothèque de skills justifiée par les tâches répétées du projet. GENERATE choisit les compétences du lot, leurs attributions et leurs dépendances ; CHECK éprouve leurs contrats et remises ; ADAPT révise seulement celles affectées. Tester au moins deux lots pertinents, dont un cas où une compétence est inutile ou indisponible. Le N0 livré reste utilisable sans relire N1. Ne remplacer ni le skill concret par sa description dans N1, ni une compétence manquante par une promesse de l’agent.

N1 conserve aussi le traitement des quatorze facteurs pour ce projet. GENERATE sélectionne leurs conséquences pour le lot, CHECK recherche les obligations perdues et ADAPT réexamine les facteurs touchés. Vérifier cette transmission sur des situations différentes ; ne pas confondre présence des noms et consignes utilisables.

Écrire le profil, les instructions, une spécification de sortie et un manifeste de cette forme :

```json
{
  "schema_version": "0.8.0",
  "kind": "meta-harness",
  "level": 1,
  "status": "PROPOSED",
  "profile": "profile.json",
  "design_rationale": "DESIGN.md",
  "entrypoint": "GENERATE.md",
  "prompts": ["GENERATE.md"],
  "output_contract": "SPEC.md",
  "source_pattern": "Eiffel++ 0.8.0 ; graines réellement utilisées à préciser",
  "capabilities": [
    {"role": "governance", "task": "Coordonner les lots couverts", "unavailable": "Méthode à définir dans GENERATE.md ; cet exemple donne seulement le format."},
    {"role": "stbl", "task": "Spécifier les lots couverts", "unavailable": "Sources et méthode à définir dans SPEC.md avant utilisation."},
    {"role": "audit", "task": "Qualifier les remises", "unavailable": "Moyens à définir avant utilisation ; cet exemple de format ne les fournit pas."},
    {"role": "product", "task": "Produire le candidat", "unavailable": "Compétences à choisir selon le projet ; cet exemple de format ne les fournit pas."}
  ]
}
```

Le fichier unique peut inclure les trois fonctions. Le nom machine `output_contract` désigne la spécification attendue, sans lui attribuer une preuve exécutable.

Examiner une variation pertinente du contexte : quelle décision changerait, et pourquoi ? Cette réflexion reste un examen argumenté. La capacité d'adaptation sera observée seulement lorsque N1 sera exécuté sur des situations distinctes. En cascade, qualifier N1, obtenir sa revue humaine et son passage avant d'appliquer son point d'entrée pour produire N0. Compter tout le travail, avec ou sans plafond commun.
