# Hyperframes Composition Brief: WarungFit — captures réelles

## Objective
Créer une nouvelle version silencieuse de la présentation WarungFit, en remplaçant les interfaces reconstruites par les captures réelles fournies par l'utilisateur lorsque celles-ci existent.

## Output
- Composition: `brag-output/WarungFit/brag-output-2026-09-19-125010/composition/`
- Video: `brag-output/WarungFit/brag-output-2026-09-19-125010/brag.mp4`
- Format: 1920x1080, 30 fps, 35 seconds
- Audio: none

## Source material
- Captures copiées dans `composition/assets/screens/` depuis le dossier fourni, sans modification des originaux.
- `home.png`: accueil réel.
- `meal-result.png`: résultat réel.
- `fix-result.png`: correction réelle.
- `nutrition-targets.png`: objectifs réels.
- `banniere.png`: identité visuelle et poster de référence.
- `meal-photo-user.jpg`: version optimisée de la photo du plat fournie par l'utilisateur pour la scène de scan.
- `fix-device.png`: recadrage du téléphone complet depuis `fix-result.png`.

## Copy changes
- Replace `Vous vérifiez.` with `L'utilisateur vérifie.`
- Keep final line: `L'IA propose. L'utilisateur vérifie.`
- Keep limitation: `Prototype portfolio · estimations approximatives`.

## Visual requirements
- Use `<img>` with `object-fit: cover` where the source capture includes device margins that should be cropped.
- Wrap every screenshot in `.real-shot` with rounded corners, clipping and a restrained shadow.
- Do not crop away meaningful UI, stretch screenshots, or alter their visible text.
- Keep the architecture diagram reconstructed because no architecture screenshot was provided.
- Use `Étude de cas portfolio · produit, UX et architecture` as the closing context line.
- Keep the architecture scene focused on the product flow instead of using a disconnected miniature screenshot.

## Audio requirements
- Remove the `<audio>` element and all music assets from this revision.
- The final MP4 must contain video only.

## Gate
Run `npx hyperframes check`, inspect snapshots, render the delivery MP4, bake the poster as frame 0, then verify with `ffprobe` that the output has no audio stream.
