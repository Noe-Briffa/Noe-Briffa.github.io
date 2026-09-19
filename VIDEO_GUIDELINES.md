# Guide vidéo pour les prochains projets

Règles de conception, d’animation et de validation pour produire des vidéos de portfolio claires, honnêtes et techniquement propres.

## 1. Objectif et narration

- Montrer le travail technique et le raisonnement, pas seulement l’interface finale.
- Écrire le parcours complet avant d’animer : problème → entrée → traitement → résultat → apprentissage.
- Donner une seule idée principale à chaque scène.
- Préférer six à huit scènes courtes à quelques écrans longs et peu informatifs.
- Montrer un résultat concret tôt dans la vidéo afin que le projet soit compréhensible sans explication extérieure.
- Terminer par ce que le projet démontre ou a permis d’apprendre, avec des formulations sobres et factuelles.
- Signaler clairement lorsqu’un projet est expérimental, en développement ou non public.
- Ne jamais inventer une fonctionnalité, une métrique, un résultat ou un niveau de maturité.

## 2. Storyboard et rythme

- Préparer un storyboard horodaté avant la composition.
- Prévoir une durée réaliste par étape et suffisamment de temps pour lire les textes.
- Garder un sujet visuel principal identifiable dès la première image de chaque scène.
- Éviter tout écran vide ou presque vide, même pendant une transition.
- Faire apparaître les éléments dans l’ordre logique du récit, pas tous simultanément.
- Après la dernière révélation importante, conserver environ deux secondes de lecture stable avant de changer de scène.
- Pour allonger ou raccourcir une vidéo sans changer son contenu, redistribuer uniformément le rythme au lieu d’ajouter artificiellement des scènes.
- Vérifier que le dernier élément d’une scène ne termine pas son animation au moment exact où la scène disparaît.

## 3. Transitions entre scènes

- Définir pour chaque transition ce qui disparaît, ce qui reste et ce qui motive la scène suivante.
- Utiliser un fondu entrant et sortant suffisamment progressif, généralement entre 0,6 et 1 seconde.
- Faire légèrement se chevaucher les scènes lorsque cela évite un écran vide, sans laisser apparaître prématurément le contenu suivant.
- Employer un déplacement discret en complément du fondu lorsque cela renforce la continuité spatiale.
- Pour deux étapes d’un même flux, conserver le même espace visuel et faire évoluer son état au lieu de remplacer brutalement tout l’écran.
- Vérifier particulièrement les secondes situées juste avant et juste après chaque changement de scène.
- Éviter les cuts directs entre deux compositions graphiques denses, sauf intention narrative explicite.

## 4. Mise en scène visuelle

- Varier la grammaire visuelle entre les scènes : interface, flux, file de jobs, transformation, architecture, comparaison ou synthèse.
- Éviter plusieurs scènes successives construites avec les mêmes cartes et la même disposition.
- Utiliser les captures réelles lorsqu’elles sont nettes, anonymisées et lisibles.
- Reconstruire les parties importantes en HTML/CSS/SVG lorsqu’une capture est trop petite ou trop floue.
- Ne jamais agrandir artificiellement une image basse résolution comme visuel principal.
- Garder les images originales sans texte incrusté ; ajouter les libellés dans la composition.
- Conserver les proportions des images et éviter toute déformation.
- Utiliser la typographie et les codes visuels de l’interface réelle lorsque celle-ci est reconstruite.
- Préparer un poster dédié, stable et représentatif, cohérent avec la première image de la vidéo.

## 5. Comparaisons et résultats

- Identifier sans ambiguïté chaque colonne ou état : Entrée, Prédiction, Référence, Avant, Après, etc.
- Vérifier que chaque image correspond réellement à son libellé.
- Ne jamais afficher deux fois la même image pour représenter deux résultats différents.
- Montrer uniquement des exemples suffisamment lisibles et représentatifs.
- Présenter les métriques exactes avec leur contexte et leur protocole d’évaluation.
- Ne pas faire passer une métrique d’entraînement pour une métrique de validation.
- Ne pas prétendre qu’une correction de code a modifié un résultat déjà produit ou un modèle déjà entraîné.
- Présenter les limites honnêtement, notamment lorsqu’un résultat est plausible sans être historiquement ou factuellement garanti.

## 6. Schémas et architectures

- Utiliser un schéma validé comme source de vérité pour les composants, libellés, positions et connexions.
- Recréer le schéma en SVG dans la composition plutôt que d’animer une capture statique.
- Révéler le flux dans l’ordre : bloc → liaison → déplacement du curseur → bloc suivant.
- Ne jamais afficher le schéma complet dès le début si la scène est censée expliquer son fonctionnement.
- Garder les nœuds déjà révélés visibles afin que le spectateur comprenne la continuité du parcours.
- Distinguer les parcours fonctionnels par couleur uniquement lorsque la distinction apporte du sens.
- Faire apparaître le cadre ou la frontière d’un système au début de la scène, pas avant celle-ci.
- Masquer chaque liaison avant son étape et vérifier qu’aucun trait parasite n’est visible.
- Préférer un chemin continu masqué pour une révélation progressive ; les pointillés peuvent neutraliser un mécanisme basé uniquement sur `stroke-dashoffset`.
- Pour une branche secondaire, terminer ou masquer clairement le parcours principal avant de commencer le suivant.

## 7. Curseurs et chemins SVG

- Ne jamais simuler un chemin coudé par une interpolation directe entre ses coordonnées de départ et d’arrivée.
- Calculer la position du curseur sur la géométrie réelle du chemin, par exemple avec `getPointAtLength()`.
- Synchroniser la progression du curseur avec le tracé de la liaison.
- Utiliser un curseur indépendant par liaison lorsque plusieurs animations peuvent se chevaucher ou conserver un état final.
- Garantir qu’un seul curseur est visible à la fois, sauf choix narratif explicite.
- Entre deux branches non connectées, masquer complètement le premier curseur avant d’initialiser le suivant.
- Faire apparaître le curseur sur le premier point du chemin et le masquer seulement après son arrivée.
- Employer un easing régulier comme `sine.inOut` pour les déplacements techniques ; éviter les accélérations trop brutales.
- Vérifier image par image que le centre du curseur reste sur la liaison, notamment dans les angles.

## 8. Texte et lisibilité

- Donner la priorité aux phrases courtes et immédiatement compréhensibles.
- Éviter les formulations commerciales, exagérées ou autocongratulatoires.
- Décrire les apprentissages par des concepts et des résultats observables.
- Éviter les formulations comme « codé à la main » ou « sans framework » lorsqu’elles ressemblent davantage à une mise en scène qu’à une information utile.
- Ne pas afficher de code décoratif, de chemins locaux ou de mentions internes.
- Ajouter la stack discrètement, seulement si elle améliore la compréhension.
- Limiter le nombre de métriques, badges et sous-titres simultanés.
- Pour un effet machine à écrire, attendre que le graphique principal soit entièrement construit.
- Pour une réponse d’IA, distinguer visuellement la question, l’identité de l’assistant, la réponse et la source.
- Mettre en valeur uniquement l’information importante dans la réponse, sans changer brutalement de typographie.

## 9. Audio

- Décider dès le storyboard si la vidéo est silencieuse ou sonorisée.
- Si aucun audio n’est nécessaire, supprimer toutes les pistes et vérifier l’absence de flux audio dans le MP4.
- Si des effets sonores sont utilisés, les associer à des actions précises : saisie, envoi, révélation ou changement d’état.
- Éviter d’ajouter des sons uniquement pour remplir le silence.
- Utiliser seulement des médias dont les droits de redistribution sont documentés.
- Ne pas utiliser de musique sans licence claire.
- Vérifier la synchronisation, le niveau sonore et l’absence de saturation sur le rendu final.

## 10. Confidentialité et authenticité

- Utiliser uniquement des données publiques, anonymisées ou fictives.
- Retirer les noms d’entreprise, clients, comptes, contacts, emails, URLs internes et chemins locaux.
- Ne pas afficher de cookies, tokens, clés, identifiants, noms de fichiers confidentiels ou extraits reconnaissables de documents privés.
- Préférer des exemples neutres et cohérents avec le fonctionnement réel du projet.
- Ne pas présenter une interface fictive comme une capture réelle ; une reconstruction doit rester fidèle aux fonctions existantes.
- Scanner les textes, compositions et médias avant intégration au portfolio.

## 11. Règles HyperFrames et GSAP

- Utiliser une timeline unique, pausée, déterministe et pilotable par HyperFrames.
- Ne pas dépendre de timers, de l’heure courante, d’événements utilisateur ou d’aléatoire non déterministe.
- Définir explicitement l’état initial des éléments à la frontière temporelle de leur scène.
- Ne pas laisser un élément d’une scène tardive visible à la première image avant que la timeline ne l’initialise.
- Utiliser principalement `opacity`, `x`, `y`, `scale` et les transformations compatibles avec le rendu.
- Ne pas animer directement la visibilité d’un élément `.clip` ; animer ses enfants et laisser HyperFrames gérer le cycle de vie des scènes.
- Employer `fromTo` lorsque plusieurs animations modifient la même propriété afin d’éviter les états implicites.
- Calculer les constantes de position une seule fois avant le rendu.
- Conserver des animations seek-safe : une capture prise directement au milieu de la vidéo doit produire le même état qu’une lecture depuis le début.
- Éviter les boucles infinies et définir toutes les durées dans la timeline.

## 12. Protocole de validation

1. Exécuter `hyperframes lint`.
2. Exécuter `hyperframes check --snapshots` et examiner les diagnostics de runtime, layout, motion et contraste.
3. Contrôler les keyframes ou l’animation map lorsque l’outil est disponible.
4. Générer un premier rendu MP4.
5. Regarder le rendu complet à vitesse normale.
6. Extraire des images fixes sur toute la vidéo, au minimum toutes les deux secondes.
7. Pour une transition ou un parcours complexe, extraire au moins quatre images par seconde.
8. Assembler les captures en planches-contact et les examiner dans l’ordre chronologique.
9. Inspecter individuellement les images proches des transitions, angles, révélations et dernières secondes.
10. Corriger puis recommencer le contrôle complet si une seule anomalie subsiste.
11. Décoder intégralement le MP4 final et vérifier ses métadonnées.
12. Vérifier le poster, la première image, les chemins relatifs et le chargement depuis un serveur HTTP local.
13. Exécuter le scan de confidentialité et `git diff --check`.

## 13. Critères d’acceptation

- Aucun écran vide ou presque vide.
- Aucun élément visible avant son étape.
- Aucun saut, flash, doublon ou élément fantôme.
- Aucune transition incompréhensible ou brutalement coupée.
- Aucun texte masqué, tronqué ou trop rapide à lire.
- Aucune image floue, déformée ou agrandie artificiellement.
- Chaque flèche, liaison et curseur suit le parcours prévu.
- La vidéo est compréhensible sans commentaire oral extérieur.
- Le rendu final possède la résolution, la cadence, la durée, le codec et l’état audio prévus.
- Le poster correspond à la vidéo finale.
- Aucun contenu confidentiel ou chemin local n’est présent.
- Une série complète de captures a été validée après la dernière modification.

## 14. Erreurs à éviter

- Commencer une scène par une grande surface vide et un texte isolé.
- Utiliser quatre scènes presque identiques qui donnent l’impression de revoir le même écran.
- Afficher tous les nœuds puis toutes les connexions au lieu de construire le flux dans son ordre logique.
- Faire disparaître une scène au moment où sa dernière animation se termine.
- Remplacer brutalement un schéma par un autre sans transition ni continuité visuelle.
- Laisser un trait, une flèche, un curseur ou le contenu de la scène suivante apparaître trop tôt.
- Interpoler directement le début et la fin d’une liaison coudée : le curseur coupe alors les angles.
- Réutiliser un curseur visible sur des branches déconnectées : son repositionnement ressemble à une téléportation.
- Valider uniquement la composition ou quelques captures et ne pas contrôler le MP4 final.
- Utiliser une capture basse résolution comme visuel principal.
- Afficher une réponse d’IA sans attribution claire ni source visible.
- Ajouter une animation, une musique ou un effet sonore sans fonction narrative.
- Rendre une vidéo plus longue en ajoutant du contenu artificiel.
- Laisser la vidéo parler davantage de l’outil de génération que du projet présenté.

## 15. Archivage

- Conserver le brief, le storyboard, la composition, les sources, les posters et le rendu final.
- Séparer les rendus temporaires de la vidéo destinée au portfolio.
- Préserver la vidéo originale lorsqu’une nouvelle version est créée.
- Conserver les planches-contact de la dernière validation réussie.
- Documenter les choix importants afin de pouvoir reprendre le projet sans reconstruire tout le contexte.
