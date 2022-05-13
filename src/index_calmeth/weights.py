import numpy as np
import index_calmeth.non_dimension as icn


def variability(data_origin: np.ndarray) -> np.ndarray:  # 指标变异性数据
    data = icn.toone(data_origin.copy(), mode='0')
    assert isinstance(data, np.ndarray)
    m, n = data.shape

    variabilities = []
    for j in range(n):
        ave_x = data[:, j].mean()
        diff = np.array(data[:, j] - ave_x)
        sum_var = np.sum(diff ** 2 / (m - 1))
        variabilities.append(sum_var ** 0.5)
    return np.array(variabilities)


def conflict(data_origin: np.ndarray) -> np.ndarray:  # 指标冲突性数据
    corr_matrix = np.corrcoef(data_origin, rowvar=False)
    conflicts = []
    p, q = corr_matrix.shape
    conflicts.extend(
        sum((1 - corr_matrix[i, j]) for i in range(p)) for j in range(q))

    return np.array(conflicts)


def critic(data_origin: np.ndarray) -> np.ndarray:
    """通过所提供数据计算critic权重

    Args:
        data_origin (np.ndarray): 待计算权重的数据

    Returns:
        np.ndarray: critic权重数组
    """
    info1 = variability(data_origin)
    info2 = conflict(data_origin)
    information = np.array(info1) * np.array(info2)
    information[np.isnan(information)] = 0

    _, q = data_origin.shape
    sum_info = information.sum()
    if sum_info == 0:
        return np.ones(q) / q
    weights = [information[c] / sum_info for c in range(q)]
    return np.array(weights)


def ewm(data_origin: np.ndarray) -> np.ndarray:
    """通过所提供数据计算entropy weight method(ewm)权重

    Args:
        data_origin (np.ndarray): 待计算权重的数据

    Returns:
        np.ndarray: ewm权重数组
    """
    data = icn.toone(data_origin.copy(), mode='0')
    assert isinstance(data, np.ndarray)
    m, n = data.shape
    entropy = []

    for j in range(n):
        data[:, j] = data[:, j] / np.sum(data[:, j])
        np.place(data[:, j], data[:, j] == 0, 1)
        ej = -np.log(1/m) * np.sum(data[:, j] * np.log(data[:, j]))
        entropy.append(ej)

    weights = [(1-entropy[c]) / (m - np.sum(entropy)) for c in range(n)]
    return np.array(weights)


def stddev(data_origin: np.ndarray) -> np.ndarray:
    """通过所提供数据计算standard deviation(stddev)权重

    Args:
        data_origin (np.ndarray): 待计算权重的数据

    Returns:
        np.ndarray: stddev权重数组
    """
    data = icn.toone(data_origin.copy(), mode='0')
    assert isinstance(data, np.ndarray)
    _, n = data.shape

    info = [np.std(data[:, j]) for j in range(n)]
    if np.sum(info) == 0:
        return np.ones(n) / n
    weights = [(i / np.sum(info)) for i in info]
    return np.array(weights)


def expert(weights: np.ndarray | list) -> np.ndarray | list:
    """脱裤子放屁的主观方法，怎么看都意义不大。

    Args:
        weights (np.ndarray): “专家”主观给出的权重

    Returns:
        np.ndarray: expert权重数组
    """
    return weights.copy()
