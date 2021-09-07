import pandas as pd
import numpy as np
import bisect


class Topsis():
    """
    对传入对pd.dataframe数据进行topsis打分
    """

    def __init__(self, dataframe):
        """
        初始化：得到可用数据矩阵及其长宽数据
        """
        self.df = dataframe.copy().iloc[:, 3:]
        self.m, self.n = self.df.shape

    def homologous(self, mode='0'):
        """
        指标同向化
        """
        if mode == '0':
            pass
        # elif mode == '1':
