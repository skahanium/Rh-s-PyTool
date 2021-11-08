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

    def score_matrix(self, weights, bv_list):
        """
        计算得分矩阵。weights为权重矩阵,bv_list为最佳值列表
        """
        if len(bv_list) != self.n:
            print("重新考虑最佳贡献值列表元素数量")
        else:
            # 计算距离矩阵
            dist_matrix = pd.DataFrame(
                np.empty((self.m, self.n)), columns=self.df.columns)
            for j in range(self.n):
                for i in range(self.m):
                    dist_matrix.iloc[i, j] = np.abs(
                        self.df.iloc[i, j] - bv_list[j])

            # 利用距离矩阵进行topsis打分
            copy_matrix = Nd.toone(dist_matrix, mode='1')
            empty_matrix1 = pd.DataFrame(np.empty((self.m, self.n)))
            empty_matrix2 = pd.DataFrame(np.empty((self.m, self.n)))
            z_max = []
            z_min = []
            for j in range(self.n):
                z_max.append(copy_matrix.iloc[:, j].max())
                z_min.append(copy_matrix.iloc[:, j].min())

            for i in range(self.m):
                for j in range(self.n):
                    empty_matrix1.iloc[i, j] = weights[j] * (z_max[j] - copy_matrix.iloc[i, j]) ** 2
                    empty_matrix2.iloc[i, j] = weights[j] * (z_min[j] - copy_matrix.iloc[i, j]) ** 2

            for i in range(self.m):
                for j in range(self.n):
                    if empty_matrix1.iloc[i, j] is np.nan:
                        empty_matrix1.iloc[i, j] = 0
                    elif empty_matrix2.iloc[i, j] is np.nan:
                        empty_matrix2.iloc[i, j] = 0

            d1 = np.sqrt(empty_matrix1.sum(axis=1))
            d2 = np.sqrt(empty_matrix2.sum(axis=1))

            result = pd.DataFrame(d2/(d1+d2))
            result = Nd.toone(result, mode='01')
            return result

