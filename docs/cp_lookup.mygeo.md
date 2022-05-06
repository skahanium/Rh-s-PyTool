<a id="cp_lookup.mygeo"></a>

# cp\_lookup.mygeo

<a id="cp_lookup.mygeo.haversine"></a>

#### haversine

```python
def haversine(lon1: float, lat1: float, lon2: float, lat2: float) -> float
```

利用两个地点的经纬度计算球面距离

**Arguments**:

- `lon1` _float_ - 地区1的经度
- `lat1` _float_ - 地区1的纬度
- `lon2` _float_ - 地区2的经度
- `lat2` _float_ - 地区2的纬度
  

**Returns**:

- `float` - 球面距离，单位：km

<a id="cp_lookup.mygeo.dist"></a>

#### dist

```python
def dist(city1: str, city2: str) -> float
```

利用两个地区的城市名称计算球面距离

**Arguments**:

- `city1` _str_ - 地区1的城市名称
- `city2` _str_ - 地区2的城市名称
  

**Returns**:

- `float` - 球面距离，单位：km

<a id="cp_lookup.mygeo.dist2"></a>

#### dist2

```python
def dist2(city: str, lon: float, lat: float) -> float
```

利用一个地区的城市名和另一个地区的经纬度计算球面距离

**Arguments**:

- `city` _str_ - 地区1的城市名称
- `lon` _float_ - 地区2的经度
- `lat` _float_ - 地区2的纬度
  

**Returns**:

- `float` - 球面距离，单位：km

