---
protocol_version: "0.3.0"
type: WORK_ORDER
id: CHG-0001
status: PROPOSED
---

# Mandat — à compléter

## Objet et références

But métier ; rôle chargé du travail ; références immuables aux dépôts applicables ; exigences et contrats ; décision autorisant ce mandat.

## Préconditions

Besoin suffisamment déterminé ; outils disponibles ; droits effectifs ; données utilisables ; ambiguïtés restantes et leur caractère bloquant.

## Capacités accordées

Chemins et branches modifiables ; commandes/environnements autorisés ; accès réseau ou données nécessaires ; actions réversibles préautorisées ; actions nécessitant une décision distincte. Ne pas inscrire de secret.

## Postconditions et critères

Livrables, contrôles et niveau de garantie ; conditions de livraison ; éléments probants attendus ; comportements positifs et négatifs concernés.

## Invariants

Pas de modification unilatérale des critères ni des décisions PO. Aucune déclaration de résultat sans exécution. Aucune extension implicite du mandat.

## Budget et arrêt

Temps, tokens, candidats, appels et concurrence ; seuil d'absence de progrès ; responsable d'escalade ; travail indépendant pouvant continuer.

## Décision d'adoption

Décideur habilité, référence vérifiable de l'acte d'approbation, date, portée et durée. Tant que cette section n'est pas établie, le mandat reste `PROPOSED`.
