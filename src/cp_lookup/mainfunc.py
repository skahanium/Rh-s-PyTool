from math import radians, cos, sin, asin, sqrt
from .classdefine import Addr
from .special import ZXCITIES



def lookup(name: str, level: str | None = None) -> str | None:
    """根据地名简称查找全称

    Args:
        name (str): 待查找地名
        level (str | None): 查询区域的行政等级，包括province、city、county三级。默认值为None，当为None时不区分查找范围，因此很可能出现重名错误

    Returns:
        str | None: 地名全称
    """
    if name in ZXCITIES.keys():
        new_name = ZXCITIES[name]
        obj_area = Addr(new_name, level="province").addr
    else:
        try:
            obj_area = Addr(name, level=level).addr
        except Exception as e:
            raise ValueError(f"无法找到{name}的全称") from e
    return None if len(obj_area) == 0 else obj_area[0, "name"]


def belongs_to(name: str, level: str | None = None) -> str | None:
    """根据地名查找其上级行政区名称

    Args:
        name (str): 待查找地名
        level (str | None): 查询区域的行政等级，包括province、city、county三级。默认值为None，当为None时不区分查找范围，因此很可能出现重名错误

    Returns:
        str | None: 上级行政区全称
    """
    if name in ZXCITIES.keys():
        new_name = ZXCITIES[name]
        obj_area = Addr(new_name, level="province")
    else:
        try:
            obj_area = Addr(name, level=level)
        except Exception as e:
            raise ValueError(f"无法找到{name}的上级行政区") from e
    return obj_area._belongs_to()


def coordinate(name: str, level: str | None = None) -> tuple[float, float] | None:
    """根据区域名得到其行政中心的坐标

    Args:
        name (str): 行政区名称
        level (str | None): 查询区域的行政等级，包括province、city、county三级。默认值为None，当为None时不区分查找范围，因此很可能出现重名错误

    Returns:
        tuple[float, float]: 行政中心经纬度
    """
    if name in ZXCITIES.keys():
        new_name = ZXCITIES[name]
        obj_area = Addr(new_name, level="province")
    else:
        try:
            obj_area = Addr(name, level=level)
            lat, lon = obj_area._coordinate()
        except Exception as e:
            raise ValueError(f"无法找到{name}的坐标") from e
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
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # haversine（半正矢）公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371 
    return c * r


def dist(
    name1: str, name2: str, level1: str | None = None, level2: str | None = None
) -> float:
    """利用两个地区的城市名称计算球面距离

    Args:
        name1 (str): 地区1的城市名称
        name2 (str): 地区2的城市名称
        level1 (str | None): 查询地区1的行政等级，包括province、city、county三级。
        level2 (str | None): 查询地区2的行政等级，包括province、city、county三级。

    Returns:
        float: 球面距离，单位：km

    Note:
        level1、level2默认值为None，当为None时不区分查找范围，因此很可能出现重名错误。
    """
    try:
        city1_lat: float
        city1_lon: float
        city1_lat, city1_lon = coordinate(name1, level=level1)
        city2_lat: float
        city2_lon: float
        city2_lat, city2_lon = coordinate(name2, level=level2)
        return haversine(city1_lat, city1_lon, city2_lat, city2_lon)
    except Exception as e:
        raise ValueError(f"无法计算{name1}与{name2}之间的球面距离") from e
