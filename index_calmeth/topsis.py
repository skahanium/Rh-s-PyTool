import itertools
import numpy as np
import pandas as pd
import index_calmeth.NonDimension as icn
from typing import Union


num = Union[int, float]


class Topsis:
    """
    对传入对pd.dataframe数据进行topsis打分
    """

    def __init__(self, dataframe: pd.DataFrame):
        """
        初始化：得到可用数据矩阵及其长宽数据。
        """
        self.__df = dataframe.copy()
        self.__m, self.__n = self.__df.shape

    def score_matrix(self, weights: list[num], bv_list: list[float]) -> pd.DataFrame | None:
        """计算得分矩阵。weights为权重矩阵,bv_list为正向最佳值列表

        Args:
            weights (list[num]): 权重列表
            bv_list (list[float]): 正向最佳值列表

        Returns:
            _type_: 若参数无误，返回转化后的数据框，否则返回None
        """
        if len(bv_list) != self.__n:
            print("重新考虑最佳贡献值列表元素数量")
        else:
            # 计算距离矩阵
            dist_matrix = pd.DataFrame(
                np.empty((self.__m, self.__n)), columns=self.__df.columns)
            for j in range(len(bv_list)):
                dist_matrix[:, j] = np.abs(self.__df.iloc[:, j] - bv_list[j])

            # 利用距离矩阵进行topsis打分
            copy_matrix = icn.toone(dist_matrix, mode='1')
            assert isinstance(copy_matrix, pd.DataFrame)
            empty_matrix1 = empty_matrix2 = pd.DataFrame(
                np.empty((self.__m, self.__n)))
            z_max = [copy_matrix.iloc[:, j].max() for j in range(self.__n)]
            z_min = [copy_matrix.iloc[:, j].min() for j in range(self.__n)]

            for j in range(self.__n):
                empty_matrix1.iloc[:, j] = weights[j] * \
                    (z_max[j] - copy_matrix.iloc[:, j]) ** 2
                empty_matrix2.iloc[:, j] = weights[j] * \
                    (z_min[j] - copy_matrix.iloc[:, j]) ** 2

            for i, j in itertools.product(range(self.__m), range(self.__n)):
                if empty_matrix1.iloc[i, j] is np.nan:
                    empty_matrix1.iloc[i, j] = 0
                elif empty_matrix2.iloc[i, j] is np.nan:
                    empty_matrix2.iloc[i, j] = 0

            d1 = np.sqrt(empty_matrix1.sum(axis=1))
            d2 = np.sqrt(empty_matrix2.sum(axis=1))
            result = icn.toone(pd.DataFrame(d2/(d1+d2)), mode='0')
            assert isinstance(result, pd.DataFrame)
            return result * 100
