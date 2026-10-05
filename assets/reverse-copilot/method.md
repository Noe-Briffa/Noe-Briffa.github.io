# Reverse Copilot — méthode des figures publiques

Source : comparaison V2 vérifiée, 20 challenges Windows PE x86-64, trois approches et deux modèles, 120 résultats historiques. Les échecs restent dans les scores. Aucun nouvel appel modèle pour cet export.

Résolution : critères communs de réponse correcte, distincts de la validité des citations et du protocole interactif. Comparaison des approches au sein de chaque modèle.

Tokens : seuls compteurs complets rapportés sont utilisés, sur l'intersection des trois approches par modèle (20 challenges GPT, 19 Muse Spark). Source canonique codex_events pour GPT, router_provider_ledger pour Muse Spark. Transport et fournisseur ne sont pas additionnés. Cache compris dans l'entrée, raisonnement compris dans la sortie. Les valeurs absentes restent null. Aucun coût d'abonnement n'est estimé.

Durées : distribution cumulée empirique, 20 cas par approche, succès et échecs inclus. À chaque seuil, nombre de cas dont runtime_seconds est inférieur ou égal au seuil / 20. Préparation exclue. Références : réponse, corrections et validation. Agent : investigation incluant outils et attente modèle. Pas d'inférence pure ni de chronologie.

Les versions Codex, plafonds de contexte et stratégies de préparation diffèrent historiquement. Une préparation exceptionnellement longue d'origine indéterminée n'entre pas dans les courbes. Les compteurs incomplets et corrections sont conservés dans l'interprétation. Corpus pédagogique avec symboles, une réponse par case : aucune garantie statistique ou généralisation aux binaires réels.

V2.5 est présentée séparément : outils supplémentaires et effort high, corpus difficile, barème corrigé et diagnostic du transport. La dernière validation n'a aucune conclusion évaluable. Aucun garde n'a déclenché.

Le JSON et les CSV contiennent uniquement des champs publics autorisés et les empreintes des fichiers sources, pas de chemins locaux, prompts, requêtes ou journaux. Le générateur Python livré exige les artefacts privés V2 vérifiés et contrôle leurs empreintes. Ceux-ci ne sont pas publiés sur le portfolio.

Le code agent.py a évolué après le benchmark pour V2.5. Sa différence avec l’empreinte de code historique est signalée dans historical_code_changes. Toutes les empreintes des données historiques restent vérifiées. Cet export ne prétend pas rejouer le benchmark avec le code actuel.
