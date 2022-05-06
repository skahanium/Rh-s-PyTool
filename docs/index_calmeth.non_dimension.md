<a id="index_calmeth.non_dimension"></a>

# index\_calmeth.non\_dimension

<a id="index_calmeth.non_dimension.tiny_convert"></a>

#### tiny\_convert

```python
def tiny_convert(ndarray: np.ndarray, mode: str,
                 change_list: list[int]) -> np.ndarray | None
```

极小型指标转化为极大型指标

**Arguments**:

- `ndarray` _np.ndarray_ - 待转化数据
- `mode` _str_ - 转化模式。mode='0'时为1/x模式，mode='1'时为max(x)-x模式
- `change_list` _list[int]_ - 待转化列下标组成的列表
  

**Returns**:

  np.ndarray | None: 若参数无误，返回转化后的数据组，否则返回None

<a id="index_calmeth.non_dimension.middle_convert"></a>

#### middle\_convert

```python
def middle_convert(ndarray: np.ndarray, change_list: list[int],
                   best_value: list[num]) -> np.ndarray | None
```

中间型指标转化为极大型指标

**Arguments**:

- `ndarray` _np.ndarray_ - 待转化数据
- `change_list` _list[int]_ - 待转化列下标组成的列表
- `best_value` _list[int|float]_ - 待转化列的最优值组成的列表。由于每个列的最优值不同，所以需要提供
  

**Returns**:

  np.ndarray | None: 若参数无误，返回转化后的数据组，否则返回None

<a id="index_calmeth.non_dimension.moderate_convert"></a>

#### moderate\_convert

```python
def moderate_convert(ndarray: np.ndarray, change_list: list[int],
                     low_limit: list[num],
                     high_limit: list[num]) -> np.ndarray | None
```

适度性指标转化为极大型指标

**Arguments**:

- `ndarray` _np.ndarray_ - 待转化数据
- `change_list` _list[int]_ - 待转化列下标组成的列表
- `low_limit` _list[int|float]_ - 待转化列的最优区间下限组成的列表。由于每个列的最优区间下限不同，所以需要提供
- `high_limit` _list[int|float]_ - 待转化列的最优区间上限组成的列表。由于每个列的最优区间上限不同，所以需要提供
  

**Returns**:

  np.ndarray | None: 若参数无误，返回转化后的数据组，否则返回None

<a id="index_calmeth.non_dimension.toone"></a>

#### toone

```python
def toone(origin_array: np.ndarray, mode: str) -> np.ndarray | None
```

多种矩阵归一化方法

**Arguments**:

- `ndarray` _np.ndarray_ - 待转化数据
- `mode` _str_ - 转化模式。mode='0'时为归一化，mode='1'时为平均归一化，mode='2'时为标准化，mode='3'时为向量归一化
  

**Returns**:

  np.ndarray | None: 若参数无误，返回转化后的数据组，否则返回None

