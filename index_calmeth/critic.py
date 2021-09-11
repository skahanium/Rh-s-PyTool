import pandas as pd
import numpy as np
import index_calmeth.NonDimension as icn


class Critic:
    """
    对传入的pd.dataframe类型数据进行critic权重计算
    """

    def __init__(self, dataframe):
        """
        初始化：由原矩阵得到可用的归一化矩阵
        """
        self.df = dataframe.copy().dropna()  # 选出无空值的观测数据以方便进行权重计算
        self.toone = icn.toone(self.df, mode='0')

    def vardata(self):
        """
        获取变异性数据
        """
        m, n = self.toone.shape  # 获取归一数据集的形状
        variabilities = []
        for j in range(n):
            ave_x = self.toone.iloc[:, j].mean()
            sum_var = 0
            for i in range(m):
                diff = self.toone.iloc[i, j] - ave_x
                sum_var += diff ** 2 / (m - 1)
            variabilities.append(sum_var ** 0.5)
        return variabilities

    def corrdata(self):
        """
        获取冲突性数据
        """
        corr_matrix = self.toone.corr()
        conflicts = []
        p, q = corr_matrix.shape
        for j in range(q):
            conflict = 0
            for i in range(p):
                conflict += (1 - corr_matrix.iloc[i, j])
            conflicts.append(conflict)
        return conflicts

    def weights(self):
        """
        通过变异性指标和冲突性指标计算最后权重
        """
        info1 = self.vardata()
        info2 = self.corrdata()
        information = np.array(info1) * np.array(info2)

        p, q = self.toone.shape
        weights = []
        for c in range(q):
            wei = information[c] / information.sum()
            weights.append(wei)
        weights = pd.DataFrame(weights).T
        return weights
