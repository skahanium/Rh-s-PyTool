import numpy as np
import index_calmeth.non_dimension as icn


class Critic:
    """
    对传入的np.ndarray类型数据进行critic权重计算
    """

    def __init__(self, ndarray: np.ndarray):
        """
        初始化：由原矩阵得到可用的归一化矩阵
        """
        self.__df = ndarray.copy()
        self.__toone = icn.toone(self.__df, mode='0')

    def variability(self) -> np.ndarray:
        """
        获取变异性数据
        """
        assert isinstance(self.__toone, np.ndarray)
        m, n = self.__toone.shape  # 获取归一数据集的形状
        variabilities = []
        for j in range(n):
            ave_x = self.__toone[:, j].mean()
            diff = np.array(self.__toone[:, j] - ave_x)
            sum_var = np.sum(diff ** 2 / (m - 1))
            variabilities.append(sum_var ** 0.5)
        return np.array(variabilities)

    def conflict(self):
        """
        获取冲突性数据
        """
        assert isinstance(self.__toone, np.ndarray)
        corr_matrix = np.corrcoef(self.__toone, rowvar=False)
        conflicts = []
        p, q = corr_matrix.shape
        conflicts.extend(
            sum((1 - corr_matrix[i, j]) for i in range(p)) for j in range(q))

        return np.array(conflicts)

    def weights(self):
        """通过变异性指标和冲突性指标计算最后权重

        Returns:
            np.ndarray: critic权重数组
        """
        info1 = self.variability()
        info2 = self.conflict()
        information = np.array(info1) * np.array(info2)
        assert isinstance(self.__toone, np.ndarray)

        _, q = self.__toone.shape
        weights = []
        for c in range(q):
            wei = information[c] / information.sum()
            weights.append(wei)
        return np.array(weights)
