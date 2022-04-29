# cp_lookup模块

## cp_lookup

---

导入模块

```python
>>>import cp_lookup.cp_lookup as cc
```

根据省级行政区域名（及其简称）给出下辖所有地级行政区域名单

```python
>>>cc.ptwoc("四川省")

('成都市',
 '自贡市',
 '攀枝花市',
 '泸州市',
 '德阳市',
 '绵阳市',
 '广元市',
 '遂宁市',
 '内江市',
 '乐山市',
 '南充市',
 '宜宾市',
 '广安市',
 '达州市',
 '资阳市',
 '眉山市',
 '巴中市',
 '雅安市',
 '阿坝藏族羌族自治州',
 '甘孜藏族自治州',
 '凉山彝族自治州')
```

根据地级行政区域名（及其简称）给出所属省级行政区名

```python
>>>cc.ctwop("成都市")

'四川省'
```

对单个地级行政区名单进行名称补全

```python
>>>cc.fillup_city("成都")

'成都市'
```

## add_ll

---

导入模块

```python
>>>import cp_lookup.add_ll as cal
```

返回省级行政区的经度与纬度

```python
>>>cal.pro_info("北京市")

(116.40717, 39.90469)
```

返回地级行政区的经度与纬度

```python
>>>cal.city_info("杭州市")

(120.15515, 30.27415)
```

## mygeo

---

导入模块

```python
>>>import cp_lookup.mygeo as clm
```

利用两个地区的经纬度计算球面距离（单位：km）

```python
>>>clm.haversine(106.550730, 29.564710, 115.464590, 38.873960)

1318.8211071873566
```

利用两个地区名计算球面距离（单位：km）

```python
>>>clm.dist('广州市', '昆明市')

1077.0043812208146
```

利用一个地区名和另一个地区的经纬度计算球面距离（单位：km）

```python
>>>clm.dist2('广州市', 106.550730, 29.564710)

979.1356992283953
```

# index_calmeth模块

## NonDimension

---

导入模块

```python
>>>import index_calmeth.non_dimension as icn
>>>import numpy as np

>>>test_data = np.random.rand(5, 6)
```

极小型指标转化为极大型指标

```python
>>>icn.tiny_convert(test_data, mode='0', change_list=[2, 3])
```

中间型型指标转化为极大型指标

```python
>>>icn.middle_convert(test_data, change_list=[2, 3], best_value=[0.5, 0.5])
```

区域型指标转化为极大型指标

```python
>>>icn.moderate_convert(test_data, [0, 1, 2, 3, 4], [0.4, 0.4, 0.4, 0.4, 0.4], [0.6, 0.6, 0.6, 0.6, 0.6])
```

指标归一化

```python
>>>icn.toone(test_data, mode='0')
```

## 

## critic

---

导入模块

```python
>>>import index_calmeth.critic as icc
```

对数组、矩阵对象进行Critic类的实例化

```python
>>>critic = icc.Critic(test_data)
```

得到指标critic权重数据

```python
>>>critic.weights()
```



## rsr

---

导入模块

```python
>>>import index_calmeth.rsr as icr
```

对数组、矩阵对象进行Rsr类的实例化。

```python
>>>rsr = icr.Rsr(test_data)
```

计算整次秩和比法得分。weights为权重矩阵，bv_list是由各指标正向最佳贡献值构成的列表

```python
>>>rsr.score_matrix1(critic.weights(), [0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
```

计算非整次秩和比法得分。weights为权重矩阵，bv_list是由各指标正向最佳贡献值构成的列表

```python
>>>rsr.score_matrix2(critic.weights(), [0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
```

### 

## topsis

---

导入模块

```python
>>>import index_calmeth.topsis as ict
```

对数组、矩阵对象进行Topsis类实例化

```python
>>>topsis = ict.Topsis(test_data)
```

计算优劣解距离法得分。weights为权重矩阵，bv_list是由各指标正向最佳贡献值构成的列表

```python
>>>topsis.score_matrix(critic.weights(), [0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
```
