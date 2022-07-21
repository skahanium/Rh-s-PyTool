### lookup

```python
lookup(name)
```

根据地名简称查找全称，具体用法参照[示例](../examples/cp_lookup.md#lookup)。

**Arguments**:

- `name` : str
  
  待查找地名

**Returns**:

- `fullname` : str
  
  地名全称

---
### belongs_to

```python
belongs_to(name)
```
根据地名查找其上级行政区名称，具体用法参照[示例](../examples/cp_lookup.md#belongs_to)。

**Arguments**:

- `name` : str

  待查找地名

**Returns**:

- `father_area` : str

  上级行政区名称

---
### coordinate
```python
coordinate(name)
```
根据区域名全称得到其行政中心的坐标，具体用法参照[示例](../examples/cp_lookup.md#coordinate)。

**Arguments**:

- `name` : str

  待查找地名

**Returns**:

- `coordinate` : tuple[float, float]

  行政中心经纬度

---
### haversine

```python
haversine(lat1, lon1, lat2, lon2)
```

使用两个区域的经度和纬度计算二者间球面距离，具体用法参照[示例](../examples/cp_lookup.md#haversine)。

**Arguments**:

- `lat1` : float
  
  区域1纬度

- `lon1` : float
  
  区域1经度

- `lat2` : float
  
  区域2纬度

- `lon2` : float
  
  区域2经度

**Returns**:

- `distance` : float
  
  两地之间的球面距离，单位：km

---
### dist

```python
dist(city1, city2)
```

使用两个城市的名称计算二者间的球面距离，具体用法参照[示例](../examples/cp_lookup.md#dist)

**Arguments**:

- `city1` : str
  
  城市1

- `city2` : str
  
  城市2

**Returns**:

- `distance` : float
  
  两地之间的球面距离，单位：km