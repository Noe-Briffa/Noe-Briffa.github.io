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
## Duration: 45 seconds

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
- Aucun son, aucune musique et aucune voix off.

## Storyboard

### Scene 1 — Accroche — 0 à 5s
« Comprendre un RAG en le construisant. » avec une interface HTML nette déjà visible.

### Scene 2 — Ingestion — 5 à 10,3s
Le document `document.pdf` entre dans le pipeline et devient trois passages distincts.

### Scene 3 — Indexation — 10,3 à 15,7s
Trois passages deviennent des vecteurs numériques lisibles, puis rejoignent un panneau ChromaDB qui confirme chaque entrée et le nombre de passages prêts pour la recherche.

### Scene 4 — Question — 15,7 à 21,1s
La question de démonstration neutre est saisie dans l’interface reconstruite en HTML.

### Scene 5 — Recherche — 21,1 à 29,2s
Un schéma unique se construit progressivement : Utilisateur → Interface web → FastAPI → ChromaDB → sentence-transformers. Le retour vert n’apparaît qu’une fois les passages sélectionnés et porte le libellé « Contexte sélectionné ».

### Scene 6 — Génération locale — 29,2 à 37,3s
Sans changer d’écran, le titre bascule vers « Génération locale », FastAPI pulse et le même indicateur devient orange avant de suivre FastAPI → llama-server → modèle GGUF.

### Scene 7 — Preuve — 37,3 à 45s
Conversation lisible : question utilisateur, avatar « Assistant local », réponse en phrase naturelle, valeur `ORION-742` mise en évidence et source `document.pdf p.1`.

**Audio summary:** vidéo entièrement silencieuse.
