# Table of Contents

- [cp_lookup.cp_lookup](#cp_lookup.cp_lookup)
  
  - [ptwoc](#cp_lookup.cp_lookup.ptwoc)
  - [ctwop](#cp_lookup.cp_lookup.ctwop)
  - [fillup_city](#cp_lookup.cp_lookup.fillup_city)

- [cp_lookup.add_ll](#cp_lookup.add_ll)
  
  - [pro_info](#cp_lookup.add_ll.pro_info)
  - [city_info](#cp_lookup.add_ll.city_info)

- [cp_lookup.mygeo](#cp_lookup.mygeo)
  
  - [haversine](#cp_lookup.mygeo.haversine)
  - [dist](#cp_lookup.mygeo.dist)
  - [dist2](#cp_lookup.mygeo.dist2)

- [index_calmeth.non_dimension](#index_calmeth.non_dimension)
  
  - [tiny_convert](#index_calmeth.non_dimension.tiny_convert)
  - [middle_convert](#index_calmeth.non_dimension.middle_convert)
  - [moderate_convert](#index_calmeth.non_dimension.moderate_convert)
  - [toone](#index_calmeth.non_dimension.toone)

- [index_calmeth.critic](#index_calmeth.critic)
  
  - [Critic](#index_calmeth.critic.Critic)
    - [variability](#index_calmeth.critic.Critic.variability)
    - [conflict](#index_calmeth.critic.Critic.conflict)
    - [weights](#index_calmeth.critic.Critic.weights)

- [index_calmeth.rsr](#index_calmeth.rsr)
  
  - [Rsr](#index_calmeth.rsr.Rsr)
    - [score_matrix1](#index_calmeth.rsr.Rsr.score_matrix1)
    - [score_matrix2](#index_calmeth.rsr.Rsr.score_matrix2)

- [index_calmeth.topsis](#index_calmeth.topsis)
  
  - [Topsis](#index_calmeth.topsis.Topsis)
    - [score_matrix](#index_calmeth.topsis.Topsis.score_matrix)

# cp_lookup.cp_lookup

#### ptwoc

```python
def ptwoc(prov: str) -> tuple[str, ...] | None
```

根据省级行政区名称获取省级下的所有市级行政区名称

**Arguments**:

- `prov` *str* - 省级行政区名称

**Returns**:

    tuple[str, ...] | None: 目标省份下辖所有地级行政区的名称。如果没有找到查询的省级行政区，返回None

#### ctwop

```python
def ctwop(city: str) -> str | None
```

根据地级行政区域名（及其简称）给出所属省级行政区名

**Arguments**:

- `city` *str* - 地级行政区名称

**Returns**:

    str | None: 目标地市所属省级行政区名称。如果没有找到查询的地级行政区，返回None

#### fillup_city

```python
def fillup_city(city: str) -> str | None
```

将地级行政区简称替换为全称

**Arguments**:

- `city` *str* - 地级行政区的名称（简称或全称）

**Returns**:

    str | None: 地级行政区的全称。如果没有找到查询的地级行政区，返回None

---

# cp_lookup.add_ll

#### pro_info

```python
def pro_info(province: str) -> tuple[float, float]
```

根据省级行政区名称获取经纬度

**Arguments**:

- `province` *str* - 省级行政区名称

**Returns**:

    tuple[float, float]: 得到的经度和纬度

#### city_info

```python
def city_info(city: str) -> tuple[float, float]
```

根据市级行政区名称获取经纬度

**Arguments**:

- `city` *str* - 市级行政区名称

**Returns**:

    tuple[float, float]: 得到的经度和纬度

---

# cp_lookup.mygeo

#### haversine

```python
def haversine(lon1: float, lat1: float, lon2: float, lat2: float) -> float
```

利用两个地点的经纬度计算球面距离

**Arguments**:

- `lon1` *float* - 地区1的经度
- `lat1` *float* - 地区1的纬度
- `lon2` *float* - 地区2的经度
- `lat2` *float* - 地区2的纬度

**Returns**:

    float: 球面距离，单位：km

#### dist

```python
def dist(city1: str, city2: str) -> float
```

利用两个地区的城市名称计算球面距离

**Arguments**:

- `city1` *str* - 地区1的城市名称
- `city2` *str* - 地区2的城市名称

**Returns**:

    float:  球面距离，单位：km

#### dist2

```python
def dist2(city: str, lon: float, lat: float) -> float
```

利用一个地区的城市名和另一个地区的经纬度计算球面距离

**Arguments**:

- `city` *str* - 地区1的城市名称
- `lon` *float* - 地区2的经度
- `lat` *float* - 地区2的纬度

**Returns**:

    float: 球面距离，单位：km

---

# index_calmeth.non_dimension

#### tiny_convert

```python
def tiny_convert(ndarray: np.ndarray, mode: str,
                 change_list: list[int]) -> np.ndarray | None
```

极小型指标转化为极大型指标

**Arguments**:

- `ndarray` *np.ndarray* - 待转化数据
- `mode` *str* - 转化模式。mode='0'时为1/x模式，mode='1'时为max(x)-x模式
- `change_list` *list[int]* - 待转化列下标组成的列表

**Returns**:

    np.ndarray | None: 若参数无误，返回转化后的数据组，否则返回None

#### middle_convert

```python
def middle_convert(ndarray: np.ndarray, change_list: list[int],
                   best_value: list[num]) -> np.ndarray | None
```

中间型指标转化为极大型指标

**Arguments**:

- `ndarray` *np.ndarray* - 待转化数据
- `change_list` *list[int]* - 待转化列下标组成的列表
- `best_value` *list[int|float]* - 待转化列的最优值组成的列表。由于每个列的最优值不同，所以需要提供

**Returns**:

    np.ndarray | None: 若参数无误，返回转化后的数据组，否则返回None

#### moderate_convert

```python
def moderate_convert(ndarray: np.ndarray, change_list: list[int],
                     low_limit: list[num],
                     high_limit: list[num]) -> np.ndarray | None
```

适度性指标转化为极大型指标

**Arguments**:

- `ndarray` *np.ndarray* - 待转化数据
- `change_list` *list[int]* - 待转化列下标组成的列表
- `low_limit` *list[int|float]* - 待转化列的最优区间下限组成的列表。由于每个列的最优区间下限不同，所以需要提供
- `high_limit` *list[int|float]* - 待转化列的最优区间上限组成的列表。由于每个列的最优区间上限不同，所以需要提供

**Returns**:

    np.ndarray | None: 若参数无误，返回转化后的数据组，否则返回None

#### toone

```python
def toone(origin_array: np.ndarray, mode: str) -> np.ndarray | None
```

多种矩阵归一化方法

**Arguments**:

- `ndarray` *np.ndarray* - 待转化数据
- `mode` *str* - 转化模式。mode='0'时为归一化，mode='1'时为平均归一化，mode='2'时为标准化，mode='3'时为向量归一化

**Returns**:

np.ndarray | None: 若参数无误，返回转化后的数据组，否则返回None

---

# index_calmeth.critic

## Critic Objects

```python
class Critic(ndarray: np.ndarray)
```

对传入的np.ndarray类型数据进行critic权重计算。

初始化np.ndarray对象并进行归一化。

#### variability

```python
def variability() -> np.ndarray
```

**Returns**:

    np.ndarray: 获取指标变异性数据

#### conflict

```python
def conflict() -> np.ndarray
```

**Returns**:

    np.ndarray: 获取指标冲突性数据

#### weights

```python
def weights() -> np.ndarray
```

**Returns**:

    np.ndarray: 通过变异性指标和冲突性指标计算critic权重

---

# index_calmeth.rsr

## Rsr Objects

```python
class Rsr(ndarray: np.ndarray)
```

对传入的np.ndarray数据进行rsr打分。

初始化np.ndarray数据，得到其长宽数据。

#### score_matrix1

```python
def score_matrix1(weights: np.ndarray, bv_list: list[num]) -> np.matrix | None
```

整次秩和比法计算得分，bv_list是由各指标正向最佳贡献值构成的列表

**Arguments**:

- `bv_list` *list[int|float]* - 正向最佳值列表

**Returns**:

    np.matrix | None: 若参数无误，返回转化后的数据组，否则返回None

#### score_matrix2

```python
def score_matrix2(weights: np.ndarray, bv_list: list[num]) -> np.matrix | None
```

非整次秩和比法计算得分，bv_list是由各指标正向最佳贡献值构成的列表

**Arguments**:

- `bv_list` *list[int|float]* - 正向最佳值列表

**Returns**:

    np.matrix | None: 若参数无误，返回转化后的数据组，否则返回None

---

# index_calmeth.topsis

## Topsis Objects

```python
class Topsis(ndarray: np.ndarray)
```

对传入对np.ndarray数据进行topsis打分。

初始化np.ndarray数据，得到其长宽数据。

#### score_matrix

```python
def score_matrix(weights: np.ndarray, bv_list: list[num]) -> np.ndarray | None
```

计算得分矩阵。weights为权重矩阵,bv_list为正向最佳值列表

**Arguments**:

- `weights` *np.ndarray* - 权重数组
- `bv_list` *list[int|float]* - 正向最佳值列表

**Returns**:

    np.ndarray: 若参数无误，返回转化后的数据组，否则返回None