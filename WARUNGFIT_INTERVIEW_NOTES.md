# WarungFit — préparation d’entretien

## Présentation en trente secondes

WarungFit est une application Flutter de suivi nutritionnel. Une photo de repas est envoyée à une Edge Function qui vérifie la session, contrôle la requête et appelle un service d’analyse d’image. L’utilisateur corrige ensuite les ingrédients ou les portions avant d’enregistrer le repas dans Supabase.

## Pourquoi Flutter et Supabase ?

Flutter permet de partager l’essentiel du code entre Android et iOS tout en gardant une interface mobile native. Supabase regroupe l’authentification, PostgreSQL, le stockage d’images et les fonctions serveur. Ce choix réduit le nombre de services à assembler pour un projet individuel.

## Comment les comptes sont-ils isolés ?

Le client utilise la session Supabase. Les tables liées à un compte appliquent des règles RLS fondées sur l’identifiant du jeton. Les images suivent aussi un chemin propre à l’utilisateur. Les Edge Functions refont une vérification de session avant les opérations sensibles.

## Pourquoi conserver une correction humaine ?

Une photo ne donne ni le poids exact ni la recette complète. Le modèle propose une estimation structurée, puis l’utilisateur peut modifier le résultat avant de l’enregistrer. L’application ne présente donc pas la sortie du modèle comme une mesure certaine.

## Quelles données sont manipulées ?

Le projet traite un profil, des objectifs nutritionnels, un historique de repas, des corrections et des photos. Les images sont stockées séparément des lignes métier. Un cache local conserve certaines informations utiles au démarrage.

## Comment fonctionne la suppression du compte ?

Le parcours supprime d’abord les images, puis les données métier et enfin le compte Auth. Cette séquence limite le risque de laisser des fichiers sans propriétaire. Le scénario complet doit encore être rejoué sur un environnement Supabase dédié avec des comptes synthétiques.

## Quelles sont les limites actuelles ?

Les estimations nutritionnelles restent approximatives. Le cache local n’est pas chiffré. Les tests structurels existent, mais l’isolation entre deux comptes et la suppression complète doivent encore être confirmées dans un environnement distant de test.

## Que changer sur une version de production ?

Je mettrais en place une validation automatisée du backend dans un environnement éphémère, une rotation documentée des identifiants publics, un suivi des erreurs sans données personnelles, une politique de conservation explicite et des tests de suppression réguliers. J’ajouterais aussi une mesure de qualité du modèle sur un jeu d’images représentatif.
