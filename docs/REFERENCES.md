# Sources et filiation

Sources consultées pour concevoir le catalogue le **6 novembre 2026**. Les textes sont résumés ; leurs contenus ne sont pas incorporés sous licence MIT. La licence du catalogue porte sur ses textes et outils propres.

## Bertrand Meyer et ses coauteurs

- **Object-Oriented Software Construction**, 2e édition, chapitre 1, §1.1–1.2, pp. 3–16 : [page de l'auteur](https://bertrandmeyer.com/oosc2/), [édition officielle et extrait](https://smarties-press.com/books/oosc2/). Dix facteurs développés et quatre complémentaires servent à la [revue qualité](../meta/QUALITY.md). Consultation du 7 novembre 2026 : les anciennes URL PDF publiques répondent 404 ; les passages encore indexés ont été utilisés, sans prétendre avoir téléchargé l'ouvrage complet.

- **Design by Contract — Introduction**, Eiffel Software : [source](https://www.eiffel.com/values/design-by-contract/introduction/). Obligations entre composants, distinction correction/robustesse et intérêt de spécifications explicites. Un contrat seul ne constitue pas une preuve.
- **Design by Contract and Assertions**, Eiffel Software, consulté le 7 novembre 2026 : [source](https://www.eiffel.org/doc/solutions/Design_by_Contract_and_Assertions). Préconditions à la charge du client, postconditions dues par le fournisseur, invariants aux frontières publiques et substitution compatible. La répartition gouvernance/STBL/produit/audit est un choix d'Eiffel++, pas une prescription de Meyer.
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

La répartition en quatre responsabilités, les formats de provenance et les heuristiques de choix constituent la proposition du catalogue. Ils ne sont pas présentés comme une méthode de Bertrand Meyer ni comme un résultat expérimental démontré.

La version 0.2.0 proposait une chaîne N2 → N1 → N0 et quatre dépôts. La version 0.3.0 retire leur caractère obligatoire : on peut réutiliser une graine et forger directement un harnais N0, dans un seul dépôt. Un générateur intermédiaire et la séparation physique des responsabilités doivent répondre à un besoin.

**Specification Driven Development** désigne ici le guidage par les spécifications du produit et celles de sa production. C'est un choix de vocabulaire et de conception d'Eiffel++, pas l'affirmation d'une norme SDD unique. Les préconditions, postconditions et invariants restent des moyens éventuels de vérifier le comportement du code. Ils ne deviennent pas, par analogie, une preuve de l'efficacité de l'organisation du travail.

Le tétraèdre rapidité/coût/fonctionnalités/autonomie décrit des préférences. Une priorité qualitative peut suffire ; ces axes ne constituent ni des mesures indépendantes ni une fonction d'optimisation déjà établie.

## Catalogues, mémoire et évolution des harnais

Sources également examinées le **6 novembre 2026** :

- **Harness Lens**, [application](https://huggingface.co/spaces/harness-hub/harness-lens) et [méthodologie à version figée](https://huggingface.co/spaces/harness-hub/harness-lens/blob/5db2b0410a38dadadefe661c3f95c30e9e360e0a/src/routes/Methodology.tsx). Cartographie des mécanismes, sources et configurations ; la présence d'une fonctionnalité ne prouve pas son utilité pour un projet.
- **The harness (still) matters**, [revue](https://tmustier.github.io/harness-benchmarks/). Point d'accès aux comparaisons et à leurs limites. Les études réutilisant les mêmes familles de tâches ne constituent pas autant de réplications indépendantes.
- Databricks, **Benchmarking Coding Agents on Databricks' Multi-Million Line Codebase**, [étude](https://www.databricks.com/blog/benchmarking-coding-agents-databricks-multi-million-line-codebase). Comparaisons situées, coût du contexte et construction de tâches locales avec des contrôles comportementaux.
- Joel Niklaus, **Don't Train the Model, Evolve the Harness**, [étude](https://joelniklaus-harness-optimization.hf.space/). Proposition et évaluation séparées de modifications du harnais, limites du transfert et distinction entre critères satisfaits et tâches entièrement réussies.
- LatchBio, **Why An Open Source Harness Outperforms Claude Code On Frontier Biology Tasks**, [étude](https://blog.latch.bio/p/why-an-open-source-harness-outperforms). Effets de consignes dépendants du type de tâche ; ces observations ne sont pas une règle universelle de conception.
- Anthropic, [mémoire des Managed Agents](https://platform.claude.com/docs/en/managed-agents/memory) et [dreaming](https://platform.claude.com/docs/en/managed-agents/dreams). Exemples de mémoire persistante et de consolidation asynchrone. N1 peut retenir ces mécanismes, les remplacer ou les omettre selon le besoin ; Eiffel++ ne dépend pas de leur fournisseur.

Ces sources alimentent les hypothèses des générateurs. Le catalogue ne reprend pas leurs prompts ni leurs résultats comme des garanties propres à Eiffel++.

## Base initiale de graines

Les [fiches de graines](../seeds/records/) indiquent les fichiers lus, les révisions immuables, les licences, les adaptations proposées et les limites. La sélection publiée comprend :

| Projet primaire | Fiche et mécanisme étudié |
| --- | --- |
| [mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent) | [Boucle courte et bornée](../seeds/records/mini-swe-loop.json) |
| [Codex](https://github.com/openai/codex) | [Consignes selon la portée des fichiers](../seeds/records/codex-scoped-instructions.json) |
| [Pi](https://github.com/earendil-works/pi) | [Chargement progressif du contexte](../seeds/records/pi-progressive-context.json) |
| [Deep Agents](https://github.com/langchain-ai/deepagents) | [Délégation de tâches séparables](../seeds/records/deepagents-delegation.json) |
| [Letta Code](https://github.com/letta-ai/letta-code) | [Mémoire attribuée et versionnée](../seeds/records/letta-versioned-memory.json) |
| [Extension publique feature-dev de Claude Code](https://github.com/anthropics/claude-code/tree/main/plugins/feature-dev) | [Exploration, décision et revue](../seeds/records/claude-feature-review.json) |
| ICO — source privée, publication du harnais autorisée | [Incréments et couloirs de travail](../seeds/records/ico-incremental-lanes.json) ; [propositions de contrôles mécaniques](../seeds/records/ico-mechanical-controls-proposal.json) |

Ce relevé est une sélection, pas une couverture exhaustive des catalogues. Les sources ont été lues, pas exécutées dans Eiffel++. Les recettes sont des synthèses originales ; les licences des projets cités continuent de s'appliquer à leurs contenus. La fiche Claude Code porte uniquement sur l'extension publique examinée, dont la licence est signalée, sans import du cœur du produit ou d'un prompt complet.

L'[exemple local](../examples/forge-local/README.md) est une composition illustrative, sans décision humaine d'adoption inventée ni résultat de production. Les futurs harnais co-construits pourront être capturés avec leurs propres traces et contre-indications.

### Publication des recettes ICO

Le 6 novembre 2026, Christian a donné dans la conversation Eiffel++ cette instruction : « Tu peux rendre public le harnais du projet privé ICO. » Les deux fiches de recettes sont publiées sur cette base. Le dépôt source conserve sa visibilité privée ; les références au commit `988c58c6376ef764c4b4a5e1e9af288703b3e84b` indiquent les fichiers examinés sans garantir leur accessibilité publique.

Cette publication porte sur les recettes génériques dérivées des instructions et des suggestions d’amélioration du harnais. Les observations métier, données, code produit et résultats d’audit privés ne sont pas incorporés. La licence MIT et son attribution sont conservées dans les fiches. Leur statut reste `source-inspected`, sans résultat d’essai ni co-construction fictive.

## Harness² — adaptation à partir des exécutions

Sources examinées le 7 novembre 2026 : [article arXiv:2610.14224v1](https://arxiv.org/abs/2610.14224v1), [dépôt Google à la révision 6868817](https://github.com/google-research/harness2/tree/6868817518876de8fd170c6a8354daca273b6191). Les fichiers `core/recursion.py`, `core/library.py`, `core/tree.py`, `core/selection.py`, `core/ledger.py` et `core/prompts.py`, sous `harness2/`, documentent les mécanismes repris. Licence Apache-2.0. Les trois nouvelles graines sont des synthèses originales, sans code ni prompt complet copié. Les scores publiés ne sont pas des résultats Eiffel++.

## Format des compétences réutilisables

[Agent Skills — Specification](https://agentskills.io/specification), consulté le 7 novembre 2026 : dossier par compétence, SKILL.md avec name/description, ressources facultatives et découverte progressive. Eiffel++ reprend cette forme ; capacités, contrats de remise et empreintes de mission sont ses propres ajouts. Son lecteur sans dépendance ne traite qu’un sous-ensemble explicite des en-têtes YAML. Aucun contenu de skill tiers n’est importé.
