# 关于Rh-s-PyTool

^^Rh-s-PyTool^^ 是本人在学校项目中自己编写的一系列python工具方法的合集，包含了一些有关行政区域名称查询与补全、坐标查询以及综合指标评价方法等方面的内容。编写这个库的主要目的是希望可以方便自己和课题组其他成员，以及未来可能加入的学弟学妹的课题研究，同时自己也练一练手。


# 主要功能

当前，^^Rh-s-PyTool^^ 主要包含了两个大的模块：[cp_lookup](api/cp_lookup.md) 和 [index_calmeth](api/index_calmeth.md) ，二者又分别包含了若干个小模块。前者的功能描述大致描述如下：

+ 根据省级行政区的名称查询全省所有地级行政单位

+ 根据地级行政单位的名称反向检查省级行政区的名称

+ 根据地区名称（地级或省级）获取行政中心的经度和纬度

+ 计算两个地区（地级或省级）之间的球面距离

后者则主要包含以下功能：

+ 将非正向指标转换为正向指标

+ 使数据指标无量纲化

+ 计算指标权重

+ 计算评估对象的综合评价分数分数

# 下载

如果对 ^^Rh-s-PyTool^^ 有一定的兴趣，或者希望尝试使用其中的某些方法，可以使用如下方法进行下载。

1. 可以从该项目的GitHub仓库中找到并下载最新的[release](https://github.com/skahanium/Rh-s-PyTool/releases)本地安装，

2. 或者从[PyPI](https://pypi.org/project/Rh-s-PyTool/)获取该模块：

```
pip3 install Rh-s-PyTool
```

3. 也可以使用[pdm](https://pdm.fming.dev)包管理系统（推荐）：

```
pdm add Rh-s-PyTool
```

(注：本模块适用于python3.10及以上版本。)