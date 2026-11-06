# Démarrer par une proposition concrète

Eiffel++ 0.3.0 est un prototype de conception de harnais, sans gain d'efficacité démontré. Le parcours courant produit directement un harnais N0 et le travaille avec l'opérateur. Un générateur N1 est facultatif.

## 1. Décrire le projet et la méthode attendue

Donner à l'agent [meta/START.md](../meta/START.md), le brief et les décisions disponibles. Indiquer les obligations, les outils accessibles, les ressources, la charge humaine souhaitée et les actions déjà déléguées. Ne pas inventer de pondérations si des priorités verbales suffisent.

La spécification du logiciel décrit le résultat recherché. La spécification de méthode décrit comment organiser sa production : moyens, contrôles, coordination et limites. Une inconnue sur l'une ne doit pas être résolue silencieusement dans l'autre.

## 2. Examiner quelques graines

```bash
python3 tools/seeds.py list
python3 tools/seeds.py show eiffel-minimal-local
```

La [base](../seeds/README.md) contient des mécanismes tirés de sources publiques et un exemple local. Le choix est raisonné à partir des besoins et des capacités ; aucun score automatique ne désigne un optimum. Ne lire que les fiches utiles. Pour une base privée, passer `--catalog CHEMIN` explicitement.

Consigner en quelques lignes : graine retenue, origine, éléments conservés, éléments écartés et raison. Une graine externe ne donne aucune permission et ne modifie pas les obligations du projet.

## 3. Forger N0 avec l'opérateur

Produire les fichiers concrets, puis montrer les décisions importantes et les limites. L'opérateur peut modifier la répartition des tâches, les contrôles, les budgets ou le degré d'autonomie dans son autorité. Regrouper les questions qui changent réellement la méthode ; poursuivre les travaux déjà autorisés.

Réemployer, paramétrer ou composer suffit lorsque cela répond au besoin. Les quatre responsabilités peuvent pointer vers les mêmes documents. Le [petit exemple](../examples/forge-local/README.md) utilise `AGENTS.md`, `SPEC.md` et `CHECKS.md` dans un seul dépôt.

Une spécification compatible avec un projet n'est pas encore un essai de cette méthode. La proposition garde ce statut jusqu'à une décision applicable ; une décision ne transforme pas un contrôle non exécuté en succès.

## 4. Vérifier la structure et matérialiser si utile

Depuis la racine du catalogue, avec Python 3.10 ou plus récent :

```bash
python3 tools/meta_harness.py check examples/forge-local/harness
python3 tools/meta_harness.py materialize examples/forge-local/harness --output ../essai-eiffel --git-init
```

Remplacer l'exemple par le paquet effectivement forgé. La destination doit être nouvelle. Le mode `single-repo` produit une racine Git ; le mode historique `four-repos` en produit quatre. Les références restent `UNBOUND` tant qu'elles ne sont pas établies dans un environnement réel.

Le contrôle est structurel. Il ne juge ni les besoins, ni les instructions, ni l'autorité d'une décision. La matérialisation ne configure pas les outils de vérification, les permissions ou l'intégration continue. Voir le [déploiement](DEPLOYMENT.md).

## 5. Essayer un travail limité

Exécuter un premier lot réel selon N0. Relever au minimum ce qui a été accepté, ce qui a échoué, le temps humain, les coûts accessibles et les conditions d'exécution. Conserver les valeurs inconnues comme inconnues. Examiner un changement d'exigence ou une reprise seulement si cela appartient à l'usage prévu.

L'[expérience comparative](../templates/01-governance/templates/EXPERIMENT.md) sert à départager une incertitude utile. Une petite tâche ne nécessite pas systématiquement une campagne de benchmarks. Une affirmation de gain, elle, nécessite une comparaison pertinente.

## 6. Conserver l'instance comme nouvelle graine

Copier et remplir la [note d'exemple](../examples/forge-local/record.json) avec les faits réels : contexte, parents, modifications, référence de co-construction si elle existe, résultats et limites. Capturer le paquet N0, pas tout le dépôt du logiciel :

```bash
python3 tools/seeds.py capture examples/forge-local/harness --record examples/forge-local/record.json --output ../graine-a-examiner
python3 tools/seeds.py check --catalog ../graine-a-examiner
```

La commande ne demande pas une nouvelle approbation à la place d'un mandat existant. Elle ne fabrique pas non plus l'accord d'un humain. Elle conserve les statuts fournis et une empreinte du paquet. Avec les fichiers d'exemple, le résultat reste illustratif et non testé.

Une instance destinée au catalogue public pourra être capturée dans `seeds/instances/IDENTIFIANT` après examen de ce qui peut être partagé. Une instance privée reste hors de ce dépôt public. Le [guide des graines](../seeds/README.md) précise la provenance et les niveaux d'observation.

## Parcours plus élaborés

Le [guide des prompts](../meta/README.md) décrit la génération facultative de N1 et l'adaptation. Les anciens paquets 0.2.0 restent lisibles et conservent leurs exigences d'origine ; ils ne sont pas requalifiés rétroactivement.

`instantiate.py` reste un copieur de composants génériques en quatre dépôts. Son existence ne signifie pas que cette implantation soit recommandée pour chaque projet.
