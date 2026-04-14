# Mini-projet : Classification d'images de smileys

Ce projet consiste à entraîner un classificateur automatique capable de
distinguer des images de smileys joyeux et des images de smileys
tristes, en suivant la méthodologie VI-ME-RÉ-BAR :
**[VI]sualisation**, **[ME]sure**, **[RÉ]férence** (*baseline*) et
**[BAR]res d'erreur**.

## Contexte et objectif

Le jeu de données est composé de vingt images de smileys réparties en
deux classes : les smileys gais et les smileys tristes. La principale
différence visuelle entre les deux classes réside dans la forme de la
bouche, qui est courbée vers le haut pour les smileys joyeux et vers
le bas pour les smileys tristes. L'enjeu du projet est de formaliser
cette intuition en des attributs numériques (*features*) exploitables
par un algorithme de classification.

## Structure du projet

Le projet est organisé autour de plusieurs feuilles de travail au
format MyST Markdown, exécutables sous Jupyter :

- `index.md` est la feuille principale qui résume l'avancement du
  projet et sert de mini-rapport.
- `1_tableaux.md` contient un rappel sur la manipulation de tableaux
  avec NumPy et Pandas.
- `2_images.md` présente les techniques de base pour charger et
  afficher des images.
- `3_extraction_d_attributs.md` détaille les méthodes d'extraction
  d'attributs à partir des images (élongation, couleur, filtre
  adapté).
- `4_analyse_de_donnees.md` est le rapport d'analyse de données, qui
  suit la trame VI-ME-RÉ-BAR et conserve la trace des expérimentations
  successives.
- `5_classificateurs.md` présente plusieurs classificateurs
  (1-Nearest Neighbor, Parzen Window, arbre de décision, One Rule,
  Perceptron) et compare leurs performances sur le jeu de données de
  pommes et bananes fourni en référence.
- `utilities.py` regroupe toutes les fonctions utilitaires réutilisables,
  à la fois celles issues du TP3 et les nouvelles fonctions développées
  pour ce projet.

## Attributs implémentés

Deux approches principales ont été développées et comparées pour
caractériser les smileys.

La première, `position_bouche`, analyse la moitié inférieure de
l'image après filtrage du premier plan, et calcule la position
verticale moyenne des pixels détectés. L'idée est que la bouche d'un
smiley joyeux sera plus haute dans cette zone, et celle d'un smiley
triste plus basse. Cette approche s'est révélée peu performante lors
des tests.

La seconde approche repose sur un **filtre adapté** (*Matched Filter*),
implémenté dans la classe `MatchedFilter`. Ce filtre construit un
gabarit (*template*) en calculant la moyenne des images normalisées
d'une classe d'entraînement, puis mesure la corrélation entre ce
gabarit et une nouvelle image. Cette méthode a produit des résultats
nettement supérieurs et a été retenue pour le classificateur final.

Les fonctions utilitaires existantes comprennent également `redness`
(mesure de la teinte rouge), `elongation` (rapport d'élongation calculé
par décomposition en valeurs singulières), ainsi que plusieurs
fonctions de visualisation (`show_color_channels`, `color_histogram`,
`elongation_plot`).

## Classificateur retenu

Le classificateur choisi est **One Rule** (`OneRule`), implémenté dans
`utilities.py`. Il sélectionne automatiquement l'attribut le plus
corrélé à la classe cible, détermine un seuil de décision optimal
entre les deux classes, et produit une prédiction binaire. Combiné à
l'attribut issu du `MatchedFilter`, il offre de bonnes performances
sur ce jeu de données.

## Résultats et performance

Les performances ont été évaluées avec un découpage stratifié 50/50
entre données d'entraînement et données de test (via `split_data`).
Le taux d'erreur (`error_rate`) a été utilisé comme métrique principale.
La combinaison `MatchedFilter` + `OneRule` s'est avérée bien plus
fiable que l'approche initiale `position_bouche`, et généralise
correctement sur les données de test.

À titre de comparaison, l'étude des classificateurs sur le jeu de
référence (pommes et bananes) a montré que le Perceptron obtenait les
meilleurs résultats avec un taux d'erreur de 0.0 en entraînement et
0.1 en test, tandis que la fenêtre de Parzen plafonnait à 0.5 sur les
deux ensembles, ce qui correspond à une classification aléatoire.

## Prérequis et installation

Ce projet utilise Python 3 ainsi que les bibliothèques suivantes :
`numpy`, `pandas`, `Pillow`, `scikit-learn`, `matplotlib` et `seaborn`.
Le package `intro_science_donnees` fourni par l'enseignement est
également nécessaire.

La qualité du code est vérifiée avec `flake8` (longueur maximale de
ligne fixée à 88 caractères) et les types sont contrôlés avec `mypy`.
Les tests automatiques sont exécutés via `pytest` avec support des
doctests. La configuration de ces outils se trouve dans `setup.cfg`.

Pour lancer les feuilles, il suffit d'ouvrir Jupyter et d'exécuter les
cellules dans l'ordre. Il est recommandé de commencer par `index.md`
pour avoir une vue d'ensemble du projet.

## Auteurs

Projet réalisé en binôme dans le cadre de l'UE Introduction à la
Science des Données(Lazim Sar et Adam El Asrag).
