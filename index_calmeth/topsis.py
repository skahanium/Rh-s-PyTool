import numpy as np
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
        copy_matrix = Nd.toone(self.df, mode='3')
        print(copy_matrix)
        scoring = []
        Z_max = Z_min = []
        for j in range(self.n):
            Z_max.append(copy_matrix.iloc[:, j].max())
            Z_min.append(copy_matrix.iloc[:, j].min())

        for i in range(self.m):
            var1 = var2 = 0
            for j in range(self.n):
                var1 += weights[j] * (Z_max[j]-copy_matrix.iloc[i, j]) ** 2
                var2 += weights[j] * (Z_min[j]-copy_matrix.iloc[i, j]) ** 2
            scoring.append(np.sqrt(var2)/(np.sqrt(var1)+np.sqrt(var2)))
        return np.array(scoring).T

