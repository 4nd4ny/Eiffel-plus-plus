# Responsabilités et remises

| Rôle logique | Entrées → remise | Autorité et arrêt |
| --- | --- | --- |
| Gouvernance | Demande et sources → mandat borné ; verdicts → décision motivée | Ouvre le lot et conserve les empreintes. N’invente ni acceptation métier ni budget. |
| STBL | Mandat et exigences → contrat : préconditions, postconditions, effets, invariants, obligations et propositions | Résout les contradictions connues ; signale celles qui changent le comportement dû. Ne modifie pas le code. |
| Audit | Contrat et moyens → plan avant production ; candidat figé → résultats et couverture | Peut refuser une preuve incomplète. Ne répare pas le candidat pendant son examen et ne redéfinit pas les obligations pour le faire passer. |
| Produit | Contrat, plan et code de travail → candidat complet, changements et motifs | Choisit l’implémentation dans le lot. Ne modifie pas les contrôles figés ni la référence. |

En pratique : `orchestrer-lot` → `specifier-contrat` → `planifier-audit` → `modifier-moteur` ou `modifier-interface` → `verifier-candidat` → `decider-livraison`. Le manifeste donne les ports exacts. La planification remet son plan à Gouvernance pour figer le lot puis à Produit pour travailler. Le produit remet son reçu de candidat à Audit. Un diagnostic sans modification utilise une méthode native Produit : identifier la référence, sans charger une compétence d’édition.

Les missions sont préparées par `tools/skills.py prepare`, puis examinées avec `verify` et remises avec `handoff --order-sha256`. Le coordinateur conserve l’empreinte renvoyée à la préparation hors du dossier de mission. PASS de la remise signifie seulement que les pièces attendues et leur contexte sont identifiés ; le destinataire doit encore juger leur contenu. Une copie complète est vérifiée avec l’atelier, car un reçu de fichier ne couvre pas à lui seul le code qu’il désigne.

L’essai de cet exemple est un auto-examen. Des rôles distincts dans des fichiers ne constituent pas une séparation des droits.
