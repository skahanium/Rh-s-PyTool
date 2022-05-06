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


def conflict(data_origin) -> np.ndarray:  # 指标冲突性数据
    corr_matrix = np.corrcoef(data_origin, rowvar=False)
    conflicts = []
    p, q = corr_matrix.shape
    conflicts.extend(
        sum((1 - corr_matrix[i, j]) for i in range(p)) for j in range(q))

    return np.array(conflicts)


def critic(data_origin) -> np.ndarray:
    """通过变异性指标和冲突性指标计算最后权重

    Returns:
        np.ndarray: critic权重数组
    """
    info1 = variability(data_origin)
    info2 = conflict(data_origin)
    information = np.array(info1) * np.array(info2)
    for i in range(len(information)):
        if information[i] is np.nan:
            information[i] = 0

    _, q = data_origin.shape
    sum_info = information.sum()
    if sum_info == 0:
        return np.ones(q) / q
    weights = [information[c] / sum_info for c in range(q)]
    return np.array(weights)