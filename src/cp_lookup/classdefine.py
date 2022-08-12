from jieba import lcut
import jieba
import polars as pl
from .special import SIMILAR_NAMES, SAME_NAMES
from .packagepath import full_path

try:
    data = pl.read_csv(full_path())
except Exception:
    data = pl.read_csv("src/cp_lookup/attachment/adcodes.csv")

data = data.with_columns(pl.col("adcode").apply(str).alias("adcode"))

SPECIAL_WORDS = [area for area in data["name"] if len(lcut(area)) != 1]
for word in SPECIAL_WORDS:
    jieba.add_word(word)


class AreaNameError(Exception):
    """自定义异常类"""

    def __init__(self, error_info):
        super().__init__(self)
        self.error_info = error_info

    def __str__(self):
        return self.error_info


def _prov_codes() -> list:
    adcodes = data["adcode"]
    return [code for code in adcodes if str.endswith(code, "0" * 10)]


def _city_codes() -> list:
    adcodes = data["adcode"]
    prov_codes = _prov_codes()
    return [
        code
        for code in adcodes
        if (str.endswith(code, "0" * 8)) & (code not in prov_codes)
    ]


def _county_codes() -> list:
    adcodes = data["adcode"]
    prov_codes = _prov_codes()
    city_codes = _city_codes()
    return [
        code
        for code in adcodes
        if ((code not in prov_codes) & (code not in city_codes))
    ]


PROVINCECODE: list = _prov_codes()
CITYCODE: list = _city_codes()
COUNTYCODE: list = _county_codes()
NOTPROVINCE: list = CITYCODE + COUNTYCODE
NOTCOUNTY: list = PROVINCECODE + CITYCODE


def _level_choose(level: str | None) -> pl.DataFrame:
    options = ["province", "city", "county", "not province", "not county", None]
    assert level in options, "错误的等级选项！！！"
    match level:
        case "province":
            return data.filter(pl.col("adcode").is_in(PROVINCECODE))
        case "city":
            return data.filter(pl.col("adcode").is_in(CITYCODE))
        case "county":
            return data.filter(pl.col("adcode").is_in(COUNTYCODE))
        case "not province":
            return data.filter(pl.col("adcode").is_in(NOTPROVINCE))
        case "not county":
            return data.filter(pl.col("adcode").is_in(NOTCOUNTY))
        case _:
            return data


def _num_one(info: list[str], level_data: pl.DataFrame):
    addr = info[0]
    if len(level_data.filter(pl.col("name").str.contains(addr))) != 1:
        raise AreaNameError("地名重复或有误！！！")
    else:
        return level_data.filter(pl.col("name").str.contains(addr))


def _num_two(info: list[str], level_data: pl.DataFrame):
    father, addr = info
    if father == addr:
        addr_name = SAME_NAMES[addr][1]
        return data.filter(pl.col("name") == addr_name)
    else:
        fdata = _level_choose("not county")
        fcode = fdata.filter(pl.col("name").str.contains(father))[0, "adcode"]
        addr_codes = level_data.filter(pl.col("name").str.contains(addr))["adcode"]
        for code in addr_codes:
            if (code[:4] == fcode[:4]) | (code[:2] == fcode[:2]):
                return level_data.filter(pl.col("adcode") == code)


def _num_three(info: list[str], level_data: pl.DataFrame):
    gdfather, father, addr = info
    gddata = _level_choose("province")
    fdata = _level_choose("city")
    ldata = _level_choose("county")
    if len(level_data.filter(pl.col("name").str.contains(addr))) == 1:
        return level_data.filter(pl.col("name").str.contains(addr))
    gdcode = gddata.filter(pl.col("name").str.contains(gdfather))[0, "adcode"]
    fcode = fdata.filter(pl.col("name").str.contains(father))[0, "adcode"]
    addr_codes = ldata.filter(pl.col("name").str.contains(gdfather))["adcode"]
    for code in addr_codes:
        if code[:2] == fcode[:2] == gdcode[:2]:
            return level_data.filter(pl.col("adcode") == code)


class Addr:
    """以区域名构建一个地区的类，包含该地区的adcode、区域名、经纬度等信息。"""

    def __init__(self, name: str, adcode: int | None = None, level: str | None = None):
        if adcode:
            self.addr = data[data["adcode"] == adcode]
        elif name in SIMILAR_NAMES.keys():
            self.addr = data[data["adcode"] == SIMILAR_NAMES.get(name)]
        else:
            obj_area_data = _level_choose(level) if level else data
            info = lcut(name)
            nums = len(info)
            match nums:
                case 1:
                    self.addr = _num_one(info, obj_area_data)
                case 2:
                    self.addr = _num_two(info, obj_area_data)
                case 3:
                    self.addr = _num_three(info, obj_area_data)

    def _belongs_to(self) -> str | None:
        assert isinstance(self.addr, pl.DataFrame)
        code = self.addr[0, "adcode"]
        fcode = (
            code[:2] + "0" * 10 if str.endswith(code, "0" * 8) else (code[:4] + "0" * 8)
        )
        fdata = data.filter(pl.col("adcode") == fcode)
        return fdata[0, "name"]

    def _coordinate(self) -> tuple[float, float]:
        assert isinstance(self.addr, pl.DataFrame)
        lat = self.addr[0, "latitude"]
        lon = self.addr[0, "longitude"]
        return lat, lon
