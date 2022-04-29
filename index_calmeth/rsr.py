import numpy as np
from typing import Union


num = Union[int, float]


class Rsr:
    """
    对传入的np.ndarray数据进行rsr打分
    """

    def __init__(self, ndarray: np.ndarray):
        """
        初始化：得到可用数据矩阵及其长宽数据
        """
        self.__df = ndarray.copy()
        self.__m, self.__n = self.__df.shape

    def score_matrix1(self, weights: np.ndarray, bv_list: list[num]) -> np.matrix | None:
        """整次秩和比法计算得分，bv_list是由各指标正向最佳贡献值构成的列表

        Args:
            bv_list (list[int|float]): 正向最佳值列表

        Returns:
            np.matrix | None: 若参数无误，返回转化后的数据组，否则返回None
        """
        if len(bv_list) != self.__n:
            print("重新考虑最佳贡献值列表元素数量")
        else:
            # 计算距离矩阵
            bv_matrix = np.tile(np.array(bv_list), (self.__m, 1))
            dist_matrix: np.ndarray = np.absolute(self.__df - bv_matrix)
            # 计算打分矩阵
            rsr_matrix = np.empty((self.__m, self.__n))  # 创建与距离矩阵形状相同的空矩阵
            for q in range(self.__n):
                compare_list: np.ndarray = np.sort(dist_matrix[:, q])
                rsr_matrix[:, q] = np.searchsorted(
                    compare_list, dist_matrix[:, q])
            return (rsr_matrix / self.__m * 100) * np.matrix(weights).T

    def score_matrix2(self, weights: np.ndarray, bv_list: list[num]) -> np.matrix | None:
        """非整次秩和比法计算得分，bv_list是由各指标正向最佳贡献值构成的列表

        Args:
            bv_list (list[int|float]): 正向最佳值列表

        Returns:
            np.matrix | None: 若参数无误，返回转化后的数据组，否则返回None
        """
        if len(bv_list) != self.__n:
            print("重新考虑最佳贡献值列表元素数量")
        else:
            # 计算距离矩阵
            bv_matrix = np.tile(np.array(bv_list), (self.__m, 1))
            dist_matrix: np.ndarray = np.absolute(self.__df - bv_matrix)
            # 计算打分矩阵
            rsr_matrix: np.ndarray = np.empty(
                (self.__m, self.__n))  # 创建与距离矩阵形状相同的空矩阵
            for q in range(self.__n):
                max_v = dist_matrix[:, q].max()
                min_v = dist_matrix[:, q].min()
                rsr_matrix[:, q] = 1 + ((self.__m - 1) *
                                        (dist_matrix[:, q] - min_v) / (max_v - min_v))
            # 得分标准化
            score_matrix = np.empty((self.__m, self.__n))
            for q in range(self.__n):
                max_v = rsr_matrix[:, q].max()
                min_v = rsr_matrix[:, q].min()
                score_matrix[:, q] = rsr_matrix[:, q] / \
                    (max_v - min_v) * 100
            return score_matrix * np.matrix(weights).T
