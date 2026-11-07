# Forger un harnais à partir des spécifications

**Point d'entrée du prototype Eiffel++ 0.6.0.** Donner ce prompt à l'agent avec le brief, les sources utiles et, s'il existe, le profil du projet. L'efficacité de cette méthode de conception n'a pas encore été évaluée sur la production de logiciels.

## Mission

Produis un harnais N0 assez concret pour commencer le travail autorisé. Pars des spécifications du produit et des conditions de sa production : budget, outils, compétences, décisions réservées et manière de reconnaître un résultat acceptable.

L'intention est le harnais minimal suffisant : relier le contrat du comportement, sa réalisation et sa vérification, en conservant les quatre responsabilités. Choisir les agents selon le travail et l'indépendance nécessaires. Retirer les répétitions et les étapes sans effet utile ; la longueur et le nombre d'agents ne sont pas des objectifs. Comparer à une référence explicite avant de revendiquer un bénéfice.

Recherche une graine pertinente, puis réemploie-la, adapte-la ou compose plusieurs mécanismes. Une organisation inchangée peut être le bon résultat. Invente seulement ce que les ressources disponibles ne couvrent pas. Un générateur spécialisé N1 est facultatif ; il doit avoir un réemploi attendu qui justifie sa conception.

## Parcours court

1. **Comprendre ce qui compte.** Utiliser [01-characterize.md](prompts/01-characterize.md) et les [repères de qualité du logiciel](QUALITY.md). Exploiter les décisions existantes et isoler les inconnues qui changeraient réellement la méthode. Des priorités verbales et des plafonds suffisent ; ne pas fabriquer des coefficients.
2. **Chercher un point de départ.** Parcourir l'index de la [base de graines](../seeds/README.md), puis lire seulement les fiches candidates. Examiner leur contexte, leurs sources, leurs limites et les capacités nécessaires. Une source inspectée n'est pas un harnais évalué dans ce projet.
3. **Forger un candidat.** Appliquer [02-generate-meta-harness.md](prompts/02-generate-meta-harness.md). Fournir N0 directement lorsque cela suffit. Présenter les choix qui comptent pour l'opérateur : organisation du travail, contrôles, attention humaine, coût attendu et inconnues. Proposer une variante seulement si elle aide à trancher un vrai désaccord.
4. **Co-construire et examiner.** Intégrer les corrections et arbitrages effectivement donnés par l'opérateur, puis utiliser [03-qualify.md](prompts/03-qualify.md). Une décision déjà acquise n'est pas redemandée. Une revue textuelle ne devient pas un résultat d'exécution.
5. **Employer, observer et conserver.** Commencer le lot autorisé, relever ce qui se passe et appliquer [04-adapt.md](prompts/04-adapt.md) si nécessaire. Lorsque l'opérateur choisit de conserver l'instance, enregistrer sa provenance, le harnais effectif et les observations disponibles dans une nouvelle graine.

Ces fonctions peuvent tenir dans une séance. La co-construction exige une contribution humaine identifiable ; ne pas l'inventer pour remplir une fiche. Une instance peut être conservée comme non testée. L'essai et son résultat restent distincts de son adoption.

Dans une préparation exportée, l'index des graines indique les seules fiches fournies ou l'absence de sélection. Ne pas supposer que le catalogue complet ou les artefacts référencés sont disponibles. Conserver N0 dans un dossier distinct du paquet d'entrée.

## Ce qui doit rester explicite

Le [cadre de conception](CONTRACT.md) conserve le besoin, les droits et les limites des résultats. Les [arbitrages](TETRAHEDRON.md) guident les choix. Le [protocole](../protocol/README.md) fournit les états et références lorsqu'ils sont nécessaires.

N0 rend utilisables les échanges entre gouvernance, STBL, audit et produit décrits dans le [cadre de conception](CONTRACT.md) : entrées, remise attendue, responsable et droits. Elles peuvent partager fichiers, dépôt ou agent ; annoncer le degré d'indépendance réellement obtenu. Quatre noms dans un manifeste ne suffisent pas à organiser le travail.

Déduire les [capacités et skills](../protocol/SKILLS.md) des tâches : opération, responsabilité, méthode disponible ou manquante, remise et destinataire. N1 conserve les compétences réemployables et N0 embarque celles utiles au lot. Éprouver au moins une mission réelle et sa passation avant de revendiquer le fonctionnement de cette orchestration.

Produire en même temps que les instructions et scripts du niveau suivant sa [note de conception](../protocol/DESIGN.md) : choix effectifs, motifs, compromis, limites et points d’adaptation métier. Chaque N1 et N0 a sa propre note ; elle doit permettre à l’humain de comprendre et modifier la méthode sans retrouver la conversation d’origine.

Conserver un point d'entrée court, le profil utilisé, les graines sources et les raisons des adaptations. Un manifeste décrit les fichiers produits ; il ne prouve ni leur qualité ni les mécanismes qu'ils prescrivent. Les contrôles prévus mais non exécutés restent `NOT_RUN`.

## Budget et arrêt

Compter le travail de conception, les échanges humains, les essais et les révisions. Sans borne donnée, proposer un candidat principal et au plus une alternative motivée, puis une revue de cohérence. Ne pas réinitialiser le budget en changeant d'agent ou de niveau.

S'arrêter lorsqu'une organisation utilisable répond au besoin dans le mandat, ou lorsqu'un conflit précis empêche la suite. Ne pas prolonger la conception pour rendre le dispositif plus impressionnant. Une nouvelle procédure doit changer une décision, prévenir un défaut pertinent ou réduire un travail identifié.
