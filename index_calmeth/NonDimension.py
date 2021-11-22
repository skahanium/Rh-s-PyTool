from functools import reduce
import numpy as np


class NonDimension:
    """
    构建实例化对象进行正向化、归一化等预处理。
    方法来源：https://blog.csdn.net/limiyudianzi/article/details/103410150
    """

    def __init__(self, dataframe):
        """
        初始化：得到可用数据矩阵及其长宽数据
        """
        self.__df = dataframe.copy()
        self.__m, self.__n = self.__df.shape

    def tiny_convert(self, mode, change_list):
        """
        极小型指标转化为极大型指标
        """
        df1 = self.__df.copy()
        if mode == '0':
            for j in range(self.__n):
                if j in change_list:
                    df1.iloc[:, j] = 1 / df1.iloc[:, j]
            return df1

        elif mode == '1':
            for j in range(self.__n):
                if j in change_list:
                    j_max = df1.iloc[:, j].max()
                    df1.iloc[:, j] = j_max - df1.iloc[:, j]
            return df1

        else:
            print('请正确地选择模式')

    def middle_convert(self, change_list, best_value):
        """
        中间型指标转化为极大型指标
        """
        if len(change_list) != len(best_value):
            print("请检查可变列表和最佳值列表的元素数量")
        else:
            copy_matrix = self.__df.copy()
            for j in range(self.__n):
                if j in change_list:
                    for i in range(self.__m):
                        copy_matrix.iloc[i, j] = 1 - np.abs(self.__df.iloc[i, j] - best_value[change_list.index(j)]) / \
                                                 np.abs(self.__df.iloc[:, j] - best_value[change_list.index(j)]).max()
            return copy_matrix

    def moderate_convert(self, change_list, low_limit, high_limit):
        """
        适度性指标转化为极大型指标
        """
        if len(low_limit) == len(high_limit) == len(change_list):
            df2 = self.__df.copy()
            for j in range(self.__n):
                if j in change_list:
                    a = low_limit[change_list.index(j)]
                    b = high_limit[change_list.index(j)]
                    mm = max(a - self.__df.iloc[:, j].min(), self.__df.iloc[:, j].max() - b)
                    # mm为偏离最优区间最远的值
                    for i in range(self.__m):
                        if self.__df.iloc[i, j] < a:
                            df2.iloc[i, j] = 1 - (a - self.__df.iloc[i, j]) / mm
                        elif self.__df.iloc[i, j] > b:
                            df2.iloc[i, j] = 1 - (self.__df.iloc[i, j] - b) / mm
                        else:
                            df2.iloc[i, j] = 1
            return df2

        else:
            print("请检查可变列表与上下界列表的元素数量")

    def toone(self, mode):
        """
        矩阵归一化
        """
        copy_matrix = self.__df.copy()
        if mode == '0':
            """
            Rescaling
            """
            for j in range(self.__n):
                mmax = self.__df.iloc[:, j].max()
                mmin = self.__df.iloc[:, j].min()
                for i in range(self.__m):
                    copy_matrix.iloc[i, j] = (self.__df.iloc[i, j] - mmin) / (mmax - mmin)
            return copy_matrix
        elif mode == '1':
            """
            Mean normalization
            """
            for j in range(self.__n):
                mmean = self.__df.iloc[:, j].mean()
                mmax = self.__df.iloc[:, j].max()
                mmin = self.__df.iloc[:, j].min()
                for i in range(self.__m):
                    copy_matrix.iloc[i, j] = (self.__df.iloc[i, j] - mmean) / (mmax - mmin)
            return copy_matrix
        elif mode == '2':
            """
            Standardization
            """
            for j in range(self.__n):
                mmean = self.__df.iloc[:, j].mean()
                mstd = self.__df.iloc[:, j].std()
                for i in range(self.__m):
                    copy_matrix.iloc[i, j] = (self.__df.iloc[i, j] - mmean) / mstd
            return copy_matrix
        elif mode == '3':
            """
            正则化
            """
            for j in range(self.__n):
                vec_length = np.sqrt(np.array(reduce(fn, self.__df.iloc[:, j])))
                for i in range(self.__m):
                    copy_matrix.iloc[i, j] = self.__df.iloc[i, j] / vec_length
            return copy_matrix
        else:
            print('输入正确的模式')


############################################################################
def fn(x, y):
    return x**2 + y**2
############################################################################


def tiny_convert(dataframe, mode, change_list):
    """
    极小型指标转化为极大型指标
    """
    df1 = dataframe.copy()
    m, n = df1.shape
    if mode == '0':
        for j in range(n):
            if j in change_list:
                df1.iloc[:, j] = 1 / df1.iloc[:, j]
        return df1

    elif mode == '1':
        for j in range(n):
            if j in change_list:
                j_max = df1.iloc[:, j].max()
                df1.iloc[:, j] = j_max - df1.iloc[:, j]
        return df1

    else:
        print('请正确地选择模式')


def middle_convert(dataframe, change_list, best_value):
    """
    中间型指标转化为极大型指标
    """
    if len(change_list) != len(best_value):
        print("请检查可变列表和最佳值列表的元素数量")
    else:
        copy_matrix = dataframe.copy()
        m, n = copy_matrix.shape
        for j in range(n):
            if j in change_list:
                for i in range(m):
                    copy_matrix.iloc[i, j] = 1 - np.abs(dataframe.iloc[i, j] - best_value[change_list.index(j)]) / \
                                             np.abs(dataframe.__df.iloc[:, j] - best_value[change_list.index(j)]).max()
        return copy_matrix


def moderate_convert(dataframe, change_list, low_limit, high_limit):
    """
    适度性指标转化为极大型指标
    """
    if len(low_limit) == len(high_limit) == len(change_list):
        df2 = dataframe.copy()
        m, n = df2.shape
        for j in range(n):
            if j in change_list:
                a = low_limit[change_list.index(j)]
                b = high_limit[change_list.index(j)]
                mm = max(a - dataframe.iloc[:, j].min(), dataframe.iloc[:, j].max() - b)
                for i in range(m):
                    if dataframe.iloc[i, j] > a:
                        df2.iloc[i, j] = 1 - (a - dataframe.iloc[i, j]) / mm
                    elif dataframe.iloc[i, j] < b:
                        df2.iloc[i, j] = 1 - (dataframe.iloc[i, j] - b) / mm
                    else:
                        df2.iloc[i, j] = 1
        return df2

    else:
        print("请检查可变列表与上下界列表的元素数量")


def toone(dataframe, mode):
    """
    矩阵归一化
    """
    copy_matrix = dataframe.copy()
    m, n = copy_matrix.shape
    if mode == '0':
        """
        归一化
        """
        for j in range(n):
            mmax = dataframe.iloc[:, j].max()
            mmin = dataframe.iloc[:, j].min()
            for i in range(m):
                copy_matrix.iloc[i, j] = (dataframe.iloc[i, j]-mmin) / (mmax-mmin)
        return copy_matrix
    elif mode == '01':
        """
        归一化后化作百分制分数
        """
        for j in range(n):
            mmax = dataframe.iloc[:, j].max()
            mmin = dataframe.iloc[:, j].min()
            for i in range(m):
                copy_matrix.iloc[i, j] = (dataframe.iloc[i, j]-mmin) / (mmax-mmin) * 100
        return copy_matrix
    elif mode == '1':
        """
        平均归一化
        """
        for j in range(n):
            mmean = dataframe.iloc[:, j].mean()
            mmax = dataframe.iloc[:, j].max()
            mmin = dataframe.iloc[:, j].min()
            for i in range(m):
                copy_matrix.iloc[i, j] = (dataframe.iloc[i, j]-mmean) / (mmax-mmin)
        return copy_matrix
    elif mode == '2':
        """
        标准化
        """
        for j in range(n):
            mmean = dataframe.iloc[:, j].mean()
            mstd = dataframe.iloc[:, j].std()
            for i in range(m):
                copy_matrix.iloc[i, j] = (dataframe.iloc[i, j]-mmean) / mstd
        return copy_matrix
    elif mode == '3':
        """
        正则化
        """
        for j in range(n):
            vec_length = np.sqrt(np.array(reduce(fn, dataframe.iloc[:, j])))
            for i in range(m):
                copy_matrix.iloc[i, j] = dataframe.iloc[i, j] / vec_length
        return copy_matrix
    else:
        print('输入正确的模式')
