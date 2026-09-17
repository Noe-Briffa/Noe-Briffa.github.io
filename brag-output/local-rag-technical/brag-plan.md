# Brag Plan: Local RAG Assistant — technique

## What is this app?
Un pipeline RAG local sur PDF, dont les étapes de retrieval et de génération sont orchestrées directement en Python.

## The angle
Rendre visible le travail de compréhension : chaque fonction représente une étape du RAG avant l’appel au modèle local.

## Hook (first 2-3 seconds)
« Pas de framework RAG clé en main. »

## Key moments (the middle)
- Extraction, chunking et indexation ChromaDB.
- Embeddings et sélection MMR.
- Contexte formaté, prompt puis appel llama.cpp.

## Outro / punchline
« Une réponse locale. Une source vérifiable. »

## User flow worth showing
Ingestion → retrieval MMR → génération → réponse sourcée.

## Tone
- Preset: polished
- Creative direction: technical build log
- Interpretation: typographie monospace, transitions nettes et extraits de code courts mais lisibles.

## Format: landscape — 1920x1080
## Duration: 25 seconds

## Visual identity (from the project)
- Background: #17212b
- Accent: #f58220 / #b8e26f
- Text: #f7f3e9
- Display font: Consolas fallback
- Body font: Inter fallback
- Strongest visual element: fonctions réelles de `api/indexer.py` et capture UI.

## Share copy (draft)
J’ai étudié le RAG puis codé son orchestration : extraction PDF, embeddings, MMR, contexte et génération locale avec llama.cpp.

## Audio direction
- Role: intentional silence
- Music: none — licence de redistribution non documentée pour la musique groupée.
- SFX posture: none — rendu silencieux pour éviter toute ambiguïté de licence.
- Restraint rule: priorité à la lisibilité des extraits de code.

## Storyboard

### Scene 1 — Hook — 4.2s
Accroche technique et phrase d’intention.

### Scene 2 — Ingestion — 4.8s
Extraits authentiques : extraction PDF, `chunk_text`, index ChromaDB.

### Scene 3 — Architecture — 5.5s
Schéma Archify montrant les composants locaux.

### Scene 4 — Retrieval / generation — 5.0s
`retrieve_topk`, MMR, `format_context`, prompt et `/completion`.

### Scene 5 — Proof — 5.5s
Capture UI, réponse et source `document.pdf`, puis stack finale.

**Audio summary:** rendu silencieux, sans piste externe non vérifiée.
