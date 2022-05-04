import numpy as np
from typing import Union


num = Union[int, float]


class Rsr:
    """
    将传入的np.ndarray数据转换为rsr类。
    初始化np.ndarray数据得到其长宽数据。
    """

    @classmethod
    def __init__(cls, ndarray: np.ndarray):
        cls.df = ndarray.copy()
        cls.m, cls.n = cls.df.shape

    @classmethod
    def score_matrix1(cls, weights: np.ndarray, bv_list: list[num]) -> np.matrix | None:
        """整次秩和比法计算得分，bv_list是由各指标正向最佳贡献值构成的列表

        Args:
            bv_list (list[int|float]): 正向最佳值列表

        Returns:
            np.matrix | None: 若参数无误，返回转化后的数据组，否则返回None
        """
        if len(bv_list) != cls.n:
            print("重新考虑最佳贡献值列表元素数量")
        else:
            # 计算距离矩阵
            bv_matrix = np.tile(np.array(bv_list), (cls.m, 1))
            dist_matrix: np.ndarray = np.absolute(cls.df - bv_matrix)

            # 计算打分矩阵
            rsr_matrix = np.empty((cls.m, cls.n))
            for q in range(cls.n):
                compare_list: np.ndarray = np.sort(dist_matrix[:, q])
                rsr_matrix[:, q] = np.searchsorted(
                    compare_list, dist_matrix[:, q])
            return rsr_matrix * np.matrix(weights).T

    @classmethod
    def score_matrix2(cls, weights: np.ndarray, bv_list: list[num]) -> np.matrix | None:
        """非整次秩和比法计算得分，bv_list是由各指标正向最佳贡献值构成的列表

        Args:
            bv_list (list[int|float]): 正向最佳值列表

        Returns:
            np.matrix | None: 若参数无误，返回转化后的数据组，否则返回None
        """
        if len(bv_list) != cls.n:
            print("重新考虑最佳贡献值列表元素数量")
        else:
            # 计算距离矩阵
            bv_matrix = np.tile(np.array(bv_list), (cls.m, 1))
            dist_matrix: np.ndarray = np.absolute(cls.df - bv_matrix)

            # 计算打分矩阵
            rsr_matrix: np.ndarray = np.empty(
                (cls.m, cls.n))
            for q in range(cls.n):
                max_v = dist_matrix[:, q].max()
                min_v = dist_matrix[:, q].min()
                rsr_matrix[:, q] = 1 + ((cls.m - 1) *
                                        (dist_matrix[:, q] - min_v) / (max_v - min_v))
            return rsr_matrix * np.matrix(weights).T
