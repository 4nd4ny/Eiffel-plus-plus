# Travailler sur ICO

Lire le mandat du lot, [ROLES.md](ROLES.md) et la compétence correspondante dans le manifeste. La [note de conception](DESIGN.md) explique les choix et leur adaptation métier. Le code demeure dans une copie de travail séparée de ce paquet.

1. Gouvernance borne le lot, choisit les acteurs et conserve les empreintes. STBL relie les comportements dus à leurs sources. Audit fixe les critères avant la modification.
2. Produit utilise la compétence moteur ou interface ; il remet un candidat complet, sa justification et ses limites. Audit vérifie ce candidat et remet les observations à Gouvernance.
3. Gouvernance conserve la référence en cas d’égalité, de régression ou d’incertitude. Une sélection expérimentale ne vaut ni adoption métier ni déploiement.

[DEMARRER.md](DEMARRER.md) donne les commandes ; [CONTRAT.md](CONTRAT.md) les invariants ; [ROUTAGE.md](ROUTAGE.md) les chemins et moyens du produit ; [QUALITE.md](QUALITE.md) les décisions par facteur.

Un seul acteur peut assumer les quatre responsabilités dans ce mandat : déclarer alors l’auto-examen. Aucun fichier ne crée de droits ni de nouveaux agents. STALE impose un nouveau lot qualifié ; ne pas réécrire l’empreinte attendue pour faire passer une modification. Un contrôle manquant reste NOT_RUN ou UNKNOWN. Deux cycles de correction au maximum par lot, puis bilan des écarts ; aucun appel de modèle automatique.
