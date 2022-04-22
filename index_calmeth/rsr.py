import pandas as pd
import numpy as np
import bisect
from typing import Union


num = Union[int, float]


class Rsr:
    """
    对传入的pd.dataframe数据进行rsr打分
    """

    def __init__(self, dataframe: pd.DataFrame):
        """
        初始化：得到可用数据矩阵及其长宽数据
        """
        self.__df = dataframe.copy()
        self.__m, self.__n = self.__df.shape

    def score_matrix1(self, bv_list: list[num]) -> pd.DataFrame | None:
        """整次秩和比法计算得分，bv_list是由各指标正向最佳贡献值构成的列表

        Args:
            bv_list (list[num]): 正向最佳值列表

        Returns:
            pd.DataFrame | None: 若参数无误，返回转化后的数据框，否则返回None
        """
        if len(bv_list) != self.__n:
            print("重新考虑最佳贡献值列表元素数量")
        else:
            # 计算距离矩阵
            bv_matrix = pd.DataFrame(
                np.tile(np.array(bv_list).T, (self.__m, 1)), columns=self.__df.columns)
            dist_matrix = (self.__df - bv_matrix).abs()
            # 计算打分矩阵
            rsr_matrix = pd.DataFrame(
                np.empty((self.__m, self.__n)), columns=self.__df.columns)  # 创建与距离矩阵形状相同的空矩阵
            for q in range(self.__n):
                compare_list = np.sort(dist_matrix.iloc[:, q])
                for p in range(self.__m):
                    rsr_matrix.iloc[p, q] = bisect.bisect_left(
                        compare_list, dist_matrix.iloc[p, q])  # type: ignore
            return rsr_matrix / self.__m * 100

    def score_matrix2(self, bv_list: list[num]) -> pd.DataFrame | None:
        """非整次秩和比法计算得分，bv_list是由各指标正向最佳贡献值构成的列表

        Args:
            bv_list (list[num]): 正向最佳值列表

        Returns:
            pd.DataFrame | None: 若参数无误，返回转化后的数据框，否则返回None
        """
        if len(bv_list) != self.__n:
            print("重新考虑最佳贡献值列表元素数量")
        else:
            # 计算距离矩阵
            bv_matrix = pd.DataFrame(
                np.tile(np.array(bv_list).T, (self.__m, 1)), columns=self.__df.columns)
            dist_matrix = (self.__df - bv_matrix).abs()
            # 计算打分矩阵
            rsr_matrix = pd.DataFrame(
                np.empty((self.__m, self.__n)), columns=self.__df.columns)  # 创建与距离矩阵形状相同的空矩阵
            for q in range(self.__n):
                max_v = dist_matrix.iloc[:, q].max()
                min_v = dist_matrix.iloc[:, q].min()
                for p in range(self.__m):
                    rsr_matrix.iloc[p, q] = 1 + ((self.__m - 1) * (
                        dist_matrix.iloc[p, q] - min_v) / (max_v - min_v))
            # 得分标准化
            score_matrix = pd.DataFrame(
                np.empty((self.__m, self.__n)), columns=self.__df.columns)
            for q in range(self.__n):
                max_v = rsr_matrix.iloc[:, q].max()
                min_v = rsr_matrix.iloc[:, q].min()
                for p in range(self.__m):
                    score_matrix.iloc[p, q] = rsr_matrix.iloc[p,
                                                              q] / (max_v - min_v) * 100
            return score_matrix
