# Le tétraèdre des arbitrages

La position dans le tétraèdre exprime ce que le projet privilégie. Elle guide la génération du harnais ; elle ne constitue pas une mesure de sa performance.

## Quatre sommets, une convention explicite

| Sommet | Clé machine | Ce que l'on cherche à favoriser | Mesures possibles |
| --- | --- | --- | --- |
| Rapidité | `speed` | Une livraison utile dans le délai souhaité. | Temps jusqu'à acceptation, délai des décisions, temps de reprise. |
| Économie | `economy` | Une consommation maîtrisée des ressources. | Coût des modèles, calcul, outils et infrastructure ; coût de génération et de maintenance du harnais. |
| Fonctionnalités | `scope` | La valeur fonctionnelle effectivement acceptée. | Utilité des besoins satisfaits, pondérée selon leur importance ; couverture du périmètre attendu. |
| Autonomie | `autonomy` | Une charge humaine réduite dans le mandat choisi. | Minutes de supervision, interruptions, décisions sollicitées, délai d'attente humaine. |

La convention du quatrième axe est « autonomie utile croissante ». Un projet qui souhaite un contrôle humain actif l'exprime dans sa politique de délégation et ses critères d'usage. Accorder davantage de permissions n'est pas en soi une amélioration de cet axe.

L'autonomie effective dépend aussi de la capacité à détecter ses limites et à demander la bonne décision. Un agent silencieux qui abandonne des obligations ne devient pas autonome au sens du projet.

## Coordonnées de préférence

Le profil contient quatre poids finis, positifs ou nuls, dont la somme vaut 1 :

\[
w_R+w_C+w_F+w_A=1.
\]

Le point de préférence est le barycentre des sommets avec ces poids. Une position proche du sommet rapidité donne davantage d'importance au délai dans les arbitrages permis. Elle ne prescrit ni un nombre d'agents, ni une taille de contexte, ni une méthode de développement.

Fragment illustratif de `preferences`, à compléter par les mesures du profil :

```json
{
  "weights": {
    "speed": 0.40,
    "economy": 0.20,
    "scope": 0.25,
    "autonomy": 0.15
  },
  "status": "PROPOSED",
  "source": "Exemple illustratif ; ne décrit pas les préférences d'un client réel."
}
```

Les poids exacts ne sont pas obligatoires dans la demande initiale. Le générateur peut proposer une traduction d'une préférence verbale, en la marquant comme telle. Si plusieurs traductions changeraient la méthode, il montre cet effet ou pose une question ciblée.

Les poids peuvent différer selon les phases ou les familles de tâches. Dans ce cas, N1 explicite leurs conditions d'application et conserve un profil identifiable pour chaque N0 engendré. Ils ne changent pas discrètement pour rendre un résultat plus favorable.

## Mesures et utilité

`preferences.measures` documente une mesure principale pour chaque axe : `metric`, `unit`, `direction` (`minimize` ou `maximize`) et éventuellement `target`. Des mesures secondaires peuvent compléter l'interprétation.

Par convention, `economy` suit les ressources techniques ; `autonomy` suit l'attention humaine. Le coût économique total peut aussi monétiser cette attention, mais il faut alors expliciter le recouvrement des deux axes pour éviter un double comptage involontaire.

`scope` ne compte pas simplement les fonctionnalités. Une capacité essentielle peut valoir davantage que dix accessoires. Les obligations fonctionnelles minimales constituent des contraintes ; les autres éléments peuvent contribuer à une utilité pondérée acceptée. Un périmètre partiel ne devient pas complet parce que son score est élevé.

Si les échelles et leurs points d'ancrage sont définis, une utilité de comparaison peut prendre la forme :

\[
U(h\mid p,x)=\sum_{i\in\{R,C,F,A\}} w_i\,u_i(m_i(h,x)),
\]

où `h` est le harnais, `p` le profil, `x` le contexte, `m` une mesure et `u` sa conversion en utilité comparable. Cette fonction n'est employée qu'entre candidats satisfaisant les contraintes applicables. Les échelles et leur sens doivent rester fixes pendant une comparaison.

En l'absence de mesures ou d'échelles justifiées, garder une comparaison qualitative et des attentes explicites. Ne pas inventer des gains chiffrés pour calculer un score. Le générateur peut néanmoins choisir un premier harnais cohérent avec le besoin et le mandat.

## Une préférence ne définit pas à elle seule une solution

Deux projets au même barycentre peuvent exiger des harnais différents. Le domaine, les risques, les outils, l'historique, la réversibilité et les compétences disponibles déterminent ce qui est possible et pertinent.

Le tétraèdre représente donc l'intention d'arbitrage. L'ensemble des performances réalisables peut être irrégulier et évolue avec le projet. Une variante peut améliorer plusieurs axes à la fois, par exemple en remplaçant une vérification répétitive par un contrôle mécanique.

Le générateur doit relier chaque choix important à une condition du contexte et à un effet attendu, puis indiquer ce qui permettrait de le réviser. L'objectif est une adaptation justifiable, sans prétendre déduire mécaniquement un harnais optimal de quatre coefficients.
