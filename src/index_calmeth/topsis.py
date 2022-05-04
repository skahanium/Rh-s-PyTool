import numpy as np
import index_calmeth.non_dimension as icn
from typing import Union


num = Union[int, float]


class Topsis:
    """
    将传入对np.ndarray数据转换为topsis类。
    初始化np.ndarray数据得到可用数据矩阵及其长宽数据。
    """

    @classmethod
    def __init__(cls, ndarray: np.ndarray):
        cls.df = ndarray.copy()
        cls.m, cls.n = cls.df.shape

    @classmethod
    def distance_matrix(cls, bv_list: list[num]) -> np.ndarray | None:
        """计算距离矩阵
        Args:
            bv_list (list[int|float]): 正向最佳值列表
        Returns:
            np.ndarray: 若参数无误则返回距离矩阵，否则返回None
        """
        if len(bv_list) != cls.n:
            print("重新考虑最佳贡献值列表元素数量")
        else:
            # 计算距离矩阵
            bv_matrix = np.tile(np.array(bv_list), (cls.m, 1))
            return np.absolute(cls.df - bv_matrix)

    @classmethod
    def score_matrix(cls, weights: np.ndarray, bv_list: list[num]) -> np.ndarray | None:
        """计算得分矩阵。weights为权重矩阵,bv_list为正向最佳值列表

        Args:
            weights (np.ndarray): 权重数组
            bv_list (list[int|float]): 正向最佳值列表

        Returns:
            np.ndarray: 若参数无误，返回转化后的数据组，否则返回None
        """
        dist_matrix = cls.distance_matrix(bv_list)
        assert isinstance(dist_matrix, np.ndarray)
        copy_matrix = icn.toone(dist_matrix, mode='0')
        assert isinstance(copy_matrix, np.ndarray)

        empty_matrix1 = np.empty((cls.m, cls.n))
        empty_matrix2 = np.empty((cls.m, cls.n))
        z_max = [copy_matrix[:, j].max() for j in range(cls.n)]
        z_min = [copy_matrix[:, j].min() for j in range(cls.n)]

        for j in range(cls.n):
            empty_matrix1[:, j] = weights[j] * \
                (z_max[j] - copy_matrix[:, j]) ** 2
            empty_matrix2[:, j] = weights[j] * \
                (z_min[j] - copy_matrix[:, j]) ** 2

        d1: np.ndarray = np.sqrt(empty_matrix1.sum(axis=1))
        d2: np.ndarray = np.sqrt(empty_matrix2.sum(axis=1))
        result: np.ndarray = (d2/(d1+d2))
        return result.reshape(result.shape[0], 1)
