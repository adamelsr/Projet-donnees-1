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

+++ {"nbgrader": {"checksum": "ba540a64a5c4b5b4f5bf9318ad3609d7", "grade": false, "locked": true, "grade_id": "cell-19c6eb4994e2384a", "schema_version": 3, "solution": false, "cell_type": "markdown"}, "deletable": false, "editable": false}

# Manipuler des images

+++ {"editable": false, "deletable": false, "nbgrader": {"schema_version": 3, "grade": false, "solution": false, "checksum": "367b2aaa29a7a087acf944d330ea8b11", "locked": true, "task": false, "cell_type": "markdown", "grade_id": "cell-19c6eb4994e2384b"}}

Dans cette feuille, vous allez apprendre à effectuer quelques
manipulations et traitements simples sur les images.  Nous allons
commencer par nous entraîner sur une image riche en couleurs (source:
[wikimedia](https://commons.wikimedia.org/wiki/File:Apple_icon_2.png)):

:::{figure} media/apple.png
:alt: media/apple.png
:width: 40px
:align: center
:::

Pour cela, nous la chargeons avec la bibliothèque `PIL` (Python
Imaging Library) en précisant le nom du fichier la contenant, puis
l'affectons à une variable `img` pour pouvoir la manipuler par la
suite:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  solution: false
  checksum: fc4316407949214dd25659ce94a2c8ff
  cell_type: code
  schema_version: 3
  grade: false
  grade_id: cell-38a01921463de697
  locked: true
---
from PIL import Image
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  grade: false
  grade_id: cell-b5659c2e482c3848
  schema_version: 3
  locked: true
  solution: false
  checksum: 7cd24c6d30411319b4b3ad9ee00354fc
---
img = Image.open("media/apple.png")
```

+++ {"nbgrader": {"grade": false, "schema_version": 3, "cell_type": "markdown", "grade_id": "cell-e75aecf3bd8946db", "solution": false, "locked": true, "checksum": "2d659b6c78fbcb6dc4b70deb2c31d7bc"}, "editable": false, "deletable": false}

Voici cette image:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  solution: false
  grade_id: cell-5f412c59d2396365
  schema_version: 3
  locked: true
  checksum: b50b98470eb5f237c85aeee0a899fd14
  grade: false
  cell_type: code
---
img
```

+++ {"editable": false, "nbgrader": {"schema_version": 3, "grade_id": "cell-450a9499627740e6", "cell_type": "markdown", "checksum": "e40db6e9befd8bd904ea5c08897869cf", "solution": false, "locked": true, "grade": false}, "deletable": false}

Pour l'afficher avec des axes et -- lorsque l'image a une basse
résolution -- mieux repérer les pixels individuels, on peut utiliser
`matplotlib`:

```{code-cell} ipython3
---
editable: false
nbgrader:
  grade: false
  cell_type: code
  schema_version: 3
  grade_id: cell-1b1461380b6fef35
  solution: false
  locked: true
  checksum: 10493e3d9ca1f599aa7c62052f5abf3b
deletable: false
---
import matplotlib.pyplot as plt
```

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  grade: false
  grade_id: cell-1b1461380b6fef36
  checksum: 1c892a66a9b93dd8f844691500a9461d
  locked: true
  schema_version: 3
  solution: false
editable: false
---
plt.imshow(img);
```

+++ {"editable": false, "deletable": false, "nbgrader": {"task": false, "cell_type": "markdown", "grade": false, "locked": true, "grade_id": "cell-b74d7516557d88dd", "checksum": "254806d17d1bb93bf6d739397403bee8", "schema_version": 3, "solution": false}}

:::{hint} Interfaces traditionnelle et objet de matplotlib

Pourquoi un `;` à la fin de la commande précédente?  Parce que
`plt.imshow` ne renvoie pas une image, mais l'affiche par effet de
bord. Le `;` évite l'affichage de ce que renvoie vraiment `plt.imshow`
(un objet de type figure).

Cette approche quelque peu datée est traditionnelle dans des systèmes
comme `Matlab`. La bibliothèque `matplotlib.pyplot` l'a reproduit pour
faciliter la migration d'utilisateurs de ces systèmes. Par habitude
beaucoup d'exemples sur internet utilisent encore cette approche; cela
peut rester pratique comme raccourci dans des exemples en une ligne
comme ci-dessus.

Mais on sait depuis -- et c'est ce que nous vous enseignons depuis le
début de l'année -- que l'on obtient du code beaucoup plus modulaire
si l'on sépare proprement les traitements et calculs (par exemple
construire une figure) des entrées et sorties (par exemple afficher la
figure).

De ce fait, pour tout usage non trivial, il est préférable d'utiliser
l'interface objet de `matplotlib`, comme dans l'exemple suivant:
    
:::

```{code-cell} ipython3
---
editable: false
deletable: false
nbgrader:
  schema_version: 3
  checksum: 4296a87605d5600bd42c2ec885c8b47b
  grade_id: cell-811d54735c3ff4e5
  locked: true
  grade: false
  task: false
  solution: false
  cell_type: code
---
from matplotlib.figure import Figure
```

```{code-cell} ipython3
---
nbgrader:
  schema_version: 3
  cell_type: code
  solution: false
  locked: true
  task: false
  grade_id: cell-0c1a66846231a7bb
  checksum: b4f1aba47e03a2738c7446c1894a2ddf
  grade: false
deletable: false
editable: false
---
fig = Figure()              # Construction d'une nouvelle figure
subplot = fig.add_subplot() # Ajout d'une zone de dessin (appelée «axes» dans matplotlib) à la figure
subplot.imshow(img)         # Ajout d'une image à la zone de dessin
fig                         # Affichage de la figure
```

+++ {"deletable": false, "nbgrader": {"grade_id": "cell-67d310808fac6650", "grade": false, "cell_type": "markdown", "checksum": "a1395327180c929e710c10338ec18529", "locked": true, "schema_version": 3, "solution": false}, "editable": false}

Consultez la documentation de **PIL Image** sur internet, pour trouver
comment obtenir la largeur et la hauteur de cette image. Stockez le
résultat dans des variables `width` et `height` et vérifiez la
cohérence avec la figure ci-dessus.

```{code-cell} ipython3
---
nbgrader:
  task: false
  schema_version: 3
  solution: true
  grade: false
  cell_type: code
  grade_id: cell-46598b84e0c79fc6
  locked: false
  checksum: 0591dd4e4263702807ca56712faf4fea
deletable: false
---
img.size
width=256
height=256
```

```{code-cell} ipython3
---
nbgrader:
  grade: true
  solution: false
  cell_type: code
  locked: true
  schema_version: 3
  points: 1
  grade_id: cell-c6bfc2a73d6866ce
  task: false
  checksum: 727a5f8f2c889479e7681bff4e7b22f4
editable: false
deletable: false
---
assert width == 256
assert height == 256
```

+++ {"editable": false, "deletable": false, "nbgrader": {"checksum": "5aa69c14fc4e4590042c8e5692162775", "grade_id": "cell-5aa2ff2d91d5b0b3", "solution": false, "locked": true, "cell_type": "markdown", "grade": false, "schema_version": 3}}

## Images comme tableaux

On souhaite maintenant pouvoir accéder au contenu de l'image pour
pouvoir calculer avec. Pour cela, nous allons convertir l'image en un
tableau de nombres `NumPy`, tels ceux que nous avons manipulés dans la
[fiche précédente](1_tableaux.md).

Voici le tableau associé à l'image:

```{code-cell} ipython3
---
editable: false
deletable: false
nbgrader:
  locked: true
  cell_type: code
  solution: false
  schema_version: 3
  checksum: bbb2d1e391bf0019b32da5b93f05a5b1
  task: false
  grade: false
  grade_id: cell-8f62152c1e513665
---
import numpy as np
```

```{code-cell} ipython3
---
nbgrader:
  cell_type: code
  grade: false
  grade_id: cell-f1cf391e96f32f52
  locked: true
  solution: false
  checksum: 14c2ac7ae3388ba529818944cb00339a
  schema_version: 3
deletable: false
editable: false
---
M = np.array(img)
```

+++ {"deletable": false, "nbgrader": {"checksum": "fb79bd105e1614d14f1c213fe77ee593", "grade": true, "locked": false, "schema_version": 3, "points": 0, "task": false, "grade_id": "cell-1a34fbbc93618b40", "cell_type": "markdown", "solution": true}}

En vous référant éventuellement au cours, combien de lignes, de
colonnes et de couches devrait avoir ce tableau?

Ce tableau devrait avoir 256 lignes, 256 colonnes et 4 couches car l'image est de format RGBA ( Red, Green, Blue and alpha / transparence)

Vérifier avec l'attribut `shape`:

```{code-cell} ipython3
---
nbgrader:
  solution: true
  schema_version: 3
  checksum: fbad0bebc7fe362ecae7f9d867a41349
  cell_type: code
  grade_id: cell-f3258fc6004a71d6
  grade: false
  locked: false
deletable: false
---
M.shape
```

+++ {"nbgrader": {"checksum": "28ce720e19aa96998b118b7f225a0a8d", "locked": true, "grade_id": "cell-397f146412f6fb75", "cell_type": "markdown", "grade": false, "schema_version": 3, "solution": false}, "editable": false, "deletable": false}

Pourquoi quatre couches? Rouge, Vert, Bleu, ... et transparence!

+++ {"deletable": false, "editable": false, "nbgrader": {"schema_version": 3, "solution": false, "cell_type": "markdown", "checksum": "9ee110b88a5ebad3e627effe4d6182fc", "grade": false, "grade_id": "cell-397f146412f6fb76", "locked": true}}

### Comprendre les couches de couleurs

Comme toujours, pour mieux comprendre des données, il faut les
visualiser !  Voici une figure représentant notre image et ses trois
couches rouge, vert, bleu.  Observez comment les couleurs de l'image
de départ (blanc, vert, noir, rouge) se décomposent dans les
différentes couches.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  grade: false
  locked: true
  task: false
  solution: false
  schema_version: 3
  checksum: bcf0dc465bbe1270b29f119b907ad266
  grade_id: cell-49b556a7e4717b09
---
# Échelles de couleur (colormap) allant du noir à la couleur primaire correspondante
from matplotlib.colors import LinearSegmentedColormap
black_red_cmap   = LinearSegmentedColormap.from_list('black_red_cmap',   ["black", "red"])
black_green_cmap = LinearSegmentedColormap.from_list('black_green_cmap', ["black", "green"])
black_blue_cmap  = LinearSegmentedColormap.from_list('black_blue_cmap',  ["black", "blue"])

fig = Figure(figsize=(30, 5));
(subplot, subplotr, subplotg, subplotb) = fig.subplots(1, 4)  # Quatre zones de dessin
# Dessin de l'image et de ses trois couches
subplot.imshow(M)
imgr = subplotr.imshow(M[:,:,0], cmap=black_red_cmap,   vmin=0, vmax=255)
imgg = subplotg.imshow(M[:,:,1], cmap=black_green_cmap, vmin=0, vmax=255)
imgb = subplotb.imshow(M[:,:,2], cmap=black_blue_cmap,  vmin=0, vmax=255)
# Ajout des barres d'échelle de couleur aux images
fig.colorbar(imgr, ax=subplotr);
fig.colorbar(imgg, ax=subplotg);
fig.colorbar(imgb, ax=subplotb);
fig
```

+++ {"deletable": false, "nbgrader": {"grade_id": "cell-953569768ed43403", "locked": true, "task": false, "grade": false, "checksum": "b11a9ebb0dfb591f0e9eb7b1cda60cc1", "schema_version": 3, "cell_type": "markdown", "solution": false}, "editable": false}

Par la suite, nous visualiserons de même de nombreuses images.  Il est
donc temps d'automatiser la construction de la figure ci-dessus.

:::{admonition} Exercice

Ouvrez le fichier [utilities.py](utilities.py) et complétez-y la
fonction `show_color_channels` à partir du code ci-dessus.

:::

```{code-cell} ipython3
---
nbgrader:
  grade: false
  cell_type: code
  solution: false
  grade_id: cell-40f2b1ca26aac943
  checksum: 0e0c41454956ed3735d0ea836320cb54
  schema_version: 3
  task: false
  locked: true
editable: false
deletable: false
---
# Automatically reload code when changes are made
%load_ext autoreload
%autoreload 2
from intro_science_donnees import *
from utilities import *
```

```{code-cell} ipython3
---
editable: false
nbgrader:
  schema_version: 3
  locked: true
  grade_id: cell-f01f30acda19b78b
  cell_type: code
  solution: false
  task: false
  checksum: 9f2425888eb560cc5960d99333f9763e
  grade: false
deletable: false
---
show_source(show_color_channels)
```

```{code-cell} ipython3
---
nbgrader:
  grade_id: cell-66040947f316edfb
  points: 1
  schema_version: 3
  solution: false
  task: false
  grade: true
  cell_type: code
  checksum: 9ad91a641c3bf70ea432483f5d39ff4b
  locked: true
deletable: false
editable: false
---
show_color_channels(img)
```

+++ {"nbgrader": {"task": false, "locked": true, "grade_id": "cell-fda75a63d59e2209", "grade": false, "solution": false, "checksum": "b3ae860daf9ea17e4e03590118be55dc", "cell_type": "markdown", "schema_version": 3}, "editable": false, "deletable": false}

Vérification: `show_color_channels` renvoie bien une figure

```{code-cell} ipython3
---
nbgrader:
  schema_version: 3
  checksum: cb8ea7ebed14f226e1daef4773e4ea17
  locked: true
  task: false
  grade: true
  grade_id: cell-80328561c59cf158
  points: 1
  cell_type: code
  solution: false
deletable: false
editable: false
---
assert isinstance(show_color_channels(img), Figure)
```

+++ {"editable": false, "nbgrader": {"grade_id": "cell-0cf719f423e37ef5", "checksum": "f7bd8a7b56a3821945eb64ca61b1cebd", "task": false, "grade": false, "cell_type": "markdown", "solution": false, "schema_version": 3, "locked": true}, "deletable": false}

Étudions maintenant les images du jeu de données de la semaine
dernière:

```{code-cell} ipython3
---
nbgrader:
  grade_id: cell-1c62320d37fe2e8f
  checksum: 2459c104673389925f906a48ed6fe013
  locked: true
  grade: false
  task: false
  solution: false
  cell_type: code
  schema_version: 3
deletable: false
editable: false
---
import os.path
dataset_dir = os.path.join(data.dir, 'ApplesAndBananasSimple')
images = load_images(dataset_dir, "*.png")
```

```{code-cell} ipython3
---
editable: false
deletable: false
nbgrader:
  checksum: b1f6c574776c5e7928f57c3f9b898b58
  solution: false
  grade: false
  grade_id: cell-a7f1576c7b9d8917
  locked: true
  cell_type: code
  schema_version: 3
  task: false
---
image_grid(images, titles=images.index)
```

+++ {"nbgrader": {"grade_id": "cell-9f449b989ea74be6", "schema_version": 3, "task": false, "cell_type": "markdown", "locked": false, "solution": true, "checksum": "641aa9d1643283fdc0edfe561349d3b0", "points": 0, "grade": true}, "deletable": false}

:::{admonition} Exercice

Observez l'image suivante et ses couches. Expliquez ce que vous
voyez. Essayez d'autres exemples.

Ici, nous pouvons voir 4 images de bananes. Dans chaque image, il y a des axes avec une abscisse et une ordonnée. Dans la 1 ère image, nous voyons une banane jaune de couleur normale avec derrière un fond blanc.
Puis, pour les images restantes, il y a 3 bananes mais avec un fond respectivement: rouge, vert et bleu avec une echelle d'intensité selon la couleur de l'arrière plan. Et, on constate bien que pour le rouge et le vert, le jaune de la banane est devenu soit rouge ou vert tandis que pour le bleu, le jaune de la banane est devenu noir.
:::

```{code-cell} ipython3
img = images[10]
show_color_channels(img)
img = images[0]
show_color_channels(img)
```

+++ {"deletable": false, "editable": false, "nbgrader": {"schema_version": 3, "cell_type": "markdown", "grade_id": "cell-291f681a5aab593d", "checksum": "12b7f4e53942fba1052f2d8c5ace6a4c", "locked": true, "solution": false, "grade": false, "task": false}}

Nous allons maintenant observer l'**histogramme des couleurs**
apparaissant dans une image, en utilisant l'utilitaire
`color_histogram` (vous pouvez comme d'habitude en consulter la
documentation et le code par introspection avec `color_histogram?` et
`color_histogram??`):

```{code-cell} ipython3
---
nbgrader:
  cell_type: code
  solution: false
  grade: false
  task: false
  locked: true
  checksum: 150948f151ad9f3824cbb0a43b071a9e
  grade_id: cell-ed77018895a029a9
  schema_version: 3
deletable: false
editable: false
---
color_histogram(img)
```

+++ {"deletable": false, "nbgrader": {"grade": true, "solution": true, "grade_id": "cell-a887ca1b2eac11df", "points": 2, "schema_version": 3, "checksum": "8a1d0feb47db8a2737140feed95b45a5", "task": false, "cell_type": "markdown", "locked": false}}

:::{admonition} Exercice

Observez les histogrammes ci-dessous de la dixième et la troisième
image, et interprétez-les.

Pour l'histogramme de la dixième image : 
Nous pouvons voir l'amplitude de chaque couleur selon leur densité. Ici, on remarque donc que pour la couleur rouge, l'amplitude est fortement élevée avec pour 250 d'amplitudes, une densité max de 0.017-0.018. Et plus on descend en amplitude, moins il y a de rouge.
Concernant la couleur verte, c'est un peu le même cas que le rouge avec pour son amplitude max, une densité d'environ 0.016. Et pareil quand on descend en amplitude, la couleur verte disparait peu à peu.
Alors que pour la couleur bleue, c'est l"inverse. Autrement dit, pour son amplitude max à 250, elle a environ 0.014 de densité. Toutefois quand on descend jusqu'à son amplitude minimale de 25, elle a 0.013 de densité.
Grâce à ces observations, on comprend que dans l'image originale de la pomme jaune-verte, son echelle de couleur comporte beaucoup de rouge puis de vert et enfin un peu de bleu.La raison est que la couleur jaune se forme de rouge et de vert ( Sous forme RGB, c'est : 255 255 0) d'ou la raison de leurs fortes amplitudes et de densités. Et comme, l'image ne comporte pas de bleu, alors sa densité pour une faible amplitude est élevée contrairement aux autres. Ce qui explique quand même sa présence pour une amplitude à 250 est sûrement le fond blanc car le blanc comporte du rouge, du vert eu bleu (d'après RGB: 255 255 255)).

Pour l'histogramme de la troisième image :

Encore une fois, nous pouvons regarder l'amplitude de chaque couleur selon leur densité. Ici, on remarque donc que pour la couleur rouge de l'image avec la pomme et le fond blanc, l'amplitude est fortement élevée avec pour 250 d'amplitudes, une densité max de 0.018. Et plus on descend en amplitude, plus le rouge disparaît.
Concernant la couleur verte, c'est un peu le même cas que le rouge avec pour son amplitude max, une densité d'environ 0.014. Et pareil quand on descend en amplitude, la couleur verte disparait peu à peu.
Alors que pour la couleur bleue, ca ressemble un peu à celle de l'image précédente. Autrement dit, pour son amplitude max à 250, elle a environ 0.012 de densité. Toutefois quand on descend jusqu'à son amplitude minimale de 25, elle a 0.013 de densité.
Grâce à ces observations, on comprend que dans l'image originale de la pomme jaune-verte, son echelle de couleur comporte beaucoup de rouge puis moins de vert et enfin un peu de bleu.
La raison est que la pomme est rouge et un peu de jaune et le fond est blanc ce qui explique ces amplitudes de couleurs.


:::

```{code-cell} ipython3
---
editable: false
deletable: false
nbgrader:
  schema_version: 3
  locked: true
  task: false
  checksum: fe1db908c96b5fabf540deecbd4de345
  cell_type: code
  solution: false
  grade: false
  grade_id: cell-3828ddf071670eff
---
img = images[9]
show_color_channels(img)
```

```{code-cell} ipython3
---
editable: false
deletable: false
nbgrader:
  cell_type: code
  locked: true
  grade_id: cell-3d6d2c2781569087
  solution: false
  schema_version: 3
  checksum: bb06a95dbdef21b812d75e4c3598e7d7
  grade: false
  task: false
---
color_histogram(img)
```

```{code-cell} ipython3
---
nbgrader:
  solution: false
  locked: true
  cell_type: code
  grade_id: cell-4f5ef22b7b70c0c8
  schema_version: 3
  checksum: 9eee30bb80b5461f77c8bab61aec3fa8
  grade: false
  task: false
deletable: false
editable: false
---
img = images[2]
show_color_channels(img)
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  solution: false
  checksum: 86bdf73b6de46bb6e03d27e2049141b2
  grade_id: cell-7ef43bfaf750914f
  grade: false
  schema_version: 3
  task: false
  locked: true
---
color_histogram(img)
```

+++ {"deletable": false, "editable": false, "nbgrader": {"schema_version": 3, "grade": false, "grade_id": "cell-5d6255f7be07beda", "solution": false, "cell_type": "markdown", "locked": true, "checksum": "6d2ac3d0585daa5448d3557fb35bfd64"}}

## Séparation des couleurs

Nous allons maintenant extraire les trois canaux, rouge, vert,
bleu. Pour le canal des rouges, on extrait le sous-tableau à deux
dimensions de toutes les cases d'indice $(i,j,k)$ avec $k=0$. Le 
`* 1.0` sert à convertir les valeurs en nombres à virgule.

```{code-cell} ipython3
---
nbgrader:
  locked: true
  schema_version: 3
  solution: false
  cell_type: code
  grade: false
  checksum: ebd7f3ac0452d4af2805ee65c072992a
  grade_id: cell-dfe51efcf6df748b
deletable: false
editable: false
---
R = M[:,:,0] * 1.0
```

+++ {"editable": false, "nbgrader": {"cell_type": "markdown", "grade": false, "locked": true, "grade_id": "cell-59920f8c83495b86", "schema_version": 3, "checksum": "1956de28640b45b1d33bca95a1ef2388", "solution": false}, "deletable": false}

Regarder le résultat directement n'est pas très informatif :

```{code-cell} ipython3
---
deletable: false
nbgrader:
  solution: false
  checksum: 818ecd7d2413dbfd33d86b9a881f88b8
  grade: false
  grade_id: cell-79a4159977138616
  cell_type: code
  locked: true
  schema_version: 3
editable: false
---
R
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "grade": false, "grade_id": "cell-58b15c024481ac3d", "checksum": "f78969aede85e0e0845474e62b274a2e", "schema_version": 3, "solution": false, "locked": true}}

Comme d'habitude, il vaut mieux le *visualiser* :

```{code-cell} ipython3
---
editable: false
deletable: false
nbgrader:
  locked: true
  checksum: d3f8a542750fb667a0006e2731499d76
  grade: false
  schema_version: 3
  solution: false
  cell_type: code
  grade_id: cell-403d27ca87e158c3
---
fig = Figure(figsize=(5,5))
ax, axr = fig.subplots(1,2)
ax.imshow(M)
axr.imshow(R, cmap='Greys_r', vmin=0, vmax=255)
fig
```

+++ {"editable": false, "nbgrader": {"locked": true, "solution": false, "grade_id": "cell-f5748504b4d52000", "cell_type": "markdown", "checksum": "0ba3504692210914a0772b0a5b258bcc", "task": false, "grade": false, "schema_version": 3}, "deletable": false}

:::{admonition} Exercice

Extrayez de même le canal des verts et des bleus de la première image
dans les variables `G` et `B`. N'hésitez pas à les visualiser !

:::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  solution: true
  cell_type: code
  task: false
  grade_id: cell-2793bd4b1f83558d
  schema_version: 3
  grade: false
  checksum: 84ef9c8b6022f20aaaf3339aa5a393dc
  locked: false
---
G=M[:,:,1] * 1.0
G
```

```{code-cell} ipython3
---
nbgrader:
  task: false
  cell_type: code
  schema_version: 3
  solution: false
  checksum: 554525ffc81338eba8930f0cf73ca91e
  grade_id: cell-841034979ffe6094
  grade: true
  points: 1
  locked: true
deletable: false
editable: false
---
assert G.shape == (256, 256)
assert abs(G.mean() - 158.27) < 0.1
```

```{code-cell} ipython3
---
nbgrader:
  locked: false
  schema_version: 3
  grade_id: cell-8baf6161cb011920
  solution: true
  grade: false
  checksum: 00dac5227fae9117048c559d1793e90d
  cell_type: code
  task: false
deletable: false
---
B=M[:,:,2] * 1.0
B
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  solution: false
  schema_version: 3
  grade_id: cell-841034979ffe6095
  checksum: 0026e93a099e056f8b2f5bb578ebf29b
  grade: true
  points: 1
  cell_type: code
  locked: true
  task: false
---
assert B.shape == (256, 256)
assert abs(B.mean() - 148.39) < 0.1
```

+++ {"deletable": false, "editable": false, "nbgrader": {"locked": true, "grade_id": "cell-233c14413c6e3e6f", "grade": false, "schema_version": 3, "cell_type": "markdown", "checksum": "a795bb7e0891ac3388498b32016ec6f1", "solution": false}}

Il est maintenant facile de faire de l'arithmétique sur tous les
pixels. Par exemple la somme des intensités en vert et rouge s'écrit:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  solution: false
  grade: false
  checksum: 8c5959d639d7951b07c72c42d2327905
  grade_id: cell-0bd25c9e1e6c6abf
  locked: true
  schema_version: 3
  cell_type: code
---
G + R
```

+++ {"deletable": false, "editable": false, "nbgrader": {"grade": false, "solution": false, "cell_type": "markdown", "schema_version": 3, "checksum": "c4b27d04842cd440b2dc42486b8dc3f8", "grade_id": "cell-5d168111627796e1", "locked": true}}

:::{admonition} Exercice

Calculez et visualisez la luminosité de tous les pixels de l'image, la
*luminosité* d'un pixel $(r,g,b)$ étant définie comme la moyenne
$v=\frac{r+g+b}{3}$:

:::

```{code-cell} ipython3
---
nbgrader:
  cell_type: code
  checksum: 93109febd0552684cd6e4de30f5ab725
  locked: false
  schema_version: 3
  solution: true
  task: false
  grade: false
  grade_id: cell-4956fa101f9c567c
deletable: false
---
V=(R+G+B)/3
```

```{code-cell} ipython3
---
editable: false
nbgrader:
  checksum: 7c5e41e9533f15b0c0cca359420e2595
  grade: true
  grade_id: cell-841034979ffe6096
  solution: false
  task: false
  locked: true
  points: 1
  schema_version: 3
  cell_type: code
deletable: false
---
assert V.shape == (256, 256)
assert abs(V.mean() - 172.44) < 0.1
```

+++ {"editable": false, "nbgrader": {"solution": false, "grade_id": "cell-5d168111627796e2", "schema_version": 3, "locked": true, "cell_type": "markdown", "grade": false, "checksum": "f52b82486f95773b2b9c2e42805e921c"}, "deletable": false}

Vous venez de transformer l'image en niveaux de gris! Pour que cela
colle au mieux avec notre perception visuelle, il faudrait en fait
utiliser une moyenne légèrement pondérée; voir par exemple la
[Wikipedia](https://fr.wikipedia.org/wiki/Niveau_de_gris#Convertir_une_image_couleur_en_niveau_de_gris).

+++ {"nbgrader": {"locked": true, "schema_version": 3, "grade": false, "checksum": "7f4af73eb1742c465180687ba662f362", "solution": false, "cell_type": "markdown", "grade_id": "cell-d0fb04b5c7bf1744"}, "deletable": false, "editable": false}

## Conclusion

Vous avons vu dans cette feuille comment charger une image dans Python
et effectuer quelques manipulations, visualisations et calculs simples
dessus. Cela a été l'occasion de mieux comprendre la décomposition
d'une image en couches de couleur.

:::{admonition} Exercice

Mettez à jour votre rapport, et notamment la section « revue de code »
pour vérifier vos utilitaires dans [utilities.py](utilities.py).

:::

Vous pouvez maintenant passer à
l'[extraction d'attributs](3_extraction_d_attributs.md)

```{code-cell} ipython3

```
