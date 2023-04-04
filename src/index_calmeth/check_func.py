import numpy as np


def array_check(data: np.array):
    """
    检查数据是否符合要求
    """

    if data is None:
        raise ValueError('数据不能为空！')

    if not isinstance(data, np.ndarray):
        raise ValueError('数据类型必须为numpy数组！')

    if data.shape[0] < 2:
        raise ValueError('数据必须至少有两行！')

    if np.isnan(data).any():
        raise ValueError('数据不能包含NaN值！')

    if np.isinf(data).any():
        raise ValueError('数据不能包含无穷值！')
