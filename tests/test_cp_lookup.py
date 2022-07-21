from cp_lookup import belongs_to, lookup, dist, coordinate


def test_belongs_to():
    assert belongs_to("盘锦") == "辽宁省"
    assert belongs_to("青海海南") == "青海省"


def test_lookup():
    assert lookup("北京朝阳") == "朝阳区"
    assert lookup("青海海南") == "海南藏族自治州"


def test_dist():
    assert dist("铁岭市", "自贡市") == 2221.108451374754


def test_coordinate():
    assert coordinate("齐齐哈尔") == (47.354348, 123.918186)
