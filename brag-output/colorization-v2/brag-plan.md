# Brag plan — Colorisation d’images v2

## Angle

Présenter la colorisation comme un parcours complet de computer vision : une image en niveaux de gris devient une prédiction colorisée, puis le résultat est comparé à une référence.

## Format

- 1920×1080, 30 fps, environ 40 secondes
- Français, sans musique, voix off ni effets sonores
- Palette éditoriale crème, vert sourd et orange
- Assets exclusivement issus de `assets/colorization/`

## Storyboard

1. Accroche — 0–5 s : entrée en niveaux de gris et promesse de colorisation.
2. Résultat — 5–11 s : entrée, prédiction et référence dans trois cartes distinctes.
3. Prétraitement — 11–16 s : RGB, CIELAB et canal L révélés dans l’ordre.
4. Pipeline — 16–23 s : canal L, U-Net + CBAM et reconstruction RGB.
5. Évaluation — 23–30 s : comparaison triptyque et métriques déjà présentes dans le projet.
6. Apprentissage — 30–36 s : prétraitement, architecture, inférence et évaluation.
7. Conclusion — 36–40 s : résultat plausible, référence nécessaire, limites explicites.

## Principes de contrôle

Chaque scène possède un sujet visuel immédiat. Les flèches sont masquées avant leur étape et révélées par tracé. Les cartes d’entrée, de prédiction et de référence restent explicitement étiquetées. Aucun contenu métier, chemin local ou extrait de code n’est affiché.
