import numpy as np
from .non_dimension import toone
from .check_func import array_check


def topsis(
    data_origin: np.ndarray, weights: list[int | float] | np.ndarray
    ) ->  np.matrix | None:
    """计算优劣解距离法得分矩阵，weights为权重矩阵。

    Args:
        data_origin (np.ndarray): 待计算数据
        weights (np.ndarray): 权重数组

    Returns:
        np.matrix: 若参数无误，返回得分数据，否则返回None
    """
    array_check(data=data_origin)
    data = data_origin.copy()
    data = toone(data, mode='3')

    dist_max = np.multiply(np.square(np.subtract(data.max(axis=0), data)),
                        np.square(weights))
    dist_min = np.multiply(np.square(np.subtract(data.min(axis=0), data)),
                        np.square(weights))

    dist_max *= weights
    dist_min *= weights

    dist_z_max: np.ndarray = np.sqrt(dist_max.sum(axis=1))
    dist_z_min: np.ndarray = np.sqrt(dist_min.sum(axis=1))

    result: np.ndarray = dist_z_min / (dist_z_max + dist_z_min)
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
    array_check(data=data_origin)
    data = data_origin.copy()
    length, _ = data.shape

    assert isinstance(weights, (list, np.ndarray)), "weights必须是一维数组或列表"
    weights = np.mat(weights)
    compare_indices = np.argsort(data, axis=0)
    rsr_matrix = np.argsort(compare_indices, axis=0)
    return rsr_matrix * np.mat(weights).T/ length


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
    array_check(data=data_origin)
    data = data_origin.copy()
    length, _ = data.shape

    assert isinstance(weights, (list, np.ndarray)), "weights必须是一维数组或列表"
    max_value = np.max(data, axis=0)
    min_value = np.min(data, axis=0)
    rsr_matrix = 1 + ((length - 1) * (data - min_value) / (max_value - min_value))
    return rsr_matrix * np.mat(weights).T / length
