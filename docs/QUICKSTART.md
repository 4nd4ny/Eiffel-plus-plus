# Démarrer : l'étape zéro du projet

Eiffel++ 0.2.0 génère la méthode de travail avant de produire le logiciel. Les trois niveaux sont N2 (patron générique), N1 (prompts spécialisés de conception) et N0 (harnais opérationnel du projet). Le logiciel est le résultat du travail de N0.

## 1. Donner une intention au patron

Lire ou transmettre à un agent [meta/START.md](../meta/START.md). Fournir un brief : résultat recherché, situation actuelle, impératifs, ressources et limites de délégation. Les informations déjà présentes dans les documents du projet doivent être réutilisées ; il n'est pas nécessaire de recopier un questionnaire complet.

Le [profil à quatre axes](../meta/TETRAHEDRON.md) exprime les préférences de rapidité, économie, fonctionnalités utiles et autonomie. Identifier les obligations non compensables séparément. Les valeurs proposées par un agent restent des hypothèses, avec leur source, jusqu'à leur adoption dans le mandat.

Les [deux exemples complets](../examples/meta/README.md) sont fictifs. Ils montrent des choix différents, pas des profils imposés à tous les projets.

## 2. Préparer un paquet autonome si nécessaire

Depuis la racine du catalogue, avec Python 3.10 ou plus récent :

```bash
python3 tools/meta_harness.py prepare --brief examples/meta/dashboard-local/brief.md --profile examples/meta/dashboard-local/profile.json --output ../etape-zero
```

La destination doit être nouvelle et extérieure au catalogue. Le paquet préparé contient les entrées et les instructions de génération. Cette commande ne produit pas, à elle seule, un méta-harnais ou un harnais adapté : elle n'appelle aucun LLM. Confier son point d'entrée à l'agent choisi pour la synthèse.

On peut aussi utiliser directement le patron dans le catalogue, sans passer par ce script. N2 demande seulement les précisions qui changeraient matériellement la méthode, puis poursuit sous les hypothèses autorisées.

## 3. Générer N1, puis N0

N2 produit un dossier `meta-harness/` contenant un manifeste `meta-harness.json`, un profil, un contrat de génération et des prompts spécialisés. Ces prompts définissent comment concevoir la méthode, comment l'examiner et quand la réviser. Ils ne doivent pas simplement choisir un modèle préétabli en fonction de quatre coefficients.

L'agent applique ensuite l'entrée de N1 pour produire un dossier `harness/` : manifeste `harness.json`, profil identique et quatre répertoires `governance`, `stbl`, `audit`, `product`. Chaque rôle possède un `AGENTS.md` court, un README et les procédures dont ce projet a besoin. Les quatre responsabilités peuvent mobiliser un nombre variable d'agents et de contrôles déterministes.

Conserver des raisons de conception rattachées aux exigences, préférences et hypothèses. Fixer un budget d'étape zéro. Un contrôle proportionné peut suffire à démarrer un travail réversible ; les expériences approfondies répondent à des incertitudes précises et ne sont pas un préalable universel.

## 4. Contrôler les sorties générées

Les commandes suivantes prennent les exemples fournis ; remplacer les chemins par les sorties effectivement produites pour son projet :

```bash
python3 tools/meta_harness.py check examples/meta/dashboard-local/meta-harness
python3 tools/meta_harness.py check examples/meta/dashboard-local/harness
```

Le contrôle porte sur le profil, les manifestes, les chemins et les fichiers requis. Il ne vérifie ni l'autorité d'une décision, ni la qualité sémantique des prompts, ni les performances de la méthode. Le [prompt de qualification](../meta/prompts/03-qualify.md) organise cet examen ; les capacités et obligations techniques requièrent leurs vérifications effectives.

Une sortie `PROPOSED` ne devient pas `ACCEPTED` par le seul succès du contrôle structurel. Une délégation existante peut permettre son adoption dans les limites déjà accordées.

## 5. Matérialiser les quatre dépôts

```bash
python3 tools/meta_harness.py materialize examples/meta/dashboard-local/harness --meta-harness examples/meta/dashboard-local/meta-harness --output ../dashboard-local --git-init
```

L'outil copie les fichiers N0 fournis, leur ajoute un instantané du protocole et des métadonnées de génération. L'option `--meta-harness` conserve N1 dans la gouvernance sous `_eiffel/meta-harness` ; ses profils doivent correspondre à ceux de N0. Sans cette option, la présence de N1 n'est pas présumée et les métadonnées le signalent. Le patron N2 courant est conservé sous `_eiffel/meta` pour une régénération ultérieure, avec ses empreintes : sa disponibilité ne prouve pas qu'il a effectivement engendré le N1 reçu.

Quatre racines Git indépendantes sont créées avec `--git-init`, sans commit ni remote. Aucun droit n'est accordé et aucune publication distante n'est faite. Les références restent `UNBOUND` jusqu'à leur résolution réelle. Les empreintes de contenu identifient des fichiers, sans prouver une approbation ni une provenance authentifiée.

Installer les mécanismes d'accès, de contrôle et d'exécution décrits dans le [déploiement](DEPLOYMENT.md) selon le harnais effectivement généré. Ne pas confondre présence d'une consigne et activation d'un mécanisme.

## 6. Produire le logiciel avec N0

Utiliser les points d'entrée des quatre rôles et le mandat actif. STBL conserve les besoins et les décisions autorisées ; le produit réalise un candidat ; l'audit applique les contrôles requis au candidat exact ; la gouvernance conserve la méthode et les références.

Avant acceptation, établir `governance_commit`, `stbl_commit`, `audit_commit` et `product_commit`. Le plan d'audit est figé avant exécution ; le rapport est conservé dans un commit ultérieur. Les états inconclusifs ou périmés ne deviennent pas des réussites.

## 7. Adapter au niveau nécessaire

N0 émet des observations courtes : coût, délai, fonctionnalités effectivement acceptées, temps humain, défauts et limites. Utiliser le prompt d'adaptation de N1 lorsqu'un événement pertinent le justifie. Garder les deux générations et leurs raisons.

Remonter à N2 seulement si le domaine de validité de N1 change. Préserver les décisions métier et les frontières d'autorité. Une amélioration de méthode n'exige pas de redemander une permission déjà accordée ; un élargissement du mandat suit l'autorité compétente.

## Compatibilité avec la bibliothèque générique

```bash
python3 tools/instantiate.py --project atelier --name "Inscriptions aux ateliers" --output ../atelier --git-init
```

Cette commande historique copie les composants génériques. Elle conserve le patron N2 dans la gouvernance, mais ne crée pas de N1 spécialisé. Utiliser alors `templates/EXPERIMENT.md` comme point d'entrée pour générer ou adapter la méthode. L'[exemple de réservation](../examples/booking/README.md) illustre les contrats métier, indépendamment du choix de générateur.
