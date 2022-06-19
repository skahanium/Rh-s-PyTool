# cp_lookup模块

## cp_lookup.cp_lookup

cp_lookup.cp_lookup是一个与地市级、省级行政区名称相关的模块，可以用于处理一些与这两级行政区名称相关的信息。

从模块中导入函数：

```python
>>>from cp_lookup.cp_lookup import ptwoc, ctwop, fillup_city
```

### ptwoc

已知省名，得到其下辖所有地市级行政区：

```python
>>>print(ptwoc("四川省"))

('成都市', '自贡市', '攀枝花市', '泸州市', '德阳市', '绵阳市', '广元市', '遂宁市', '内江市', '乐山市', '南充市', '宜宾市', '广安市', '达州市', '资阳市', '眉山市', '巴中市', '雅安市', '阿坝藏族羌族自治州', '甘孜藏族自治州', '凉山彝族自治州')
```

### ctwop

已知市名，得到其所属省份的名称：

```python
>>>print(ctwop("成都市"))

四川省
```

### fillup_city

已知地级行政区简称，将其补充为全称：

```python
>>>print(fillup_city("绵阳"))

绵阳市
```

## cp_lookup.add_ll

cp_lookup.add_ll是一个与地市级、省级行政区地理位置相关的模块，可以查询此两级行政区域行政中心坐标的信息。

从模块中导入函数：

```python
>>>from cp_lookup.add_ll import pro_info, city_info
```

### pro_info

查询省级行政区行政中心坐标：

```python
>>>print(pro_info("河南省"))

(113.75322, 34.76571)
```

### city_info

查询地级行政区行政中心坐标：

```python
>>>print(city_info("杭州市"))

(120.15515, 30.27415)
```

## cp_lookup.mygeo

cp_loolup.mygeo是一个计算球面距离的模块，可以用于计算不同区域之间的远近。

从模块中导入函数：

```python
>>>from cp_lookup.mygeo import haversine, dist
```

### haversine

半正矢函数，利用两个地点的经纬度计算球面距离。

```python
>>>print(haversine(112.355160, 28.553910, 110.199890, 20.044220))

971.0438178627454
```

### dist

利用区域名或地区经纬度计算两地间的球面距离。（区域名必须属于地级或省级的行政区域）

```python
>>>print(dist("益阳市", "海口市"))

971.0438178627454

>>>print(dist("益阳市", 110.199890, 20.044220))

971.0438178627454

>>>print(dist(110.199890, 20.044220, "益阳市"))

971.0438178627454
```
