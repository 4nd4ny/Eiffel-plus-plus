# Brief fictif — tableau de bord CSV local

Statut : PROPOSED. Source : exemple construit pour Eiffel++ 0.2.0. Aucun client réel ni mandat effectif.

Un petit collectif possède un catalogue CSV non sensible : id, nom, categorie, quantite. Il veut ouvrir un fichier local, filtrer les lignes par catégorie et connaître le nombre de lignes retenues. Le fichier source doit rester inchangé et aucune donnée ne doit quitter le poste.

L'horizon est court. Le délai et le coût priment sur les fonctions optionnelles. Une recherche textuelle ou un export filtré peut être proposé si cela ne compromet pas les obligations. Le catalogue ne fixe ni framework ni outil de test.

Le méta-harnais doit produire un mode de travail proportionné : peu de contexte initial, une réalisation locale simple, des contrôles observables, et des questions métier regroupées. Une préférence faible pour l'autonomie ne commande pas d'interrompre l'humain inutilement.

Les inconnues utiles sont le navigateur disponible, le sens des doublons et des quantités manquantes. On peut avancer sur les traitements indépendants de ces réponses. Le profil de préférences et ses cibles sont dans [profile.json](profile.json).

## Transformation à essayer

Remplacer « fichier local non sensible » par « catalogue partagé avec comptes utilisateurs et synchronisation ». Le N1 doit revoir le besoin, les frontières de confiance, la méthode et les contrôles. Modifier seulement un poids ou ajouter une ligne à un prompt serait insuffisant.
