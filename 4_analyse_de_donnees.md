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

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "e877a7f5aa56b85ddc209ecbb2d54445", "grade": false, "grade_id": "cell-3876f910a24fe8a7", "locked": true, "schema_version": 3, "solution": false}, "slideshow": {"slide_type": ""}, "tags": []}

# VI-ME-RÉ-BAR sur vos propres données!

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "69fce3c36f15f567b2208ecd06ac87f9", "grade": false, "grade_id": "cell-3b25fe1716dd8293", "locked": true, "schema_version": 3, "solution": false, "task": false}}

**Instructions**:
- Ci-dessous, mettez ici une description de votre jeu de données: lequel avez vous choisi ?
- Quel est le défi ? Intuitivement quels critères pourraient
  permettre de distinguer les deux classes d'images?

+++ {"deletable": false, "nbgrader": {"cell_type": "markdown", "checksum": "c2f6232958f8a0474f55f80141de80b7", "grade": true, "grade_id": "cell-96350e0e04c4d91f", "locked": false, "points": 3, "schema_version": 3, "solution": true, "task": false}}

Nous avons choisi un jeu de données composé d’images de smileys, réparties en deux classes les smileys gais et les smileys tristes. Le défi est de distinguer les smileys gais des smileys tristes. Intuitivement, la principale différence entre les deux classes est la forme de la bouche : courbée vers le haut pour les smileys joyeux et vers le bas pour les smileys tristes.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 7cf3162b4b4a0509dde50afe71e6ba58
  grade: false
  grade_id: cell-f463237384c14d8c
  locked: true
  schema_version: 3
  solution: false
  task: false
---
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

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "b5bcf7ce90464828259054e0f8d258ce", "grade": false, "grade_id": "cell-1e377d9f288ab8e0", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Étape 1: prétraitement et [VI]sualisation

+++

Le jeu de données consiste en les images suivantes:

**Instruction :** Chargez votre jeu de données comme dans la feuille
`3_jeux_de_donnees.md` de la semaine dernière, en stockant les
images dans la variables `images` et en les affichant.

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 9991b25280d0f128861e5ec4a3e1d385
  grade: false
  grade_id: cell-596455595966feb5
  locked: false
  schema_version: 3
  solution: true
  task: false
---
dataset_dir = os.path.join(data.dir, 'Smiley')
images = load_images(dataset_dir, "*.png")
image_grid(images, titles=images.index)
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: a2d30e6e80157634ba3fbd15f8eab118
  grade: true
  grade_id: cell-d3b1c03f1fbc66c4
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert isinstance(images, pd.Series)
assert len(images) == 20
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "b750e129defcac1b2774f8d55bd0bfa3", "grade": false, "grade_id": "cell-1ad9ea64fc9cfd94", "locked": true, "schema_version": 3, "solution": false, "task": false}}

### Prétraitement

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "714373fb2541b5c66e981259f6752be5", "grade": false, "grade_id": "cell-c5eeea84f126a6a9", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Les données sont très souvent prétraitées c'est-à-dire **résumées
selon différentes caractéristiques** : chaque élément du jeu de
données est décrit par un ensemble [**d'attributs**](https://en.wikipedia.org/wiki/Feature_(machine_learning))
-- propriétés ou caractéristiques mesurables de cet élément ; pour un
animal, cela peut être sa taille, sa température corporelle, etc.

C'est également le cas dans notre jeu de données : une image est
décrite par le couleur de chacun de ses pixels. Cependant les pixels
sont trop nombreux pour nos besoins. Nous voulons comme la semaine
dernière les remplacer par quelques attributs mesurant quelques
propriétés essentielles de l'image, comme sa couleur ou sa forme
moyenne: ce sont les données prétraitées.

La semaine dernière, les données prétraitées vous ont été fournies
pour les pommes et les bananes.
Cette semaine, grâce aux trois feuilles précédentes, vous avez les
outils et connaissances nécessaires pour effectuer le prétraitement 
directement vous-même:

- la feuille de rappel sur la [gestion de tableaux](1_tableaux.md); 
- la feuille sur le [traitement des images](2_images.md);
- la feuille sur l'[extraction d'attributs](3_extraction_d_attributs.md).

Pour commencer, la table ci-dessous contient les attributs `redness`
et `elongation` -- tels que vous les avez défini dans la feuille
[extraction d'attributs](3_extraction_d_attributs.md) -- appliqués à
votre jeu de données :

```{code-cell} ipython3
---
code_folding: []
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: da7c94c2617d9e0303be67f6842c8ca9
  grade: false
  grade_id: cell-4b826c34cfe02997
  locked: true
  schema_version: 3
  solution: false
  task: false
tags: []
---
df = pd.DataFrame({
        'redness':    images.apply(redness),
        'elongation': images.apply(elongation),
        'class':      images.index.map(lambda name: 1 if name[0] == 'a' else -1),
})
df
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "6e0baac282309fa452529502cd850a54", "grade": false, "grade_id": "cell-3ea685b93ca235c7", "locked": true, "schema_version": 3, "solution": false, "task": false}}

::::{admonition} Exercice

1.  Implémentez dans `utilities.py` au moins deux nouveaux attributs
    adaptés à votre jeu de données. Si vous en avez besoin pour les
    tests par exemple, vous pouvez utiliser les cellules ci-dessous
    voire en créer de nouvelles.

    :::{tip} Indications
     
    Vous pouvez par exemple vous inspirer
    - des attributes existants comme `redness`;
    - des exemples donnés dans le cours: *matched filter*, analyse en
      composantes principales (PCA).
     
    :::

::::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 17beaba12b726af9ffd42295fa27181c
  grade: false
  grade_id: cell-90320016ffc3a6b2
  locked: false
  schema_version: 3
  solution: true
  task: false
---
from numbers import Number

def grayscale(img: Image.Image) -> np.ndarray:
    """Return image in gray scale"""
    return np.mean(np.array(img)[:, :, :3], axis=2)

class MatchedFilter:
    ''' Matched filter class to extract a feature from a template'''
    def __init__(self, examples: Iterable[Image.Image]):
        ''' Create the template for a matched filter; use only grayscale'''
        # Compute the average of all images after conversion to grayscale
        M = np.mean([grayscale(img)
                     for img in examples], axis=0)
        # Standardize
        self.template = (M - M.mean()) / M.std()

    def show(self):
        """Show the template"""
        fig = Figure(figsize=(3, 3))
        ax = fig.add_subplot()
        ax.imshow(self.template, cmap='gray')
        return fig

    def match(self, img: Image.Image) -> Number:
        '''Extract the matched filter value for a PIL image.'''
        # Convert to grayscale and standardize
        M = grayscale(img)
        M = (M - M.mean()) / M.std()
        # Compute scalar product with the template
        # This reinforce black and white if they agree
        return np.mean(np.multiply(self.template, M))
```

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: b3f1ac26ce9f9faa1dacaa69c394f80b
  grade: false
  grade_id: cell-90320016ffc3a6b3
  locked: false
  schema_version: 3
  solution: true
  task: false
---
#Comment utiliser MatchFilter ?

# on match avec les 10 premières images : celles qui sourient
filtre_sourire = MatchedFilter(images[:10]) 

#on regarde le filtre moyen
display(filtre_sourire.show())

# on calcule la correlation moyenne entre une figure à tester et le filtre moyen
print("MATCH SOURIRE \n Pour un sourire :", filtre_sourire.match(images[9]))
print("Pour un smiley triste :" , filtre_sourire.match(images[19]))

# il faudrait encore calculer la corrélation moyenne avec le filtre moyen des smileys tristes
# puis comparer les ratios pour savoir à quelle classe appartient notre smiley !!


# on match avec les 10 dernieres images : celles qui ne sourient pas
filtre_triste = MatchedFilter(images[10:])
display(filtre_triste.show())

# on calcule la correlation moyenne entre une figure à tester et le filtre moyen
print("MATCH TRISTE \n Pour un sourire :", filtre_triste.match(images[9]))
print("Pour un smiley triste :" , filtre_triste.match(images[19]))

# il faudrait encore calculer la corrélation moyenne avec le filtre moyen des smileys tristes
# puis comparer les ratios pour savoir à quelle classe appartient notre smiley !!



# Ensuite, pour determiner le meilleur filtre/ match, on compare la valeur absolue des diff entre les matchs pour un sourire et un smiley triste;
# Et,on regarde quelle match a la plus grande et meilleure difference ce qui différencie bien une corrélation et une moins bonne correlation.

# Ici, le meilleur Match est le match Sourire car on arrive à bien distinguer les valeurs.
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "9e3c2c5bccc147dcdea0e47a3a31e1ec", "grade": false, "grade_id": "cell-4a701722d7649d16", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition}

2.  Comment avez-vous choisis ces attributs ? Quelle était votre motivation ?

:::

+++ {"deletable": false, "nbgrader": {"cell_type": "markdown", "checksum": "d0eb7ea9bb20d04ff21f9e386a533abd", "grade": true, "grade_id": "cell-91da4c6a22145c84", "locked": false, "points": 2, "schema_version": 3, "solution": true, "task": false}}

Pour la première attribut qui correspond à notre fonction Position_bouche, on a pensé que un sourire etait placé plus haut sur le visage que celui sans sourire donc on a voulu isoler selon les pixels noirs du sourire. On a appliqué un filtre foreground filter, puis on  a coupé l'image en 2 pour conserver la partie sourire uniquement et ses pixels. Et après on fait la moyenne des positions dans l'images et on s'attendait à avoir un résultat different selon le sourire ou non.

Pour le second attribut, on a vu qu'avec une fonction classique cela ne marchait pas donc on a utilisé une partie du cours qui est le MatchFilter oû le but était de recuperer les images selon leurs sourires ou non. Puis, on regarde le filtre moyen selon si c'est un sourire ou non et on a par la suite calculer la correlation moyenne entre une figure à tester et le filtre moyen du sourire et sans sourire.

Ensuite, pour determiner le meilleur filtre/ match, on compare la valeur absolue des diff entre les matchs pour un sourire et un smiley triste.
Et, on regarde quel match a la plus grande et meilleure difference, ce qui va donc différencier bien une corrélation et une moins bonne correlation selon le sourire ou non.

 Ici, le meilleur Match est le match Sourire car on arrive à bien distinguer les valeurs entre 0.80 qui est proche de 1 pour un sourire, donc une potentielle corrélation et celle la plus éloignée 0.64 pour un smiley triste.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "3f6bf8d2092971f47957b93499987d73", "grade": false, "grade_id": "cell-7978fcc57a3231fd", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition}

3.  Affichez le code de vos nouveaux attributs ici, en utilisant `show_source`.

:::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 3c7419cdb72975c74d0c6929a94102f3
  grade: true
  grade_id: cell-431dcb3869e672c0
  locked: false
  points: 3
  schema_version: 3
  solution: true
  task: false
---
show_source(position_bouche)
```

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: f80923385999bb694c1887bded7f0330
  grade: true
  grade_id: cell-0bb9313d2345f7a7
  locked: false
  points: 3
  schema_version: 3
  solution: true
  task: false
---
import importlib
import utilities
importlib.reload(utilities)

from utilities import MatchedFilter
show_source(MatchedFilter)
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "3874148c83a81ca56d6aae3455a79932", "grade": false, "grade_id": "cell-d144e561c7a8d7d9", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition}

4.  Ajoutez une colonne par attribut dans la table `df`, en conservant
    les précédents.

:::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: fc7c13f57edacc111f0be320d75eaf7c
  grade: false
  grade_id: cell-d933a673c19c7e6d
  locked: false
  schema_version: 3
  solution: true
  task: false
---
import importlib
import utilities
importlib.reload(utilities)

from utilities import MatchedFilter

filtre_sourire = MatchedFilter(images[:10])
filtre_triste = MatchedFilter(images[10:])

df["position_bouche"]=images.apply(position_bouche)
print(df["position_bouche"])
df["filtre_sourire"]=images.apply(lambda img:filtre_sourire.match(img))
df["filtre_triste"]=images.apply(lambda img: filtre_triste.match(img))
df.head(n=20)
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "bb480abd9baac97518a69b7de64cf014", "grade": false, "grade_id": "cell-d635e7502cb91b2a", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Vérifications:
- la table d'origine est préservée:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 00cf3c65f455842623627fceda673e2d
  grade: true
  grade_id: cell-105a1d4f853b203c
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert len(df[df['class'] ==  1]) == 10
assert len(df[df['class'] == -1]) == 10
assert 'redness' in df.columns
assert 'elongation' in df.columns
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "450cedbf2975206641aa60b1b396769d", "grade": false, "grade_id": "cell-86b1db13ae3622b1", "locked": true, "schema_version": 3, "solution": false, "task": false}}

- Nouveaux attributs:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: b087dcf13b7252daecf1d1f8e2450318
  grade: true
  grade_id: cell-d8f0986d0b430798
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert len(df.columns) > 3, "Ajoutez au moins un attribut!"
assert df.notna().all(axis=None), "Valeurs manquantes!"
for attribute in df.columns[3:]:
    assert pd.api.types.is_numeric_dtype(df[attribute]), \
        f"L'attribut {attribute} n'est pas numérique"
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: acd89c5343b85c78b5bc14691087c6be
  grade: true
  grade_id: cell-03e40d6a322dfc9d
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert len(df.columns) > 4, "Gagnez un point en ajoutant un autre attribut"
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "af386a77ecaac605cc658e83a685616a", "grade": false, "grade_id": "cell-592f7c21def71b06", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition} Exercice

5.  Standardisez les colonnes à l'exception de la colonne `class`,
    afin de calculer les corrélations entre colonnes.

:::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 39efeffa4c52eea4c717d8bd853ec9d4
  grade: false
  grade_id: cell-0c29581ba1da5a27
  locked: false
  schema_version: 3
  solution: true
  task: false
---
dfstd = (df-df.mean()) / df.std()
dfstd['class'] = df['class']
dfstd
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "11583edd1f5d181027fac76ecf2e729b", "grade": false, "grade_id": "cell-feea0a235f81712c", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Vérifions :

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 2e045804a7ee3835b8ebd6c668d16562
  grade: false
  grade_id: cell-69e2c8c203efb549
  locked: true
  schema_version: 3
  solution: false
  task: false
---
dfstd.describe()
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: c46020ebc9892ac98e0a366de26fbc7e
  grade: true
  grade_id: cell-b6120056f2331c33
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert dfstd.shape == df.shape
assert dfstd.index.equals(df.index)
assert dfstd.columns.equals(df.columns)
assert (abs(dfstd.mean()) < 0.01).all()
assert (abs(dfstd.std() - 1) < 0.1).all()
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "720b9082c215b4223679b9f77a642dd3", "grade": false, "grade_id": "cell-16a95948fd5c0ef3", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Le prétraitement est terminé!

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "90a4b4e0ea8602608efc8be5f4b76809", "grade": false, "grade_id": "cell-043c3e7edafa0af9", "locked": true, "schema_version": 3, "solution": false, "task": false}}

### Visualisation

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "aa3b49eceaca27f8cdd72e1baa086ad5", "grade": false, "grade_id": "cell-eb183dfd2fb60a40", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition} Exercice

1.  Extrayez quelques statistiques de base du tableau de données:

:::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 0881ec64fe676b605aaa6373540d2fb4
  grade: false
  grade_id: cell-5adf965bf26113e8
  locked: false
  schema_version: 3
  solution: true
  task: false
---
dfstd.describe(include="all")
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "b1768a1560d41784ba7e7d3fd9a90c06", "grade": false, "grade_id": "cell-6c7b07fdc56a1970", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition}

2.  Visualisez le tableau de données sous forme de carte de chaleur (*heat map*):

:::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: bfada635f889c5cf06b033442e83ad70
  grade: false
  grade_id: cell-59b086b9a7351acb
  locked: false
  schema_version: 3
  solution: true
  task: false
---
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.heatmap(dfstd, annot=True, cmap='coolwarm')  
plt.title("Heatmap des valeurs du DataFrame")
plt.show()
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "837594d7e5fda9f10c50dc4fff38bf86", "grade": false, "grade_id": "cell-dee09fc8d9185846", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition}

3.  Visualisez de même sa matrice de corrélation:

:::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 2ef96fc103a66cc7c64ed4d219ce1561
  grade: false
  grade_id: cell-5d6f2f8188882c92
  locked: false
  schema_version: 3
  solution: true
  task: false
---
dfstd_corr = dfstd.corr(numeric_only=True)
dfstd_corr.style.background_gradient(cmap='coolwarm', axis=None)
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "f7e26c8fe726d89f14ad7b66b5295983", "grade": false, "grade_id": "cell-6e71eda9745ba384", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition}

4.  Affichez le nuage de points (*scatter plot*) pour toutes les paires d'attributs:

:::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 729d2686cf059a436e43746804a32c7f
  grade: false
  grade_id: cell-10bd824917033e6a
  locked: false
  schema_version: 3
  solution: true
  task: false
---
import seaborn as sns
import matplotlib.pyplot as plt
sns.pairplot(dfstd, hue='class', vars=['position_bouche', 'filtre_sourire','filtre_triste'],palette="Set2")
plt.show()
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "7cfbdec1f3ef8d91db00f74c964155a1", "grade": false, "grade_id": "cell-bca3d5b71feb6ff1", "locked": true, "schema_version": 3, "solution": false, "task": false}}

### Observations

:::{admonition} Exercice

Décrivez ici vos observations: corrélations apparentes
ou pas, interprétation de ces corrélations à partir du nuage de
points, etc. Est-ce que les attributs choisis semblent suffisants?
Quel attribut semble le plus discriminant? Est-ce qu'un seul d'entre
eux suffirait?

:::

+++ {"deletable": false, "nbgrader": {"cell_type": "markdown", "checksum": "6f529903b12f2180d2a775daba172e25", "grade": true, "grade_id": "cell-e22718dde2cfd4ba", "locked": false, "points": 4, "schema_version": 3, "solution": true, "task": false}}

Lorsqu'on regarde les observations par rapport à la variable class, on voit d'abord grâce à la matrice de corrélation que les attributs redness et elongation ont très peu de corrélation avec la variable class. Ensuite, quand on regarde le nuage de point avec le filtre_sourire et le filtre_triste, il y a bien une corrélation positive  entre eux avec leurs points qui vont vers le haut et sont bien séparés entre la classe 1 et -1. Toutefois quand on regarde avec position_bouche, il n'y a pas de corrélation visible ou elle est faible car lorsqu'on compare avec les 2 filtres, les points sont mélangées, dispersés, et ne montent pas et ne descendent pas.

Alors, certains attributs sont insuffisants comme redness et elongation ( matrice de corrélation). Puis, il y a aussi la position bouche qui présente une corrélation faible avec les autres variables tandis que les filtre_sourire et filtre_triste sont utiles dans la corrélation et semblent suffire.

Quand on regarde de plus près le filtre_sourire et le filtre_triste, on remarque que l'attribut qui semble le plus discriminant donc qui sépare le mieux les class ( 1 et -1), est bien le filtre_sourire car il a une plus différence de valeur entre le max de class 1 et le max de class -1 que le filtre_triste.

Un attribut seul semble ne pas être suffisant pour établir la séparation entre les class ( 1 et -1) car on voit quand même que leurs points ne sont pas totalement séparés et pas vraiment exacts donc cela ne permet pas de classifier parfaitement toutes les informations , données.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "780219ca7ddda552ea13fa1fd6609265", "grade": false, "grade_id": "cell-2668dce82b589f34", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Étape 2: [ME]sure de performance (*[ME]tric*)

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "fca79a2271986cdbbefd31158166a6fb", "grade": false, "grade_id": "cell-fe6ef77774bf777c", "locked": true, "schema_version": 3, "solution": false, "task": false}}

### Partition (*split*) du jeu de données en ensemble d'entraînement et ensemble de test

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "bed56e322ddbec31973f30495c836de6", "grade": false, "grade_id": "cell-1a09d1e1733ada10", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition} Exercice

1.  Extrayez, depuis `dfstd`, les deux attributs choisis dans `X` et
    la vérité terrain dans `Y`:

:::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 8e0f37996838a9eed59b6301330faa6e
  grade: false
  grade_id: cell-fb5cd75f3de3a8a2
  locked: false
  schema_version: 3
  solution: true
  task: false
---
# On a pris position_bouche et filtre_sourire car filtre_triste ressemble au filtre_sourire et cela serait redondant si on prennait les deux.
X = dfstd[['position_bouche', 'filtre_sourire']]
Y = dfstd['class']
```

Vérifions:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: cac3960f3b06171eac77d75b29d25c2f
  grade: true
  grade_id: cell-666625af65184ae8
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert isinstance(X, pd.DataFrame), "X n'est pas une table Pandas"
assert X.shape == (20,2), "X n'est pas de la bonne taille"
assert set(X.columns) != {'redness', 'elongation'}
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 5c28d178e0d6b3777990f25d2adfa7aa
  grade: true
  grade_id: cell-6155db153be32033
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert 'redness' not in X.columns and 'elongation' not in X.columns, \
   "Pour un point de plus: ne réutilisez ni la rougeur, ni l'élongation"
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "6734a8b64d128e1a463014b05ba249fc", "grade": false, "grade_id": "cell-672066b540b7e27b", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition}

2.  Maintenant partitionnez l'index des images en ensemble
    d'entraînement (`train_index`) et ensemble de test
    (`test_index`). Récupérez les attributs et classes de vos images
    selon l'ensemble d'entraînement `(Xtrain, Ytrain)` et celui de
    test `(Xtest, Ytest)`.

:::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 8e4d6c9e5e50657996187616eb9b0173
  grade: false
  grade_id: cell-240f317e24d0e8c5
  locked: false
  schema_version: 3
  solution: true
  task: false
---
from sklearn.model_selection import train_test_split
import numpy as np
train_index, test_index = split_data(X, Y, seed=0)
train_index, test_index



Xtrain = X.iloc[train_index]
Xtest  = X.iloc[test_index]

Ytrain = Y.iloc[train_index]
Ytest  = Y.iloc[test_index]
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 543dd26f1d5b2db6c2810087c5dabde0
  grade: true
  grade_id: cell-3be096fc97970fbc
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert train_index.shape == test_index.shape
assert list(sorted(np.concatenate([train_index, test_index]))) == list(range(20))

assert Xtest.shape == Xtrain.shape
assert pd.concat([Xtest, Xtrain]).sort_index().equals(X.sort_index())

assert Ytest.shape == Ytrain.shape
assert pd.concat([Ytest, Ytrain]).sort_index().equals(Y.sort_index())
assert Ytest.value_counts().sort_index().equals(Ytrain.value_counts().sort_index())
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "9b1e0676f8068beefad0d275e6cb470f", "grade": false, "grade_id": "cell-50c7b65a31fd47cb", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition}

3.  Affichez les images qui serviront à entraîner notre modèle de
    prédiction (*predictive model*):

:::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: c466d1664ce5b0e21a60fea5e3a10288
  grade: false
  grade_id: cell-ad5ca9b40a1f2cd1
  locked: false
  schema_version: 3
  solution: true
  task: false
---
image_grid(images.iloc[train_index], titles=train_index)
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "e78c977a0f27717a1d8f8e7b7b5cf7cf", "grade": false, "grade_id": "cell-031b7382abe186ef", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition} 

4.  Affichez celles qui permettent de le tester et d'évaluer sa
    performance:

:::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: c8fecb49712cdcc05789e2066e173a2f
  grade: false
  grade_id: cell-1f3414a9f879a9d1
  locked: false
  schema_version: 3
  solution: true
  task: false
---
image_grid(images.iloc[test_index], titles=test_index)
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "2c7d7e6ea31490cfb96c3004294b4dee", "grade": false, "grade_id": "cell-e44d2840e7481ec1", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition}

5.  Représentez les images sous forme de nuage de points en fonction
    de leurs attributs:

:::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: f0b3f94b32e945753930d8b8d1b948e0
  grade: true
  grade_id: cell-c7dc96827c21b4b9
  locked: false
  points: 1
  schema_version: 3
  solution: true
  task: false
---

make_scatter_plot(dfstd, images, train_index, test_index, axis='square')
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "afd8382f219297572fbc59a91a75e80f", "grade": false, "grade_id": "cell-ef6ffea3c9345a6f", "locked": true, "schema_version": 3, "solution": false, "task": false}}

### Taux d'erreur

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "90c12208eda43e282d9820f338a8b52e", "grade": false, "grade_id": "cell-2edc6abcf3a72dd2", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Pour mesurer les performances de la classification, nous utiliserons
comme la semaine dernière le taux d'erreur comme métrique, d'une part
sur l'ensemble d'entraînement, d'autre part sur l'ensemble de test.

:::{admonition} Exercice

Implémentez la fonction `error_rate` dans
[utilities.py](utilities.py). Pour vérifier que c'est correctement
fait, nous affichons son code ci-dessous:

:::

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 19048026419c75b7d2b389917743506b
  grade: false
  grade_id: cell-baa5e37a60edad22
  locked: true
  schema_version: 3
  solution: false
  task: false
---
show_source(error_rate)
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "0aad688914be7e65788713978ac3c2a8", "grade": false, "grade_id": "cell-2831ca6c9a3bfce5", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Étape 3: [RE]férence (*base line*)

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "460a70846edc8dd32952b00dbe109551", "grade": false, "grade_id": "cell-9876b02ba8d2de55", "locked": true, "schema_version": 3, "solution": false, "task": false}}

### Classificateur

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "e8f454b46d210986ca6b70502fd58575", "grade": false, "grade_id": "cell-5f7be836c3e06143", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition} Consignes

- En Semaine 4: faites la suite de cette feuille avec l'algorithme du
  plus proche voisin, comme en Semaine 3.

- En Semaine 5: faites d'abord la feuille sur les
  [classificateurs](5_classificateurs.md) puis faites la suite de
  cette feuille avec votre propre classificateur, en notant au
  préalable votre choix de classificateur ici:

:::

:::{admonition} Exercice

Quel classificateur avez-vous choisit en semaine 5 ? Pourquoi
avez-vous choisis celui-ci ?

:::

+++ {"deletable": false, "nbgrader": {"cell_type": "markdown", "checksum": "93394cf4d1361a6928672f6bec5edec3", "grade": true, "grade_id": "cell-014e08189e3a6014", "locked": false, "points": 2, "schema_version": 3, "solution": true, "task": false}}

Nous avons choisi le classificateur OneRule car il est simple et adapté à un petit jeu de données avec peu d’attributs. Il permet de sélectionner automatiquement l’attribut le plus discriminant.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "6c618535ab7707c83f9a37d5ec9f4eea", "grade": false, "grade_id": "cell-f541bcd7f0f3912d", "locked": true, "schema_version": 3, "solution": false, "task": false}}

::::{admonition} Exercice

1.  Ci-dessous, définissez puis entraînez votre classificateur sur
    l'ensemble d'entraînement.

    :::{admonition} Indication
     
    Si vous avez besoin de code supplémentaire pour cela, mettez-le dans
    [utilities.py](utilities.py).
     
    :::

::::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: cb4d4d2d1a75555cfb83c78f500a09d4
  grade: false
  grade_id: cell-85205b5012588319
  locked: false
  schema_version: 3
  solution: true
  task: false
---
from utilities import OneRule, error_rate

clf = OneRule()
clf.fit(Xtrain, Ytrain)
Ypred = clf.predict(Xtest)
e_te = error_rate(Ytest, Ypred)
print("Test error rate:", e_te)
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "2fe78f01c9fc49705d02ef8b4f96faef", "grade": false, "grade_id": "cell-991d8893ddaefe2b", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition}

2.  Calculez les prédictions sur l'ensemble d'entraînement et
    l'ensemble de test, ainsi que les taux d'erreur dans les deux cas:

:::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 1a7b1aee6a3e1209597c820dc1c71516
  grade: false
  grade_id: cell-85205b5012588320
  locked: false
  schema_version: 3
  solution: true
  task: false
---
Ytrain_predicted = clf.predict(Xtrain)
e_tr = error_rate(Ytrain, Ytrain_predicted)
Ytest_predicted = clf.predict(Xtest)
e_te = error_rate(Ytest, Ytest_predicted)
print("OneRule Classifier Performance:")
print("Training error:", e_tr)
print("Test error:", e_te)
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 3eb2e601b91778183a2a03138ce8359a
  grade: true
  grade_id: cell-195ba103a7ccc55b
  locked: true
  points: 3
  schema_version: 3
  solution: false
  task: false
tags: []
---
assert Ytrain_predicted.shape == Ytrain.shape
assert Ytest_predicted.shape == Ytest.shape
assert 0 <= e_tr and e_tr <= 1
assert 0 <= e_te and e_te <= 1
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "fae208e6bd19f0670dd8df95f6d64171", "grade": false, "grade_id": "cell-139252fc350603b2", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Visualisons les prédictions obtenues:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: d52aa128366c4fd41fdcf88b6103e580
  grade: false
  grade_id: cell-fdaa23f990c0b172
  locked: true
  schema_version: 3
  solution: false
  task: false
---
# The training examples are shown as white circles and the test examples are black squares.
# The predictions made are shown as letters in the black squares.
make_scatter_plot(X, images.apply(transparent_background_filter),
                  train_index, test_index, 
                  predicted_labels=Ytest_predicted, axis='square')
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "00fb56afb030c89b52f77facddd94ba1", "grade": false, "grade_id": "cell-b0226451f00b5833", "locked": true, "schema_version": 3, "solution": false, "task": false}}

### Interprétation

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "00f090215ba8b516f6aa8b7af0fa09db", "grade": false, "grade_id": "cell-b0226451f00b5834", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition} Exercice

Quelle est la performance des prédictions pour le jeu d'entraînement
et pour le jeu de test ? Celle-ci vous parait-elle optimate ? Donnez
enfin une interprétation des résultats, en expliquant pourquoi votre
performance est bonne ou pas. Avez vous une première intuition de
comment l'améliorer ?

:::

+++ {"deletable": false, "nbgrader": {"cell_type": "markdown", "checksum": "ef89d849ecc26d3c154c01574d8fc334", "grade": true, "grade_id": "cell-3587c106c4f95899", "locked": false, "points": 5, "schema_version": 3, "solution": true, "task": false}}

La performation des prédictions pour le train error est de 0.2 et pour le test error, il est de 0.6. Cela parait pas très optimal car le train error n'est pas de 0 donc il n'est pas parfait mais en plus de cela le taux d'erreur de test est de 0.6 ce qui montre il généralise plutot mal les nouvelles données ce qui ressemble au overfitting.

Ces résultats pourrait s'expliquer par le fait que le modèle OneRule est trop simpliste , il utilise position_bouche mais il prend aussi en compte les autres attributs avec filtre_sourire. Et cela peut aussi s'expliquer par les résultats qu'on avait eu pour ce jeu de données avec nos nouveaux attributs.

Pour l'améliorer on pourrait utiliser un autre classificateur comme l'arbre de decision qui avait l'air intéressant avec le True et False ou le KNN. Une autre manière serait d'avoir encore plus de données ( loi des grands nombres) qui permettrait eventuellement de réduire le taux d'erreur d'entrainements et de tests.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "8a2a785561a621cbac2dc3ca33e6a4ac", "grade": false, "grade_id": "cell-5539fbbf5565fb1b", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Étape 4: [BAR]res d'erreur (*error bar*)

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "715345f6a6cae5dc4563f6ee707623ad", "grade": false, "grade_id": "cell-5539fbbf5565fb1c", "locked": true, "schema_version": 3, "solution": false, "task": false}}

### Barre d'erreur 1-sigma

:::{admonition} Exercice

Comme première estimation de la barre d'erreur, calculez la barre
d'erreur 1-sigma pour le taux d'erreur `e_te`:

:::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: a41cc34ca674ef499973ee023b1d1e61
  grade: false
  grade_id: cell-40a54824a74c8fdc
  locked: false
  schema_version: 3
  solution: true
  task: false
tags: []
---
n_te=len(Ytest) # correspond au nombre de tests effectués !
sigma=np.sqrt((e_te *(1-e_te))/n_te) # On ajoute le np sinon ca renvoie une erreur

print("TEST SET ERROR RATE: {0:.2f}".format(e_te))
print("TEST SET STANDARD ERROR: {0:.2f}".format(sigma))
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: fc40b782c4fe7b984a8fa034200adfac
  grade: true
  grade_id: cell-58772f70bb5eccfd
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert n_te + 5 == 3**2 + len(Ytest) - 2**2
assert round(sigma**2,3) == round((e_te/n_te - e_te**2/n_te),3)
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "586d48f4fdf3853c340c3eb8ac0aaf5c", "grade": false, "grade_id": "cell-209765e9c10f8f32", "locked": true, "schema_version": 3, "solution": false, "task": false}}

### Barre d'erreur par validation croisée (Cross-Validation)

Nous calculons maintenant une autre estimation de la barre d'erreur en
répétant l'évaluation de performance pour de multiples partitions
entre ensemble d'entraînement et ensemble de test : on parle de validation croisée répétée.


:::{admonition} Exercice

Complétez le code ci-dessous pour faire de la validation croisée répétée.

:::

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 99be4a5c9bf2828fc8365de559a76353
  grade: true
  grade_id: cell-9b669928087e60b0
  locked: false
  points: 3
  schema_version: 3
  solution: true
  task: false
---
#Soit n_te le nombre de validations croisées qu'on fait
n_te = 10
# on définit un ensemble de 10 splits de notre jeux de données
SSS = StratifiedShuffleSplit(n_splits=n_te, test_size=0.5, random_state=5)

# Initialisation de l'ensemble des erreurs pour les n_te itérations de validation croisée
# np.zeros crée un tableau rempli de zéros de taille [n_te, 1] 
# (une colonne pour chaque itération)
E = np.zeros([n_te, 1])

# Boucle sur les splits générés par la validation croisée
# enumerate renvoie à la fois l'indice (i) 
#et les indices des échantillons pour le split actuel
for i, (train_index, test_index) in enumerate(SSS.split(X, Y)):
    # Affichage des indices des données utilisées pour l'entraînement et le test
    print("TRAIN:", train_index, "TEST:", test_index)
    
    # Séparation des données d'entraînement et de test selon les indices générés
    Xtrain, Xtest = X.iloc[train_index], X.iloc[test_index]
    Ytrain, Ytest = Y.iloc[train_index], Y.iloc[test_index]
    
    # Entraînement du modèle sur les données d'entraînement
    # La méthode fit permet d'ajuster le modèle aux données
    clf = OneRule()
    clf.fit(Xtrain, Ytrain)
    Ypred = clf.predict(Xtest)
    E[i] = error_rate(Ytest, Ypred)

    # On a du modifié le programme car cela utilisait le KNN au lieu de ce qu'on voulait nous le OneRule

    
# Calcul de la moyenne des erreurs sur tous les splits
# np.mean calcule la moyenne des valeurs dans un tableau
e_te_ave = np.mean(E)

# Affichage de la moyenne des taux d'erreur (arrondie à 2 chiffres après la virgule)
print("\n\nCV ERROR RATE: {0:.2f}".format(e_te_ave))

# Calcul de l'écart-type des taux d'erreur
# np.std calcule la dispersion des valeurs autour de la moyenne
print("CV STANDARD DEVIATION: {0:.2f}".format(np.std(E)))

# Calcul de l'erreur standard sur l'ensemble de test
# np.sqrt calcule la racine carrée
sigma = np.sqrt(e_te_ave * (1 - e_te_ave) / n_te)

# Affichage de l'erreur standard sur l'ensemble de test
print("TEST SET STANDARD ERROR (for comparison): {0:.2f}".format(sigma))
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "ce4a94b062b9848806e25c15e4dec98b", "grade": false, "grade_id": "cell-df1f1b0b05e548d4", "locked": true, "schema_version": 3, "solution": false, "task": false}}

### Conclusion

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "1b72d1133a026b82d37c50d1637b7b7a", "grade": false, "grade_id": "cell-df1f1b0b05e548d6", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition} Exercice

Faites ci-dessous une synthèse des performances obtenues, tout d'abord
avec votre référence (*baseline*), puis avec les variantes que vous
aurez explorées en changeant d'attributs et de classificateur. Vous
pouvez par exemple présenter votre réponse sous forme d'un tableau.
Puis vous commenterez sur la difficulté du problème ainsi que les
pistes possibles pour obtenir de meilleures performances ou pour
généraliser le problème.

:::

+++ {"deletable": false, "nbgrader": {"cell_type": "markdown", "checksum": "989bef7b6f89f347f62e28548439cfad", "grade": true, "grade_id": "cell-8676a3839d9b5559", "locked": false, "points": 5, "schema_version": 3, "solution": true, "task": false}}

Pour nos performances, au tout début avec seulement les attributs 'redness et elongation", cela ne marchait pas du tout car il n'y avait aucune corrélation entre les 2 types de smileys. En effet, ces attributs ne nous permettent pas de classifier les 2 attributs différents entre le smiley content et triste.
Alors on a injecté 2 nouveaux attributs qui sont la position de la bouche et le filtre_sourire pour nous aider à classifier les attributs. Pour position bouche, cela ne nous avait pas beaucoup aidé mais par contre c'etait mieux avec le filtre sourire bien que c'était lon d'être parfait.
Ensuite, on a tenté d'interpreter nos résultats obtenues en comparant différents attributs et en choissant le meilleur.

Pour continuer, on s'est servi de ce qu'on a eu pour mesurer nos performances en faisant des modèles de prédictions pour l'entraîenment et le test. Avant de tester les différents classificateurs, on a implémenté une fonction error_rate afin de calculer le taux d'erreur d'entraîenment et de test très important pour comparer les différents classifcateurs et determiner lequel est le meilleur. Après avoir fait les démarches de la fueille 5 sur les classifcateurs, on est arrivé à la conclusion que le meilleur classificateur en général ( pommes, bananes) est le Percepton qui a le meilleur résultat avec le plus faible taux d’erreur avec notamment le test error de 0.1, et est donc le plus fiable pour la classification de pommes et de bannanes. 

Toutefois, pour notre jeu de données, on a pris le OneRule pour tester un nouveau classificateur mais aussi car il nous semblait pertinent pour les smileys ( et aussi pour les points bonus!!) et au final , cela n'a pas très bien fonctionné mais ce n'est pas grave car on pense que cela ne restait pas catastrophique dans une mesure.

Concernant les diffcultés, la chose la plus difficile était de vraiment comprendre et d'interpreter les classficateurs car il y avait énormement d'informations et surtout parfois en anglais ( documentation) donc on a du faire quelques recherche sur internet pour mieux comprendre les choses. 
Pour avoir de meilleurs performances, on peut soit utiliser un meilleur classificateur tel que le KNN ou l'arbre de decision ou avoir plus de données sous notre main en utilisant le principe de la loi des grands nombres afin de réduire le taux d'erreur eventuellement.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "22b48b3dee5f8564c709f3616c536053", "grade": false, "grade_id": "cell-df1f1b0b05e548d5", "locked": true, "schema_version": 3, "solution": false, "task": false}}

:::{admonition} Exercice

Complétez votre [rapport](index.md).

:::
