[![PyPI](https://img.shields.io/pypi/v/Rh-s-PyTool)](https://pypi.org/project/Rh-s-PyTool/)
[![CodeQL](https://github.com/skahanium/Rh-s-PyTool/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/skahanium/Rh-s-PyTool/actions/workflows/codeql-analysis.yml)
[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/skahanium/Rh-s-PyTool.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/skahanium/Rh-s-PyTool/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/skahanium/Rh-s-PyTool.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/skahanium/Rh-s-PyTool/context:python)
[![DOI](https://zenodo.org/badge/392722517.svg)](https://zenodo.org/badge/latestdoi/392722517)
[![CodeFactor](https://www.codefactor.io/repository/github/skahanium/rh-s-pytool/badge)](https://www.codefactor.io/repository/github/skahanium/rh-s-pytool)

# 关于Rh-s-PyTool

Rh-s-PyTool是本人研究生期间在学校项目中自己编写的一系列python工具方法的合集，包含了一些有关行政区域名称、坐标查询以及综合指标评价方面的内容。目前而言Rh-s-PyTool还是一个过于简陋的工具库，有待进一步完善和丰富。

本人也会在今后的时间里长期维护这个库，不断向其中添加新的工具与方法，提高它的质量。

# 主要功能

目前，Rh-s-PyTool主要包含了两个大的模块：**cp_lookup**和**index_calmeth**，二者又分别包含了若干个小模块。前者的功能描述大致描述如下：

+ 根据省级行政区的名称查询全省所有地级行政单位

+ 根据地级行政单位的名称反向检查省级行政区的名称

+ 根据地区名称（地级或省级）获取行政中心的经度和纬度

+ 计算两个地区（地级或省级）之间的球形距离

后者则主要包含以下功能：

+ 将非正向指标转换为正向指标

+ 使数据指标无量纲化

+ 计算指标权重

+ 计算评估对象的综合评价分数分数

## 下载

可以从该项目的GitHub仓库中找到并下载最新的[release](https://github.com/skahanium/Rh-s-PyTool/releases)本地安装，

或者从[PyPI](https://pypi.org/project/Rh-s-PyTool/)获取该模块：

```
pip3 install Rh-s-PyTool
```

也可以使用[pdm](https://pdm.fming.dev)包管理系统（推荐）：

```
pdm add Rh-s-PyTool
```

注：本模块适用于python3.10及以上版本。

## 文档
中文文档:[ Rh-s-PyTool Module ]

[Rh-s-PyTool Module]:https://skahanium.github.io/Rh-s-PyTool/
