# Reprise — intégration Local RAG Assistant

## État actuel

- Portfolio statique étendu à deux études de cas dans `index.html`.
- Projet colorisation conservé.
- Étude Local RAG ajoutée avec objectif, flux, architecture, stack, difficulté réelle et limites.
- Capture UI et schéma d’architecture copiés dans `assets/local-rag/`.
- Version polished intégrée par défaut dans la page.
- Variante technique accessible depuis la page pour comparaison.
- Aucun nom d’entreprise, document métier ou chemin local conservé dans les fichiers publiables.

## Vidéos produites

- `brag-output/local-rag-polished/brag.mp4` — 20 s, 1920×1080, 30 fps.
- `brag-output/local-rag-technical/brag.mp4` — 25 s, 1920×1080, 30 fps.
- Posters extraits et intégrés comme première frame.
- Storyboards et briefs présents dans chaque dossier.
- Rendus silencieux : aucune musique dont les droits de redistribution seraient ambigus.

## Vérifications effectuées

- `hyperframes lint` : OK pour les deux compositions.
- `hyperframes check` : OK pour les deux compositions.
- `hyperframes keyframes` et snapshots : OK.
- Métadonnées vidéo : OK, durées et dimensions conformes.
- Serveur HTTP local : index, images et vidéos retournent HTTP 200.
- Capture finale : `portfolio-preview-rag.png`.

## Historique Git local

1. `2e70c70` — snapshot avant intégration.
2. `61d7c74` — étude RAG et structure portfolio.
3. `993a764` — médias, vidéos et documentation brag.
4. `84d10f9` — retrait des chemins locaux des briefs.

Le dépôt n’a aucun remote et rien n’a été poussé.

## À reprendre

1. Regarder les deux vidéos et choisir la version finale à conserver comme vidéo principale.
2. Si nécessaire, améliorer le montage choisi (notamment la lisibilité ou le rythme) puis rerendre.
3. Vérifier le portfolio sur mobile et décider si la capture finale doit être remplacée.
4. Faire un dernier `git diff`, scanner les fichiers suivis, puis créer le commit final.

## Point d’attention

Le dossier `brag-output/*/composition/` reste local et ignoré ; les briefs, storyboards, posters et rendus finaux sont conservés dans Git.
