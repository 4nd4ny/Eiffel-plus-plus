# Charger le contexte utile

Les chemins ci-dessous sont relatifs au code ICO, absent de l’exemple public. Leur présence a été vérifiée dans l’instantané privé employé pour la comparaison. Charger la tranche du lot, pas l’ensemble des documents à chaque action.

| Tranche | Source / contrôle à consulter | Points de contrat |
| --- | --- | --- |
| Import | `src/import`, tests voisins | Entrées malformées, normalisation sans perte d’information utile, exclusion d’URL actives, dédoublonnage. |
| Réponses | `src/answer`, tests voisins | Citations dans la réponse, indices valides, absence de preuve et abstention ; ne pas assimiler citation présente et vérité établie. |
| Recherche et mémoire | `src/search`, `src/memory`, `docs/FORMAT.md` | Format persistant, migrations, déterminisme, index dérivé, comportement sur absence ou corruption. |
| Fournisseurs et API | `src/llm`, `src/embed`, `src/server`, tests voisins | Contrats d’adaptateur, indisponibilité, annulation, autorisation de sortie de données. |
| Synchronisation | `src/sync`, tests voisins | Clés et secrets hors des traces, reprise, conflit et intégrité des fichiers ; doubles locaux avant tout réseau. |
| Personnes et commandes | `src/people`, `src/clock.ts`, `src/cli.ts`, tests voisins | Attribution, dates, identité des contacts, état local et erreurs de commande ; préserver les formats existants. |
| Interface | `web/src`, tests voisins | Parcours, sources visibles, états vides/erreurs, clavier et affichage mobile. |

Moyens inscrits dans le projet : `npm run typecheck`, `npm run test:local`, `npm run build`, `npm run test:e2e`, `npm run scan:leaks`. Vérifier leurs préconditions et les scripts avant lancement. L’absence de dépendances ou de navigateur est une capacité manquante à rapporter, pas un succès. Ne pas installer ni relier les dépendances du dépôt original implicitement.

Le diagnostic privé disponible dans cette régénération couvre deux modules purs et onze sondes historiques. Il n’exerce ni l’interface, ni le chiffrement, ni la synchronisation, ni la vérité des réponses. Les suites du produit restent nécessaires pour un lot qui les touche.
