[![PyPI](https://img.shields.io/pypi/v/Rh-s-PyTool)](https://pypi.org/project/Rh-s-PyTool/)
[![CodeQL](https://github.com/skahanium/Rh-s-PyTool/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/skahanium/Rh-s-PyTool/actions/workflows/codeql-analysis.yml)
[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/skahanium/Rh-s-PyTool.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/skahanium/Rh-s-PyTool/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/skahanium/Rh-s-PyTool.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/skahanium/Rh-s-PyTool/context:python)
[![DOI](https://zenodo.org/badge/392722517.svg)](https://zenodo.org/badge/latestdoi/392722517)

## Rh-s-PyTool
Rh-s-PyTool is a collection of python codes I wrote in my school project, including a series of used tools and methods. See **Documentation** for details.

## Main function

It mainly contains two large modules, each of which contains several small modules.

The main functions of the former **cp_lookup** include:

- Querying all the prefecture-level administrative units in the province based on the name of the provincial-level administrative region.
- Reverse-checking the name of the provincial-level administrative region based on the name of the prefecture-level administrative unit.
- Obtaining the longitude and latitude of the administrative center based on the name of the region (prefecture-level and above).
- Calculating the spherical distance between two places (ground level and above).

The main functions of the latter **index_calmeth** are:

- Converting non-positive indicators to positive indicators.
- Making data metrics dimensionless.
- Calculating indicator weights.
- Calculating  rsr score of the evaluation objects.
- Calculating topsis score of the evaluation objects.

## Installing
You can download the compressed package from **release** and install it locally,

or get it from **PyPI**:

```
pip3 install Rh-s-PyTool
```

You can also use the **pdm** package management system ( recommended ):

```
pdm add Rh-s-PyTool
```

Note: Since the python3.10 version is used when the module is finally aggregated, if you want to try these code, it is best to use python3.10 or above.

## Documentation
Notion : [ Rh-s-PyTool Module ]

[Rh-s-PyTool Module]: https://rh-s-pytool-coral.vercel.app
