---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "b0a4740255b8d8b7a6f692e2e0ff4f49", "grade": false, "grade_id": "cell-4911a792a82448d7", "locked": true, "schema_version": 3, "solution": false}}

# Semaine 4

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "786d36df746cf4f02c90284217f2427a", "grade": false, "grade_id": "cell-4911a792a82448d8", "locked": true, "schema_version": 3, "solution": false}}

## Consignes

Avant mardi 23h59:
- [x] Relire les [diapos du cours 4](CM4.md)
- [x] Faire les feuilles 1 à 3 et commencer la feuille 4

+++

## Cours

- [x] [CM4: Construction et sélection d'attributs](CM4.md)

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## TP: VI-ME-RÉ-BAR sur vos propres données

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "6ddfc3399f1add7b265709660b31d77d", "grade": false, "grade_id": "cell-4911a792a82448d9", "locked": true, "schema_version": 3, "solution": false}}

### Objectif

La semaine dernière, vous vous êtes familiarisés avec le schéma
VI-ME-RÉ-BAR -- [VI]sualisation, [ME]sure, [RÉ]férence (*baseline*),
[BAR]res d'erreur -- en reproduisant une analyse de données
préexistante dont l'objet était de classifier automatiquement des
images de pommes et bananes. 

Maintenant, c'est à vous de jouer! Vous allez effectuer en binôme
votre propre analyse de données, sur l'un des jeux de données fournis.
Chacun de ces jeux consiste en vingt images réparties en deux classes:
poules et canards, émoticons tristes et gais, paumes et dos de la
main, ou chiffres manuscrits zéro et un. Saurez-vous apprendre à
l'ordinateur à distinguer automatiquement ces deux classes d'images?
Nous avons veillé à ce que votre défi ne soit ni trop simple, ni trop
compliqué.

Ce travail sera l'objet du premier projet qui va se dérouler sur les
deux semaines qui viennent:

Semaine 4:
- Choix du jeu de données.
- Feuilles 1 à 3 et début de la feuille 4: chargement des données

Semaine 5:
- Fin de la feuille 4 et feuille 5. Cela revient à : 
    - Traitement des images numériques pour en extraire des attributs
	  (*features*) simples.
    - Utilisation d'un premier classificateur donné par vos
      enseignantes et enseignants, afin d'obtenir une performance de
      [RÉ]férence (*baseline*) pour ce jeu de données et aussi d'un
      autre classificateur suite à la feuille 5.
    - Évaluation de la performance.

Déposez au fur et à mesure votre travail dans son état
d'avancement. Votre version définitive (après le dépot de la Semaine 5) sera évaluée par vos
enseignants.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "79233c2ae945f17d047f2af3d135b0e9", "grade": false, "grade_id": "cell-4911a792a82448dA", "locked": true, "schema_version": 3, "solution": false}}

### Consignes

Vous documenterez au fur et à mesure votre analyse de données dans le
document exécutable [analyse de données](4_analyse_de_donnees.md), en
suivant la trame fournie. Gardez notamment une trace des
expérimentations intermédiaires («nous avons essayé telle combinaison
d'attributs; voici les résultats et la performance obtenue»). Ce
document devra rester à tout moment synthétique, suivant notamment les
[bonnes pratiques](../Semaine3/1_bonnes_pratiques.md) vues la semaine
dernière:
- Mettez dans le fichier `utilities.py` les utilitaires du TP3 que
  vous souhaitez réutiliser, ainsi que vos nouvelles fonctions.
- Complétez régulièrement le rapport ci-dessous, notamment pour qu'il
  affiche le code de toutes les fonctions que vous avez
  implantées. Vérifiez à chaque fois le résultat des outils de
  vérifications (`flake8`, ...).
- Lorsque vous avez besoin de brouillon -- par exemple pour mettre au
  point du code -- créez des petites feuilles Jupyter séparées pour ne
  pas polluer votre document.

La qualité de la rédaction sera l'un des critères d'évaluation du
mini-projet.

+++ {"nbgrader": {"grade": false, "grade_id": "cell-4911a792a82448dB", "locked": false, "schema_version": 3, "solution": false}}

### Au travail!

- [x] Vérifiez votre inscription avec votre binôme pour le projet 1
     dans le [document
     partagé](https://codimd.math.cnrs.fr/3f98v4-YT4CN2ktM6_g5lw?both). 
- [x] Révisez les [recommandations pour travailler en
      binôme](https://nicolas.thiery.name/Enseignement/IntroScienceDonnees/ComputerLab/travailBinome.html).
- [x] Consultez la section « Rapport » en fin de feuille.
- [x] Faites un rappel sur la [manipulation des tableaux](1_tableaux.md).
- [x] Apprenez à traiter des [images](2_images.md)  ...
- [x] et à [extraire des attributs](3_extraction_d_attributs.md) de
     votre jeu de données
- [x] Effectuez votre [analyse de donnees](4_analyse_de_donnees.md),
     en suivant les instructions fournies.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "c25fecb4fe3f650f12477a1027446ffb", "grade": false, "grade_id": "cell-4911a792a82448dE", "locked": true, "schema_version": 3, "solution": false}}

### Rédaction

Cette feuille joue aussi le rôle de mini-rapport. Elle vous permettra
à vous et votre enseignant.e d'évaluer rapidement votre avancement sur
ce mini-projet.

Au fur et à mesure du TP, vous cocherez ci-dessus les actions que vous
aurez effectuées; pour cela, double-cliquez sur la cellule pour
l'éditer, et remplacez `- [ ]` par `- [x]`. Vous prendrez aussi des
notes ci-dessous. Enfin, vous consulterez la section « Revue de code »
ci-dessous pour vérifier la qualité de votre code.

+++ {"deletable": false, "nbgrader": {"cell_type": "markdown", "checksum": "6563f058f4e26554f094663c22bb3f3c", "grade": true, "grade_id": "cell-4911a792a82448dF", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}}

Nous avons choisi le jeu de données de smileys gais et tristes. Nous avons fini les feuilles 1,2,3,4 et 5 ainsi que les questions bonus.Nous avons créé pour la feuille 4 une fonction pour voir si la bouche était plus vers le haut ou le bas et ainsi en déduire si c'était un sourire ou non et donc un smileys gais ou non. Cette fonction n'as pas fourni de très bon résultat au niveau des test. Nous avons décidé pour notre 2e implémentation d'utiliser MatchedFilter qui nous à été beaucoup plus utile et à beaucoup mieux réussi les test. Matchedfilter n'est pas parfait mais est beaucoup plus précis et permet d'avoir de bien meilleures résultats aux test qu'avec la fonction position_bouche. Nous avons utilisé le classificateur One rule.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "db64aca779ecc9f6030d7442c300f254", "grade": false, "grade_id": "cell-4911a792a82448dG", "locked": true, "schema_version": 3, "solution": false, "task": false}}

#### Revue du code

##### Affichage du code des principales fonctions

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: b894707ad3d82699fc1be0d5af8226fb
  grade: false
  grade_id: cell-006fb180e6a86e73
  locked: true
  schema_version: 3
  solution: false
  task: false
---
from intro_science_donnees import show_source
from utilities import *
# Feuille 2_images.md
show_source(show_color_channels)
show_source(foreground_filter)
show_source(redness)
```

Si vous définissez d'autres fonctions, affichez en le code ici.

```{code-cell} ipython3
from intro_science_donnees import show_source
from utilities import *
show_source(position_bouche)

import importlib
import utilities
importlib.reload(utilities)

from utilities import MatchedFilter
show_source(MatchedFilter)
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "1615526520bba898c4e974f3bd99a00e", "grade": false, "grade_id": "cell-d21a1d7d40d56302", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": ""}}

## Conventions de codage avec Flake 8

L'outil `flake8` permet de vérifier que votre code respecte les
conventions de codage usuelles de Python, telles que définies
notamment par le document [PEP
8](https://www.python.org/dev/peps/pep-0008/). 

La semaine dernière plusieurs erreurs avaient été laissées dans `utilities.py`
afin que vous les corrigiez. Cette
semaine nous avons introduit d'autres erreurs classiques. Une fois le TP finit affichez les avertissements dans la cellule suivante; suivez les indications données et
modifiez [utilities.py](utilities.py) afin de respecter les
conventions de codage.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: af09a7ad3797f2e5dc5ec66e98ee34e2
  grade: true
  grade_id: cell-ce5cf24a9e83ff0e
  locked: true
  points: 2
  schema_version: 3
  solution: false
  task: false
---
from intro_science_donnees import code_checker
code_checker("flake8 utilities.py")
```

### Barême indicatif /20

* 1_tableaux.md : 1,5 points
* 2_images.md : 2 points
* 3_extraction_d_attributs.md : 1 point
* 4_analyse_de_données.md : 10 points
* 5_classificateur.md : 4 points (+ 3 points bonus pour le OneR)
* index.md : 1,5 points
