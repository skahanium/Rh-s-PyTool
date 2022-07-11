import pandas as pd
import numpy as np
import re
from math import radians, cos, sin, asin, sqrt

data = np.array(pd.read_csv("src/attachment/adcodes.csv"))
areas = np.unique(data[:, 1])


def _level_judge(adcode: int) -> int:
    """根据adcode对地区行政等级进行判断。

    Args:
        adcode (int): 12位adcode

    Returns:
        int: 1：省级行政区；2:地级行政区；3:县级行政区
    """
    if str.endswith(str(adcode), "0"*10):
        return 1
    elif str.endswith(str(adcode), "0"*8):
        return 2
    else:
        return 3


def _father_code(adcode: int) -> int:
    """对于地级或县级行政区会根据adcode返回上级行政区的adcode，对于升级行政区会返回自身的adcode。

    Args:
        adcode (int): 12位adcode

    Returns:
        int: 返回的上级行政区adcode或自身的adcode。
    """
    if _level_judge(adcode) == 1:
        return adcode
    elif _level_judge(adcode) == 2:
        return adcode // (10**10) * (10**10)
    else:
        return adcode // (10**8) * (10**8)


class Addr_info():
    """
    根据行政区名称或adcode创建的类，包含了行政区名称、adcode、坐标、行政等级、上级行政区adcode、上级行政区名称等属性，以及一个判断行政区是否属于另一个行政区的方法。
    """

    def __init__(self, name: str, adcode=None):
        obj = data[data[:, 1] ==
                   name] if adcode is None else data[data[:, 0] == adcode]
        _m, _ = obj.shape
        if _m == 1:
            self.info = obj
            self.name = name
            self.adcode = self.info[0, 0]
            self.longitude = self.info[0, 2]
            self.latitude = self.info[0, 3]
            self.level = _level_judge(self.adcode)
            self.fcode = _father_code(self.adcode)
            self.father = data[data[:, 0] == self.fcode][0, 1]
        elif _m == 0:
            print("请输入正确地名或adcode")
        else:
            print("区域名称存在重复对象，请另输入adcode")

    def belongs_to(self, another: str) -> bool:
        """判断行政区是否属于另一个行政区的方法。

        Args:
            another (str): 另一个行政区的名称

        Returns:
            bool: 判断的结果
        """
        return self.father == another


def fillup(name: str) -> list | None:
    """根据行政区简称进行补全，并返回所有符合的对象。

    Args:
        name (str): 行政区简称（当然，非要用全称也可以）

    Returns:
        list | None: 全部补全结果。
    """
    if len(name) >= 3:
        result = [area for area in areas if re.search(name, area)]
        if not result:
            result = [area for area in areas if re.search(name[:-1], area)]
        return result
    elif len(name) == 2:
        result = []
        result.extend(area for area in areas if re.search(name, area))
        return result
    else:
        print("单个字无法查询")


def lookup(name: str, level: int, adcode: int | None = None, add_father: bool = True) -> str | None:
    """根据行政区名称（或简称）、行政等级或adcode精确查找。考虑到某些区域会重名，可以调节add_father参数来决定是否要添加上级行政区名作为前缀以进行区分。

    Args:
        name (str): 行政区名称（或简称）
        level (int): 行政等级。1：省级行政区；2:地级行政区；3:县级行政区
        adcode (int | None, optional): 12位adcode
        add_father (bool, optional): 是否要添加上级行政区名作为前缀，默认为True。

    Returns:
        str | None: 查找结果
    """
    objs = fillup(name)
    assert objs is not None
    for obj in objs:
        if Addr_info(obj, adcode=adcode).level == level:
            return Addr_info(obj, adcode=adcode).father + obj if add_father else obj


def haversine(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
    """利用两个地点的经纬度计算球面距离

    Args:
        lon1 (float): 地区1的经度
        lat1 (float): 地区1的纬度
        lon2 (float): 地区2的经度
        lat2 (float): 地区2的纬度

    Returns:
        float: 球面距离，单位：km
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(
        radians, [lon1, lat1, lon2, lat2])  # radians：将角度转化为弧度

    # haversine（半正矢）公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r


def dist(city1: str, city2: str) -> float:  # type: ignore
    """利用两个地区的城市名称计算球面距离

    Args:
        city1 (str): 地区1的城市名称
        city2 (str): 地区2的城市名称

    Returns:
        float: 球面距离，单位：km
    """
    return haversine(Addr_info(city1).longitude, Addr_info(city1).latitude, Addr_info(city2).longitude, Addr_info(city2).latitude)
