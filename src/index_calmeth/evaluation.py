import numpy as np
from .non_dimension import toone


def topsis(
    data_origin: np.ndarray, weights: list[int | float] | np.ndarray
) -> np.matrix | None:
    """计算优劣解距离法得分矩阵，weights为权重矩阵。

    Args:
        data_origin (np.ndarray): 待计算数据
        weights (np.ndarray): 权重数组

    Returns:
        np.matrix: 若参数无误，返回得分数据，否则返回None
    """
    data = data_origin.copy()
    data = toone(data, mode='3')
    if data is None:
        return None
    m, n = data.shape

    empty_matrix1 = np.empty((m, n))
    empty_matrix2 = np.empty((m, n))
    z_max = [data[:, j].max() for j in range(n)]
    z_min = [data[:, j].min() for j in range(n)]

    for j in range(n):
        empty_matrix1[:, j] = weights[j] * (z_max[j] - data[:, j]) ** 2
        empty_matrix2[:, j] = weights[j] * (z_min[j] - data[:, j]) ** 2

    d1: np.ndarray = np.sqrt(empty_matrix1.sum(axis=1))
    d2: np.ndarray = np.sqrt(empty_matrix2.sum(axis=1))
    result: np.ndarray = d2 / (d1 + d2)
    return np.mat(result.reshape(result.shape[0], 1))


def rsr(
    data_origin: np.ndarray, weights: list[int | float] | np.ndarray
) -> np.matrix | None:
    """计算整次秩和比得分矩阵，weights为权重矩阵。

    Args:
        data_origin (np.ndarray): 待计算数据
        weights (np.ndarray): 权重数组

    Returns:
        np.matrix: 若参数无误，返回得分数据，否则返回None
    """
    try:
        data = data_origin.copy()
        m, n = data.shape
    except AttributeError:
        print("data_origin must be a np.ndarray")
        return None

    try:
        weights = np.mat(weights)
        if weights.shape[1] != 1:
            print("weights must be a 1D array")
            return None
    except AttributeError:
        print("weights must be a 1D array")
        return None

    rsr_matrix = np.empty((m, n))
    for q in range(n):
        compare_list: np.ndarray = np.sort(data[:, q])
        rsr_matrix[:, q] = np.searchsorted(compare_list, data[:, q])
    return rsr_matrix * weights / m


def ni_rsr(
    data_origin: np.ndarray, weights: list[int | float] | np.ndarray
) -> np.matrix | None:
    """计算非整次秩和比得分矩阵，weights为权重矩阵。

    Args:
        data_origin (np.ndarray): 待计算数据
        weights (np.ndarray): 权重数组

    Returns:
        np.matrix: 若参数无误，返回得分数据，否则返回None
    """
    data = data_origin.copy()
    m, n = data.shape

    if not isinstance(weights, (list, np.ndarray)):
        raise TypeError("weights should be list or ndarray.")

    if isinstance(weights, list) and not all(
        isinstance(w, (int, float)) for w in weights
    ):
        raise TypeError("weights should be list of int or float.")

    if isinstance(weights, np.ndarray) and not all(
        isinstance(w, (np.int, np.int_, np.float, np.float_)) for w in weights
    ):
        raise TypeError("weights should be ndarray of int or float.")

    if len(weights) != n:
        raise ValueError("weights should be the same length as data.")

    rsr_matrix = np.empty((m, n))
    for q in range(n):
        max_v = data[:, q].max()
        min_v = data[:, q].min()
        rsr_matrix[:, q] = 1 + ((m - 1) * (data[:, q] - min_v) / (max_v - min_v))
    return rsr_matrix * np.mat(weights).T / m
