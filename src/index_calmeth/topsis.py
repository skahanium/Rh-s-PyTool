import numpy as np
import index_calmeth.non_dimension as icn
from typing import Union


num = Union[int, float]


class Topsis:
    """
    对传入对np.ndarray数据进行topsis打分
    """

    def __init__(self, ndarray: np.ndarray):
        """
        初始化：得到可用数据矩阵及其长宽数据。
        """
        self.__df = ndarray.copy()
        self.__m, self.__n = self.__df.shape

    def score_matrix(self, weights: np.ndarray, bv_list: list[num]) -> np.ndarray | None:
        """计算得分矩阵。weights为权重矩阵,bv_list为正向最佳值列表

        Args:
            weights (np.ndarray): 权重数组
            bv_list (list[int|float]): 正向最佳值列表

        Returns:
            np.ndarray: 若参数无误，返回转化后的数据组，否则返回None
        """
        if len(bv_list) != self.__n:
            print("重新考虑最佳贡献值列表元素数量")
        else:
            # 计算距离矩阵
            dist_matrix = np.empty((self.__m, self.__n))
            for j in range(len(bv_list)):
                dist_matrix[:, j] = np.absolute(self.__df[:, j] - bv_list[j])

            # 利用距离矩阵进行topsis打分
            copy_matrix = icn.toone(dist_matrix, mode='0')
            assert isinstance(copy_matrix, np.ndarray)
            empty_matrix1 = np.empty((self.__m, self.__n))
            empty_matrix2 = np.empty((self.__m, self.__n))
            z_max = [copy_matrix[:, j].max() for j in range(self.__n)]
            z_min = [copy_matrix[:, j].min() for j in range(self.__n)]

            for j in range(self.__n):
                empty_matrix1[:, j] = weights[j] * \
                    (z_max[j] - copy_matrix[:, j]) ** 2
                empty_matrix2[:, j] = weights[j] * \
                    (z_min[j] - copy_matrix[:, j]) ** 2

            d1 = np.sqrt(empty_matrix1.sum(axis=1))
            d2 = np.sqrt(empty_matrix2.sum(axis=1))
            result = (d2/(d1+d2))
            result = (result - result.min()) / \
                (result.max() - result.min())
            return result.reshape(result.shape[0], 1) * 100
