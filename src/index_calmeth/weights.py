import numpy as np
from .non_dimension import toone
from .check_func import array_check


def __variability(data: np.ndarray) -> np.ndarray:
    array_check(data=data)
    length, _ = data.shape
    ave_x = np.mean(data, axis=0)
    diff = data - ave_x
    sum_var = np.sum(diff**2, axis=0) / (length - 1)
    return np.sqrt(sum_var)


def __conflict(data: np.ndarray) -> np.ndarray:
    array_check(data=data)
    try:
        corr_matrix: np.ndarray = np.corrcoef(data, rowvar=False)
    except np.linalg.LinAlgError as e:
        raise np.linalg.LinAlgError("指标存在严重多重共线性") from e
    conflicts: np.ndarray = (1 - corr_matrix).sum(axis=0)
    return conflicts


def critic(data_origin: np.ndarray) -> np.ndarray:
    """
    通过所提供数据计算critic权重

    Args:
        data_origin (np.ndarray): 待计算权重的数据

    Returns:
        np.ndarray: critic权重数组
    """
    info1: np.ndarray = __variability(data_origin)
    info2: np.ndarray = __conflict(data_origin)
    information: np.ndarray = np.multiply(info1, info2)
    information = np.nan_to_num(information)
    _, width = data_origin.shape
    sum_info: float = information.sum()
    if sum_info == 0:
        return np.ones(width) / width
    weights: np.ndarray = information / sum_info
    return weights


def ewm(data_origin: np.ndarray) -> np.ndarray:
    """通过所提供数据计算entropy weight method(ewm)权重

    Args:
        data_origin (np.ndarray): 待计算权重的数据

    Returns:
        np.ndarray: ewm权重数组
    """
    array_check(data=data_origin)
    data = toone(data_origin.copy(), mode='0')
    assert isinstance(data, np.ndarray)
    length, _ = data.shape
    data /= np.sum(data, axis=0)
    data = np.clip(data, a_min=1e-10, a_max=None)
    entropy = -np.log(1 / length) * np.sum(data * np.log(data), axis=0)
    return (1 - entropy) / (length - np.sum(entropy))


def stddev(data_origin: np.ndarray) -> np.ndarray:
    """通过所提供数据计算standard deviation(stddev)权重

    Args:
        data_origin (np.ndarray): 待计算权重的数据

    Returns:
        np.ndarray: stddev权重数组
    """
    array_check(data=data_origin)
    data = toone(data_origin.copy(), mode='0')
    width = data.shape[1]
    info = np.std(data, axis=0)
    return np.ones(width) / width if np.sum(info) == 0 else np.divide(info, np.sum(info))


def gini(data_origin: np.ndarray) -> np.ndarray:
    """
    计算基尼系数法权重

    Args:
        data (np.ndarray): 待计算权重的数据

    Returns:
        np.ndarray: 基尼系数法权重数组
    """
    array_check(data=data_origin)
    length, _ = data_origin.shape
    diff_array = np.abs(data_origin[:, :, np.newaxis] - data_origin[:, :, np.newaxis].T)
    score = 2 / (length * (length - 1)) * np.sum(diff_array, axis=(0, 1))
    return score / np.sum(score)
