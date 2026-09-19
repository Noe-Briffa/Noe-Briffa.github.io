# Local Second Brain — checklist de refonte vidéo

## Suivi

- [x] Checklist créée avant modification
- [x] Points finaux retirés dans `index.html`
- [x] Première scène corrigée dans la composition
- [x] Scène Sources différenciée
- [x] Scène Pipeline différenciée
- [x] Scène Enrichissement différenciée
- [x] Nœud `Agents IA compatibles MCP` ajouté
- [x] Schéma Archify validé
- [x] Architecture SVG animée dans la vidéo
- [x] Première composition contrôlée
- [x] Rendu MP4 généré
- [x] 23 images contrôlées toutes les 2 secondes
- [x] Problèmes visuels corrigés et nouveau rendu effectué si nécessaire
- [x] Poster vérifié
- [x] Portfolio testé via HTTP local
- [x] Scan de confidentialité terminé
- [x] Checklist finale complétée

## Journal de validation

| Étape | Résultat | Notes |
|---|---|---|
| Création de la checklist | OK | Créée avant toute autre modification |
| Page et architecture | OK | Liste nettoyée, spécification Archify validée et branche MCP ajoutée |
| Composition | OK | Nouvelles scènes, SVG animé, lint/check HyperFrames sans erreur |
| Contrôle intermédiaire | À CORRIGER | Le frame 0 était trop vide, correction appliquée avant nouveau rendu |
| Contrôle final | OK | 23 images à t=0,2…44 s inspectées ; transition à 28 s continue et nœud agents lisible |
| Rendu et intégration | OK | MP4 silencieux 45 s copié dans `assets/local-second-brain/`, poster régénéré |
| Vérifications | OK | ffprobe, serveur HTTP local et scan de confidentialité réussis |

## Passe 2 — mini-schémas, transitions et parcours animé

- [x] Nouvelle passe ouverte avant modification
- [x] Spécification Archify des flux créée
- [x] Vue Sources validée et livrée
- [x] Vue Pipeline validée et livrée
- [x] Vue Enrichissement validée et livrée
- [x] Scène Sources remplacée par un flux Archify animé
- [x] Scène Pipeline remplacée par un flux Archify animé
- [x] Scène Enrichissement remplacée par un flux Archify animé
- [x] Transition Pipeline → Enrichissement explicitée
- [x] Transitions ralenties sans dépasser 45 secondes
- [x] Architecture principale animée bloc → liaison → bloc
- [x] Point lumineux synchronisé avec les liaisons
- [x] Contrôle HyperFrames réussi
- [x] 23 images contrôlées après le nouveau rendu
- [x] Contrôle technique et confidentialité terminés

| Flux Archify | OK | Validation showcase 9/9, livraison et visual-check sans débordement |
| Composition pass 2 | OK | Scènes 2–4 refondues, transitions ralenties et curseurs synchronisés |
| Rendu pass 2 | OK | MP4 silencieux 45 s régénéré et copié dans `assets/local-second-brain/` |
| Contrôle visuel pass 2 | OK | Planche de 23 images inspectée ; aucun écran vide bloquant ni chevauchement identifié |

## Passe 3 — légendes, transitions et apprentissages

- [x] Légende Sources convertie en apparition type machine à écrire après le flux
- [x] Légende Pipeline convertie en apparition type machine à écrire après le flux
- [x] Bandeau `Pipeline — Enrichissement` supprimé
- [x] Séquence Enrichissement terminée avant la sortie de scène
- [x] Transition Enrichissement → Architecture rendue progressive
- [x] Cadre `Traitements locaux` révélé au début de l’architecture
- [x] Premiers blocs visibles dès l’entrée des scènes pour éviter les panneaux vides
- [x] Quatre apprentissages révélés séquentiellement de gauche à droite
- [x] Contrôle HyperFrames relancé après les corrections
- [x] Nouveau rendu MP4 généré et poster régénéré
- [x] 23 images finales contrôlées à t=0,2…44 s
- [x] Contrôles ffprobe, HTTP, confidentialité et diff Git relancés

| Correction finale | OK | Légendes typewriter, transition progressive et apprentissages séquencés |
| Contrôle final pass 3 | OK | 23 images inspectées ; aucune scène vide ou coupure bloquante |

## Passe 4 — transitions, curseur et séquence finale

- [x] Transition Sources → Pipeline adoucie autour de 12–13 s
- [x] Transition Pipeline → Enrichissement adoucie autour de 19–20 s
- [x] Curseur lumineux de l’architecture ralenti, renforcé et resynchronisé
- [x] Éléments de la scène finale masqués avant leur apparition séquentielle
- [x] HyperFrames `check --snapshots` relancé : 0 erreur et 0 avertissement
- [x] Rendu MP4 silencieux régénéré et copié dans `assets/local-second-brain/`
- [x] 23 images à t=0,2…44 s contrôlées après le nouveau rendu
- [x] Images critiques des transitions, de l’architecture et de la conclusion contrôlées
- [x] Poster régénéré depuis le rendu final
- [x] Contrôles ffprobe, HTTP, confidentialité et `git diff --check` terminés

| Correction finale | OK | Fondus renforcés aux frontières 12–13 s et 19–20 s |
| Parcours architecture | OK | Curseur visible plus longtemps, avec déplacement ralenti entre les nœuds |
| Conclusion | OK | La liste démarre masquée puis révèle les éléments dans l’ordre |
| Contrôle final pass 4 | OK | 23 images régulières et captures critiques inspectées ; aucun écran vide bloquant |

## Passe 5 — fondu initial et temps de lecture architecture

- [x] Fondu sortant de l’accroche ajouté entre 4,95 s et 5,75 s
- [x] Fondu entrant de la scène Sources repositionné autour de 5,75–6 s
- [x] Parcours Architecture avancé pour laisser environ deux secondes de lecture stable avant la scène finale
- [x] Scène finale décalée à 38 s sans changer la durée totale de 45 s
- [x] HyperFrames `check --snapshots` relancé
- [x] Nouveau MP4 silencieux rendu et copié dans `assets/local-second-brain/`
- [x] Contrôle ciblé des transitions 5–6 s et de la fin Architecture effectué
- [x] Planche de 23 images à t=0,2…44 s contrôlée
- [x] Poster, ffprobe, confidentialité et `git diff --check` vérifiés

| Correction finale | OK | Accroche terminée avant l’entrée de Sources ; aucun chevauchement de texte illisible |
| Architecture | OK | Dernière liaison terminée avant un maintien visuel d’environ deux secondes |
| Contrôle final pass 5 | OK | Transitions et planche complète inspectées ; durée et format inchangés |

## Passe 6 — fluidité du curseur et contrôle dense

- [x] Skills HyperFrames et HyperFrames Animation relus avant modification
- [x] Curseur agrandi, halo renforcé et déplacement `sine.inOut` appliqué
- [x] Durées des étapes Architecture redistribuées pour ralentir le parcours
- [x] 42 images Architecture contrôlées à 4 images par seconde
- [x] 23 images globales contrôlées toutes les deux secondes
- [x] Trou visuel entre Architecture et la scène finale détecté puis corrigé
- [x] Nouveau rendu MP4 et poster générés
- [x] Contrôle HyperFrames relancé : 0 erreur, 0 avertissement de lint/runtime/motion
- [x] `ffprobe`, confidentialité et `git diff --check` vérifiés

| Curseur Architecture | OK | Trajectoire ralentie, halo visible et easing progressif contrôlés sur les images clés |
| Transition finale | OK | Le fondu est prolongé jusqu’à l’entrée de la scène finale, sans écran vide |
| Contrôle dense pass 6 | OK | Contact sheets Architecture et globale inspectées après le rendu final |

## Passe 7 — suivi géométrique des liaisons SVG

- [x] Curseur partagé remplacé par un curseur indépendant pour chaque liaison
- [x] Position calculée avec `getPointAtLength()` sur la géométrie réelle des chemins
- [x] Trois parcours Architecture ordonnés et changements de branche masqués
- [x] Un seul curseur visible à la fois
- [x] Dernier parcours terminé environ deux secondes avant la sortie de scène
- [x] HyperFrames `lint` et `check --snapshots` exécutés
- [x] 90 images globales contrôlées à deux images par seconde
- [x] 42 images Architecture contrôlées à quatre images par seconde
- [x] Virages des chemins API → Pipeline et MCP → Obsidian contrôlés individuellement
- [x] Nouveau MP4 copié dans le portfolio
- [x] `VIDEO_GUIDELINES.md` enrichi avec les règles de suivi SVG
- [x] Métadonnées, confidentialité et `git diff --check` vérifiés

| Point contrôlé | Résultat | Preuve |
|---|---|---|
| Suivi des chemins | OK | Les curseurs restent centrés sur les segments horizontaux, verticaux et les angles |
| Changements de branche | OK | Chaque curseur disparaît avant l’initialisation du parcours suivant |
| Contrôle dense | OK | 90 captures globales et 42 captures Architecture réunies en planches-contact |
| Temps de lecture final | OK | Le dernier curseur disparaît avant 36,1 s ; la sortie commence à 38,05 s |
