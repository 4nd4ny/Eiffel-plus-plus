# Générer N0 pour ICO

Lire le profil, [la justification N1](DESIGN.md), le mandat et la source métier de la tranche. La bibliothèque `blueprint/` contient les méthodes, contrats et quatre responsabilités. QUALITE y conserve les quatorze décisions de projet. Les instructions sont une conception dérivée de N2, pas une reproduction du code ICO.

Choisir `full` pour l’atelier complet demandé, `import` pour un lot Import ou `interface` pour un parcours UI. `generate.py --mode MODE --output DESTINATION_NEUVE` matérialise ce choix sans appel de modèle. Réviser ensuite le contrat concret du lot à partir de ses sources ; aucune sonde historique ne devient une exigence par défaut.

En mode import, retirer modifier-interface ; en mode interface, retirer modifier-moteur. Dans les deux cas garder les remises STBL/Audit/Gouvernance et les invariants. Le N0 doit démarrer sans relire N1, offrir les rôles et compétences choisis, expliquer la copie de travail et les moyens manquants. La note N0 est livrée en même temps et complétée par le choix du lot, son motif et ses limites ; ne pas lui substituer la présente note.

Éprouver le résultat avec CHECK. Un mandat dépassant ces modes exige une adaptation argumentée, pas un choix approximatif. Les obligations connues restent dans le contrat ; les dépendances absentes restent explicitement indisponibles. Conserver la provenance, le budget commun d’un candidat et deux cycles, les preuves réellement obtenues et la distinction entre exemple public et réalisation privée.
