# Brag Plan: Local RAG Assistant — polished

## What is this app?
Un assistant local répond à une question sur un PDF en retrouvant les passages pertinents puis en générant une réponse sourcée.

## The angle
Montrer que le projet est une compréhension concrète du RAG : l’orchestration extraction → recherche → contexte → génération a été écrite en Python.

## Hook (first 2-3 seconds)
« Comprendre un RAG en le construisant. »

## Key moments (the middle)
- Une question apparaît dans l’interface réelle.
- L’architecture locale révèle les étapes du pipeline.
- La réponse revient avec la source `document.pdf`.

## Outro / punchline
« Pipeline RAG local, orchestré en Python. »

## User flow worth showing
Question → recherche des passages → réponse locale et source.

## Tone
- Preset: polished
- Creative direction: quiet technical product film
- Interpretation: mouvements fluides, peu de texte, preuve visuelle avant les slogans.

## Format: landscape — 1920x1080
## Duration: 25 seconds

## Visual identity (from the project)
- Background: #f4f1e9
- Accent: #f58220 / #b8e26f
- Text: #18211f
- Display font: Georgia fallback
- Body font: Inter fallback
- Strongest visual element: capture UI et schéma d’architecture Archify.

## Share copy (draft)
J’ai construit un RAG local en Python : PDF, recherche vectorielle, contexte et réponse sourcée, sans framework RAG clé en main.

## Audio direction
- Role: ponctuation discrète des interactions.
- Music: aucune.
- SFX posture: trois sons CC0 du pack Brag (saisie, envoi, révélation finale), à faible volume.
- Restraint rule: le son confirme l’action sans prendre le dessus sur la lisibilité.

## Storyboard

### Scene 1 — Accroche — 0 à 3s
« Comprendre un RAG en le construisant. » avec une interface HTML nette déjà visible.

### Scene 2 — Ingestion — 3 à 6s
Le document `document.pdf` entre dans le pipeline et devient trois passages distincts.

### Scene 3 — Indexation — 6 à 9s
Les passages deviennent des embeddings, puis rejoignent un index ChromaDB local.

### Scene 4 — Question — 9 à 12s
La question de démonstration neutre est saisie dans l’interface reconstruite en HTML.

### Scene 5 — Recherche — 12 à 17s
Le schéma se construit progressivement : Utilisateur → Interface web → FastAPI → ChromaDB → sentence-transformers, puis le contexte revient vers FastAPI.

### Scene 6 — Génération locale — 17 à 21s
Le chemin FastAPI → llama-server → modèle GGUF est révélé et animé en orange.

### Scene 7 — Preuve — 21 à 25s
Gros plan sur la question, la réponse `ORION-742` et la source `document.pdf p.1`.

**Audio summary:** trois accents CC0 discrets, sans voix off ni musique.
