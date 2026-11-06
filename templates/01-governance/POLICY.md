# Politique — à adopter pour {{PROJECT_NAME}}

Statut initial : **PROPOSED**. Aucun champ ci-dessous ne constitue une configuration effective.

## Autorité et périmètre

- Responsable de la méthode : à désigner.
- Product Owner et délégations : à référencer dans {{STBL_REPO}}.
- Responsable audit : à désigner.
- Responsable de livraison : à désigner.
- Dépôts et branches normatives : à identifier.
- Méthode d'authentification des décisions : à configurer et documenter.

## Profil de garantie

Le profil distingue les priorités, leurs sources, les mesures disponibles, les obligations non compensables et le mandat. Des poids `speed`, `economy`, `scope`, `autonomy` peuvent les préciser sans être obligatoires. La charge humaine s'observe en temps actif, interruptions et décisions ; elle ne se confond pas avec l'absence de contrôle. Une préférence pour l'autonomie n'accorde aucun droit nouveau.

Définir, par famille de besoins, les contrôles obligatoires, les critères, les environnements et l'autorité habilitée à accepter les risques résiduels. Distinguer exploration non livrable, développement standard et périmètres nécessitant une assurance renforcée. Les obligations de sécurité découlent du domaine et du modèle de menace.

## Règle normale de livraison

Les exigences applicables sont `ACCEPTED`. Aucun point ouvert bloquant ne subsiste. Les contrôles obligatoires possèdent des résultats valides `PASS`, attachés au candidat exact. Le verdict d'audit est `ACCEPT` sur le périmètre requis. L'état intégré et l'artefact livré correspondent aux références examinées. La livraison reste dans le mandat autorisé.

`ACCEPT_WITH_RESERVATIONS`, `UNKNOWN`, `STALE` et l'absence de contrôle n'activent pas cette règle. Une dérogation éventuelle est distincte, décidée par l'autorité habilitée, bornée et traçable ; les contrôles restent dans leur état réel. Indiquer les règles non dérogeables.

## Économie du harnais

- Définir des budgets par lot : temps, tokens, outils, candidats et travail en cours.
- Retourner les différences, échecs et références utiles plutôt que les journaux complets.
- Réutiliser uniquement les résultats dont les conditions sont maîtrisées.
- Mesurer le coût jusqu'à l'acceptation, y compris corrections et temps humain.
- Interrompre les boucles sans progrès ; ne pas répéter le même prompt sans nouveau diagnostic.

## Changements

Toute modification des critères, pouvoirs ou niveaux de garantie suit `templates/POLICY_CHANGE.md`. Elle précise quels travaux et résultats deviennent périmés. Une proposition peut être préparée par un agent ; son adoption requiert l'autorité enregistrée dans le mandat.

Adapter N0 dans la délégation existante à partir des observations, directement ou avec N1 lorsqu'un tel générateur est utilisé. Réexaminer ses hypothèses si le contexte change. Définir les déclencheurs, le budget de révision et le retour possible ; ne pas changer continuellement de méthode pour optimiser un indicateur bruité.
