##############################################################################
# Imports

from numbers import Number
from typing import Iterable, Union, Any
import warnings

from PIL import Image  # type: ignore
import numpy as np
import pandas as pd  # type: ignore

from sklearn.model_selection import StratifiedShuffleSplit  # type: ignore

from matplotlib.offsetbox import OffsetImage, AnnotationBbox  # type: ignore
from matplotlib.figure import Figure  # type: ignore
from matplotlib.axes import Axes  # type: ignore
from matplotlib.colors import LinearSegmentedColormap  # type: ignore


warnings.simplefilter(action="ignore", category=FutureWarning)

##############################################################################
# Traitement d'images

black_red_cmap = LinearSegmentedColormap.from_list(
    "black_red_cmap", ["black", "red"]
)
black_green_cmap = LinearSegmentedColormap.from_list(
    "black_green_cmap", ["black", "green"]
)
black_blue_cmap = LinearSegmentedColormap.from_list(
    "black_blue_cmap", ["black", "blue"]
)


def show_color_channels(img: Image.Image) -> Figure:
    """
    Return a figure displaying the image together with its red,
    green, and blue layers
    """
    from matplotlib.colors import LinearSegmentedColormap

    M = np.array(img)

    black_red_cmap = LinearSegmentedColormap.from_list(
        "black_red_cmap", ["black", "red"]
    )
    black_green_cmap = LinearSegmentedColormap.from_list(
        "black_green_cmap", ["black", "green"]
    )
    black_blue_cmap = LinearSegmentedColormap.from_list(
        "black_blue_cmap", ["black", "blue"]
    )

    fig = Figure(figsize=(30, 5))
    subplot, subplotr, subplotg, subplotb = fig.subplots(1, 4)

    subplot.imshow(M)
    imgr = subplotr.imshow(M[:, :, 0], cmap=black_red_cmap, vmin=0, vmax=255)
    imgg = subplotg.imshow(M[:, :, 1], cmap=black_green_cmap, vmin=0, vmax=255)
    imgb = subplotb.imshow(M[:, :, 2], cmap=black_blue_cmap, vmin=0, vmax=255)

    fig.colorbar(imgr, ax=subplotr)
    fig.colorbar(imgg, ax=subplotg)
    fig.colorbar(imgb, ax=subplotb)

    return fig


def color_histogram(img: Image.Image) -> Figure:
    """
    Return a histogram of the color channels of the image
    """
    M = np.array(img)

    # Si je mets un commentaire dans mon code c'est bien.
    # Mais s'il respecte les conventions de codage c'est mieux.
    # Décalez ce commentaire pour respecter les conventions !

    n, p, m = M.shape
    MM = np.reshape(M, (n * p, m))

    if m == 4:
        MM = MM[:, 0:3]

    colors = ["red", "green", "blue"]

    fig = Figure(figsize=(12, 6))
    ax = fig.add_subplot()

    ax.hist(MM, bins=10, density=True, histtype="bar",
            color=colors, label=colors)

    ax.set_xlabel("Pixel amplitude in each color channel")
    ax.set_ylabel("Pixel density")

    return fig


def foreground_filter(
    img: Union[Image.Image, np.ndarray], theta: int = 150
) -> np.ndarray:
    """Create a black and white image outlining the foreground."""
    M = np.array(img)
    G = np.min(M[:, :, 0:3], axis=2)
    F = G < theta
    return F


def transparent_background_filter(
    img: Union[Image.Image, np.ndarray], theta: int = 10
) -> Image.Image:
    """Create a cropped image with transparent background."""
    F = foreground_filter(img, theta=theta)
    M = np.array(img)
    N = np.zeros([M.shape[0], M.shape[1], 4], dtype=M.dtype)
    N[:, :, :3] = M[:, :, :3]
    N[:, :, 3] = F * 255
    return Image.fromarray(N)


def transparent_background(img: Image.Image) -> Image.Image:
    """Sets the white background of an image to transparent"""
    data = img.getdata()
    newData = []

    for a in data:
        a = a[:3]
        if np.mean(np.array(a)) == 255:
            a = a + (0,)
        else:
            a = a + (255,)
        newData.append(a)

    img.putdata(newData)
    return img


##############################################################################
# Attributs


def redness(img: Image.Image) -> float:
    """Return the redness of a PIL image."""
    M = np.array(img)
    R = M[:, :, 0] * 1.0
    G = M[:, :, 1] * 1.0
    F = foreground_filter(img)
    mean_red = np.mean(R[F])
    mean_green = np.mean(G[F])
    return mean_red - mean_green


def elongation(img: Image.Image) -> float:
    """Extract the scalar value elongation from a PIL image."""
    F = foreground_filter(img)
    xy = np.argwhere(F)
    C = np.mean(xy, axis=0)
    Cxy = xy - np.tile(C, [xy.shape[0], 1])
    U, s, V = np.linalg.svd(Cxy)
    return s[0] / s[1]


def elongation_plot(img: Image.Image, subplot: Axes) -> None:
    """Plot the principal axes of the SVD when computing the elongation"""
    F = foreground_filter(img)
    xy = np.argwhere(F)
    C = np.mean(xy, axis=0)
    Cxy = xy - np.tile(C, [xy.shape[0], 1])
    U, s, V = np.linalg.svd(Cxy)

    N = len(xy)
    a0 = s[0] / np.sqrt(N)
    a1 = s[1] / np.sqrt(N)

    subplot.plot(C[1], C[0], "ro", linewidth=50, markersize=10)

    subplot.plot(
        [C[1], C[1] + a0 * V[0, 1]],
        [C[0], C[0] + a0 * V[0, 0]],
        "r-",
        linewidth=3,
    )
    subplot.plot(
        [C[1], C[1] - a0 * V[0, 1]],
        [C[0], C[0] - a0 * V[0, 0]],
        "r-",
        linewidth=3,
    )
    subplot.plot(
        [C[1], C[1] + a1 * V[1, 1]],
        [C[0], C[0] + a1 * V[1, 0]],
        "g-",
        linewidth=3,
    )
    subplot.plot(
        [C[1], C[1] - a1 * V[1, 1]],
        [C[0], C[0] - a1 * V[1, 0]],
        "g-",
        linewidth=3,
    )


##############################################################################
# Nouveaux ATTRIBUTS


def position_bouche(img: Image.Image) -> float:
    F = foreground_filter(img)
    a, b = F.shape
    F_bas = F[a // 2:, :]
    xy = np.argwhere(F_bas)

    if xy.size == 0:
        return 0.0

    return np.mean(xy[:, 0])


def grayscale(img: Image.Image) -> np.ndarray:
    """Return image in gray scale"""
    return np.mean(np.array(img)[:, :, :3], axis=2)


class MatchedFilter:
    """Matched filter class to extract a feature from a template"""

    def __init__(self, examples: Iterable[Image.Image]):
        """Create the template for a matched filter; use only grayscale"""
        M = np.mean([grayscale(img) for img in examples], axis=0)
        self.template = (M - M.mean()) / M.std()

    def show(self):
        """Show the template"""
        fig = Figure(figsize=(3, 3))
        ax = fig.add_subplot()
        ax.imshow(self.template, cmap="gray")
        return fig

    def match(self, img: Image.Image) -> Number:
        """Extract the matched filter value for a PIL image."""
        M = grayscale(img)
        M = (M - M.mean()) / M.std()
        return np.mean(np.multiply(self.template, M))


##############################################################################
# Analyse de performance


def error_rate(solutions: pd.Series, predictions: pd.Series) -> Any:
    """Return the error rate between two vectors."""
    return (solutions != predictions).mean()


def split_data(X, Y, verbose=True, seed=0):
    """Make a 50/50 training/test data split (stratified)."""
    SSS = StratifiedShuffleSplit(
        n_splits=1, test_size=0.5, random_state=seed
    )
    (train_index, test_index), = SSS.split(X, Y)

    if verbose:
        print("TRAIN:", train_index, "TEST:", test_index)

    return train_index, test_index


##############################################################################
# Classifier


class OneRule:
    def __init__(self) -> None:
        self.is_trained = False
        self.ig = 0
        self.w = 1
        self.theta = 0

    def fit(self, X: pd.DataFrame, Y: pd.Series) -> None:
        df = pd.concat([X, Y.rename("class")], axis=1)
        corrs = df.corr()["class"].drop("class")

        self.attribute = corrs.abs().idxmax()
        self.sign = int(np.sign(corrs[self.attribute]))

        class0_mean = X[Y == -1][self.attribute].mean()
        class1_mean = X[Y == 1][self.attribute].mean()
        self.theta = (class0_mean + class1_mean) / 2

        self.is_trained = True

        print(
            f"FIT: Training Successful. Feature selected: "
            f"{self.attribute}; Polarity: {self.sign}; "
            f"Threshold: {self.theta:5.2f}."
        )

    def predict(self, X: pd.DataFrame) -> pd.Series:
        G = X[self.attribute]

        Y = pd.Series(
            np.where(G >= self.theta, self.sign, -self.sign),
            index=X.index,
        )

        print("PREDICT: Prediction done")
        return Y
