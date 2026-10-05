https://noe-briffa.github.io


## Reverse Copilot — projet principal

Site statique HTML/CSS. Reverse Copilot apparaît en premier sur l'accueil et dans le catalogue. La page présente Ghidra, la boucle contrôlée, le benchmark V2 et les limites V2.5. Aucun modèle n'est appelé par le site.

### Reproduire les graphiques

```powershell
python scripts/generate_reverse_copilot.py --comparison '<dossier-comparaison-V2-validé>'
```

Le générateur utilise Python standard library, contrôle les 120 résultats, six groupes et empreintes historiques, puis produit données publiques, trois SVG et tableaux HTML. Les artefacts privés sources ne sont pas distribués. `--output-directory` permet une génération séparée pour comparer les empreintes sans modifier la page.

```powershell
python scripts/check_reverse_copilot.py
python -m http.server 8765 --bind 127.0.0.1
```

Ouvrir `http://127.0.0.1:8765/projets/reverse-copilot.html`. Aucune publication automatique. Les JSON/CSV n'incluent pas de chemins locaux ou d'identifiants privés ; les données manquantes restent null. Méthode complète : `assets/reverse-copilot/method.md`.

### Vérifications de livraison

Huit tests standard library couvrent les 120 cas, six groupes, compteurs incomplets, export répété à l’identique, rejet des données altérées, ordre des projets, liens et tableaux accessibles. Contrôle navigateur : accueil, catalogue et page projet à 390, 768 et 1440 pixels, sans débordement de page ni image manquante. Focus clavier visible et ouverture des tableaux par Entrée vérifiés ; règles CSS de réduction des animations contrôlées. Les graphiques défilent localement sur mobile. Les captures de contrôle restent hors du site. Résumé public : `assets/reverse-copilot/validation.json`.
