## 示例简介
可以通过一个计算区域系统性金融风险的示例，对Rh-s-PyTool进行快速熟悉和大致了解。

假设我们拥有贵州省各州市某年中一系列经济指标的截面数据，现在采用**综合指数评分法**对截面数据进行计算，得到当年各州市的区域系统性金融风险。（注：所使用数据来源于贵州的统计年鉴，但在本示例中指标的经济意义不重要，
故修改指标名称为字母隐去其实际含义。同时对后续所采用评分方法的适用性不做考量，直接假定它适合本示例。**因而本示例仅供参考！！！！**）

## 导入必要模块
```python
>>>from cp_lookup import lookup                  # 区域名处理模块
>>>import index_calmeth.non_dimension as icn     # 无量纲化模块
>>>import index_calmeth.weights as icw           # 权重计算模块
>>>import index_calmeth.evaluation as ice        # 评价打分模块
>>>from pyecharts import options as opts
>>>from pyecharts.charts import Map
>>>import pandas as pd
>>>import numpy as  np
```

## 导入原始数据
```python
>>>data = pd.read_excel(r'示例数据.xlsx')
```

### 查看数据框形状
```python
>>>data.shape

(9, 19)
```

### 查看数据前五行
```python
>>>data.head()
```
<center>

![原数据前五行](assets/head.png)
</center>

## 数据预处理
### 补全州市名称
这一步本不是必要，但各个数据平台的数据中地区名有的是简称，有的是全称，像黔西南、凉山等地区简称和全称差距不小。为了研究的方便，最好还是统一为全称。
```python
>>>data["州市"] = data["州市"].apply(lookup)
>>>data.head()
```
<center>

![补全后前五行](assets/new_head.png)
</center>

### dataframe转ndarray
计算过程仅涉及指标数据，暂时无需州市名称、年份等信息，因此暂时排除。同时指标计算部分的模块出于计算效率和数据结构一致性的考虑，没有使用pandas库。通用的数据结构是numpy的ndarray，因此需要将dataframe类数据进行转换。
```python
>>>df = np.array(data.iloc[:, 3:])
```

### 指标正向化
假设第2、4、6、8个指标为逆向指标，由于后续评分函数在设计时假设所有指标为正向指标，因此在这里需要利用[tiny_convert](./api/index_calmeth.md#tiny_convert)函数将非正向指标正向化。
```python
>>>df = icn.tiny_convert(df, mode='0', change_list=[1, 3, 5, 7])
```

### 指标归一化
后续计算不同指标的权重时，需排除指标量纲的影响，这里使用[tonoe](./api/index_calmeth.md#toone)函数归一化消除量纲。
```python
>>>df = icn.toone(df, mode="0")
```

## 正式计算
### 计算指标权重
采用[基尼系数法](./api/index_calmeth.md#gini)求权重。
```python
>>>weights = icw.gini(df)
```

### 得到结果
利用[topsis](./api/index_calmeth.md#topsis)方法和前面得到的指标权重计算出区域系统性金融风险分值。
```python
>>>result = pd.DataFrame(ice.topsis(df, weights), index=data["州市"], columns=["topsis"])
>>>result.head()
```
<center>

![风险分值](assets/result_head.png)

</center>

## 其它
利用pyecharts模块对计算结果进行可视化
```python
c = (
    Map()
    .add("贵州", [list(z) for z in zip(result.index, result["topsis"]*100)], "贵州")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="贵州地图"), visualmap_opts=opts.VisualMapOpts()
    )
    .render()
)
```
将得到的html文件在浏览器中打开：
<center>

![风险地图](assets/map.png)
</center>