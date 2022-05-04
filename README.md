![PyPI](https://img.shields.io/pypi/v/Rh-s-PyTool)
[![CodeQL](https://github.com/skahanium/Rh-s-PyTool/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/skahanium/Rh-s-PyTool/actions/workflows/codeql-analysis.yml)
[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/skahanium/Rh-s-PyTool.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/skahanium/Rh-s-PyTool/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/skahanium/Rh-s-PyTool.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/skahanium/Rh-s-PyTool/context:python)
[![DOI](https://zenodo.org/badge/392722517.svg)](https://zenodo.org/badge/latestdoi/392722517)

# Rh-s-PyTool

Rh-s-PyTool是本人在学校课题中写过的python代码整理后得到的合集，包括了一系列使用过的工具和方法。具体内容参见**Documentation**。

# 主要功能

主要包含了两个大模块，二者各自又包含了若干小模块。前者**cp_lookup**的主要功能包括根据省级行政区名称查询该省所有地级行政单位、根据地级行政单位名称反查所属省级行政区名称、根据区域（地级及以上）名称得到行政中心经纬度、计算两地（地级及以上）球面距离。后者**index_calmeth**的主要功能为指标体系正向化、归一化、计算critic权重、计算rsr得分、计算topsis得分。

# 下载

可以从release下载压缩包本地安装，

或从PyPI上下载：

```
pip3 install Rh-s-PyTool
```

也可以使用pdm包管理系统（推荐）：

```
pdm add Rh-s-PyTool
```

注：由于最后汇总模块的时候使用的是python3.10版本，而本人对python各代版本的差异不甚了解，如果想尝试一下这些代码，最好用python3.10以上版本。

# 文档

Documentation : [ Notion ]

[Notion]: https://skahanium.notion.site/Rh-s-PyTool-bf7ab98fba544187b2132c613f0835ea
