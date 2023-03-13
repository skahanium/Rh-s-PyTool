import itertools
import numpy as np
from .non_dimension import toone


def __variability(data: np.ndarray) -> np.ndarray:
    if data is None:
        raise ValueError('data cannot be None')

    if not isinstance(data, np.ndarray):
        raise ValueError('data must be a numpy array')

    if data.shape[0] < 2:
        raise ValueError('data must have at least 2 rows')

    if np.isnan(data).any():
        raise ValueError('data must not contain NaN values')

    if np.isinf(data).any():
        raise ValueError('data must not contain infinity values')

    m, n = data.shape
    ave_x = np.mean(data, axis=0)
    diff = data - ave_x
    sum_var = np.sum(diff**2, axis=0) / (m - 1)
    return np.sqrt(sum_var)


def __conflict(data_origin: np.ndarray) -> np.ndarray:
    try:
        corr_matrix: np.ndarray = np.corrcoef(data_origin, rowvar=False)
    except np.linalg.LinAlgError:  # Singular matrix
        corr_matrix = np.zeros((data_origin.shape[1], data_origin.shape[1]))
    p: int
    q: int
    p, q = corr_matrix.shape
    conflicts: List[float] = [
        sum(1 - corr_matrix[i, j] for i in range(p)) for j in range(q)
    ]
    return np.array(conflicts)


def critic(data_origin: np.ndarray) -> np.ndarray:
    # sourcery skip: raise-specific-error
    """
    通过所提供数据计算critic权重

    Args:
        data_origin (np.ndarray): 待计算权重的数据

    Returns:
        np.ndarray: critic权重数组
    """
    try:
        info1: np.ndarray = __variability(data_origin)
        info2: np.ndarray = __conflict(data_origin)
        information: np.ndarray = np.array(info1) * np.array(info2)
        information[np.isnan(information)] = 0

        _, q = data_origin.shape
        sum_info: float = information.sum()
        if sum_info == 0:
            return np.ones(q) / q
        weights: np.ndarray = np.array([information[c] / sum_info for c in range(q)])
        return weights
    except Exception as err:
        raise Exception("Error when calculating critic weights") from err


def ewm(data_origin: np.ndarray) -> np.ndarray:
    """通过所提供数据计算entropy weight method(ewm)权重

    Args:
        data_origin (np.ndarray): 待计算权重的数据

    Returns:
        np.ndarray: ewm权重数组
    """
    data = toone(data_origin.copy(), mode='0')
    assert isinstance(data, np.ndarray)
    m, n = data.shape
    entropy = []

    for j in range(n):
        data[:, j] = data[:, j] / np.sum(data[:, j])
        np.place(data[:, j], data[:, j] == 0, 1)
        ej = -np.log(1 / m) * np.sum(data[:, j] * np.log(data[:, j]))
        entropy.append(ej)

    weights = [(1 - entropy[c]) / (m - np.sum(entropy)) for c in range(n)]
    return np.array(weights)


def stddev(data_origin: np.ndarray) -> np.ndarray:
    """通过所提供数据计算standard deviation(stddev)权重

    Args:
        data_origin (np.ndarray): 待计算权重的数据

    Returns:
        np.ndarray: stddev权重数组
    """
    data = toone(data_origin.copy(), mode='0')
    n = data.shape[1]
    info = np.std(data, axis=0)
    return np.ones(n) / n if np.sum(info) == 0 else np.divide(info, np.sum(info))


def gini(data: np.ndarray) -> np.ndarray:
    """
    计算基尼系数法权重

    Args:
        data (np.ndarray): 待计算权重的数据

    Returns:
        np.ndarray: 基尼系数法权重数组
    """

    if not isinstance(data, np.ndarray):
        raise TypeError("data must be an instance of np.ndarray")

    if data.ndim != 2:
        raise ValueError("data must be a 2-dimensional array")

    m, n = data.shape
    Gini = np.zeros(n)

    for j in range(n):
        diff_array = np.abs(np.subtract.outer(data[:, j], data[:, j]))
        Gini[j] = np.sum(diff_array) / (m**2 - m)

    return Gini / np.sum(Gini)
