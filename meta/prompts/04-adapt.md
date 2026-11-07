# Adapter une instance et enrichir la base de graines

## Mission

À partir d'un changement ou d'observations, modifier la partie utile du harnais. Conserver le [cadre de conception](../CONTRACT.md), les décisions acceptées et le budget restant. La méthode peut être simplifiée ou conservée sans changement.

## Choisir la transformation

| Situation | Suite possible |
| --- | --- |
| Un paramètre ou une procédure locale ne convient plus. | Modifier N0 dans le mandat et reprendre les contrôles concernés. |
| Une nouvelle tâche reste proche d'une instance disponible. | Réemployer ou adapter cette graine, directement ou avec N1 si ce générateur existe. |
| Des situations récurrentes imposent de refaire les mêmes décisions de méthode. | Examiner si un N1 réutilisable apporterait quelque chose ; ne pas le créer automatiquement. |
| N1 ne couvre plus le domaine ou coûte plus qu'il ne rapporte. | Le réviser, revenir au patron N2 ou conserver une conception directe de N0. |
| Le besoin ou les droits doivent changer. | Préparer la décision compétente et poursuivre les parties déjà autorisées. |

Une nouvelle préférence n'impose pas une nouvelle organisation. Distinguer l'observation de son explication supposée. Plusieurs relances du même échec ne sont pas plusieurs confirmations indépendantes. Une erreur rare mais grave peut compter davantage qu'un inconfort fréquent.

Pour une adaptation motivée par l'exécution, conserver l'observation et sa référence, formuler une hypothèse et l'effet attendu avant l'essai. Préparer le plus petit changement pertinent. Comparer à la version de départ avec les mêmes informations utiles ; conserver aussi les régressions et l'absence de différence. Les [composants et fiches d'expérience](../../protocol/ADAPTATION.md) peuvent être joints au paquet, sans imposer un essai à toute modification documentaire.

## Co-construire la révision

Montrer à l'opérateur le changement concret, sa raison, les effets attendus et les conséquences sur son travail. Solliciter les choix qui ne sont pas déjà délégués ; appliquer les corrections autorisées. Consigner les contributions réellement reçues et les inconnues restantes.

Garder la version de départ et les résultats associés. Préciser le devenir du travail en cours. Une règle nouvelle n'est pas appliquée rétroactivement à un ancien rapport. Un profil révisé et les paquets qui l'emploient doivent rester cohérents ; si N1 est archivé avec N0, leurs profils correspondent.

Pour une écriture partagée, utiliser un mécanisme conditionnel disponible qui vérifie la révision attendue. Calculer deux hashes dans un prompt ne remplace pas une opération atomique. En cas de conflit, relire et réévaluer la partie concernée.

## Capturer ce qui mérite d'être réutilisé

Lorsque l'opérateur choisit de conserver l'instance, préparer une fiche selon la [base de graines](../../seeds/README.md). Elle décrit :

- les sources et graines parentes, avec leurs versions lorsqu'elles sont connues ;
- les conditions d'emploi, capacités nécessaires, limites et situations où éviter l'instance ;
- les choix de travail réellement retenus et les contributions humaines identifiables ;
- les observations et références d'essais disponibles, ou l'absence d'essai ;
- les conditions de réutilisation, licence et confidentialité.

Le type `co-designed-instance` exige une co-construction réelle. `review.status: co-designed` et sa `decision_ref` décrivent cette provenance ; le script ne l'authentifie pas. L'adoption est une décision distincte. `evidence.level` conserve le niveau effectivement établi : `untested` sans essai, `local-observation` avec observations situées, `comparison` avec comparaison documentée. Une source lue reste `source-inspected` ; un exemple rédigé reste `illustrative`.

Pour capturer un paquet N0 existant depuis la racine du catalogue :

```bash
python3 tools/seeds.py capture ../mon-harnais --record ../fiche-instance.json --output ../ma-graine
```

La commande conserve le paquet et sa fiche avec une empreinte ; elle ne publie rien et ne produit aucun verdict. Examiner les données avant d'intégrer l'instance dans une base partagée. Un contenu privé n'est pas rendu public par son adaptation ou sa reformulation. Les notes de séance complètes ne sont pas nécessaires à la réutilisation.

## Apprendre sans accumuler

Une observation favorable ne garantit pas le transfert. Réexaminer les conditions au prochain emploi. Conserver les échecs, les coûts et les contre-indications ; éviter les doublons sans différence utile. La suppression d'une procédure inutile est une amélioration possible.

Arrêter les révisions sans information nouvelle. Un changement d'agent, de séance ou de niveau ne recrée pas le budget. Ne lancer une comparaison que si elle peut trancher une question encore pertinente ; ne présenter aucune attente comme un gain observé.

Conserver la sortie de référence parmi les options lorsqu'elle satisfait encore les critères applicables. Une adaptation sans gain établi ne l'emporte pas par sa seule nouveauté. Ne jamais réutiliser une référence invalide, un contrôle périmé ou un artefact différent de celui qui a été évalué. Vérifier toute composition nouvelle avant de la remettre.
