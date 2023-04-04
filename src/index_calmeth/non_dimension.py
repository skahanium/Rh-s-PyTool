from typing import Union, List
import numpy as np
from numba import njit

############################################################################################
# 辅助函数区域
############################################################################################

@njit
def fn(
    x: Union[int, float],
    low: Union[int, float],
    high: Union[int, float],
    M: Union[int, float],
) -> Union[int, float]:
    assert isinstance(x, (int, float)), "x必须为数值"
    assert isinstance(low, (int, float)), "low必须为数值"
    assert isinstance(high, (int, float)), "high必须为数值"
    assert isinstance(M, (int, float)), "M必须为数值"
    assert low <= high, "low必须小于等于high"
    assert M > 0, "M必须大于0"
    if x <= low:
        return 1 - (low - x) / M
    elif x >= high:
        return 1 - (x - high) / M
    else:
        return 1


##############################################################################################


def tiny_convert(
    ndarray: np.ndarray, mode: str, change_list: list[int]
) -> np.ndarray | None:
    """极小型指标转化为极大型指标

    Args:
        ndarray (np.ndarray): 待转化数据
        mode (str): 转化模式。mode='0'时为1/x模式，mode='1'时为max(x)-x模式
        change_list (list[int]): 待转化列下标组成的列表

    Returns:
        np.ndarray | None: 若参数无误，返回转化后的数据组，否则返回None
    """
    df1 = ndarray.copy().astype(float)
    if mode not in ('0', '1'):
        raise ValueError('请正确地选择模式')
    if not all(isinstance(i, int) for i in change_list):
        raise TypeError('change_list的元素必须为整数')
    if any(i >= df1.shape[1] for i in change_list):
        raise IndexError('change_list的元素必须小于数据组的列数')

    if mode == '0':
        for j in change_list:
            df1[:, j] = 1 / df1[:, j]
        return df1

    elif mode == '1':
        for j in change_list:
            df1[:, j] = df1[:, j].max() - df1[:, j]
        return df1


def middle_convert(
    ndarray: np.ndarray, change_list: list[int], best_value: list[int | float]
) -> np.ndarray | None:
    """中间型指标转化为极大型指标

    Args:
        ndarray (np.ndarray): 待转化数据
        change_list (list[int]): 待转化列下标组成的列表
        best_value (list[int|float]): 待转化列的最优值组成的列表。

    Returns:
        np.ndarray | None: 若参数无误，返回转化后的数据组，否则返回None
    """
    assert len(change_list) != len(best_value), "请检查可变列表和最佳值列表的元素数量"
    assert all(isinstance(i, int) for i in change_list), "可变列表的元素为整数"
    assert all(isinstance(i, (int, float)) for i in best_value), "最佳值列表的素为数值"

    copy_matrix = ndarray.astype(float).copy()
    for j, col in enumerate(change_list):
        best_val = best_value[j]
        diff = np.abs(copy_matrix[:, col] - best_val)
        M = max(diff)
        copy_matrix[:, col] = 1 - diff / M
    return copy_matrix


def moderate_convert(
    ndarray: np.ndarray,
    change_list: List[int],
    low_limit: List[Union[int, float]],
    high_limit: List[Union[int, float]],
) -> Union[np.ndarray, None]:
    """适度性指标转化为极大型指标

    Args:
        ndarray (np.ndarray): 待转化数据
        change_list (list[int]): 待转化列下标组成的列表
        low_limit (list[int|float]): 待转化列的最优区间下限组成的列表。
        high_limit (list[int|float]): 待转化列的最优区间上限组成的列表。

    Returns:
        np.ndarray | None: 若参数无误，返回转化后的数据组，否则返回None
    """
    assert len(low_limit) == len(high_limit) == len(change_list), "检查三列表的元素数量"
    df2 = ndarray.astype(float)
    a = np.array(low_limit)[change_list]
    b = np.array(high_limit)[change_list]
    M = np.maximum(
        a - np.min(df2[:, change_list], axis=0),
        np.max(df2[:, change_list], axis=0) - b,
    )
    mask = a <= b
    assert np.all(mask), "最优区间下限必须小于等于最优区间上限"
    df2[:, change_list] = fn(df2[:, change_list], a, b, M)
    return df2


def toone(origin_array: np.ndarray, mode: str) -> np.ndarray | None:
    """多种矩阵归一化方法

    Args:
        ndarray (np.ndarray): 待转化数据
        mode (str): 转化模式。mode='0'时为归一化，
        mode='1'时为平均归一化，mode='2'时为标准化，mode='3'时为向量归一化

    Returns:
        np.ndarray | None: 若参数无误，返回转化后的数据组，否则返回None
    """
    ndarray = origin_array.copy().astype(float)
    m, n = ndarray.shape
    copy_matrix = np.empty((m, n))
    match mode:
        case '0':
            col_max = ndarray.max(axis=0)
            col_min = ndarray.min(axis=0)
            copy_matrix = (ndarray - col_min) / np.where(
                col_max == col_min, 1, col_max - col_min
            )

        case '1':
            col_mean = ndarray.mean(axis=0)
            col_max = ndarray.max(axis=0)
            col_min = ndarray.min(axis=0)
            copy_matrix = (ndarray - col_mean) / np.where(
                col_max == col_min, 1, col_max - col_min
            )

        case '2':
            col_std = np.std(ndarray, axis=0)
            col_mean = np.mean(ndarray, axis=0)
            copy_matrix = (ndarray - col_mean) / np.where(col_std != 0, col_std, 1)

        case '3':
            copy_matrix = ndarray / np.sqrt(np.sum(ndarray**2, axis=0))

        case _:
            print("请正确选择模式")
            copy_matrix = None

    return copy_matrix
