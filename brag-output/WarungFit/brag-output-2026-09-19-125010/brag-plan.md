# Brag Plan: WarungFit — captures réelles

## Angle
Montrer le vrai produit plutôt qu'une reconstruction : WarungFit part d'un tableau de bord réel, présente un résultat réel, puis montre l'écran réel de correction. Le message reste sobre : l'IA propose, l'utilisateur vérifie.

## Modifications demandées
- Remplacer `Vous vérifiez.` par `L'utilisateur vérifie.` dans le panneau éditorial.
- Supprimer entièrement la musique de fond.
- Livrer une vidéo totalement silencieuse, sans flux audio dans le MP4.
- Utiliser les captures présentes dans `Images pres/ready` sans modifier le dossier source.
- Arrondir chaque capture intégrée et conserver ses proportions.

## Captures utilisées
- `banniere.png` : visuel de marque dans l'introduction et référence du poster.
- `home.png` : écran réel d'accueil dans la scène d'entrée.
- `meal-result.png` : résultat réel dans la scène d'analyse.
- `fix-result.png` : écran réel de correction dans la scène centrale.
- `nutrition-targets.png` : rappel réel des objectifs dans la scène architecture.
- `meal-photo-user.jpg` : version optimisée de la photo du plat fournie par l'utilisateur pour la scène de scan.
- `fix-device.png` : capture recadrée autour du téléphone complet, sans le couper.

## Storyboard révisé — 35 secondes

1. **0–5 s — Le produit réel** : bannière WarungFit et capture `home.png` dans un cadre arrondi.
2. **4,5–10,8 s — L'analyse commence** : nouvelle photo du repas fournie par l'utilisateur dans un cadre éditorial simple.
3. **10,2–19,2 s — Un résultat réel** : capture `meal-result.png`, avec un court label `Estimation à vérifier`.
4. **18,5–26,7 s — L'utilisateur vérifie** : capture `fix-result.png` et panneau éditorial affichant exactement `L'utilisateur vérifie.`
5. **26–31,7 s — Le flux produit** : schéma Flutter → Edge Function → analyse visuelle, avec une phrase de synthèse sur le parcours de vérification.
6. **30,75–35 s — Conclusion** : `L'IA propose. L'utilisateur vérifie.` et `Étude de cas portfolio · produit, UX et architecture`.

## Direction visuelle
- Fond crème existant conservé.
- Captures affichées dans des cadres blancs ou bleu très pâle, rayon `28–36 px`.
- `overflow: hidden` sur les cadres pour éviter les bords abrupts.
- Ombre légère, sans déformation ni agrandissement artificiel.
- Transitions par fondus et déplacements courts.

## Audio
- Aucun audio.
- Pas de musique, pas de narration, pas de SFX.

## Validation
- `hyperframes check`.
- Contrôle des captures à plusieurs instants et des transitions.
- Planche-contact à intervalles de deux secondes.
- Poster extrait d'une image stable puis intégré en première frame.
- `ffprobe` doit confirmer `audio stream = 0`.
