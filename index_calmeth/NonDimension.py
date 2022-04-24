from functools import reduce
import numpy as np
import pandas as pd
from typing import Union


num = Union[int, float]


def fn(x: num, y: num) -> num:
    """toone函数mode='3'时的辅助函数

    Args:
        x (num): 参数1
        y (num): 参数2

    Returns:
        num: 两数平方和
    """
    return x**2 + y**2


def tiny_convert(dataframe: pd.DataFrame, mode: str, change_list: list[int]) -> np.ndarray | None:
    """极小型指标转化为极大型指标

    Args:
        dataframe (pd.DataFrame): 待转化数据框
        mode (str): 转化模式。mode='0'时为1/x模式，mode='1'时为max(x)-x模式
        change_list (list[int]): 待转化列下标组成的列表

    Returns:
        np.ndarray | None: 若参数无误，返回转化后的数据组，否则返回None
    """
    df1 = np.array(dataframe)
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


def middle_convert(dataframe: pd.DataFrame, change_list: list[int], best_value: list[num]) -> np.ndarray | None:
    """中间型指标转化为极大型指标

    Args:
        dataframe (pd.DataFrame): 待转化数据框
        change_list (list[int]): 待转化列下标组成的列表
        best_value (list[num]): 待转化列的最优值组成的列表。由于每个列的最优值不同，所以需要提供

    Returns:
        np.ndarray | None: 若参数无误，返回转化后的数据组，否则返回None
    """
    if len(change_list) != len(best_value):
        print("请检查可变列表和最佳值列表的元素数量")
    else:
        copy_matrix = np.array(dataframe)
        for j in change_list:
            M = max(np.abs(copy_matrix[:, j] -
                    best_value[change_list.index(j)]))
            copy_matrix[:, j] = 1 - \
                np.abs(copy_matrix[:, j] -
                       best_value[change_list.index(j)]) / M
        return copy_matrix


def fn2(low: num, high: num, x: num, M: num) -> num:
    """
    辅助函数，用于计算适度性指标转化为极大型指标的公式
    """
    assert low <= high
    if x < low:
        return 1 - (low - x) / M
    elif x > high:
        return 1 - (x - high) / M
    else:
        return 1


def moderate_convert(dataframe: pd.DataFrame, change_list: list[int], low_limit: list[num], high_limit: list[num]) -> np.ndarray | None:
    """适度性指标转化为极大型指标

    Args:
        dataframe (pd.DataFrame): 待转化数据框
        change_list (list[int]): 待转化列下标组成的列表
        low_limit (list[num]): 待转化列的最优区间下限组成的列表。由于每个列的最优区间下限不同，所以需要提供
        high_limit (list[num]): 待转化列的最优区间上限组成的列表。由于每个列的最优区间上限不同，所以需要提供

    Returns:
        np.ndarray | None: 若参数无误，返回转化后的数据组，否则返回None
    """
    if len(low_limit) == len(high_limit) == len(change_list):
        df2 = np.array(dataframe)
        for j in change_list:
            a = low_limit[j]
            b = high_limit[j]
            assert a <= b
            M = max(a - min(df2[:, j]), max(df2[:, j] - b))
            df2[:, j] = df2[:, j].apply(lambda x: fn2(a, b, x, M))
        return df2

    else:
        print("请检查可变列表与上下界列表的元素数量")


def toone(dataframe: pd.DataFrame, mode: str) -> np.ndarray | None:
    """多种矩阵归一化方法

    Args:
        dataframe (pd.DataFrame): 待转化数据框
        mode (str): 转化模式。mode='0'时为归一化，mode='1'时为平均归一化，mode='2'时为标准化，mode='3'时为向量归一化

    Returns:
        np.ndarray | None: 若参数无误，返回转化后的数据组，否则返回None
    """
    copy_matrix = np.array(dataframe)
    _, n = copy_matrix.shape
    if mode == '0':
        """
        归一化
        """
        for j in range(n):
            mmax = copy_matrix[:, j].max()
            mmin = copy_matrix[:, j].min()
            copy_matrix[:, j] = (
                copy_matrix[:, j] - mmin) / (mmax - mmin)
        return copy_matrix
    elif mode == '1':
        """
        平均归一化
        """
        for j in range(n):
            mmean = copy_matrix[:, j].mean()
            mmax = copy_matrix[:, j].max()
            mmin = copy_matrix[:, j].min()
            copy_matrix[:, j] = (
                copy_matrix[:, j] - mmean) / (mmax - mmin)
        return copy_matrix
    elif mode == '2':
        """
        标准化
        """
        for j in range(n):
            mmean = copy_matrix[:, j].mean()
            mstd = copy_matrix[:, j].std()
            copy_matrix[:, j] = (copy_matrix[:, j] - mmean) / mstd
        return copy_matrix
    elif mode == '3':
        """
        向量归一化
        """
        for j in range(n):
            vec_length = np.sqrt(np.array(reduce(fn, copy_matrix[:, j])))
            copy_matrix[:, j] = copy_matrix[:, j] / vec_length
        return copy_matrix
    else:
        print('输入正确的模式')
