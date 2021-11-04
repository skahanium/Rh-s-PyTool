import numpy as np
import pandas as pd
import index_calmeth.NonDimension as Nd


class Topsis:
    """
    对传入对pd.dataframe数据进行topsis打分。
    注：dataframe必须经过正向化处理。
    """

    def __init__(self, dataframe):
        """
        初始化：得到可用数据矩阵及其长宽数据。
        """
        self.df = dataframe.copy()
        self.m, self.n = self.df.shape

    def score_matrix(self, weights):
        """
        计算得分矩阵。weights为权重矩阵,得分越低越优秀。
        """
        copy_matrix = Nd.toone(self.df, mode='1')
        empty_matrix = copy_matrix.copy()
        z_max = z_min = []
        for j in range(self.n):
            z_max.append(copy_matrix.iloc[:, j].max())
            z_min.append(copy_matrix.iloc[:, j].min())

        for i in range(self.m):
            for j in range(self.n):
                empty_matrix.iloc[i, j] = weights[j] * (z_max[j]-copy_matrix.iloc[i, j]) ** 2

        for i in range(self.m):
            for j in range(self.n):
                if empty_matrix.iloc[i, j] is np.nan:
                    empty_matrix.iloc[i, j] = 0

        scoring = empty_matrix.sum(axis=1)
        scoring = pd.DataFrame(scoring)
        result = Nd.toone(scoring, mode='01')
        return result
