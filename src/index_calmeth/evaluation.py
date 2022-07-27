import numpy as np
from .non_dimension import toone


def topsis(
    data_origin: np.ndarray, weights: list[int | float] | np.ndarray
) -> np.matrix:
    """计算优劣解距离法得分矩阵，weights为权重矩阵。

    Args:
        data_origin (np.ndarray): 待计算数据
        weights (np.ndarray): 权重数组

    Returns:
        np.matrix: 若参数无误，返回得分数据，否则返回None
    """
    data = data_origin.copy()
    data = toone(data, mode='3')
    assert isinstance(data, np.ndarray)
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


def rsr(data_origin: np.ndarray, weights: list[int | float] | np.ndarray) -> np.matrix:
    """计算整次秩和比得分矩阵，weights为权重矩阵。

    Args:
        data_origin (np.ndarray): 待计算数据
        weights (np.ndarray): 权重数组

    Returns:
        np.matrix: 若参数无误，返回得分数据，否则返回None
    """
    data = data_origin.copy()
    m, n = data.shape

    rsr_matrix = np.empty((m, n))
    for q in range(n):
        compare_list: np.ndarray = np.sort(data[:, q])
        rsr_matrix[:, q] = np.searchsorted(compare_list, data[:, q])
    return rsr_matrix * np.mat(weights).T / m  # type: ignore


def ni_rsr(
    data_origin: np.ndarray, weights: list[int | float] | np.ndarray
) -> np.matrix:
    """计算非整次秩和比得分矩阵，weights为权重矩阵。

    Args:
        data_origin (np.ndarray): 待计算数据
        weights (np.ndarray): 权重数组

    Returns:
        np.matrix: 若参数无误，返回得分数据，否则返回None
    """
    data = data_origin.copy()
    m, n = data.shape

    rsr_matrix = np.empty((m, n))
    for q in range(n):
        max_v = data[:, q].max()
        min_v = data[:, q].min()
        rsr_matrix[:, q] = 1 + ((m - 1) * (data[:, q] - min_v) / (max_v - min_v))
    return rsr_matrix * np.mat(weights).T / m  # type: ignore
