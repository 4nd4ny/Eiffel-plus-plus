# Générer le lot CSV

La [note de conception du générateur](DESIGN.md) explique les choix stables et leurs conditions de révision.

Reçois le brief, le profil et le mode produire-ou-examiner. Le contrat SPEC.md fait foi. Pour produire, copie les deux skills et leurs ressources ; attribue filter-rows à Produit et check-rows à Audit. Pour examiner un candidat déjà fourni, ne copie que check-rows ; la tâche Produit devient réception et identification du fichier, avec une méthode native et aucun droit de correction du candidat.

Écris AGENTS.md avec la passation STBL → Produit → Audit → Gouvernance. STBL fournit rules, Produit candidate, Audit report. Le coordinateur prépare les missions avec skills.py, conserve chaque order_sha256 et lie les remises aux ports de la suivante. Les chemins de commande sont relatifs à la mission. Lire une compétence ne la lance pas.

Dans harness.json 0.6.0, reprendre les composants sélectionnés et adapter capabilities au mode ; garder les quatre responsabilités. Copier SPEC.md, profile.json et les fichiers des composants sans dépendance externe implicite. Les obligations de SPEC.md restent les mêmes dans les deux modes. Livrer un N0 autonome en instructions ; l’outil Eiffel++ demeure une capacité de l’environnement à identifier.

Appliquer CHECK.md avant remise. Une capacité manquante est explicitement indisponible ; ne pas inventer de résultat. Un seul acteur peut tenir tous les rôles en auto-examen. Aucun modèle, droit ou réseau nouveau n’est autorisé.

Livrer aussi DESIGN.md propre au N0, référencé par design_rationale : mode retenu, raison des compétences et rôles choisis, compromis, moyens de vérification et points d’adaptation métier. Le lot d’examen seul explique pourquoi filter-rows est retiré et comment les obligations sont conservées. Écrire cette note avec les instructions et scripts ; ne pas recopier la note générale N1.
