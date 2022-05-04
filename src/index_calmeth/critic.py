import numpy as np
import index_calmeth.non_dimension as icn


class Critic:
    """
    将传入的np.ndarray类型数据转换为Critic类。
    初始化np.ndarray得到可用的归一化矩阵。
    """
    @classmethod
    def __init__(cls, ndarray: np.ndarray):
        cls.toone = icn.toone(ndarray.copy(), mode='0')

    @classmethod
    def variability(cls) -> np.ndarray:
        """
        Returns:
            np.ndarray: 指标变异性数据
        """
        assert isinstance(cls.toone, np.ndarray)
        m, n = cls.toone.shape  # 获取归一数据集的形状
        variabilities = []
        for j in range(n):
            ave_x = cls.toone[:, j].mean()
            diff = np.array(cls.toone[:, j] - ave_x)
            sum_var = np.sum(diff ** 2 / (m - 1))
            variabilities.append(sum_var ** 0.5)
        return np.array(variabilities)

    @classmethod
    def conflict(cls) -> np.ndarray:
        """
        Returns:
            np.ndarray: 指标冲突性数据
        """
        assert isinstance(cls.toone, np.ndarray)
        corr_matrix = np.corrcoef(cls.toone, rowvar=False)
        conflicts = []
        p, q = corr_matrix.shape
        conflicts.extend(
            sum((1 - corr_matrix[i, j]) for i in range(p)) for j in range(q))

        return np.array(conflicts)

    @classmethod
    def weights(cls) -> np.ndarray:
        """通过变异性指标和冲突性指标计算最后权重

        Returns:
            np.ndarray: critic权重数组
        """
        info1 = cls.variability()
        info2 = cls.conflict()
        information = np.array(info1) * np.array(info2)
        for i in range(len(information)):
            if information[i] is np.nan:
                information[i] = 0
        assert isinstance(cls.toone, np.ndarray)

        _, q = cls.toone.shape
        sum_info = information.sum()
        if sum_info == 0:
            return np.ones(q) / q
        weights = [information[c] / sum_info for c in range(q)]
        return np.array(weights)
