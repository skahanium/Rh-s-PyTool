<a id="cp_lookup.cp_lookup"></a>

# cp\_lookup.cp\_lookup

<a id="cp_lookup.cp_lookup.ptwoc"></a>

#### ptwoc

```python
def ptwoc(prov: str) -> tuple[str, ...] | None
```

根据省级行政区名称获取省级下的所有市级行政区名称

**Arguments**:

- `prov` _str_ - 省级行政区名称
  

**Returns**:

  tuple[str, ...] | None: 目标省份下辖所有地级行政区的名称。如果没有找到查询的省级行政区，返回None

<a id="cp_lookup.cp_lookup.ctwop"></a>

#### ctwop

```python
def ctwop(city: str) -> str | None
```

根据地级行政区域名（及其简称）给出所属省级行政区名

**Arguments**:

- `city` _str_ - 地级行政区名称
  

**Returns**:

  str | None: 目标地市所属省级行政区名称。如果没有找到查询的地级行政区，返回None

<a id="cp_lookup.cp_lookup.fillup_city"></a>

#### fillup\_city

```python
def fillup_city(city: str) -> str | None
```

将地级行政区简称替换为全称

**Arguments**:

- `city` _str_ - 地级行政区的名称（简称或全称）
  

**Returns**:

  str | None: 地级行政区的全称。如果没有找到查询的地级行政区，返回None

