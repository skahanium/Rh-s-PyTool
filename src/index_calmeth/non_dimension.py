from functools import reduce
import numpy as np


############################################################################################
# 辅助函数区域
############################################################################################


def fn(x: int | float, y: int | float) -> int | float:  # 辅助函数，用于向量归一化计算
    return x**2 + y**2


def fn2(
    x: int | float, low: int | float, high: int | float, M: int | float
) -> int | float:  # 辅助函数，用于计算适度性指标转化为极大型指标的公式
    assert low <= high
    if x < low:
        return 1 - (low - x) / M
    elif x > high:
        return 1 - (x - high) / M
    else:
        return 1


vfn2 = np.vectorize(fn2)
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
    if mode == '0':
        for j in change_list:
            df1[:, j] = 1 / df1[:, j]
        return df1

    elif mode == '1':
        for j in change_list:
            df1[:, j] = df1[:, j].max() - df1[:, j]
        return df1

    else:
        print('请正确地选择模式')


def middle_convert(
    ndarray: np.ndarray, change_list: list[int], best_value: list[int | float]
) -> np.ndarray | None:
    """中间型指标转化为极大型指标

    Args:
        ndarray (np.ndarray): 待转化数据
        change_list (list[int]): 待转化列下标组成的列表
        best_value (list[int|float]): 待转化列的最优值组成的列表。由于每个列的最优值不同，所以需要提供

    Returns:
        np.ndarray | None: 若参数无误，返回转化后的数据组，否则返回None
    """
    if len(change_list) != len(best_value):
        print("请检查可变列表和最佳值列表的元素数量")
    else:
        copy_matrix = ndarray.copy().astype(float)
        for j in change_list:
            M = max(np.abs(copy_matrix[:, j] - best_value[change_list.index(j)]))
            copy_matrix[:, j] = (
                1 - np.abs(copy_matrix[:, j] - best_value[change_list.index(j)]) / M
            )
        return copy_matrix


def moderate_convert(
    ndarray: np.ndarray,
    change_list: list[int],
    low_limit: list[int | float],
    high_limit: list[int | float],
) -> np.ndarray | None:
    """适度性指标转化为极大型指标

    Args:
        ndarray (np.ndarray): 待转化数据
        change_list (list[int]): 待转化列下标组成的列表
        low_limit (list[int|float]): 待转化列的最优区间下限组成的列表。由于每个列的最优区间下限不同，所以需要提供
        high_limit (list[int|float]): 待转化列的最优区间上限组成的列表。由于每个列的最优区间上限不同，所以需要提供

    Returns:
        np.ndarray | None: 若参数无误，返回转化后的数据组，否则返回None
    """
    if len(low_limit) == len(high_limit) == len(change_list):
        df2 = ndarray.copy().astype(float)
        for j in change_list:
            a = low_limit[change_list.index(j)]
            b = high_limit[change_list.index(j)]
            assert a <= b
            M = max(a - min(df2[:, j]), max(df2[:, j]) - b)
            df2[:, j] = vfn2(df2[:, j], a, b, M)
        return df2

    else:
        print("请检查可变列表与上下界列表的元素数量")


def toone(origin_array: np.ndarray, mode: str) -> np.ndarray | None:
    """多种矩阵归一化方法

    Args:
        ndarray (np.ndarray): 待转化数据
        mode (str): 转化模式。mode='0'时为归一化，mode='1'时为平均归一化，mode='2'时为标准化，mode='3'时为向量归一化

    Returns:
        np.ndarray | None: 若参数无误，返回转化后的数据组，否则返回None
    """
    ndarray = origin_array.copy().astype(float)
    m, n = ndarray.shape
    copy_matrix = np.empty((m, n))
    match mode:
        case '0':
            for j in range(n):
                mmax = ndarray[:, j].max()
                mmin = ndarray[:, j].min()
                copy_matrix[:, j] = (
                    (ndarray[:, j] - mmin) / (mmax - mmin) if mmax != mmin else 1
                )
            return copy_matrix
        case '1':
            for j in range(n):
                mmean = ndarray[:, j].mean()
                mmax = ndarray[:, j].max()
                mmin = ndarray[:, j].min()
                copy_matrix[:, j] = (
                    (ndarray[:, j] - mmean) / (mmax - mmin) if mmax != mmin else 0
                )
            return copy_matrix
        case '2':
            for j in range(n):
                mmean = ndarray[:, j].mean()
                mstd = ndarray[:, j].std()
                copy_matrix[:, j] = (ndarray[:, j] - mmean) / mstd if mstd != 0 else 0
            return copy_matrix
        case '3':
            for j in range(n):
                vec_length = np.sqrt(np.array(reduce(fn, ndarray[:, j])))
                copy_matrix[:, j] = ndarray[:, j] / vec_length
            return copy_matrix
