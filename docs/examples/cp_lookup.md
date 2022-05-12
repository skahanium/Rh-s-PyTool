# cp_lookup模块

## cp_lookup.cp_lookup
从模块中导入函数：
```python
>>>from cp_lookup.cp_lookup import ptwoc, ctwop, fillup_city
```

### ptwoc
```python
>>>print(ptwoc("四川省"))
('成都市', '自贡市', '攀枝花市', '泸州市', '德阳市', '绵阳市', '广元市', '遂宁市', '内江市', '乐山市', '南充市', '宜宾市', '广安市', '达州市', '资阳市', '眉山市', '巴中市', '雅安市', '阿坝藏族羌族自治州', '甘孜藏族自治州', '凉山彝族自治州')
```

### ctwop
```python
>>>print(ctwop("成都市"))
四川省
```

### fillup_city
```python
>>>print(fillup_city("绵阳"))
绵阳市
```


## cp_lookup.add_ll
从模块中导入函数：
```python
>>>from cp_lookup.add_ll import pro_info, city_info
```

### pro_info
```python
>>>print(pro_info("河南省"))
(113.75322, 34.76571)
```

### city_info
```python
>>>print(city_info("杭州市"))
(120.15515, 30.27415)
```


## cp_loolup.mygeo
从模块中导入函数：
```python
>>>from cp_lookup.mygeo import haversine, dist, dist2
```

### haversine
```python
>>>print(haversine(112.355160, 28.553910, 110.199890, 20.044220))
971.0438178627454
```

### dist
```python
>>>print(dist("益阳市", "海口市"))
971.0438178627454
```

### dist2
```python
>>>print(dist2("益阳市", 110.199890, 20.044220))
971.0438178627454
```