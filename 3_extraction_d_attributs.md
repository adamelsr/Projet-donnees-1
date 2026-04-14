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

+++ {"nbgrader": {"solution": false, "grade": false, "locked": true, "cell_type": "markdown", "schema_version": 3, "checksum": "c3193d3781fa34b362a149608a4ee622", "grade_id": "cell-6a16688d41d1d6e3"}, "slideshow": {"slide_type": ""}, "editable": false, "tags": [], "deletable": false}

# Extraction d'attributs: rougeur et élongation

Dans cette feuille, vous allez implémenter l'extraction de la rougeur
et de l'élongation, les deux attributs que nous avons utilisés la
semaine dernière sur le jeu de données pommes/bananes.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  grade_id: cell-c36993e7677e3c21
  locked: true
  schema_version: 3
  cell_type: code
  solution: false
  grade: false
  checksum: e1ac2871ff99a4b3bb13626ee854a708
---
import matplotlib.pyplot as plt
%matplotlib inline

%load_ext autoreload
%autoreload 2
    
from intro_science_donnees import *  #les librairies classiques pour ISD (numpy, PIL...) y sont incluses
from utilities import *


dataset_dir = os.path.join(data.dir, 'ApplesAndBananasSimple')
images = load_images(dataset_dir, "*.png")
```

+++ {"editable": false, "nbgrader": {"grade_id": "cell-723aac78a7b9fad5", "grade": false, "task": false, "solution": false, "locked": true, "checksum": "c21e55883ba7a3172ed4139e460b882e", "cell_type": "markdown", "schema_version": 3}, "deletable": false}

## Extraction du premier plan de l'image

Pour calculer les caractéristiques de nos images, nous devons d'abord
extraire le premier plan de l'image en séparant l'objet de son
arrière-plan. Pour la plupart des images de cet ensemble de données
simple, l'objet se trouve sur un fond clair. Une stratégie simple
consiste donc à choisir un seuil `theta` (*threshold* en anglais) et
décider que tout pixel dont la valeur rouge, verte ou bleue est en
dessous du seuil appartient au premier plan.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "schema_version": 3, "solution": false, "task": false, "checksum": "800b0789d0e9b4b68c5d386acc9574e9", "grade_id": "cell-723aac78a7b9fad6", "locked": true, "grade": false}}

Prenons une pomme :

```{code-cell} ipython3
---
nbgrader:
  cell_type: code
  grade_id: cell-483009445c0d3402
  solution: false
  grade: false
  checksum: 3d776bc3ecdb131e49edc9bd15fe3145
  locked: true
  schema_version: 3
  task: false
editable: false
deletable: false
---
img = images['a10.png']
img
```

+++ {"editable": false, "nbgrader": {"locked": true, "grade_id": "cell-bed9462b9c313709", "checksum": "db3094d25bd61f00120fb7f6ae80e20e", "task": false, "schema_version": 3, "cell_type": "markdown", "solution": false, "grade": false}, "deletable": false}

On calcule, pour chaque pixel, le minimum de la valeur rouge, verte et
bleue :

```{code-cell} ipython3
---
editable: false
deletable: false
nbgrader:
  cell_type: code
  solution: false
  checksum: fc1960fca0a0ff6350f74025281b9e71
  locked: true
  schema_version: 3
  grade_id: cell-c38b3a66ab27cba9
  grade: false
  task: false
---
M = np.array(img)
G = np.min(M[:,:,0:3], axis=2)
```

Visualisons le résultat :

```{code-cell} ipython3
---
editable: false
deletable: false
nbgrader:
  checksum: 518240276b243c36c51438e092d7e1cb
  solution: false
  cell_type: code
  grade: false
  schema_version: 3
  grade_id: cell-c38b3a66ab27cbaa
  locked: true
  task: false
---
fig = Figure(figsize=(5, 5))       # Construction d'une nouvelle figure
subplot = fig.add_subplot(1, 2, 1) # Ajout d'une zone de dessin à gauche
subplot.imshow(M)                  # Ajout de l'image à la zone de dessin
subplot = fig.add_subplot(1, 2, 2) # Ajout d'une zone de dessin à droite
subplot.imshow(G, cmap='Greys_r', vmin=0, vmax=255)  # Ajout de l'image
fig                                # Affichage de la figure
```

+++ {"deletable": false, "editable": false, "nbgrader": {"schema_version": 3, "solution": false, "locked": true, "cell_type": "markdown", "grade_id": "cell-2d2a9c5ad3797eb9", "task": false, "grade": false, "checksum": "aa85a68fcfd625edef416f8fdb4ea9e9"}}

On choisit un seuil, ici à 150 à partir duquel on déduit un tableau
`F` de booléens où `F[i,j]` est `True` chaque fois que le pixel de
coordonnées `i`, `j` est au premier plan. Le tableau `F` peut être vu
comme une image en noir et blanc (respectivement, `False` et `True`) :

```{code-cell} ipython3
theta = 244
F = G < theta
plt.imshow(F);
```

+++ {"nbgrader": {"grade": false, "grade_id": "cell-9644608558a4dac4", "task": false, "cell_type": "markdown", "locked": true, "schema_version": 3, "solution": false, "checksum": "231ee50fdbc96fba13b88128bf8a7bf3"}, "editable": false, "deletable": false}

:::{admonition} Exercice
Essayez de changer la valeur de `theta`.
:::

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "6b82eb3d48602967bbc143b5fecd2f0f", "task": false, "grade_id": "cell-b14b5c077f03c98e", "locked": true, "solution": false, "grade": false, "schema_version": 3}}

:::{admonition} Exercice

En vous inspirant de ce qui précède, implémentez dans
[utilities.py](utilities.py) la fonction `foreground_filter(img, theta
= 150)` qui prend comme argument un tableau numpy `img` (c'est à dire
l'image PIL) et un seuil `theta`. La fonction renvoie une image
seuillée. Vérifiez-le sur notre image:

:::

```{code-cell} ipython3
---
nbgrader:
  task: false
  checksum: 6108a1b9228e595cf6db0a1e971a09b6
  solution: false
  locked: true
  cell_type: code
  grade: true
  grade_id: cell-5ebda2cbd264f4b4
  schema_version: 3
  points: 1
editable: false
deletable: false
---
plt.imshow(foreground_filter(img, 150));
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  schema_version: 3
  locked: true
  task: false
  checksum: 6c676be5d634ca7be0b7b73b66cf7617
  solution: false
  grade: false
  grade_id: cell-bb3b6429eafd310b
---
show_source(foreground_filter)
```

```{code-cell} ipython3
---
editable: false
nbgrader:
  task: false
  cell_type: code
  locked: true
  solution: false
  grade_id: cell-6a2537da445f1e93
  checksum: 997e07716a27f217e5c59ed0e0822a3b
  grade: true
  schema_version: 3
  points: 1
deletable: false
---
F = foreground_filter(img, 150)
assert isinstance(F, np.ndarray)
assert F.shape == (32, 32)
assert F.dtype == np.dtype('bool')
```

+++ {"nbgrader": {"locked": true, "grade_id": "cell-70f5be05bd26e966", "grade": false, "schema_version": 3, "solution": false, "checksum": "d2a0f09d8774f5adaf91b6bfca6206c8", "task": false, "cell_type": "markdown"}, "deletable": false, "editable": false}

::::{admonition} Exercice

Maintenant, appliquez le filtre avec un seuil de 200 à toutes les
images du jeu de données. Gardez le résultat en mémoire dans la
variable `images_filtrees`. Puis, affichez le résultat.

:::{tip} Indications
- Utiliser une compréhension `[f(x) for x in ...]` pour appliquer le filtre à toutes les images. 
- Utilisez `image_grid` pour afficher le résultat.
:::

::::

```{code-cell} ipython3
---
tags: []
deletable: false
nbgrader:
  solution: true
  locked: false
  checksum: f181dd2939cd80fb1d6e8b7fb19bc9ef
  schema_version: 3
  grade: false
  cell_type: code
  grade_id: cell-c8553d6b292ccbb3
  task: false
---
images_filtrees=[foreground_filter(element,200) for element in images ]
image_grid(images_filtrees)
```

```{code-cell} ipython3
---
nbgrader:
  grade_id: cell-b1d980788b1401fd
  task: false
  schema_version: 3
  locked: true
  checksum: 6e78324332a8b66f2cd0258eff045a00
  points: 1
  solution: false
  cell_type: code
  grade: true
deletable: false
editable: false
---
assert len(images_filtrees) == 20
assert images_filtrees[10].sum() == 166
assert images_filtrees[14].sum() == 363
assert images_filtrees[7].sum() == 1014
```

+++ {"deletable": false, "editable": false, "nbgrader": {"grade_id": "cell-d03d95544a53dc77", "solution": false, "grade": false, "schema_version": 3, "task": false, "cell_type": "markdown", "checksum": "a09515fe49d6428ce77e488c49ddb13b", "locked": true}}

::::{admonition} Exercice

[utilities.py](utilities.py) fournit une fonction
`transparent_background_filter` qui appelle `foreground_filter` et
filtre tous les pixels en arrière-plan transparent. Appliquez ce
filtre à toutes les images du jeu de données. Essayez différents
seuils de `theta`. A la fin, affichez les images pour le meilleur
seuil obtenu.

:::{tip} Indications
- Utiliser une compréhension `[f(x) for x in ...]` pour appliquer le
  filtre à toutes les images.
- Utilisez `image_grid` pour afficher le résultat.
- Commencez par tester des theta très différents les uns des autres
  comme 50, 100, 150, 200 puis rafinez votre seuil pour trouver le
  meilleur seuil.

:::

::::

```{code-cell} ipython3
---
deletable: false
tags: []
nbgrader:
  checksum: b6865a0d67904bb7896c609cae530e6a
  locked: false
  schema_version: 3
  solution: true
  grade: true
  points: 3
  task: false
  cell_type: code
  grade_id: cell-7d3d20b63df6cf3f
---
images_background=[transparent_background_filter(element,175) for element in images ]
image_grid(images_background)
```

+++ {"editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "d1131053089bd08afa5fc98c4ea7a81b", "schema_version": 3, "grade": false, "grade_id": "cell-7ff2716f64bd3d49", "solution": false, "locked": true}, "deletable": false}

## 2. Extraction de l'attribut `rougeur` 
  
Nous voulons maintenant extraire la « rougeur » de l'image, définie
comme la moyenne (mean/average) des pixels de premier plan du canal
`rouge` (*red*) (c'est-à-dire ceux qui sont `True` in `F`) moins la
moyenne des pixels de premier plan dans le canal `vert` (*green*).

::::{admonition} Exercice

1.  Implémentez la fonction `redness(img)` dans
    [utilities.py](utilities.py).

    :::{tip} Indications

    - Pour le calcul du premier plan, vous utiliserez le seuil par défaut
      de `foreground_filter`.
    - Pour calculer la moyenne, il est préférable de travailler avec des
      nombres à virgule flottante.
    - Commencez par extraire, le canal vert avec `G = M[:, :, 1] *
      1.0`. Faites de meme avec le canal rouge dans un tableau `R`.
    - Ensuite, sachez que si on a un tableau `R` et un tableau booléen
       (tel que `F`) de mêmes dimensions, alors `R[F]` renvoie un tableau
       avec uniquement les valeurs `R[i,j]` telles que `F[i,j]` vaut True.
    - Enfin, nous rappelons que `np.mean(R)` calcule la moyenne de toutes
      les valeurs d'un tableau `R` ou `G` ;

    Par exemple:

    :::

::::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  schema_version: 3
  checksum: a3e5b506c599a40a7c170e9875556809
  locked: true
  grade: false
  task: false
  solution: false
  grade_id: cell-3978f78a9fa10f97
editable: false
---
R = np.array([[1,2], [3,4]])
R
```

```{code-cell} ipython3
---
nbgrader:
  locked: true
  cell_type: code
  task: false
  schema_version: 3
  grade_id: cell-fddf27700769bbcf
  grade: false
  checksum: 978046f9d24ecb9556993c0b9fd12450
  solution: false
deletable: false
editable: false
---
F = np.array([[True, False], [True, True]])
F
```

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  schema_version: 3
  grade: false
  solution: false
  grade_id: cell-4e4d97156b7429c6
  task: false
  checksum: e14f0c15f70303eee8a0164b7ecb00ae
  locked: true
editable: false
---
R[F]
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  grade: false
  schema_version: 3
  task: false
  grade_id: cell-8aa181cfa4b01d43
  checksum: b895f310e0b5ec09d9c3e248d8976c90
  locked: true
  solution: false
---
show_source(redness)
```

+++ {"editable": false, "nbgrader": {"checksum": "f9720cc7dd12c99e7fa7d99286d46979", "locked": true, "grade_id": "cell-18f3bcf64ae7aba4", "task": false, "grade": false, "cell_type": "markdown", "schema_version": 3, "solution": false}, "deletable": false}

:::{admonition}

2.  Vérifiez visuellement la fonction `redness` sur les images du jeu
    de données:

:::

```{code-cell} ipython3
---
nbgrader:
  task: false
  grade_id: cell-99f50ef634746588
  solution: false
  grade: false
  schema_version: 3
  locked: true
  checksum: 0513375e2d9712d4482e9b1d738771d2
  cell_type: code
editable: false
deletable: false
---
image_grid(images, 
           titles=["{0:.2f}".format(redness(img)) for img in images])
```

+++ {"editable": false, "deletable": false, "nbgrader": {"schema_version": 3, "task": false, "locked": true, "grade": false, "grade_id": "cell-d242fc8639feb9aa", "checksum": "f130210158bafbf57060bcd7e1a7b40e", "solution": false, "cell_type": "markdown"}}

:::{admonition}

3.  Vérifiez votre fonction `redness` avec les assertions suivantes:

:::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  checksum: a3142956f413035d726f4573832c6a48
  grade: true
  grade_id: cell-e71108648b4ffe35
  cell_type: code
  schema_version: 3
  solution: false
  locked: true
  task: false
  points: 3
editable: false
---
assert abs(redness(images['b01.png']) -  0   ) < 0.1
assert abs(redness(images['a01.png']) - 41.48) < 0.1
assert abs(redness(images['a09.png']) - -3.66) < 0.1
```

+++ {"deletable": false, "editable": false, "nbgrader": {"grade": false, "grade_id": "cell-6c663025fad82c24", "locked": true, "schema_version": 3, "solution": false, "cell_type": "markdown", "checksum": "4a0aacf3bd9d5c0307d052ff58b90e66"}}

## 3. Extraction de l'attribut `elongation` 

Comme second attribut pour distinguer les pommes des bananes, nous
avons extrait l'**élongation** du fruit. Cela correspond au rapport de
la longueur sur la largeur de l'objet.  Mais comment mesurer ces
caractéristiques en premier lieu, lorsque les fruits peuvent avoir
n'importe quelle orientation, et qu'il peut y avoir du bruit dans
l'image ? C'est ce que nous allons voir maintenant.

Nous profiterons de l'occasion pour montrer une astuce élégante, mise
en oeuvre dans la fonction `elongation` déjà implémentée.

:::{admonition} Exercice

Affichez les images des fruits du jeu de données à l'aide
d'`image_grid` et utilisez la fonction `elongation` pour leur donner
en titre leur élongation. Vérifiez visuellement que c'est
plausible. Vous voudrez peut-être utiliser une règle dans le titre!

:::

```{code-cell} ipython3
---
nbgrader:
  solution: true
  grade: false
  grade_id: cell-f9e43c63bbd10689
  task: false
  locked: false
  checksum: 20b716e554c6a7f5ed4668f5c424c06f
  cell_type: code
  schema_version: 3
deletable: false
---
image_grid(images,
    titles=["{:.2f}".format(elongation(img)) for img in images])
```

+++ {"nbgrader": {"schema_version": 3, "checksum": "924c5ffa9068b6c8d26d50ed44ca03d4", "locked": true, "solution": false, "cell_type": "markdown", "grade": false, "grade_id": "cell-6c663025fad82c25"}, "editable": false, "deletable": false}

Alors, comment cela marche ?

Nous convertissons l'image en noir et blanc en un nuage de points :
*Chaque point représente les coordonnées d'un des pixels de premier
plan*. Ensuite, nous identifions les **axes principaux** du nuage de
points, en utilisant un algorithme très utilisé appelé **décomposition
en valeurs singulières**. Le premier axe principal est la direction de
la **plus grande variance** du nuage de points. La seconde est la
direction orthogonale à la première.  Le rapport d'élongation sera
défini comme le rapport des écarts-types dans les deux directions
principales.

+++ {"editable": false, "deletable": false, "nbgrader": {"task": false, "grade_id": "cell-e341ca269458c49f", "checksum": "fd0ca5469241f31c182d49b26cf6edc1", "cell_type": "markdown", "solution": false, "locked": true, "grade": false, "schema_version": 3}}

Illustrons ce principe avec une image de banane :

```{code-cell} ipython3
---
tags: []
deletable: false
nbgrader:
  grade: false
  cell_type: code
  schema_version: 3
  checksum: 3495ab327667f16da4ff9bc68f675d4a
  locked: false
  task: false
  grade_id: cell-9d25432bcc1b5c19
  solution: true
---
img = images['b02.png']
```

```{code-cell} ipython3
---
deletable: false
nbgrader:
  locked: true
  checksum: 72af7894425a4237fc935b3fae9d8381
  cell_type: code
  grade_id: cell-9d25432bcc1b5c20
  grade: false
  solution: false
  schema_version: 3
  task: false
editable: false
---
# Build the cloud of points defined by the foreground image pixels
F = foreground_filter(img)
xy = np.argwhere(F)
# Build the picture
fig = Figure(figsize=(20, 5))
# Original image
subplot = fig.add_subplot(1, 3, 1)
subplot.imshow(img)
subplot.set_title("Original image", fontsize=18) 
# The foreground as a black and white picture
subplot = fig.add_subplot(1, 3, 2)
subplot.imshow(foreground_filter(img))
subplot.set_title("Foreground", fontsize=18) 
# The cloud of points, as a scatter plot, together with the principal axes
subplot = fig.add_subplot(1, 3, 3)
subplot.scatter(xy[:,1], xy[:,0])
elongation_plot(img, subplot)
subplot.set_xlim(0, 31)
subplot.set_ylim(31, 0)
subplot.set_aspect('equal', adjustable='box')
subplot.set_title("Cloud of points and principal axes",  fontsize=18)
fig
```

+++ {"deletable": false, "editable": false, "nbgrader": {"grade": false, "grade_id": "cell-4c27a2b71c75cb5a", "locked": true, "solution": false, "cell_type": "markdown", "checksum": "a5362dd604c4be0d04463c877d289755", "schema_version": 3, "task": false}}

:::{admonition} Exercice
Essayez de nouveau avec d'autres figures
:::

```{code-cell} ipython3
---
nbgrader:
  grade_id: cell-7dbc3c0bf7a0ccb6
  cell_type: code
  schema_version: 3
  solution: false
  grade: true
  checksum: 6f06d60035cc1b97f0203c2a58ad182a
  locked: true
  points: 1
  task: false
tags: []
deletable: false
editable: false
---
assert img != images['b01.png']
```

+++ {"nbgrader": {"schema_version": 3, "cell_type": "markdown", "grade": false, "solution": false, "task": false, "grade_id": "cell-ce7f4108c0750424", "checksum": "d86890b6944676e62a543d0ca40dd9b3", "locked": true}, "deletable": false, "editable": false}

:::{hint} Pour aller plus loin

L'astuce a été d'utiliser la décomposition en valeurs
singulières. Nous avons vu ce principe lors du CM4 qui parlait en
détail des ACP (Analyses en Composantes Principales, *PCA* en anglais)
sur des poissons. Vous verrez les mathématiques derrière cette méthode
lors de vos cours d'algèbre linéaire mais sachez que, grâce aux
bibliothèques existantes, vous pouvez déjà utiliser cette méthode en
quelques lignes !

:::

```{code-cell} ipython3
---
tags: []
deletable: false
editable: false
slideshow:
  slide_type: ''
nbgrader:
  cell_type: code
  checksum: a043132d5f5b926d8cfb07fe10657d01
  grade_id: cell-07d0c891c7a0e4b2
  locked: true
  task: false
  solution: false
  grade: false
  schema_version: 3
---
show_source(elongation)
```

+++ {"deletable": false, "editable": false, "nbgrader": {"grade": false, "task": false, "schema_version": 3, "locked": true, "grade_id": "cell-2d9761ffe4351de2", "checksum": "fbb96e0b40729cbea39eea7c2f8cc116", "solution": false, "cell_type": "markdown"}}

## Conclusion

:::{admonition} Exercice

Ici, nous avons implémenté l'extraction de deux attributs, suffisants
pour séparer les pommes des bananes. Cherchez quels attributs vous
pourriez utiliser pour vos images et implémentez dans
[utilities.py](utilities.py) les fonctions adéquates !
    
:::

Mettez à jour votre rapport, puis passez à la feuille d'[analyse de
données](4_analyse_de_donnees.md).
