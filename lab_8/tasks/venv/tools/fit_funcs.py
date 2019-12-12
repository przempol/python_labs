import numpy as np


def least_sq(xy):
    """
    Fits linear function to given vector of 2D points.

    Funkcja liczy parametry funkcji liniowej ax+b do danych za pomocą metody
    najmniejszych kwadratów.
    (1 pkt.)

    A = (N*Sum(xy)-Sum(x)*Sum(y))/Delta
    B = (Sum(x^2)*Sum(y)-Sum(x)*Sum(xy))/Delta
    Delta = N*Sum(x^2) - (Sum(x)^2)

    :param xy: vector of 2D points (shape (2, n))
    :type xy: np.ndarray
    :return: Tuple of fitted parameters
    """
    # zrobic w srodowisku wirtualnym
    # mnozenie macierzowe, bez uzycia forow
    x = xy[0]
    y = xy[1]
    n = xy.shape[1]
    delta = n * np.sum(x**2) - np.sum(x) ** 2
    a = n * np.sum(x*y) - np.sum(x)*np.sum(y)
    a /= delta
    b = np.sum(x**2) * np.sum(y) - np.sum(x) * np.sum(x*y)
    b /= delta
    return tuple([a, b])
