from math import radians, cos, sin, asin, sqrt
import cp_lookup.add_ll as cal


def haversine(lon1, lat1, lon2, lat2):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
    """
    利用两个地点的经纬度计算球面距离
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


def dist(city1, city2):
    '''
    利用两个地区的城市名计算球面距离
    '''
    distance = haversine(float(cal.cities[city1][1]), float(cal.cities[city1][2]),
                         float(cal.cities[city2][1]), float(cal.cities[city2][2]))
    return distance


def dist2(city, lon, lat):
    """
    利用一个地区的城市名和另一个地区的经纬度计算球面距离
    """
    distance = haversine(float(cal.cities[city][1]), float(cal.cities[city][2]),
                         lon, lat)
    return distance
