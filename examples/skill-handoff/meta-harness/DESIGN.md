# Pourquoi ce générateur CSV

Le [profil](profile.json) et le [contrat CSV](SPEC.md) décrivent un exemple fictif local. Deux usages récurrents motivent N1 : produire puis examiner un tableau, ou examiner un candidat déjà fourni. Aucune entreprise réelle n'a accepté ces règles ; ses politiques de données, d'accès et de livraison restent à fournir avant un usage concerné.

## Choix structurants

**Conserver deux compétences distinctes.** `filter-rows` produit un candidat ; `check-rows` le compare aux entrées de référence. Cette frontière rend l'oracle réutilisable sans production et permet de tester les deux méthodes séparément. Une compétence unique aurait moins de remises, mais chargerait la production dans le lot d'examen seul. Les scripts ne s'appellent pas entre eux ; leur auteur commun ne constitue pas une indépendance d'audit.

**Garder un seul paquet et des rôles logiques.** Les fichiers sont locaux, le contrat est petit et le mandat ne demande pas de séparation organisationnelle. Quatre dépôts ajouteraient ici de la coordination sans établir de droits distincts. Ce choix devra changer si l'examen indépendant devient une obligation effective.

**Conserver un contrat commun et sélectionner par lot.** `GENERATE.md` choisit les compétences et `capabilities` décrit leurs attributions. En mode examen seul, Produit identifie le fichier reçu avec une méthode native ; Audit conserve les mêmes exigences. N1 évite de redéfinir ce choix pour chaque lot, mais son avantage économique n'est pas mesuré : pour un usage unique, une génération directe de N0 serait suffisante.

**Identifier les missions avant remise.** Les empreintes lient règles, candidat et outils ; elles servent la vérifiabilité et le refus de résultats périmés. Elles n'attestent ni la qualité du besoin ni l'identité des acteurs. La sélection des lignes, leur ordre et leur multiplicité demeurent les postconditions à examiner, même si la remise mécanique réussit.

## Adapter aux exigences de l'entreprise

| Changement du besoin | Où intervenir et quoi vérifier |
| --- | --- |
| Nouvelle catégorie, format inchangé | Règles d'entrée du lot ; conserver les skills et tester la sélection, notamment vide. |
| Format, encodage ou règle de sélection différents | SPEC.md, scripts des deux skills, puis cas normaux et invalides. Réviser GENERATE/CHECK et les notes N0 concernées. |
| Examen par un responsable distinct requis | Instructions de rôles, attributions et environnement d'identités ; vérifier la séparation effective avant de la revendiquer. |
| Volume nécessitant un traitement progressif | Mesurer d'abord la charge et la limite ; réexaminer les deux scripts, actuellement fondés sur une lecture en mémoire, et leurs tests. Aucun seuil accepté n'est connu. |
| Règles de confidentialité ou de livraison nouvelles | Mettre à jour le mandat du profil et les moyens concernés ; identifier la décision compétente. La note seule ne permet pas une sortie de données ou un déploiement. |

Les [contrôles de génération](CHECK.md) doivent confronter ces motifs au N0 obtenu et à une variation utile. Les tests déterministes établissent un comportement borné ; ils ne démontrent pas le gain de performance d'un LLM. [ADAPT.md](ADAPT.md) indique comment réviser les compétences et leurs justifications ensemble.
