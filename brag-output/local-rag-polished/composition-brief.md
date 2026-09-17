# Hyperframes Composition Brief: Local RAG Assistant — polished

## Objective
Create a polished 25-second portfolio video showing the complete local PDF RAG flow and the Python orchestration behind it.

## Output
- Composition: `brag-output/local-rag-polished/composition/`
- Render: `brag-output/local-rag-polished/brag.mp4`
- Format: landscape, 1920x1080, 25 seconds

## Source material
- Project root: source project (local path intentionally omitted)
- UI reference: rebuilt as crisp HTML/CSS from the real application
- Architecture source: rebuilt as animated HTML/SVG from the Archify component graph
- Product: Local RAG Assistant
- Copy: « Comprendre un RAG en le construisant. »; « Pipeline RAG local, orchestré en Python. »

## Creative direction
Polished technical product film. Preserve a clear visual subject in every scene, build the architecture progressively, and end on a readable sourced answer. Avoid generic AI claims and confidential data.

## Visual identity
Background #f4f1e9; text #18211f; accents #f58220 and #b8e26f; Georgia/Inter fallbacks.

## Storyboard
1. Hook — 0–3s — title and crisp reconstructed UI.
2. Ingestion — 3–6s — PDF extraction and chunking.
3. Indexation — 6–9s — embeddings into ChromaDB.
4. Question — 9–12s — typed question and send action.
5. Retrieval — 12–17s — architecture nodes and edges revealed in order; the green return path appears only after selection and is explicitly labelled.
6. Local generation — 17–21s — the same diagram remains visible while the header changes and the orange branch reaches llama-server and GGUF.
7. Proof — 21–25s — a compact conversation identifies « Assistant local », presents the answer as a sentence, and keeps `ORION-742` plus `document.pdf p.1` readable.

## Audio
No music and no voiceover. Use only four low-volume CC0 effects from the Brag asset pack for typing, send, the retrieval-to-generation handoff, and final reveal.

## Hyperframes requirements
Use deterministic seek-safe GSAP; never move the visual subject out of frame. Keep all text readable and validate with `hyperframes lint`, `check`, `keyframes`, 73 composition snapshots, then the same 73 timestamps from the final MP4 before delivery.
