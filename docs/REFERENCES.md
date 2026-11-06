# Sources et filiation

Sources consultées pour concevoir le catalogue le **6 novembre 2026**. Les textes sont résumés ; leurs contenus ne sont pas incorporés sous licence MIT. La licence du catalogue porte sur ses textes et outils propres.

## Bertrand Meyer et ses coauteurs

- **Design by Contract — Introduction**, Eiffel Software : [source](https://www.eiffel.com/values/design-by-contract/introduction/). Obligations entre composants, distinction correction/robustesse et intérêt de spécifications explicites. Un contrat seul ne constitue pas une preuve.
- **Seamless development**, Eiffel Software : [source](https://www.eiffel.com/values/seamless-development/). Continuité des concepts entre exigences, conception, code et évolution. Eiffel++ transpose cette motivation en références communes et vues cohérentes, sans prétendre imposer une notation unique à tous les langages.
- Andreas Leitner, Ilinca Ciupa, Manuel Oriol, Bertrand Meyer et Arno Fiva, **Contract Driven Development = Test Driven Development – Writing Test Cases**, ESEC/FSE 2007 : [article](https://se.inf.ethz.ch/people/ciupa/papers/esecfse07.pdf). Précédent de l'automatisation des tests à partir de contrats et d'exécutions en échec.
- Bertrand Meyer, **AI for software engineering: from probable to provable**, prépublication 2025, publication dans Communications of the ACM en 2026 : [texte](https://se.inf.ethz.ch/~meyer/publications/cacm/probable-provable.pdf) et [bibliographie officielle](https://se.inf.ethz.ch/~meyer/publications/). Proposition d'associer génération par IA, spécification et vérification formelle dans une démarche itérative.
- Li Huang, Bertrand Meyer et Manuel Oriol, **Combining Tests and Proofs for Better Software Verification**, prépublication : [texte](https://se.inf.ethz.ch/~meyer/publications/cacm/tests-and-proofs.pdf). Complémentarité des tests, preuves et contre-exemples ; une tentative de preuve échouée ne démontre pas nécessairement un défaut du programme.
- Maria Naumcheva, Sophie Ebersold, Jean-Michel Bruel et Bertrand Meyer, **UOOR: Seamless and Traceable Requirements**, 2025 : [article](https://arxiv.org/html/2502.18617v1). Exigences évolutives et liens de traçabilité entre artefacts.

## Synthèse, agents et vérification

- Armando Solar-Lezama, **Introduction to Program Synthesis — Lecture 10** : [cours](https://people.csail.mit.edu/asolar/SynthesisCourse2020/Lecture10.htm). Synthèse guidée par contre-exemples. Eiffel++ en reprend la boucle d'apprentissage, sans lui attribuer une garantie de convergence avec un LLM.
- **Dafny Reference Manual** : [documentation](https://dafny.org/dafny/DafnyRef/DafnyRef.html). Spécifications, hypothèses, invariants et vérification. Un modèle vérifié n'est pas automatiquement une preuve de tout le système déployé.
- Anthropic, **Effective harnesses for long-running agents**, 26 novembre 2025 : [retour d'expérience](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents). Contexte persistant, progression et vérification de bout en bout.
- Anthropic, **Harness design for long-running application development**, 24 mars 2026 : [retour d'expérience](https://www.anthropic.com/research/harness-design-long-running-apps). Réévaluation des découpages et des évaluateurs à mesure que les modèles progressent. Expérience située, pas démonstration universelle contre Scrum.
- OpenAI, **Harness engineering**, 11 février 2026 : [retour d'expérience](https://openai.com/index/harness-engineering/). Environnement lisible par les agents, règles exécutables et boucles de retour. Les gains annoncés dans ce cas ne sont pas une estimation générale pour Eiffel++.
- OpenAI, **Why SWE-bench Verified no longer measures frontier coding capabilities**, 23 février 2026 : [analyse](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/). Exemples d'oracles trop étroits ou non alignés avec la demande ; motivation d'une procédure de contestation des critères.

## Validation, sécurité et forge

- NASA, **Systems Engineering Handbook — Fundamentals** : [manuel](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/). Distinction entre conformité aux exigences et accomplissement de l'usage attendu.
- OWASP, **Application Security Verification Standard**, version stable 5.0.0 consultée : [projet](https://asvs.owasp.org/). Source possible d'exigences de sécurité pour les applications web. Un projet doit choisir explicitement la version et les exigences applicables ; utiliser le catalogue ne vaut pas conformité ASVS.
- GitHub, [code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners), [branches protégées](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) et [création de dépôts](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository). Références pour les mécanismes de forge, à revérifier lors d'une installation.

## Choix propres à Eiffel++

La répartition en quatre dépôts, leurs métapatrons, le protocole d'échange, les états, les formats de mandat, la liaison aux quatre commits et les heuristiques de coût constituent la proposition de ce catalogue. Ils ne sont pas présentés comme une méthode de Bertrand Meyer ni comme un résultat expérimental déjà démontré.

La version 0.2.0 formalise la demande de Christian : trois niveaux de génération et un tétraèdre de préférences rapidité/coût/fonctionnalités/autonomie. N2 engendre des prompts spécialisés N1, puis N1 engendre le harnais N0. Cette architecture et ses contrats sont une proposition propre au projet, sans revendication de nouveauté scientifique ni garantie d'optimalité.

## Catalogues, mémoire et évolution des harnais

Sources également examinées le **6 novembre 2026** :

- **Harness Lens**, [application](https://huggingface.co/spaces/harness-hub/harness-lens) et [méthodologie à version figée](https://huggingface.co/spaces/harness-hub/harness-lens/blob/5db2b0410a38dadadefe661c3f95c30e9e360e0a/src/routes/Methodology.tsx). Cartographie des mécanismes, sources et configurations ; la présence d'une fonctionnalité ne prouve pas son utilité pour un projet.
- **The harness (still) matters**, [revue](https://tmustier.github.io/harness-benchmarks/). Point d'accès aux comparaisons et à leurs limites. Les études réutilisant les mêmes familles de tâches ne constituent pas autant de réplications indépendantes.
- Databricks, **Benchmarking Coding Agents on Databricks' Multi-Million Line Codebase**, [étude](https://www.databricks.com/blog/benchmarking-coding-agents-databricks-multi-million-line-codebase). Comparaisons situées, coût du contexte et construction de tâches locales avec des contrôles comportementaux.
- Joel Niklaus, **Don't Train the Model, Evolve the Harness**, [étude](https://joelniklaus-harness-optimization.hf.space/). Proposition et évaluation séparées de modifications du harnais, limites du transfert et distinction entre critères satisfaits et tâches entièrement réussies.
- LatchBio, **Why An Open Source Harness Outperforms Claude Code On Frontier Biology Tasks**, [étude](https://blog.latch.bio/p/why-an-open-source-harness-outperforms). Effets de consignes dépendants du type de tâche ; ces observations ne sont pas une règle universelle de conception.
- Anthropic, [mémoire des Managed Agents](https://platform.claude.com/docs/en/managed-agents/memory) et [dreaming](https://platform.claude.com/docs/en/managed-agents/dreams). Exemples de mémoire persistante et de consolidation asynchrone. N1 peut retenir ces mécanismes, les remplacer ou les omettre selon le besoin ; Eiffel++ ne dépend pas de leur fournisseur.

Ces sources alimentent les hypothèses des générateurs. Le catalogue ne reprend pas leurs prompts ni leurs résultats comme des garanties propres à Eiffel++.
