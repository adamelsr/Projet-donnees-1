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

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "6074d701b3588906df8ca144f135fe99", "grade": false, "grade_id": "cell-63247b06949c9806", "locked": true, "schema_version": 3, "solution": false}, "slideshow": {"slide_type": ""}, "tags": []}

# Manipuler des tableaux

Dans cette feuille, vous allez apprendre à effectuer quelques
manipulations simples sur les tableaux, comme nous l'avions fait au
premier semestre avec les `vector` de C++. En Python, de tels tableaux
peuvent être représentés par les `array` de la bibliothèque `NumPy`
(usuellement abrégée en `np`) :

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 9c3f5d5cb593afc848b35bc23508bf55
  grade: false
  grade_id: cell-8c751ead7518dfea
  locked: true
  schema_version: 3
  solution: false
---
import numpy as np
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "4fd5cbde5429f2982ac9751f22b2c960", "grade": false, "grade_id": "cell-1063495ca725c5db", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Tableaux à deux dimensions

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "dfac298c8c6c4f205299b6cf310a5a53", "grade": false, "grade_id": "cell-9a29dafa51e1a013", "locked": true, "schema_version": 3, "solution": false}}

Voilà un tableau à deux dimensions avec deux lignes et quatre
colonnes:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 7cb43c2d929cc16a479bb323b5797149
  grade: false
  grade_id: cell-67fbacbcf94193b3
  locked: true
  schema_version: 3
  solution: false
---
T = np.array([[1, 2, 3, 4], 
              [5, 6, 7, 8]])
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 722eb1481c7f22f0a26b7b3a9b865113
  grade: false
  grade_id: cell-845dffdd69e40937
  locked: true
  schema_version: 3
  solution: false
---
T
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "e4b026ff926e4239ba5644d1dcd6dc9b", "grade": false, "grade_id": "cell-47cf516abf13b964", "locked": true, "schema_version": 3, "solution": false}}

On peut retrouver les tailles de ce tableau avec:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: a1ab35b251b03547c95bf160ea2bcdd1
  grade: false
  grade_id: cell-3cfd6fa0623e6f98
  locked: true
  schema_version: 3
  solution: false
---
T.shape
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "e305214dc702325e2f921792f8b094cc", "grade": false, "grade_id": "cell-c8f6590b61b5b276", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Vous vous rappellez que les `vector` de C++ sont intrinsèquement des
tableaux à une dimension, et que l'on émule des tableaux à deux
dimensions avec des tableaux de tableaux. Ici, en revanche, les
tableaux `array` de numpy permettent de construire explicitement des
tableaux à deux dimensions.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "1c35762da5c36c75fdb86d3dc2a6a734", "grade": false, "grade_id": "cell-3080232c4e2fb2df", "locked": true, "schema_version": 3, "solution": false}}

### Exercice

1. Construisez un tableau à trois lignes et trois colonnes, contenant
   les entiers de 1 à 9 de gauche à droite et de haut en bas comme
   dans la figure suivante:

       1 2 3
       4 5 6
       7 8 9

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: bbd5ec8d0c08d45e4cec41fcff437281
  grade: false
  grade_id: cell-1b95ffffb22a38df
  locked: false
  schema_version: 3
  solution: true
  task: false
---
T2=np.array([[1,2,3],
           [4,5,6],
           [7,8,9]])
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "ff72beaf7319a2e76325912258108167", "grade": false, "grade_id": "cell-f23c45dc4abb2118", "locked": true, "schema_version": 3, "solution": false}}

Nous testons la forme du tableau:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: b192f2c627830d51a9eb10a8c6129145
  grade: true
  grade_id: cell-3dcbc34e7cdb8449
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert T2.shape == (3,3)
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "473b88c0c5b7366dc6b1e1e94fbccb3c", "grade": false, "grade_id": "cell-96fc71e105b68b41", "locked": true, "schema_version": 3, "solution": false, "task": false}}

ainsi que son contenu :

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 63a383e3e61ecdd20d9bd680c6e7da1f
  grade: true
  grade_id: cell-b2598336ebcb56a2
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert [ T2[i,j] for i in range(3) for j in range(3) ] == [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "49c89155418473f66a056b5b7adb683e", "grade": false, "grade_id": "cell-21d9a01c8d293ab4", "locked": true, "schema_version": 3, "solution": false}}

Voici comment accéder au contenu d'une case individuelle du tableau :

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 2e3a1fee5a81d040573266cd4298f663
  grade: false
  grade_id: cell-9ca4451347ad1cf3
  locked: true
  schema_version: 3
  solution: false
---
T2[1,2]
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "9c20aba9730f7d17da5db1b67008e594", "grade": false, "grade_id": "cell-0c42459abbd31832", "locked": true, "schema_version": 3, "solution": false}}

Cette case est en deuxième ligne et troisième colonne: en effet, comme
en C++, les lignes et colonnes sont numérotées à partir de 0.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "24865da222354aead7858ac2ff96a31f", "grade": false, "grade_id": "cell-4aaf4afc9dab0881", "locked": true, "schema_version": 3, "solution": false}}

Si l'on veut extraire toute une ligne, ou toute une colonne, on
remplace la coordonnée que l'on ne veut pas spécifier par `:`.

Voici donc la deuxième colonne :

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: f4c04730adc08ef40ade35dbf4e632c9
  grade: false
  grade_id: cell-6c91767340cf600d
  locked: true
  schema_version: 3
  solution: false
---
T2[:,1]
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "947471cc48e21b51def4e80bd7f7b3a1", "grade": false, "grade_id": "cell-7d229a134ec6e867", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Extrayez la deuxième ligne du tableau et affectez-la à la variable
`li` dont vous afficherez le contenu :

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: dfe34b98659f9c914a7630187e43cdbf
  grade: false
  grade_id: cell-0abb1396ab91dd95
  locked: false
  schema_version: 3
  solution: true
  task: false
---
li=T2[1,:]
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: a512644996d219eb143ad64c92f8d748
  grade: true
  grade_id: cell-e22d3374bf68c443
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert isinstance(li, np.ndarray)
assert li.shape == (3,)
assert list(li) == [4,5,6]
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "efe72d3af5c1d8c82950b20179f3219d", "grade": false, "grade_id": "cell-990adcd36c40f8df", "locked": true, "schema_version": 3, "solution": false}}

## Tableaux à trois dimensions et plus

Pour le moment, nous avons utilisé des tableaux à deux dimensions.
Ultérieurement, notamment pour représenter des images, nous aurons
besoin de tableaux de plus grande dimension: un seul nombre ne suffit
en effet pas pour représenter un pixel.

`Numpy` permet de représenter des tableaux de toute dimension. Voici
un tableau de dimension 3 :

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 70013da6dfca06661b1d7226a04b209b
  grade: false
  grade_id: cell-34c03e0c6027d356
  locked: true
  schema_version: 3
  solution: false
---
T3D = np.array([[[ 1, 2, 3], [ 4, 5, 6], [ 7, 8, 9]],
                [[10,11,12], [13,14,15], [16,17,18]],
                [[19,20,21], [22,23,24], [25,26,27]]
                ])
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "f8f4feab3107f36d927db4cd039158bc", "grade": false, "grade_id": "cell-796c1a5acbab1a2b", "locked": true, "schema_version": 3, "solution": false}}

On peut le voir comme un tableau à trois couches :
    
:::{figure} media/fig_tab.svg
:width: 30%
:alt: représentation du tableau à trois dimensions
:::

Pour accéder à une case du tableau on utilise `T[i,j,k]`, où `i` est
le numéro de la ligne, `j` le numéro de la colonne et `k` le numéro de
la couche contenant la case.

Comme pour les listes, on peut extraire des sous-tableaux avec les
opérateurs de découpe de tranches (*slicing*).

:::{hint} Rappel: tranches (*slices*)
:class: dropdown

Lorsque `L` est une liste, l'opération `L[start:stop:step]` permet
d'extraire une *tranche* de `L`, liste contenant tous les éléments de
`L` d'indice entre `start` (inclus) et `stop` (exclus) par pas de
`step`. Par défaut, `start` vaut `0`, `stop` vaut `len(L)`, et `step`
vaut `1`. Ainsi, `L[:3]` contient les trois premiers éléments de `L`
(d'indice `i<3`) tandis que `L[3:]` contient les éléments suivants
(d'indice `3<=i`).

Plus généralement, cette opération s'applique à la plupart des objets
indexés par des entiers.

:::

On peut ainsi extraire ces couches comme suit :

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: eca7db301fc9a95c1223a90acbc9b073
  grade: false
  grade_id: cell-574e34b7ddc4509d
  locked: true
  schema_version: 3
  solution: false
---
T3D[:,:,0]
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: f527ab4e84f78ff2b0df65dd2ac0ea79
  grade: false
  grade_id: cell-dd11d154ece1aef6
  locked: true
  schema_version: 3
  solution: false
---
T3D[:,:,1]
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: c47db6d04707bcb3049d977cde2178c5
  grade: false
  grade_id: cell-a96fbf7480f42e12
  locked: true
  schema_version: 3
  solution: false
---
T3D[:,:,2]
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "32d4305d44b19872f26f8c5e37b5bd6b", "grade": false, "grade_id": "cell-414edd834755639f", "locked": true, "schema_version": 3, "solution": false}}

### Exercices

Extrayez la première colonne de la deuxième couche de `T3D` et
stockez-la dans la variable `C`:

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 97c5408e00c8fbe1f2ac085b1411f6fd
  grade: false
  grade_id: cell-81c4d71ee7b1a54d
  locked: false
  schema_version: 3
  solution: true
  task: false
---
C= T3D[:,0,1]
C
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "863f9bb7af6a9d13186db7a08a232f59", "grade": false, "grade_id": "cell-868c3302aea64357", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Notez que c'est un tableau à une dimension, donc noté en ligne !

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 48f39bf8c72b94c70a2e41d6a073957f
  grade: true
  grade_id: cell-995993eb1b58947e
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert list(C) == [2, 11, 20]
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "2c5c6fa99b39d074b1c1b0a5c957ce69", "grade": false, "grade_id": "cell-414edd834755639g", "locked": true, "schema_version": 3, "solution": false}}

Maintenant, extrayez un tableau contenant la première colonne de chacune des trois
couches de `T3D` et stockez le dans la variable `C`. Notez que l'on
souhaite que ces colonnes soient bien représentées par des colonnes
dans `C` !

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 32e2460e22a0bfc0e5f0697e3caaf400
  grade: false
  grade_id: cell-abdcb2e9f73d6dfe
  locked: false
  schema_version: 3
  solution: true
  task: false
---
C=T3D[:,0,:]
C
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: e262f80868e4db8544ea173aa973639d
  grade: true
  grade_id: cell-3227c3665bd8802d
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
for i in range(3):
    assert np.array_equal(T3D[:,0,i], C[:,i])
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "1ffe30a723d426e49c74c47beaf4a081", "grade": false, "grade_id": "cell-72625c162aacdd71", "locked": true, "schema_version": 3, "solution": false}}

## Statistiques simples sur les tableaux

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "8793482aa66bacbd22022602cc17dc9a", "grade": false, "grade_id": "cell-202df26286a5b3a0", "locked": true, "schema_version": 3, "solution": false}}

Numpy permet de faire des statistiques simples sur les
tableaux. Revenons à notre tableau `T` :

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: ecaceef2f7991bf4795869507af9995c
  grade: false
  grade_id: cell-e979baa940e6f47e
  locked: true
  schema_version: 3
  solution: false
---
T
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "f6b580f520d20d84d004d9c7f40527f3", "grade": false, "grade_id": "cell-29729cfe62afb790", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Calculez à la main :
- la moyenne de chaque colonne de `T`;
- la moyenne de chaque ligne de `T`;
- la moyenne de tous les éléments du tableau `T`.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "53a292fef70b49201d991c1f6784e251", "grade": false, "grade_id": "cell-00194d77bb863b7b", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Comparez vos résultats avec ceux des calculs suivants. Que calcule chaque commande ci-dessous?

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 89b3d8b2479b327aa146156f95a8b494
  grade: false
  grade_id: cell-1d9fbab6c508d984
  locked: true
  schema_version: 3
  solution: false
---
T.mean(axis=0)
```

La commande ci-dessus calcule la moyenne de chaque colonne de T et met la moyenne de chaque colonne dans un array.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: d827b580b4fba02c8bee40488cc9b296
  grade: false
  grade_id: cell-899594980a692e52
  locked: true
  schema_version: 3
  solution: false
---
T.mean(axis=1)
```

Au-dessus, la commande calcule la moyenne de chaque ligne du tableau T et le met dans un array avec comme colonne, les 2 lignes.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 33c3909e4504c6f5be8c28f7b79e6e5a
  grade: false
  grade_id: cell-e979baa940e6f47d
  locked: true
  schema_version: 3
  solution: false
---
T.mean()
```

+++ {"tags": []}

Cette commande va calculer la moyenne de tous les élements présents dans le tableau sans prendre en compte lignes ou colonnes et renvoie un float correspondant à cette moyenne.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "98a035057c22e5c5a30e92ffea4bf263", "grade": false, "grade_id": "cell-7fc37d52040f3366", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Conclusion

Voilà, vous avez vu tous les éléments de manipulation des tableaux
`NumPy` dont nous aurons besoin aujourd'hui.
