# Guide vidéo pour les prochains projets

Document de préparation et de contrôle pour les vidéos de présentation de projets.

## Avant génération

- Définir l’objectif : montrer le travail technique, pas seulement l’interface.
- Préparer un storyboard court avant de générer la composition.
- Sélectionner les meilleures sorties après inspection visuelle humaine.
- Vérifier les droits des images, vidéos, polices et musiques.
- Utiliser des exemples représentatifs du projet.
- Préparer les métriques exactes et leur protocole d’évaluation.
- Écrire le parcours narratif complet avant l’animation : problème → traitement → résultat → apprentissage.
- Donner à chaque scène un sujet visuel principal déjà visible dès sa première image ; éviter tout écran vide ou presque vide.
- Prévoir une durée réaliste par étape. Si une vidéo est accélérée ou ralentie ensuite, appliquer un facteur uniforme à toute la timeline.
- Définir explicitement les transitions : ce qui disparaît, ce qui reste et pourquoi la scène suivante commence.

## Images et comparaisons

- Garder les images originales sans texte incrusté.
- Ajouter les libellés dans la composition vidéo, avec une zone dédiée.
- Identifier clairement chaque colonne : Entrée, Prédiction, Référence.
- Ne jamais afficher deux fois la même image.
- Vérifier la correspondance entre chaque image et son libellé.
- Montrer uniquement des prédictions suffisamment convaincantes.
- Conserver les fichiers source propres pour permettre des corrections rapides.

## Texte et positionnement

- Expliquer ce que le projet permet de comprendre.
- Mettre au premier plan les données, le modèle, le pipeline, l’entraînement et l’évaluation.
- Éviter les formulations commerciales ou trop ambitieuses.
- Ne pas citer une technique qui n’a pas contribué au résultat montré.
- Ne pas afficher de mention interne comme `V1 Portfolio`.
- Limiter le nombre de métriques et préciser leur contexte.
- Présenter les limites du projet honnêtement.
- Ajouter la stack discrètement, seulement si elle améliore la compréhension.
- Décrire les apprentissages avec des concepts et des résultats observables, pas avec des extraits de code décoratifs.
- Éviter les formulations qui donnent l’impression de se mettre en scène (« codé à la main », « sans framework clé en main ») lorsqu’elles n’ajoutent pas d’information utile.
- Pour une réponse d’IA, distinguer visuellement la question utilisateur, l’identité de l’assistant, la réponse et la source.
- Utiliser la typographie de l’interface réelle dans les reconstitutions ; ne pas agrandir une capture basse résolution.

## Contrôle final

- Vérifier chaque scène à plusieurs moments du rendu.
- Contrôler titres, libellés, alignements, transitions et débordements.
- Vérifier qu’aucun ancien texte ou visuel ne reste dans la composition.
- Exécuter `lint`, `inspect` et `check` Hyperframes.
- Contrôler résolution, durée, cadence et audio.
- Regarder le rendu complet avant validation.
- Archiver storyboard, brief, composition et rendu final.
- Capturer des images fixes à intervalles réguliers, notamment au milieu de chaque transition et juste avant/après chaque révélation.
- Examiner des planches-contact plutôt que quelques images isolées : elles révèlent les sauts, éléments fantômes, traits prématurés et changements de mise en page.
- Vérifier que chaque trait, flèche ou chemin SVG est invisible avant son étape et se révèle dans le bon ordre ; préférer un chemin continu masqué à un pointillé difficile à neutraliser.
- Contrôler les transitions entre deux variantes d’un même schéma : conserver un seul espace visuel et transformer son état progressivement au lieu de dupliquer l’écran.
- Tester le rendu final, pas seulement la composition : décodage intégral du MP4, métadonnées, cadence, durée, codec, poster et présence ou absence d’audio.
- Si l’audio est demandé, ajouter peu d’effets, chacun synchronisé avec une action identifiable ; sinon supprimer entièrement les pistes et vérifier qu’aucune balise audio ne subsiste.
- Tester la première image et le poster séparément : ils doivent être stables, lisibles et représentatifs de la vidéo.

## Erreurs à éviter

- Utiliser une image de démonstration parce qu’elle est disponible, sans vérifier la qualité de sa prédiction.
- Dupliquer un visuel ou laisser un ancien titre intégré dans une image.
- Faire croire qu’une métrique d’entraînement est une métrique de validation.
- Présenter une correction de code comme si elle avait modifié un checkpoint déjà entraîné.
- Laisser la vidéo parler de l’outil de génération au lieu du projet présenté.
- Ajouter une scène ou une animation sans vérifier son rendu réel.
- Commencer une scène par une surface vide avec un petit texte isolé ; montrer immédiatement l’interface, le document ou le schéma concerné.
- Afficher un schéma complet instantanément alors que le récit prétend expliquer un flux ; révéler les nœuds et les flèches dans l’ordre du parcours.
- Laisser un élément de la scène suivante apparaître avant la transition, ou faire disparaître le contexte sans expliquer son passage vers la génération.
- Utiliser une capture floue ou basse résolution comme visuel principal ; reconstruire les éléments lisibles en HTML/SVG à partir des sources réelles.
- Mettre une réponse technique en scène sans attribution claire à l’assistant ou sans source visible.
- Ajouter de la musique ou des effets dont les droits de redistribution ne sont pas documentés.
- Rendre une vidéo plus longue en ajoutant du contenu artificiel ; ralentir uniformément les scènes existantes si seule la durée doit changer.
- Valider sur quelques captures seulement : inspecter les transitions et les dernières secondes, qui concentrent souvent les défauts les plus visibles.
