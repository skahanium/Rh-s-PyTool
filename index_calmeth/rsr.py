import pandas as pd
import numpy as np


class Rsr():
    """
    对传入的pd.dataframe数据进行rsr打分
    """

    def __init__(self, dataframe):
        """
        初始化：得到归一矩阵及其长宽数据
        """
        self.df = dataframe.iloc[:, 3:].dropna()
        self.toone = (self.df - self.df.min()) / \
            (self.df.max() - self.df.min())
        self.m, self.n = self.toone.shape
