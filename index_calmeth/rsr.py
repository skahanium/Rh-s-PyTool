import pandas as pd
import numpy as np
import bisect


class Rsr():
    """
    对传入的pd.dataframe数据进行rsr打分
    """

    def __init__(self, dataframe):
        """
        初始化：得到可用数据矩阵及其长宽数据
        """
        self.df = dataframe.copy().iloc[:, 3:]
        self.m, self.n = self.df.shape

    def score_matrix(self, bv_list):
        """
        计算得分，bv_list是由各指标正向最佳贡献值构成的列表
        注：所谓正向最佳贡献值，指的是从正面考虑指标贡献度时的最佳值。
           比如用不同指标合成金融风险指数(相较于安全而言是一个负面形容)，因此从正面考虑时对于正向指标其最佳值便是最低值，负向指标
           最佳值是最高值，适度指标由文献或前人研究来确定。
        """
        if len(bv_list) != self.n:
            print("重新考虑最佳贡献值列表元素数量")
        else:
            dist_matrix = pd.DataFrame(
                np.empty((self.m, self.n)), columns=self.df.columns)
            for j in range(self.n):
                for i in range(self.m):
                    dist_matrix.iloc[i, j] = np.abs(
                        self.df.iloc[i, j] - bv_list[j])

                rsr_matrix = pd.DataFrame(
                    np.empty((self.m, self.n)), columns=self.df.columns)  # 创建与打分矩阵形状相同的空矩阵
                for j in range(self.n):
                    for i in range(self.m):
                        compare_list = sorted(dist_matrix.iloc[:, j])
                        rsr_matrix.iloc[i, j] = bisect.bisect_left(
                            compare_list, dist_matrix.iloc[i, j])
                score_matrix = rsr_matrix / self.m * 100
                return score_matrix


