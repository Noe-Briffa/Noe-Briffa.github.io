# Audit de référence, restructuration du portfolio

## Direction visuelle

Portfolio éditorial calme : papier blanc cassé, encre vert sombre, accent lime, règles fines, titres serif à fort contraste et beaucoup d’espace. La signature visuelle reste l’ombre décalée lime du panneau de repères, sans multiplier les rotations ni les accents colorés.

## Éléments préservés

- Contenu des quatre études de cas, ancres, vidéos, résumés, diagrammes et liens existants.
- Métadonnées SEO, favicon, chargement différé, textes alternatifs, focus clavier et support de `prefers-reduced-motion`.
- Structure HTML statique, chemins publics locaux et absence de nouvelle dépendance.

## Priorités

- **P0** : rendre le positionnement lisible dès le hero, conserver des CTA CV/contact fiables, garder une seule balise `h1` et une navigation accessible.
- **P1** : transformer l’index en trois projets mis en avant, ajouter le manifeste et renforcer le pied de page.
- **P0 corrigé** : les visuels des cartes sont les quatre images découpées depuis la planche de référence, et non les posters vidéo.
- **P2** : poursuivre, si nécessaire, l’harmonisation visuelle des sections de cas d’étude sans toucher à leur contenu.

## Structure cible

Navigation fine → hero compact → repères → manifeste court → trois projets mis en avant → footer compact. La homepage est intentionnellement une landing page d’environ un écran desktop.

Les détails des projets vivent sur des pages dédiées dans `projets/`. Il n’y a pas de slider dupliqué sur la homepage.

## Projets mis en avant

1. Colorisation d’images, vision par ordinateur.
2. Local RAG Assistant, IA locale.
3. WarungFit, application mobile et recommandations nutritionnelles.

Local Second Brain reste accessible depuis l’index « Tous les projets » et la navigation entre études de cas.

## Limites de périmètre

Pas de migration de framework, pas de dépendance, pas de suppression de cas d’étude, pas d’invention d’URL sociale, pas de modification backend. Les quatre assets PNG sont des découpes directes de la planche fournie.

## Vérification

- [ ] `git diff --check`
- [ ] Tous les `img` ont un `alt` significatif.
- [ ] Les ressources locales référencées existent.
- [ ] Une seule `h1`, hiérarchie de titres cohérente.
- [ ] Homepage sans slider : exactement trois cartes mises en avant, lien WarungFit, CV, email, canonical et OG présents.
- [ ] Les quatre pages de projet existent, sont reliées et conservent les contenus détaillés, vidéos, diagrammes, métriques, limites et liens.
- [ ] Affichage mobile, navigation clavier et réduction des animations vérifiés.
