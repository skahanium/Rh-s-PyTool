# cp_lookup模块

**注：本模块中所有级别的所有行政区域都属于中国大陆省、市两级的行政区域。**

## cp_lookup.cp_lookup

### ptwoc

```python
ptwoc(province)
```

根据省行政区的名称获取该省所有地市级行政区的名称。

**Arguments**:

- `province` : str
  
  省行政区名称

**Returns**:

- `cities` : tuple of strings
  
  目标省份所有地级行政区的名称。

### ctwop

```python
ctwop(city)
```

根据地级行政区的名称（及其缩写）给出省行政区的名称。

**Arguments**:

- `city` : str
  
  地级行政区名称

**Returns**:

- `province` : str
  
  目标城市所属的省级行政区名称。

### fillup_city

```python
fillup_city(city)
```

将地级行政区的缩写替换为全名

**Arguments**:

- `city` : str
  
  地级行政区名称（缩写或全名）

**Returns**:

- `city` : str
  
  地级行政区的全名。

## cp_lookup.add_ll

### pro_info

```python
pro_info(province)
```

根据省行政区名称获得纬度和经度。

**Arguments**:

- `province` : str
  
  省行政区名称

**Returns**:

- `coordinate` : tuple of floats
  
  目标省份行政中心的经纬度

### city_info

```python
city_info(city)
```

根据市辖区名称获得纬度和经度。

**Arguments**:

+ `city` : str
  
  城市名

**Returns**:

- `coordinate` : tuple of floats
  
  目标城市行政中心的经纬度

## cp_lookup.mygeo

### haversine

```python
haversine(lon1, lat1, lon2, lat2)
```

使用两个区域的经度和纬度计算二者间球面距离。

**Arguments**:

- `lon1` : float
  
  区域1经度

- `lat1` : float
  
  区域1纬度

- `lon2` : float
  
  区域2经度

- `lat2` : float
  
  区域2纬度

**Returns**:

- `distance` : float
  
  返回两地之间的球面距离，单位：km

### dist

```python
dist(city1, city2)
```

使用两个城市的名称计算二者间的球面距离。

**Arguments**:

- `city1` : str
  
  城市1

- `city2` : str
  
  城市2

**Returns**:

- `distance` : float
  
  返回两地之间的球面距离，单位：km


```python
dist(city, lon, lat)
```

使用一个地区的城市名称和另一个地区的经度和纬度计算二者间球面距离。

**Arguments**:

- `city` : str
  
  城市1

- `lon` : float
  
  区域2的经度

- `lat` : float
  
  区域2的维度

**Returns**:

- `distance` : float
  
  返回两地之间的球面距离，单位：km


```python
dist(lon, lat, city)
```

使用一个地区的经度和纬度和另一个地区的城市名称计算二者间球面距离。

**Arguments**:


- `lon` : float
  
  区域1的经度

- `lat` : float
  
  区域1的维度

- `city` : str
  
  城市2

**Returns**:

- `distance` : float
  
  返回两地之间的球面距离，单位：km