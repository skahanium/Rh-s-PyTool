[![PyPI](https://img.shields.io/pypi/v/Rh-s-PyTool)](https://pypi.org/project/Rh-s-PyTool/)
[![CodeQL](https://github.com/skahanium/Rh-s-PyTool/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/skahanium/Rh-s-PyTool/actions/workflows/codeql-analysis.yml)
[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
[![DOI](https://zenodo.org/badge/392722517.svg)](https://zenodo.org/badge/latestdoi/392722517)
[![CodeFactor](https://www.codefactor.io/repository/github/skahanium/rh-s-pytool/badge)](https://www.codefactor.io/repository/github/skahanium/rh-s-pytool)
[![PyPI - License](https://img.shields.io/pypi/l/Rh-s-PyTool)](https://github.com/skahanium/Rh-s-PyTool/blob/main/LICENSE)
[![Docs](https://img.shields.io/badge/Docs-passing-brightgreen)](https://skahanium.github.io/Rh-s-PyTool/)
![PythonVersion](https://img.shields.io/badge/python->=3.10-brightgreen)
# 关于Rh-s-PyTool

Rh-s-PyTool是一系列python工具方法的合集，包含了一些有关行政区域名称查询与补全、坐标查询以及综合指标评价方法等方面的内容。
# 主要功能

目前，Rh-s-PyTool主要包含了两个大的模块：**cp_lookup**和**index_calmeth**，二者又分别包含了若干个小模块。前者的功能描述大致描述如下：

+ 将区域（省、市、区县）简称补充为全称

+ 根据区域名（市、区县）查询其上级行政区域的名称

+ 根据地区（省、市、区县）名称获取行政中心的经度和纬度

+ 计算两个地区（省、市、区县）行政中心间的球面距离

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
