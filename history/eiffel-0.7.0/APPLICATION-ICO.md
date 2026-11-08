# ICO : comparaison locale de la cascade et du N0 direct

8 novembre 2026. **Les deux approches réussissent les mêmes critères sur les seize réalisations étudiées. Aucun avantage de qualité ou de robustesse de la cascade n’est observé dans ce périmètre.** Ses huit réalisations prennent 57 min 19 s, contre 50 min 46 s pour le direct : 6 min 33 s supplémentaires (+12,9 % par rapport au direct), hors construction.

Cette synthèse agrégée est partageable. Le code, les harnais, les décisions détaillées et les preuves brutes ICO restent dans le dépôt local privé, sans distant. Les résultats ne sont donc pas reproductibles depuis ce catalogue public seul. L’[état précédent](https://github.com/4nd4ny/Eiffel-plus-plus/blob/5717ed7fe06c842ffc5aab6649298fb6052a4cfd/history/eiffel-0.7.0/APPLICATION-ICO.md) et l’historique Git conservent le cheminement antérieur.

## Conditions

Le besoin retenu couvre trois corrections isolées et une suite du parcours import → recherche → réponse sourcée ou abstention, avec contrôle réseau. Données fictives et modèles simulés ; le parcours utilise le produit initial, sans intégrer les trois correctifs.

A suit N2 principes → N1 méthode → quatre N0 spécialisés, après les revues humaines N2 et N1. B construit directement un N0, itéré jusqu’à v6, avec sélection de la compétence utile. Une seule construction par approche ; deux réalisations neuves par tâche et approche, séquentielles et d’ordre alterné. Même configuration de modèle héritée, sans remplacement ni plafond commun ; identifiant résolu du modèle non exposé. Sources, contrats et moyens communs gelés avant les essais. Pilotes et solutions restent hors du contexte des réalisateurs ; aucun résultat réservé ne retourne à la construction.

Un exécutant tient les quatre responsabilités logiques. Son auto-examen est complété par l’évaluateur extérieur ; ce n’est pas une architecture de quatre agents indépendants. La revue extérieure est non aveugle : l’évaluateur connaît l’approche utilisée.

## Résultats

| Contrôle | Cascade | Direct |
|---|---:|---:|
| Cas visibles des corrections (12 cas × 2 réalisations) | 24/24 | 24/24 |
| Cas réservés des corrections (43 cas × 2 réalisations) | 86/86 | 86/86 |
| Suites parcours acceptées après revue | 2/2 | 2/2 |
| Ruptures métier détectées (4 par suite) | 8/8 | 8/8 |
| Injection réseau détectée | 2/2 | 2/2 |
| Témoin sans effet accepté | 2/2 | 2/2 |
| Intégrité et compilation diagnostique | PASS | PASS |

Chaque suite passe sur la référence. Les causes d’échec des variantes ont été examinées : les incidents d’environnement, sous-tests parents et échecs secondaires ne comptent pas comme détections supplémentaires. Un seul témoin sans effet est utilisé par suite ; aucune absence universelle de faux positifs n’est établie. La relecture des douze corrections observe des changements localisés et des API préservées, sans classement général de maintenabilité.

## Durées observées

Chaque cellule donne les répétitions 1 puis 2. Les intervalles vont de la préparation/dispatch à la notification de fin et comprennent lectures, outils et rédaction. Ce ne sont pas des temps d’inférence isolés.

| Travail | Cascade — R1 ; R2 | Direct — R1 ; R2 |
|---|---|---|
| Liens | 7 min 24 s ; 6 min 31 s | 5 min 31 s ; 5 min 24 s |
| Abstention et citations | 5 min 16 s ; 5 min 31 s | 5 min 16 s ; 4 min 49 s |
| Dates et heures | 7 min 07 s ; 7 min 11 s | 6 min 45 s ; 5 min 51 s |
| Suite du parcours complet | 6 min 27 s ; 11 min 52 s | 8 min 49 s ; 8 min 21 s |
| Total des huit réalisations | 57 min 19 s | 50 min 46 s |

La forte variation du parcours cascade interdit de retenir seulement son premier passage favorable. Deux réalisations par lot ne démontrent ni équivalence statistique ni supériorité générale.

## Coût et interprétation

Tokens, facturation et coût complet de construction restent **inconnus**. Les fenêtres de construction sont partielles : notamment 104,302 s pour fabriquer les quatre N0 cascade, 223,193 s pour leur revue après pilotes et 1 392 s de fenêtres de construction/relecture directe. Ces chiffres ne forment pas deux totaux comparables. Les pilotes, travaux communs et délais de réponse humaine ne sont pas ajoutés arbitrairement ; l’attention active de l’humain n’a pas été mesurée.

Les mêmes cas sont répétés ; aucune tâche tenue à l’écart de la construction n’a été étudiée. Le comparateur possède un harnais. Le découpage en niveaux varie aussi avec l’organisation du paquet et les auxiliaires de remise : leur effet causal n’est pas isolé. Les modèles réels, l’interface, la synchronisation, le déploiement et la protection contre toutes les voies réseau restent hors qualification.

Le retour humain a élargi le périmètre après une présentation plus compréhensible du besoin. Les auxiliaires générés ont nécessité leurs propres corrections et essais. Un relevé N2 partiel, conservé sous un horodatage ultérieur, a motivé une précision du [prompt de qualification](../../meta/prompts/03-qualify.md) sur les bornes des durées et les coûts inconnus. Ces observations améliorent le processus de revue ; elles ne prouvent pas que trois niveaux produisent un meilleur logiciel.

Conserver le parcours N0 direct et demander une raison concrète de réemploi à N1 reste cohérent avec l’intention de minimalité. L’effet des auxiliaires ou le transfert à de nouvelles tâches seraient des questions distinctes à éprouver.

## Acceptation après revue des résultats

Le 8 novembre 2026, après présentation de cette comparaison et de ses limites, l’utilisateur a explicitement accepté les quatre N0 cascade dans le périmètre testé. La décision a été liée au dernier cycle conservé dans le journal privé ; le contrôle de passage a été satisfait et N0 a été clôturé. La vérification du journal confirme cette clôture. Les artefacts et preuves évalués sont inchangés.

Cette acceptation porte sur les quatre travaux dans l’environnement préparé, avec données fictives et modèles simulés. Elle ne qualifie ni l’ensemble d’ICO ni un déploiement et ne démontre aucun avantage de qualité de la cascade. Le journal distinct d’auto-application d’Eiffel++ reste dans son état antérieur. Les pièces détaillées de décision demeurent privées ; l’[état publié avant cette réponse](https://github.com/4nd4ny/Eiffel-plus-plus/blob/87d88b97432f3ead66dc0cf0836880353578072b/history/eiffel-0.7.0/APPLICATION-ICO.md) conserve la revue encore ouverte.
