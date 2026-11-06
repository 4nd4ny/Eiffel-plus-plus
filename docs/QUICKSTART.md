# Démarrer avec Eiffel++

## 1. Comprendre le catalogue

Lire le [README](../README.md), les quatre [métapatrons](../patterns/01-governance.md) et le [protocole commun](../protocol/README.md). Un métapatron décrit une famille de décisions de harnais ; il n'est pas un algorithme d'optimisation doté d'une garantie de convergence.

Le catalogue public distribue quatre modèles. Il ne fusionne pas les quatre responsabilités d'un projet : l'instanciation produit quatre racines Git indépendantes.

## 2. Générer un projet

Depuis la racine du catalogue :

```bash
python3 tools/instantiate.py --project atelier --name "Inscriptions aux ateliers" --output ../atelier --git-init
```

Les dossiers créés sont `atelier-governance`, `atelier-stbl`, `atelier-audit` et `atelier-product`. La destination entière doit être nouvelle et extérieure au catalogue. Aucun remote, compte, droit ou dépôt public n'est créé par cette commande.

## 3. Établir l'autorité et les références

Dans la gouvernance, nommer le Product Owner, les délégations, le responsable d'audit et l'autorité de livraison. Adopter une politique et un premier mandat. Installer les protections techniques du [guide de déploiement](DEPLOYMENT.md).

Chaque dépôt possède `_eiffel/project.json`. Les adresses et commits y sont initialement vides. Le fichier est un registre local de contexte ; il ne prouve pas l'existence d'un remote ni l'approbation d'une version. Une enveloppe de candidat ultérieure doit fixer les références exactes réellement observées.

Les copies `_eiffel/protocol/` sont des instantanés identifiés. Le dépôt de gouvernance adopte la version faisant autorité. Une mise à jour se propose et s'évalue explicitement ; ne pas faire flotter automatiquement les références vers `main`.

## 4. Décrire un premier besoin

Dans STBL, remplir le document principal et une fiche `REQ`, préciser sa source, rédiger les questions qui changeraient réellement le comportement et enregistrer les décisions du PO. Les critères de réussite incluent les services attendus, les refus et les conditions dégradées.

Une proposition d'agent reste `PROPOSED`. Un mandat d'exploration peut autoriser une maquette sous hypothèses visibles ; il ne suffit pas à transformer ces hypothèses en exigences acceptées.

## 5. Préparer l'examen et produire

L'audit prépare un plan, des oracles et un modèle de menace proportionné au périmètre. Le produit reçoit un ordre de travail et réalise un candidat. Les tests techniques du producteur sont utiles ; ils ne remplacent pas l'examen indépendant requis.

Figer `governance_commit`, `stbl_commit`, `audit_commit` et `product_commit`, puis construire et examiner le candidat exact. Le `audit_commit` désigne le plan avant exécution ; le rapport est conservé dans un commit ultérieur.

## 6. Livrer et faire évoluer

Appliquer les critères du mandat à l'état intégré et à l'artefact construit. Une réserve ou un contrôle inconclusif reste explicite. Les corrections d'oracles passent par une décision distincte de la correction du code.

Lors d'une évolution métier, retrouver les contrats, contrôles et composants dépendants, invalider les résultats concernés et vérifier de nouveau. L'exemple [réservation](../examples/booking/README.md) montre ce trajet.

## Les premiers documents à utiliser

| Rôle | Document de départ | Livrable courant |
| --- | --- | --- |
| Gouvernance | `AGENTS.md`, `POLICY.md`, `ROLES.md` | Mandat ou modification du harnais |
| STBL | `AGENTS.md`, `STBL.md` | Exigence, question, décision ou contrat |
| Audit | `AGENTS.md`, charte et politique d'audit | Plan, constat, élément probant ou avis |
| Produit | `AGENTS.md`, architecture et méthode de développement | Ordre de travail, candidat ou compte rendu |

Les `AGENTS.md` sont des points d'entrée courts. Ne pas charger systématiquement tous les formulaires et tous les historiques dans chaque contexte.
