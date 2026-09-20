# Prochaines étapes du portfolio

## Priorité 1 — Fiabiliser et clôturer

- [x] Synchroniser le suivi WarungFit avec la vidéo actuellement intégrée.
- [x] Vérifier les chemins relatifs et la présence des médias référencés par `index.html`.
- [x] Vérifier les vidéos finales avec `ffprobe` : codec, dimensions, fréquence et durée.
- [x] Vérifier les ressources publiées avec un serveur HTTP local.
- [x] Retirer les captures et logs temporaires générés par les vérifications locales.
- [x] Refaire un scan de confidentialité sur les fichiers publiables et les métadonnées.
- [x] Relire `git diff --check` et inspecter le diff final.
- [x] Vérifier que seuls les fichiers destinés au portfolio seront inclus dans le commit de clôture.
- [x] Créer un commit propre regroupant l’intégration du portfolio, les médias et la documentation associée.

## Priorité 2 — Repenser la page pour les recruteurs

- [x] Ajouter une introduction claire avec le profil, les spécialités et l’objectif professionnel.
- [x] Ajouter des liens visibles vers le CV et un moyen de contact ; LinkedIn reste volontairement absent.
- [x] Définir une architecture de page : profil, sélection de projets, études de cas, contact.
- [x] Donner une entrée courte aux quatre projets avant les détails techniques.
- [x] Harmoniser la hiérarchie éditoriale des études de cas.
- [x] Relire les textes visibles avec le skill Humanizer.
- [x] Recentrer le hero sur le profil SSI, l’IA appliquée, l’automatisation et la recherche de stage.
- [x] Ouvrir les trois liens CV dans un nouvel onglet sans forcer le téléchargement.
- [x] Réduire la densité mobile : navigation, hero, comparaison colorisation et boutons.
- [x] Ajouter les métadonnées SEO et Open Graph, avec une image de partage dédiée.
- [x] Ajouter un favicon.
- [x] Vérifier l’accessibilité : hiérarchie des titres, contrastes, textes alternatifs et navigation au clavier.
- [x] Vérifier les liens, les ancres et les ressources locales et externes.
- [x] Recompresser les quatre vidéos publiques et conserver leurs dimensions, durées et cadence.
- [x] Réduire le poids des images principales et des vidéos publiques sans changer les chemins utilisés par la page.
- [x] Vérifier la version finale sur mobile, desktop et réseau lent.
- [ ] Ajouter l’URL publique du portfolio au CV et aux profils professionnels.

## Priorité 3 — Évolutions éventuelles

- [ ] Envisager une migration React uniquement si une interaction réelle le justifie.
- [ ] Envisager React Three Fiber uniquement pour une visualisation 3D dédiée ; ne pas l’installer comme dépendance générale.
- [ ] Déployer le portfolio sur GitHub Pages.
- [ ] Faire la revue recruteur finale et créer un commit propre.

## Ordre recommandé

1. Repenser la structure et les textes de la page.
2. Ajouter SEO, Open Graph et favicon.
3. Vérifier accessibilité, médias, mobile et réseau lent.
4. Déployer sur GitHub Pages.
5. Faire la revue recruteur finale.
6. Terminer le scan de confidentialité et créer un commit propre.
