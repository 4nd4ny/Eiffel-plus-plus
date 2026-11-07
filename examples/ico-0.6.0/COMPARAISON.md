# Comparaison des harnais ICO

**La 0.6.0 réunit le cycle complet, les missions à compétences et les justifications. Sa robustesse mécanique est mieux intégrée ; aucune amélioration de la qualité du code produit par un LLM n’est démontrée.** La référence ICO est inchangée.

## Comparaison avec les tentatives précédentes

| Version | Ce qu’elle apportait déjà | Différence de cette régénération |
| --- | --- | --- |
| H6 initial | Rôles, contrôles, vérification de sources ; dépendances externes | Paquet de consignes transportable, runtime explicite et remises instrumentées. Ancien lanceur non relancé pour préserver ses emplacements de preuves. |
| Diagnostic observé 0.4 | Contrôles figés, sélection conservatrice de deux modules | Mêmes onze sondes réemployées ; sélection d’une copie complète de 644 fichiers, avec portée du verdict toujours limitée. |
| N0 complet 0.4 | Cycle de lot, gel du code complet, cadre et contrôles | Ces protections ne sont pas nouvelles. La 0.6 les associe aux compétences, aux ports de remise et aux notes de conception identifiées. |
| Consigne de 99 mots | Entrée très courte, contrôle fourni par l’environnement | N0 porte ici ses moyens et ses échanges ; longueur non comparable à périmètre différent. Les essais LLM n’ont pas été repris. |
| N1 Meyer et deux N0 | Contrats par lot, décisions sur les quatorze facteurs, rôles concrets | Rétablissement du refus d’un oracle ou plan modifié : enregistrer un nouveau hash ne suffit plus. Les régressions mécaniques observées auparavant ne sont pas reproduites dans les cas testés. |
| Missions 0.5 | Compétences assignées et remises refusant un contexte modifié | Ce mécanisme est conservé ; ajout des justifications 0.6, d’un atelier complet et de la sélection avec référence. Ce n’est pas une découverte nouvelle des empreintes. |

La comparaison des versions anciennes autres que le diagnostic 0.4 s’appuie sur leurs fichiers et résultats conservés. Seuls le diagnostic historique et le nouveau dispositif sont rejoués ici sur les mêmes octets. Les niveaux N1/N0 et les tests publics sont disponibles ; le produit et ses preuves brutes restent privés.

## Observations de la campagne de livraison

- **Même diagnostic : 9 PASS et 2 FAIL sur 11 sondes.** Les deux échecs concernent des renforcements proposés ; ils ne deviennent pas des obligations par la seule présence d’un test. Aucune amélioration du produit de référence.
- **Référence inchangée : KEEP_BASE. Régression injectée : KEEP_BASE. Restauration du défaut injecté : ADOPT**, avec les 644 fichiers conservés et une copie restaurée identique à la référence saine. Ce dernier cas qualifie la sélection ; il ne prouve pas la découverte d’un défaut réel par un agent.
- **Interface sans navigateur : INCONCLUSIVE.** La variante N0 Interface sélectionne sa compétence propre, mais aucune exécution UI ni conformité d’accessibilité n’est revendiquée.
- **Huit altérations refusées sur ICO** : justification, rôle, skill, contrat, plan, oracle, fichier de référence hors des deux modules et reçu du lot. La qualification publique ajoute ajouts/suppressions du candidat, liens, critères incomplets, dépendance absente et mauvaises remises.
- **14 tests spécifiques à l’exemple ; 84 tests du dépôt réussis.** Les sept SKILL.md passent leur validation. N1, N0 complet et les variantes Import/Interface passent les contrôles structurels ; la matérialisation conserve les deux notes N1/N0. Les quatorze décisions qualité restent accessibles dans chaque variante.
- Les scénarios de modification exercent **six missions et six remises** avec les quatre responsabilités ; le diagnostic sans édition utilise cinq missions et une capacité native Produit. Un seul acteur réalise et examine le travail. Les sources historiques contrôlées sont inchangées.

## Temps et coût observés

| Mesure locale | Résultat |
| --- | --- |
| Diagnostic historique direct, médiane de trois passages | 0.157 s |
| Évaluation 0.6 complète avec copies et vérifications, même oracle, médiane de trois passages | 0.759 s |
| Cycle référence, missions et sélection incluses | 7.004 s |
| Cycle régression injectée | 4.883 s |
| Cycle restauration | 4.607 s |
| Appels de modèle des scripts d’essai | 0 ; coût API de ces appels : 0 USD |
| Coût de génération dans cette conversation, tokens et coût machine | Non instrumentés ; inconnus |

Les [mesures](RESULTATS.json) proviennent de la campagne de livraison sur macOS. Python 3.14.0 et Node 20.17.0 ont exécuté ces sondes pures. Le produit déclare Node >=22 : son environnement supporté et ses suites complètes ne sont donc pas qualifiés ici. Trois paires à ordre fixe ne constituent pas une étude statistique. L’ancienne mesure est un diagnostic direct ; la nouvelle fait davantage de travail. **Aucun gain de vitesse n’est observé ni revendiqué.** Les campagnes intermédiaires et leurs échecs de préparation sont conservés localement ; le premier démarrage de la garde macOS a échoué dans l’environnement imbriqué, puis la garde a fonctionné dans l’exécution autorisée. Aucun repli sans garde n’a servi à qualifier ICO.

## Valeur et limites

La plus-value est concrète : le coordinateur sait quelle méthode charger, quelles pièces attendre et quand une preuve n’est plus valable ; l’humain peut lire pourquoi ces choix ont été faits et quels fichiers changer si son contexte métier évolue. L’oracle et les critères restent les points décisifs : un mauvais contrat bien tracé reste un mauvais contrat.

Le harnais est plus complet, pas prouvé optimal. N0 contient 22 fichiers : 207 mots au point d’entrée et 3 878 mots Markdown au total, comptés par espaces, hors manifeste et code. Ce ne sont pas des tokens effectivement lus. Les rôles et compétences ajoutent donc une charge documentaire réelle, à justifier par leurs remises et contrôles. Sept compétences ne signifient pas sept agents ; leurs textes sont chargés à la demande. La duplication de N1/N0 et les copies complètes ont un coût. Prochaine simplification justifiée par mesure : éviter les copies redondantes sans perdre l’identité des artefacts. Ne pas supprimer les contrats ou contrôles pour gagner des mots.

La qualité globale d’ICO, la supériorité face à un agent sans harnais, la rapidité d’un modèle et le coût total de production restent **non mesurés**. Les dix-huit essais LLM précédemment refusés sont restés suspendus. L’exécution décrite ici est une application des prompts par le même assistant et des tests déterministes, pas une comparaison indépendante à modèle et budget égaux.
