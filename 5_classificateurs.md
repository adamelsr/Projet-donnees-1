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

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "afbf34e64e7471cefc07d9483063e7a8", "grade": false, "grade_id": "cell-3876f910a24fe8a7", "locked": true, "schema_version": 3, "solution": false}, "slideshow": {"slide_type": ""}, "tags": []}

# Classificateurs

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "61216816be7804468ac749242b623d4a", "grade": false, "grade_id": "cell-65c63f4be1820d2e", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Dans cette feuille, nous allons explorer l'utilisation de plusieurs
classificateurs sur l'exemple des pommes et des bananes. Vous pourrez
ensuite les essayer sur votre jeu de données.

Commencons par charger les utilitaires et bibliothèques:

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 1ea7da415eef57aad06d2165be7ca4ff
  grade: true
  grade_id: cell-a2ccd1e13b05762c
  locked: false
  points: 0
  schema_version: 3
  solution: true
  task: false
---
from PIL import Image
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd                  
import os

from intro_science_donnees import *
## les utilitaires
%load_ext autoreload
%autoreload 2
from utilities import *
# Graphs and visualization library
import seaborn as sns; sns.set()      
# Configuration intégration dans Jupyter
%matplotlib inline
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "d880dfccac7e7bb362d70f774bf09ebb", "grade": false, "grade_id": "cell-875bebae978f4f5a", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Chargement et préparation des données

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "b4c6e614484358e629bcce73f49598b8", "grade": false, "grade_id": "cell-ce0810dd4273ea24", "locked": true, "schema_version": 3, "solution": false, "task": false}}

On charge le jeu de données prétraité (attributs rougeur et élongation
et classes des fruits). Cela correspond au fichier `attributs.csv` utilisé en Semaine3 :

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 76a3f12c5033c5423b3759e49ef95abc
  grade: false
  grade_id: cell-e6d48e8b35c2d42a
  locked: true
  schema_version: 3
  solution: false
  task: false
---
import os.path
attributs_file = os.path.join(data.dir, 'attributs.csv')
df= pd.read_csv(attributs_file,index_col=0)

# standardisation
dfstd =  (df - df.mean()) / df.std()
dfstd['class'] = df['class']
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "5e412381817b3618b8a7a7ca91094d61", "grade": false, "grade_id": "cell-24210bafac4b3490", "locked": true, "schema_version": 3, "solution": false, "task": false}}

On partitionne le jeu de données en ensemble de test et
d'entraînement:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 153d7ed14b1d95db0e1a369c646c7c44
  grade: false
  grade_id: cell-00b3f36097ec9704
  locked: true
  schema_version: 3
  solution: false
  task: false
---
X = dfstd[['redness', 'elongation']]
Y = dfstd['class']
#partition des images
train_index, test_index = split_data(X, Y, seed=3)

#partition de la table des attributs
Xtrain = X.iloc[train_index]
Xtest = X.iloc[test_index]
#partition de la table des étiquettes
Ytrain = Y.iloc[train_index]
Ytest = Y.iloc[test_index]
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "741881738d7829a3b3d62de9cceb02f2", "grade": false, "grade_id": "cell-9e3cf5dde27fbb00", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Classificateurs basés sur les exemples (*examples-based*)

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "45db778c1166c64282fd7d8e20a03d1b", "grade": false, "grade_id": "cell-f7f11edbe1e13a7d", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Nous allons maintenant voir comment appliquer des classificateurs
fournis par la librairie `scikit-learn`.  Commençons par le
classificateur plus proche voisin déjà vu en semaines 3 et 4.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "40979d861a5204582bc97eca2e359c92", "grade": false, "grade_id": "cell-28f37cb9aba3b0d6", "locked": true, "schema_version": 3, "solution": false, "task": false}}

### KNN : $k$-plus proche voisins

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: eedf6344cb5b6474a8330504c426b4c8
  grade: false
  grade_id: cell-786fada559c8c5e0
  locked: true
  schema_version: 3
  solution: false
  task: false
---
from sklearn.neighbors import KNeighborsClassifier

#définition du classificateur, ici on l'appelle classifier
# on choisit k=1
classifier = KNeighborsClassifier(n_neighbors=1)
# on l'ajuste aux données d'entrsainement
classifier.fit(Xtrain, Ytrain) 
# on calcule ensuite le taux d'erreur lors de l'entrainement et pour le test
Ytrain_predicted = classifier.predict(Xtrain)
Ytest_predicted = classifier.predict(Xtest)
# la fonction error_rate devrait etre présente dans votre utilities.py (TP3), sinon ajoutez-la
e_tr = error_rate(Ytrain, Ytrain_predicted)
e_te = error_rate(Ytest, Ytest_predicted)

print("Classificateur: 1 Nearest Neighbor")
print("Training error:", e_tr)
print("Test error:", e_te)
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "f8da6d0f32e1d7a10ca9f9a6ff309393", "grade": false, "grade_id": "cell-4db77bd51d290099", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition} Exercice

Quels sont les taux d'erreur pour l'ensemble d'entraînement et
l'ensemble de test ?

:::

+++ {"deletable": false, "nbgrader": {"cell_type": "markdown", "checksum": "c84bc8bccecc65edc309a08bdbc00fa9", "grade": true, "grade_id": "cell-2bcc05988216d1c5", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}}

Le taux d'erreur pour l'ensemble d'entraînement est de 0 et celui pour l'ensemble de test est 0.2.

+++

On mémorise ces taux dans une table `error_rates` que l'on complétera
au fur et à mesure de cette feuille:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: be4ace641636b1b069ceaaa16204f33e
  grade: false
  grade_id: cell-84331f5cb22a0f87
  locked: true
  schema_version: 3
  solution: false
  task: false
---
error_rates = pd.DataFrame([], columns=['entrainement', 'test'])
error_rates.loc["1 Nearest Neighbor",:] = [e_tr, e_te]
error_rates
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "5934b5e62b2349dafd3fa250305cf7e9", "grade": false, "grade_id": "cell-2034d3a7e9dbbfad", "locked": true, "schema_version": 3, "solution": false, "task": false}}

### Fenêtres de Parzen (*Parzen window* ou *radius neighbors*)

Pour ce classificateur, on ne fixe pas le nombre de voisins mais un
rayon $r$; la classe d'un élément $e$ est prédite par la classe
majoritaire parmi les éléments de l'ensemble d'entraînement dans la
sphère de centre $e$ et de rayon $r$.

:::{admonition} Exercice
1.  Complétez le code ci-dessous:
:::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 075ee8d9c439da9d08817ef6753e3fd3
  grade: false
  grade_id: cell-64dfc640f023f84e
  locked: false
  schema_version: 3
  solution: true
  task: false
---
from sklearn.neighbors import RadiusNeighborsClassifier
classifier = RadiusNeighborsClassifier(radius=2.0)

# on l'ajuste aux données d'entrainement
parzen = RadiusNeighborsClassifier(radius=20)
parzen.fit(Xtrain, Ytrain)

#prédictions
Ytrain_predicted = parzen.predict(Xtrain)
Ytest_predicted = parzen.predict(Xtest)


# on calcule ensuite le taux d'erreur lors de l'entrainement et pour le test


# Calcul des erreurs
e_tr = error_rate(Ytrain, Ytrain_predicted)
e_te = error_rate(Ytest, Ytest_predicted)



print("Classificateur: Parzen Window")
print("Training error:", e_tr)
print("Test error:", e_te)
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "2a23275f290ee32a4d526055b004f666", "grade": false, "grade_id": "cell-540f1e8f9850f69f", "locked": true, "schema_version": 3, "solution": false, "task": false}}

::::{admonition}

2.  Complétez la table `error_rates` avec ce modèle, en rajoutant une
    ligne d'index `Parzen Window`.

    :::{admonition} Indication
     
    Utiliser `.loc` comme ci-dessus.
     
    :::

::::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 6c97291bbff6a5bfcdc72decb782bd3e
  grade: false
  grade_id: cell-4274f47e142d9ed1
  locked: false
  schema_version: 3
  solution: true
  task: false
---
error_rates.loc["Parzen Window",:] = [e_tr, e_te]
error_rates
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 94009d7f2c58ec5ad7e96258e1585d05
  grade: true
  grade_id: cell-6ac30547e91d336f
  locked: true
  points: 2
  schema_version: 3
  solution: false
  task: false
---
assert isinstance(error_rates, pd.DataFrame)
assert list(error_rates.columns) == ['entrainement', 'test']
assert list(error_rates.index) == ['1 Nearest Neighbor', 'Parzen Window']
assert (0 <= error_rates).all(axis=None), "Les taux d'erreurs doivent être positifs"
assert (error_rates <= 1).all(axis=None), "Les taux d'erreurs doivent être inférieur à 1"
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "c0c51b445bb0257bbb01ed35c32f8f9a", "grade": false, "grade_id": "cell-7ca6c7b760e2f6d3", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition} 

4.  $\clubsuit$ Faites varier le rayon $r$. Qu'observez vous quand le
    rayon est grand ? petit ? Comment interprétez-vous ces phénomènes?
    Que signifie un taux d'erreur de 0.5 ? Est-ce un bon taux d'erreur?

	Vous pouvez ajouter des modèles à la table `error_rates` s'ils
    vous semblent pertinents. 

:::

+++ {"deletable": false, "nbgrader": {"cell_type": "markdown", "checksum": "907f7d1366791fc82015fecbb1f759ed", "grade": true, "grade_id": "cell-77915ac0dc089d51", "locked": false, "points": 3, "schema_version": 3, "solution": true, "task": false}}

Quand le rayon est grand, on remarque que l'erreur de l'entraînement augmente jusqu'à O.5 en égalant l'erreur de test.
Ici, comme le rayon est grand, il a alors beaucoup de voisins donc trop de données sur la zone et cela augmente donc le taux d'erreur de l'entraînement en plus de celui du test. Cela represente un cas de sous-apprentissage/ underfitting car les 2 taux d'erreurs sont mauvais.

Quand le rayon est petit, on voit que l'erreur de l'entraînement est faible jusqu'à atteindre 0 soit plus petit que l'erreur de test de 0.5 Ici, comme le rayon est petit, il n'a pas beaucoup de voisins donc le modèle peut vite changer rapidement soit instable. Cela represente un cas de sur-apprentissage/overfitting car l'erreur d'entrainement est bonne tandis que celui du test est mauvaise donc elle généralise mal.

Un taux d'erreur de 0.5 signifie 50% chances de se tromper soit une chance sur 2 que le modèle se trompe. Ce qui est par conséquent énorme et très mauvais car ici on n'a pas l'impression que c'est un modèle de prédiction mais plutôt un modèle de hasard entre 2 évènements. Dans notre cas, cela ne semble pas pertinent comme modèle à utiliser.


+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "11aa8b1bee7bca0e0941f5be75907e9b", "grade": false, "grade_id": "cell-7474d5437867f93b", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Classificateurs basés sur les attributs (*feature based*)

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "7f142dd64f1cac9b6487260ca1cff01d", "grade": false, "grade_id": "cell-bc351a36f5734e8b", "locked": true, "schema_version": 3, "solution": false, "task": false}}

### Régression linéaire

+++ {"deletable": false, "nbgrader": {"cell_type": "markdown", "checksum": "7e6e9d79470661ea852bb14ae3aed651", "grade": true, "grade_id": "cell-aa0635012d566877", "locked": false, "points": 1, "schema_version": 3, "solution": true, "task": false}}

:::{admonition} Exercice

Pourquoi ne peut-on pas appliquer la méthode de régression linéaire
pour classer nos pommes et nos bananes ?

:::

Elle ne s’applique pas aux problèmes de classification, car elle est utilisée pour prédire des valeurs continues, et non pour assigner des données à des classes discrètes.
Autrement dit, elle n'est pas adaptée à la classification car elle prédit des valeurs numériques continues comme 0.7,1.2, -6 tandis que pour la classification, la prédiction doit se faire sur les valeurs des classes comme par exemple  1 et -1 afin de pouvoir identifier et séparer les classes efficacement.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "6e75b4ffc13642cda57f2610ee0b93dc", "grade": false, "grade_id": "cell-f3fe417cf16e9bb2", "locked": true, "schema_version": 3, "solution": false, "task": false}}

### Arbres de décision

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "ca97a3e6e5fb381ffa0cf367ac37dd72", "grade": false, "grade_id": "cell-0c0e203b37439b49", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Les arbres de décison correspondent à des modèles avec des décisions
imbriquées où chaque noeud teste une condition sur une variable.  Les
étiquettes se trouvent aux feuilles.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "df901f401ff08d110978a64a71d9ead8", "grade": false, "grade_id": "cell-da133a018c6e8417", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition} Exercice

1.  Complétez le code ci-dessous.

:::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: a123282b37a47fa67ced79dab08f4543
  grade: false
  grade_id: cell-8e19513e3f66e21a
  locked: false
  schema_version: 3
  solution: true
  task: false
---
from sklearn import tree

classifier = tree.DecisionTreeClassifier()
# on l'ajuste aux données d'entrainement


tree_tp4 = tree.DecisionTreeClassifier()
tree_tp4.fit(Xtrain, Ytrain)


# on calcule les prédictions du classifieur sur les ensembles d'entrainement et de test

#prédictions
Ytrain_predicted = tree_tp4.predict(Xtrain)
Ytest_predicted = tree_tp4.predict(Xtest)

# on calcule les taux d'erreurs

e_tr2 = error_rate(Ytrain, Ytrain_predicted)
e_te2 = error_rate(Ytest, Ytest_predicted)


print("Classificateur: Arbre de decision")
print("Training error:", e_tr2)
print("Test error:", e_te2)
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "2dd910b8d591200206718159779cfd4a", "grade": false, "grade_id": "cell-d818ab75031ccf3c", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition}
2.  Complétez la table `error_rates` avec ce modèle.
:::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 54e602f2d585ff5dfc81c09fa54777d2
  grade: false
  grade_id: cell-b2218cbf456bd91c
  locked: false
  schema_version: 3
  solution: true
  task: false
---
error_rates.loc["Arbre de decision",:] = [e_tr2, e_te2]
error_rates
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 33f0ea85f8cee192d6dc5c287456f00a
  grade: true
  grade_id: cell-57894376c13e530a
  locked: true
  points: 2
  schema_version: 3
  solution: false
  task: false
tags: []
---
assert isinstance(error_rates, pd.DataFrame)
assert list(error_rates.columns) == ['entrainement', 'test']
assert error_rates.shape[0] >= 3
assert (0 <= error_rates).all(axis=None), "Les taux d'erreurs doivent être positifs"
assert (error_rates <= 1).all(axis=None), "Les taux d'erreurs doivent être inférieur à 1"
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "df39eb9cf7038e9c5ba20d14b2f6c998", "grade": false, "grade_id": "cell-f1f775a2ccb77c41", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition}
3.  Représentez l'arbre de décision comme vu lors du CM5.
:::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: ab4ebccfd10bfb3b26cd7a85e24a3e5e
  grade: true
  grade_id: cell-e4ce3f1406e9fe61
  locked: false
  points: 1
  schema_version: 3
  solution: true
  task: false
tags: []
---
import matplotlib.pyplot as plt

plt.figure(figsize=(12,12)) 
tree.plot_tree(tree_tp4, fontsize=10) 
plt.show()
# indice de gini : mesure de l'impureté du jeu de données
# Gini = 0 --> une seule classe --> groupe pur
# Gini élevé --> classes mélangées (Gini = 1 - \sum(p^2_k; où p_k est la proportion de la classe k dans le noeud)
```

+++ {"deletable": false, "nbgrader": {"cell_type": "markdown", "checksum": "87ddbb472c690ce3bc201f1a554efa51", "grade": true, "grade_id": "cell-316a87fad1287712", "locked": false, "points": 2, "schema_version": 3, "solution": true, "task": false}}

:::{admonition}

4.  Interprétez cette figure. Combien de critère(s) ont été pris en
    compte pour séparer les pommes des bananes ? Quel est le premier
    critère (attribut et valeur seuil) de séparation des échantillons?
    Que signifie une mesure de gini à 0.0 ?

:::

Ici, il y a un seul critère pris en compte pour séparer les pommes des bananes car il y a un seul seuil ou chose qui sépare les 2 classes avec les feuilles. Ce premier critère est pour l'attribut "x[1]" soit le deuxième élement et le seuil de séparation des échantillons est -0.192. Si le seuil est respecté, cela renvoie a la branche True à gauche sinon c'est la branche False à droite.

Une mesure de gini à 0.0 signifie que toutes les données appartiennent à une seule et unique classe et que donc ces données respectent tous le seuil. 

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "4d130da1537149b2d938f87bb679c7c1", "grade": false, "grade_id": "cell-ff5d2dccfd4a6505", "locked": true, "schema_version": 3, "solution": false, "task": false}}

### Perceptron

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "238953fe4b487ec962b4a8d62b1f5dd9", "grade": false, "grade_id": "cell-e4a08d06646c875e", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Le perceptron est un réseau de neurones artificiels à une seule couche
et donc avec une capacité de modélisation limitée; pour le problème
qui nous intéresse cela est suffisant. Pour plus de détails, revenez
au [cours](CM5.md)

:::{admonition} Exercice

1.  Complétez le code ci-dessous, où l'on définit un modèle de type
    `Perceptron` avec comme paramètres $10^{-3}$ pour la tolérence,
    $36$ pour l'état aléatoire (*random state*) et 100 époques
    (*max_iter*)

:::

```{code-cell} ipython3
---
deletable: false
editable: true
nbgrader:
  cell_type: code
  checksum: 1616f84f831b6981890b007c5c53afe7
  grade: false
  grade_id: cell-c6bfeee5a4a966cc
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: ''
tags: []
---
from sklearn.linear_model import Perceptron

# définition du modèle de classificateur

tp4_perceptron = Perceptron(tol=1e-3, random_state=36, shuffle=True, max_iter=100)
# *tol* est un autre critère d'arret
# Si loss <= previous_loss - tol alors on n'améliore pas le modèle
# en changeant les poids: on s'arrete.
#shuffle et random_state sont fixés afin d'avoir un exemple reproductible, comme une seed
tp4_perceptron.fit(Xtrain, Ytrain)



# on l'ajuste aux données d'entrainement

#prédictions
Ytrain_predicted = tp4_perceptron.predict(Xtrain)
Ytest_predicted = tp4_perceptron.predict(Xtest)

# on calcule ensuite le taux d'erreur lors de l'entrainement et pour le test

# Calcul des erreurs
e_tr = error_rate(Ytrain, Ytrain_predicted)
e_te = error_rate(Ytest, Ytest_predicted)


print("Classificateur: Perceptron")
print("Training error:", e_tr)
print("Test error:", e_te)
```

+++ {"deletable": false, "nbgrader": {"cell_type": "markdown", "checksum": "0a43e9467112e34f70d86df3594229ca", "grade": true, "grade_id": "cell-f8994015ecc492d3", "locked": false, "points": 1, "schema_version": 3, "solution": true, "task": false}}

:::{admonition}

2.  Lisez la documentation de `Perceptron`. À quoi correspond le
    paramètre `random_state` ?

Le paramètre random_state permet de mélanger les données d'entraînements. Ce paramètre permet de contrôler le générateur de nombres aléatoires utilisé (cf. Glossaire de random_stateparameter).
:::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 6c06d000995285781775ef088b2f0bfb
  grade: false
  grade_id: cell-4f0cec434737cda7
  locked: false
  schema_version: 3
  solution: true
  task: false
---
Perceptron?
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "ff421918c13a1458d637d7d1d2c1f042", "grade": false, "grade_id": "cell-65470533b4335e5a", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition}
3.  Complétez la table `error_rates` avec ce modèle.
:::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: a71a5f08c8bdf5f6e2efee8d4768eea4
  grade: false
  grade_id: cell-cfe370c6b70f6d27
  locked: false
  schema_version: 3
  solution: true
  task: false
---
error_rates.loc["Perceptron",:] = [e_tr, e_te]
error_rates
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 49ed7a76afdf1c5075ac8514f69c24b5
  grade: true
  grade_id: cell-b72fa191a2a82889
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert error_rates.shape[0] >= 4
assert error_rates.shape[1] == 2
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "9e6ca6403522450b3961a28490c165d0", "grade": false, "grade_id": "cell-b546e3375477b608", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## $\clubsuit$ Points bonus : construction du classificateur «une règle» (*One Rule*)

Faites cette partie ou bien passez directement à la conclusion.

:::{admonition} Exercice

1.  Créez votre premier classificateur `OneRule` qui:
    - sélectionne le "bon" attribut (rougeur ou élongation pour le
      problème des pommes/bananes), appelé $G$ (pour *good*). C'est
      l'attribut qui est le plus corrélé (en valeur absolue, toujours
      !)  aux valeurs cibles $y = ± 1$;
    - détermine une valeur seuil (*threshold*);
    - utilise l'attribut `G` et le seuil pour prédire la classe des
      éléments.
            
    Un canevas de la classe `OneRule` est fournit dans le fichier
    `utilities.py`; vous pouvez le compléter ou bien la programmer
    entièrement vous même.
     
    Ce classificateur est-il basé sur les attributs ou sur les exemples?

:::

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: f2d712983eef97347dfb9ee2113dde3a
  grade: false
  grade_id: cell-f300c99cf16ddefb
  locked: true
  schema_version: 3
  solution: false
  task: false
tags: []
---
from utilities import *
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 9f7385d47625cbe5517b632691a023d4
  grade: false
  grade_id: cell-b72b2907842cb7fb
  locked: true
  schema_version: 3
  solution: false
  task: false
---
# Use this code to test your classifier
classifier = OneRule()
classifier.fit(Xtrain, Ytrain) 
Ytrain_predicted = classifier.predict(Xtrain)
Ytest_predicted = classifier.predict(Xtest)
e_tr = error_rate(Ytrain, Ytrain_predicted)
e_te = error_rate(Ytest, Ytest_predicted)
print("Classificateur: One rule")
print("Training error:", e_tr)
print("Test error:", e_te)
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "25a14ef2bbb2dd5f54be98ecdc203f9b", "grade": false, "grade_id": "cell-472a8c23ef803ec9", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition}

2.  Complétez la table `error_rates` avec ce modèle.

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 48da8b079dc5d00daf3aa8b11b312858
  grade: true
  grade_id: cell-7b189e436af168e3
  locked: false
  points: 3
  schema_version: 3
  solution: true
  task: false
---
error_rates.loc["One Rule",:] = [e_tr, e_te]
error_rates
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: d9cc4e307aa25ea9db7429b85c63e193
  grade: true
  grade_id: cell-14c847f98a88a373
  locked: true
  points: 0
  schema_version: 3
  solution: false
  task: false
---
assert error_rates.shape[0] >= 5
assert error_rates.shape[1] == 2
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 9eac0c359d449ad1c0026e38854320af
  grade: false
  grade_id: cell-587a9581023e668d
  locked: true
  schema_version: 3
  solution: false
  task: false
---
# On charge les images
dataset_dir = os.path.join(data.dir, 'ApplesAndBananasSimple')
images = load_images(dataset_dir, "*.png")
# This is what you get as decision boundary.
# The training examples are shown as white circles and the test examples are blue squares.
make_scatter_plot(X, images.apply(transparent_background_filter),
                  [], test_index, 
                  predicted_labels='GroundTruth',
                  feat = classifier.attribute, theta=classifier.theta, axis='square')
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "ed93520471b2cefdd1e9424731afa787", "grade": false, "grade_id": "cell-1b8779ac28a26c59", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition}

3.  Comparez avec ce que vous auriez obtenu en utilisant les deux
    attributs avec le même poids lors de la décision de classe.

:::

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 5f6db3de94731a2fbf4749d55449b82f
  grade: false
  grade_id: cell-d0e8bd2a9132fea6
  locked: true
  schema_version: 3
  solution: false
  task: false
---
make_scatter_plot(X, images.apply(transparent_background_filter),
                  [], test_index, 
                  predicted_labels='GroundTruth',
                  show_diag=True, axis='square')
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "8db48dc81f852cf17c594ed3396acf42", "grade": false, "grade_id": "cell-28e6ef8e4fa12a3c", "locked": true, "schema_version": 3, "solution": false, "task": false}}

### Conclusion

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "a4a32e100329dd2c38e9dabff277d8c5", "grade": false, "grade_id": "cell-1b50f7767c53d39b", "locked": true, "schema_version": 3, "solution": false, "task": false}}

::::{admonition} Exercice

Comparez les taux d'erreur de vos différents classificateurs, lors de
l'entraînement et du test et pour le problème des pommes et des
bananes.

:::{tip} Indications

- Vous commencerez par *observer* les différents taux d'erreurs
  d'entrainement et d'apprentissage de vos classificateurs.
- Vous interpréterez le résultat en expliquant quel est le meilleur
  classificateur pour les pommes/bananes.

:::

::::

```{code-cell} ipython3
print(error_rates)
```

+++ {"deletable": false, "nbgrader": {"cell_type": "markdown", "checksum": "e547d4f47e160f74d5df32a060f61b3a", "grade": true, "grade_id": "cell-a326ec80e8758fb8", "locked": false, "points": 2, "schema_version": 3, "solution": true, "task": false}}

Tout d'abord, on voit que les tableaux repertorient l'erreur d'entraînement et de test selon le modèle de classifications.
En effet, pour le 1 nearest Neighbor, le train error est nul alors que celui du test est de 0.2. Le modèle est interessant car il a un très bon taux de train error mais généralise moins bien pour le test donc leger overfitting.

Pour le Parzen Window, on fait qu'il a train error et un test error de 0.5, ce qui est très mauvais pour le modèle de classification. Comme mentionné au-desuss, cela ne ressemble pas un modèle de prediction mais plus de hasard à cause du sous-apprentissage de l'entrainement et des tests.

Concernant l'arbre de decision et le One Rule, c'est pareil que le 1 Nearest Neighbor avec les très bonnes  perfomances de des données d'entraînements mais une moins bonne généralisation des tests due à un faible sur-apprentissage.

Et enfin, nous avons le Percepton qui a le meilleur résultat avec un taux de train error de 0.0 et un test error de 0.1 donc le meilleur jusque là. Ce modèle a le plus faible taux d'erreur avec notamment le test error de 0.1, et est donc le plus fiable pour la classification de pommes et de bannanes. Il a une très bonne performances pour l'entraînement et la meilleure généralisation pour les tests.
C'est le meilleur classificateur pour les 2 taux d'erreurs !

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "623cd73082a3b65a692ad8b02da7e0ba", "grade": false, "grade_id": "cell-466bf7addb6e465a", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Dans cette feuille vous avez découvert comment utiliser un certain
nombre de classificateurs, voire comment implanter le vôtre, et
comment jouer sur les paramètres de ces classificateurs (par exemple
la tolérance du perceptron ou le nombre de voisins du KNN) pour
essayer d'optimiser leur performance.

Mettez à jour votre rapport et déposez votre travail.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "4dd628447d01a631ccf9f1b84bdd72ae", "grade": false, "grade_id": "cell-466bf7addb6e465b", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Vous êtes maintenant prêts pour revenir à votre [analyse de
données](4_analyse_de_donnees.md) pour mettre en œuvre ces
classificateurs sur votre jeu de données.

**Dans ce premier projet, on vous demande de choisir un seul
classificateur, ainsi que ses paramètres**. Nous verrons dans la
seconde partie de l'UE comment comparer systématiquement les
classificateurs.
