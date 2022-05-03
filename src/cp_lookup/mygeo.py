from math import radians, cos, sin, asin, sqrt
import cp_lookup.add_ll as cal


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


def dist(city1: str, city2: str) -> float:
    """    利用两个地区的城市名称计算球面距离

    Args:
        city1 (str): 地区1的城市名称
        city2 (str): 地区2的城市名称

    Returns:
        float: 球面距离，单位：km
    """
    return haversine(float(cal.cities[city1][1]), float(cal.cities[city1][2]), float(cal.cities[city2][1]), float(cal.cities[city2][2]))


def dist2(city: str, lon: float, lat: float) -> float:
    """利用一个地区的城市名和另一个地区的经纬度计算球面距离

    Args:
        city (str): 地区1的城市名称
        lon (float): 地区2的经度
        lat (float): 地区2的纬度

    Returns:
        float: 球面距离，单位：km
    """
    return haversine(float(cal.cities[city][1]), float(cal.cities[city][2]), lon, lat)
