## index_calmeth.non_dimension

### tiny_convert

```python
tiny_convert(ndarray, mode, change_list)
```

将负向指标转化为正向指标，具体用法参照[示例](../examples/index_calmeth.md#tiny_convert)。

**Arguments**:

- `ndarray` : np.ndarray
  
  待转换数据集。

- `mode` : str
  
  转换模式。mode='0' 是 *1/x* 模式，而mode='1'为*max(x)-x*模式。

- `change_list` : list of ints
  
  待转换指标下标构成的列表。

**Returns**:

- `result_array` : np.ndarray
  
  返回全部转换为正向指标的数据集。

---
### middle_convert

```python
middle_convert(ndarray, change_list, best_value)
```

将中间型指标转换为正向指标，具体用法参照[示例](../examples/index_calmeth.md#middle_convert)。

**Arguments**:

- `ndarray` : np.ndarray:
  
  待转换数据集。

- `change_list` : list of ints
  
  待转换指标下标构成的列表。

- `best_value` : list of ints or floats
  
  待转换指标的最佳值组成的列表。

**Returns**:

- `result_array` : np.ndarray
  
  返回全部转换为正向指标的数据集。

---
### moderate_convert

```python
moderate_convert(ndarray, change_list, low_limit, high_limit)
```

将适度型指标转换为正向指标，具体用法参照[示例](../examples/index_calmeth.md#moderate_convert)。

**Arguments**:

- `ndarray` : np.ndarray
  
  待转换数据集。

- `change_list` : list of ints
  
  待转换指标下标构成的列表。

- `low_limit` : list of ints or floats
  
  待转换指标适度区间的下限组成的列表。

- `high_limit` : list of ints or floats
  
  待转换指标适度区间的上限组成的列表。

**Returns**:

- `result_array` : np.ndarray
  
  返回全部转换为正向指标的数据集。

---
### toone

```python
toone(origin_array, mode)
```

将待转换数据进行归一化，具体用法参照[示例](../examples/index_calmeth.md#toone)。

**Arguments**:

- `origin_array` : np.ndarray
  
  待转换数据集

- `mode` : str
  
  转换模式。mode='0'为归一化，mode='1'为平均归一化，mode='2'为标准化，mode='3'为向量归一化。

**Returns**:

- `result_array` : np.ndarray
  
  返回归一化的数据集。

---

---
## index_calmeth.weights
### critic

```python
critic(origin_array)
```

对于给定指标数据使用critic方法计算各指标权重，具体用法参照[示例](../examples/index_calmeth.md#critic)。

**Arguments**:

- `origin_array` : np.ndarray
  
  给定指标数据。

**Returns**:

- `critic_weights` : np.ndarray
  
  返回得到的critic权重。

---
### ewm

```python
ewm(origin_array)
```

对于给定指标数据使用熵权法计算各指标权重，具体用法参照[示例](../examples/index_calmeth.md#ewm)。

**Arguments**:

- `origin_array` : np.ndarray
  
  给定指标数据。

**Returns**:

- `critic_weights` : np.ndarray
  
  返回得到的熵权法权重。

---
### stddev

```python
std(origin_array)
```

对于给定指标数据使用标准离差法计算各指标权重，具体用法参照[示例](../examples/index_calmeth.md#stddev)。

**Arguments**:

- `origin_array` : np.ndarray
  
  给定指标数据。

**Returns**:

- `stddev_weights` : np.ndarray
  
  返回得到的标准离差法权重。

---

---
## index_calmeth.rating_method
### rsr

```python
rsr(data_origin, weights)
```

使用整次秩和比方法对指标数据进行综合评分（注：该方法只涉及rsr的打分部分，不包含后续的确认分布、直线回归以及排序分档），具体用法参照[示例](../examples/index_calmeth.md#rsr)。

**Arguments**:

- `data_origin` : np.ndarray
  
  正向化之后的指标数据

- `weights` : list(np.ndarray) of ints or floats
  
  指标权重数据

**Returns**:

- `rsr_score` : np.ndarray
  
  参数无误的情况下，返回rsr评分。

---
### ni_rsr

```python
ni_rsr(data_origin, weights)
```

使用非整次秩和比方法对指标数据进行综合评分（注：该方法同样只涉及rsr的打分部分，不包含后续的确认分布、直线回归以及排序分档），具体用法参照[示例](../examples/index_calmeth.md#ni_rsr)。

**Arguments**:

- `data_origin` : np.ndarray
  
  正向化之后的指标数据

- `weights` : list(np.ndarray) of ints or floats
  
  指标权重数据

**Returns**:

- `rsr_score` : np.ndarray
  
  参数无误的情况下，返回ni_rsr评分。

---
### topsis

```python
topsis(data_origin, weights)
```

使用优劣解距离法(Topsis, Technique for Order Preference by Similarity to an Ideal Solution)对指标数据进行综合评分，具体用法参照[示例](../examples/index_calmeth.md#topsis)。

**Arguments**:

- `data_origin` : np.ndarray
  
  正向化之后的指标数据

- `weights` : list(np.ndarray) of ints or floats
  
  指标权重数据

**Returns**:

- `topsis_score` : np.ndarray
  
  参数无误的情况下，返回topsis评分。
