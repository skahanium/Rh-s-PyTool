区域名处理模块，可根据区域名进行地名补全、查找上级行政区地名、查找行政中心坐标等操作，也可以根据两地区域名计算二者之间的球面距离。

**注：本模块中所有行政区域都属于中国省、市、区县三级行政划分之一。**

从模块中导入函数：

```python
>>>from cp_lookup import lookup, belongs_to, coordinate, haversine, dist
```

### lookup

已知某个区域名简称，获取其全称，接口说明参照[api](../api/cp_lookup.md#lookup)。

```python
>>>print(lookup("凉山"))

凉山彝族自治州
```

如果区域名简称存在重复，比如承德市和承德县、铁岭市和铁岭县，以及海南省、海南区、海南藏族自治州，直接查询“承德”、“铁岭”或“海南”会报错。

```python
>>>print(lookup("海南"))

地名重复或有误！
AttributeError: 'Addr' object has no attribute 'addr'
```

可以使用`level`参数从行政等级上对查询范围进行区分。
```python
>>>print(lookup("海南", level="city"))

海南藏族自治州
```

对于非省一级的行政区，也可以在前面加上上级行政区的全称或简称以进行区分。
```python
>>>print(lookup("青海海南"))

海南藏族自治州
```

---
### belongs_to

已知区域名，得到其所上级的名称，接口说明参照[api](../api/cp_lookup.md#belongs_to)。

```python
>>>print(belongs_to("成都市"))

四川省
```
同样，面对可能重复的区域简称，使用`level`参数或上级行政区名称进行区分。
```python
>>>print(belongs_to("长沙"))

AreaNameError: 地名重复或有误！！！

>>>print(belongs_to("长沙", level="city"))

湖南省

>>>print(belongs_to("长沙", level="county"))

长沙市

>>>print(belongs_to("长沙长沙")) # 注：“长沙长沙会被解析为长沙市的长沙县，因此其上级行政区为长沙市”

长沙市
```

---
### coordinate

已知区域名，得到其行政中心的坐标，遇到重复的区域名简称处理方式同上，接口说明参照[api](../api/cp_lookup.md#coordinate)。

```python
>>>print(coordinate("绵阳"))

(31.467459, 104.679004)
```

---
### dist

利用区域名或地区经纬度计算两地间的球面距离，遇到重复的区域名简称处理方式同上，接口说明参照[api](../api/cp_lookup.md#dist)。

```python
>>>print(dist("益阳市", "海口市"))

971.1062161818321
```