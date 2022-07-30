### lookup

```python
lookup(name)
```

根据地名简称查找全称，具体用法参照[示例](../examples/cp_lookup.md#lookup)。

**Arguments**:

- `name` : str
  
  待查找地名

- `level` : str | None

  查询区域的行政等级，包括province、city、county三级。默认值为None，当为None时不区分查找范围，因此很可能出现重名错误

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

- `level` : str | None

  查询区域的行政等级，包括province、city、county三级。默认值为None，当为None时不区分查找范围，因此很可能出现重名错误

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

- `level` : str | None

  查询区域的行政等级，包括province、city、county三级。默认值为None，当为None时不区分查找范围，因此很可能出现重名错误

**Returns**:

- `coordinate` : tuple[float, float]

  行政中心经纬度

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

- `level1` : str | None

  查询区域的行政等级，包括province、city、county三级。

- `level2` : str | None

  查询区域的行政等级，包括province、city、county三级。

**Returns**:

- `distance` : float
  
  两地之间的球面距离，单位：km

**Note**:

  level1、level2默认值为None，当为None时不区分查找范围，因此很可能出现重名错误