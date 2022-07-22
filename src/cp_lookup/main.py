import os
from math import radians, cos, sin, asin, sqrt
from jieba import lcut
import pandas as pd
import index_calmeth

csv_dir = f"{os.path.dirname(index_calmeth.__file__)[:-13]}cp_lookup/attachment/adcodes.csv"
data = pd.read_csv(csv_dir).set_index("adcode")
data.sort_index(inplace=True)


class Addr():
    """以区域名构建一个地区的类，包含该地区的adcode、区域名、经纬度等信息。"""

    def __init__(self, name: str, adcode: int | None = None):
        if adcode:
            self.addr = data.loc[data.index == adcode]
        else:
            info = lcut(name)
            levels = len(info)
            match levels:
                case 1:
                    addr = info[0]
                    if len(data.loc[data["name"].str.match(addr)]) != 1:
                        print("地名重复或有误！")
                    else:
                        self.addr = data.loc[data["name"].str.match(addr)]
                case 2:
                    father, addr = info
                    if len(data.loc[data["name"].str.match(addr)]) != 1:
                        fcode = data.loc[data["name"].str.match(father)].index
                        for code in data.loc[data["name"].str.match(addr)].index.to_list():
                            if (code//10**8 == fcode//10**8) | (code//10**10 == fcode//10**10):  # type: ignore
                                self.addr = data.loc[data.index == code]
                    else:
                        self.addr = data.loc[data["name"].str.match(addr)]
                case 3:
                    gdfather, father, addr = info
                    if len(data.loc[data["name"].str.match(addr)]) != 1:
                        fcode = data.loc[data["name"].str.match(father)].index
                        gfcode = data.loc[data["name"].str.match(
                            gdfather)].index
                        for code in data.loc[data["name"].str.match(addr)].index.to_list():
                            if code//10**10 == fcode//10**10 == gfcode//10**10:  # type: ignore
                                self.addr = data.loc[data.index == code]
                    else:
                        self.addr = data.loc[data["name"].str.match(addr)]

    def _belongs_to(self) -> str | None:
        code = self.addr.index.to_list()[0]
        fcode = code // 10**8 * 10**8 if code % 10**8 != 0 else code // 10**10 * 10**10
        return data.at[fcode, "name"]

    def _coordinate(self) -> tuple[float, float]:
        code = self.addr.index.to_list()[0]
        return data.at[code, "latitude"], data.at[code, "longitude"]


def lookup(name: str) -> str | None:
    """根据地名简称查找全称

    Args:
        name (str): 待查找地名

    Returns:
        str | None: 地名全称
    """
    code = Addr(name).addr.index.to_list()[0]
    return data.at[code, "name"]


def belongs_to(name: str) -> str | None:
    """根据地名查找其上级行政区名称

    Args:
        name (str): 待查找地名

    Returns:
        str | None: 上级行政区全称
    """
    return Addr(name)._belongs_to()


def coordinate(name: str) -> tuple[float, float]:
    """根据区域名得到其行政中心的坐标

    Args:
        name (str): 行政区名称

    Returns:
        tuple[float, float]: 行政中心经纬度
    """
    lat, lon = Addr(name)._coordinate()
    return lat, lon


def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """利用两个地点的经纬度计算球面距离

    Args:
        lat1 (float): 地区1的纬度
        lon1 (float): 地区1的经度
        lat2 (float): 地区2的纬度
        lon2 (float): 地区2的经度

    Returns:
        float: 球面距离，单位：km
    """
    # 将十进制度数转化为弧度
    lat1, lon1, lat2, lon2 = map(
        radians, [lat1, lon1, lat2, lon2])  # radians：将角度转化为弧度

    # haversine（半正矢）公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r


def dist(city1: str, city2: str) -> float:
    """利用两个地区的城市名称计算球面距离

    Args:
        city1 (str): 地区1的城市名称
        city2 (str): 地区2的城市名称

    Returns:
        float: 球面距离，单位：km
    """
    city1_lat, city1_lon = coordinate(city1)
    city2_lat, city2_lon = coordinate(city2)
    return haversine(city1_lat, city1_lon, city2_lat, city2_lon)
