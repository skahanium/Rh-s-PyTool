import pandas as pd

#####################################
provinces = {
    '吉林省': [125.326800, 43.896160], '黑龙江省': [126.662850, 45.742080],
    '辽宁省': [123.429250, 41.835710], '内蒙古自治区': [111.765220, 40.817330],
    '新疆维吾尔自治区': [87.627100, 43.793430], '青海省': [101.780110, 36.620870],
    '北京市': [116.407170, 39.904690], '天津市': [117.199370, 39.085100],
    '上海市': [121.473700, 31.230370], '重庆市': [106.550730, 29.564710],
    '河北省': [114.469790, 38.035990], '河南省': [113.753220, 34.765710],
    '陕西省': [108.954240, 34.264860], '江苏省': [118.762950, 32.060710],
    '山东省': [117.020760, 36.668260], '山西省': [112.562720, 37.873430],
    '甘肃省': [103.826340, 36.059420], '宁夏回族自治区': [106.258670, 38.471170],
    '四川省': [104.075720, 30.650890], '西藏自治区': [91.117480, 29.647250],
    '安徽省': [117.285650, 31.861570], '浙江省': [120.153600, 30.265550],
    '湖北省': [114.342340, 30.545390], '湖南省': [112.983400, 28.112660],
    '福建省': [119.296590, 26.099820], '江西省': [115.910040, 28.674170],
    '贵州省': [106.707220, 26.598200], '云南省': [102.709730, 25.045300],
    '广东省': [113.266270, 23.131710], '广西壮族自治区': [108.327540, 22.815210],
    '香港': [114.165460, 22.275340], '澳门': [113.549130, 22.198750],
    '海南省': [110.348630, 20.019970], '台湾省': [121.520076, 25.030724],
}
cities = {
     '北京市': ['北京市', '116.407170', '39.904690'],
     '天津市': ['天津市', '117.199370', '39.085100'],
     '上海市': ['上海市', '121.473700', '31.230370'],
     '重庆市': ['重庆市', '106.550730', '29.564710'],
     '香港': ['香港', '114.165460', '22.275340'],
     '澳门': ['澳门', '113.549130', '22.198750'],
     '石家庄市': ['河北省', '114.514300', '38.042760'],
     '唐山市': ['河北省', '118.180580', '39.630480'],
     '秦皇岛市': ['河北省', '119.599640', '39.935450'],
     '邯郸市': ['河北省', '114.539180', '36.625560'],
     '邢台市': ['河北省', '114.504430', '37.070550'],
     '保定市': ['河北省', '115.464590', '38.873960'],
     '张家口市': ['河北省', '114.887550', '40.824440'],
     '承德市': ['河北省', '117.963400', '40.951500'],
     '沧州市': ['河北省', '116.838690', '38.304410'],
     '廊坊市': ['河北省', '116.683760', '39.537750'],
     '衡水市': ['河北省', '115.670540', '37.738860'],
     '郑州市': ['河南省', '113.624930', '34.747250'],
     '开封市': ['河南省', '114.307310', '34.797260'],
     '洛阳市': ['河南省', '112.453610', '34.618120'],
     '平顶山市': ['河南省', '113.192410', '33.766090'],
     '安阳市': ['河南省', '114.393100', '36.097710'],
     '鹤壁市': ['河南省', '114.297450', '35.747000'],
     '新乡市': ['河南省', '113.926750', '35.303230'],
     '焦作市': ['河南省', '113.242010', '35.215630'],
     '濮阳市': ['河南省', '115.029320', '35.761890'],
     '许昌市': ['河南省', '113.852330', '34.035700'],
     '漯河市': ['河南省', '114.016810', '33.581490'],
     '三门峡市': ['河南省', '111.200300', '34.772610'],
     '南阳市': ['河南省', '112.528510', '32.990730'],
     '商丘市': ['河南省', '115.656350', '34.414270'],
     '信阳市': ['河南省', '114.092790', '32.147140'],
     '周口市': ['河南省', '114.696950', '33.625830'],
     '驻马店市': ['河南省', '114.022990', '33.011420'],
     '济南市': ['山东省', '117.120090', '36.651840'],
     '青岛市': ['山东省', '120.382990', '36.066230'],
     '淄博市': ['山东省', '118.054800', '36.813100'],
     '枣庄市': ['山东省', '117.321960', '34.810710'],
     '东营市': ['山东省', '118.674660', '37.433650'],
     '烟台市': ['山东省', '121.448010', '37.463530'],
     '潍坊市': ['山东省', '119.161760', '36.706860'],
     '济宁市': ['山东省', '116.587240', '35.414590'],
     '泰安市': ['山东省', '117.088400', '36.199940'],
     '威海市': ['山东省', '122.121710', '37.513480'],
     '日照市': ['山东省', '119.527190', '35.416460'],
     '莱芜市': ['山东省', '117.676670', '36.213590'],
     '临沂市': ['山东省', '118.356460', '35.104650'],
     '德州市': ['山东省', '116.359270', '37.435500'],
     '聊城市': ['山东省', '115.985490', '36.457020'],
     '滨州市': ['山东省', '117.972790', '37.382110'],
     '菏泽市': ['山东省', '115.481150', '35.233630'],
     '太原市': ['山西省', '112.556252', '37.876876'],
     '大同市': ['山西省', '113.304424', '40.081863'],
     '阳泉市': ['山西省', '113.580470', '37.856680'],
     '长治市': ['山西省', '113.116490', '36.195810'],
     '晋城市': ['山西省', '112.851130', '35.490390'],
     '朔州市': ['山西省', '112.439374', '39.357422'],
     '晋中市': ['山西省', '112.752780', '37.687020'],
     '运城市': ['山西省', '111.006990', '35.026280'],
     '忻州市': ['山西省', '112.734180', '38.416700'],
     '临汾市': ['山西省', '111.519620', '36.088220'],
     '吕梁市': ['山西省', '111.141650', '37.519340'],
     '沈阳市': ['辽宁省', '123.463100', '41.677180'],
     '大连市': ['辽宁省', '121.614760', '38.913690'],
     '鞍山市': ['辽宁省', '122.994600', '41.107770'],
     '抚顺市': ['辽宁省', '123.957220', '41.879710'],
     '本溪市': ['辽宁省', '123.766860', '41.294130'],
     '丹东市': ['辽宁省', '124.356010', '39.999800'],
     '锦州市': ['辽宁省', '121.127030', '41.095150'],
     '营口市': ['辽宁省', '122.234900', '40.666830'],
     '阜新市': ['辽宁省', '121.670110', '42.021660'],
     '辽阳市': ['辽宁省', '123.237360', '41.268090'],
     '盘锦市': ['辽宁省', '122.070780', '41.119960'],
     '铁岭市': ['辽宁省', '123.842410', '42.286200'],
     '朝阳市': ['辽宁省', '120.450800', '41.573470'],
     '葫芦岛市': ['辽宁省', '120.836990', '40.711000'],
     '长春市': ['吉林省', '125.323570', '43.816020'],
     '吉林市': ['吉林省', '126.549440', '43.837840'],
     '四平市': ['吉林省', '124.350360', '43.166460'],
     '辽源市': ['吉林省', '125.143680', '42.888050'],
     '通化市': ['吉林省', '125.939900', '41.728290'],
     '白山市': ['吉林省', '126.424430', '41.940800'],
     '松原市': ['吉林省', '124.825150', '45.141100'],
     '白城市': ['吉林省', '122.838710', '45.619600'],
     '延边朝鲜族自治州': ['吉林省', '129.509100', '42.891190'],
     '哈尔滨市': ['黑龙江省', '126.535800', '45.802160'],
     '齐齐哈尔市': ['黑龙江省', '123.917960', '47.354310'],
     '鸡西市': ['黑龙江省', '130.969540', '45.295240'],
     '鹤岗市': ['黑龙江省', '130.297850', '47.349890'],
     '双鸭山市': ['黑龙江省', '131.159100', '46.646580'],
     '大庆市': ['黑龙江省', '125.110961', '46.595319'],
     '伊春市': ['黑龙江省', '128.840490', '47.727520'],
     '佳木斯市': ['黑龙江省', '130.318820', '46.799770'],
     '七台河市': ['黑龙江省', '131.003060', '45.770650'],
     '牡丹江市': ['黑龙江省', '129.632440', '44.552690'],
     '黑河市': ['黑龙江省', '127.528520', '50.245230'],
     '绥化市': ['黑龙江省', '126.969320', '46.652460'],
     '大兴安岭地区': ['黑龙江省', '124.592160', '51.923980'],
     '南京市': ['江苏省', '118.796470', '32.058380'],
     '无锡市': ['江苏省', '120.312370', '31.490990'],
     '徐州市': ['江苏省', '117.285770', '34.204400'],
     '常州市': ['江苏省', '119.973650', '31.810720'],
     '苏州市': ['江苏省', '120.583190', '31.298340'],
     '南通市': ['江苏省', '120.893710', '31.979580'],
     '连云港市': ['江苏省', '119.222950', '34.596690'],
     '淮安市': ['江苏省', '119.015950', '33.610160'],
     '盐城市': ['江苏省', '120.161640', '33.349510'],
     '扬州市': ['江苏省', '119.412690', '32.393580'],
     '镇江市': ['江苏省', '119.425000', '32.189590'],
     '泰州市': ['江苏省', '119.925540', '32.455460'],
     '宿迁市': ['江苏省', '118.275490', '33.961930'],
     '杭州市': ['浙江省', '120.155150', '30.274150'],
     '宁波市': ['浙江省', '121.550270', '29.873860'],
     '温州市': ['浙江省', '120.699390', '27.994920'],
     '嘉兴市': ['浙江省', '120.755500', '30.745010'],
     '湖州市': ['浙江省', '120.088050', '30.893050'],
     '绍兴市': ['浙江省', '120.580200', '30.030330'],
     '金华市': ['浙江省', '119.647590', '29.078120'],
     '衢州市': ['浙江省', '118.874190', '28.935920'],
     '舟山市': ['浙江省', '122.207780', '29.985390'],
     '台州市': ['浙江省', '121.420560', '28.656110'],
     '丽水市': ['浙江省', '119.922930', '28.467200'],
     '合肥市': ['安徽省', '117.229010', '31.820570'],
     '芜湖市': ['安徽省', '118.433130', '31.352460'],
     '蚌埠市': ['安徽省', '117.389320', '32.915480'],
     '淮南市': ['安徽省', '116.999800', '32.625490'],
     '马鞍山市': ['安徽省', '118.506110', '31.670670'],
     '淮北市': ['安徽省', '116.798340', '33.954790'],
     '铜陵市': ['安徽省', '117.812320', '30.944860'],
     '安庆市': ['安徽省', '117.063540', '30.542940'],
     '黄山市': ['安徽省', '118.338660', '29.715170'],
     '滁州市': ['安徽省', '118.316830', '32.301810'],
     '阜阳市': ['安徽省', '115.814950', '32.889630'],
     '宿州市': ['安徽省', '116.963910', '33.646140'],
     '六安市': ['安徽省', '116.523240', '31.734880'],
     '亳州市': ['安徽省', '115.779310', '33.844610'],
     '池州市': ['安徽省', '117.491420', '30.664690'],
     '宣城市': ['安徽省', '118.758660', '30.940780'],
     '福州市': ['福建省', '119.296470', '26.074210'],
     '厦门市': ['福建省', '118.089480', '24.479510'],
     '莆田市': ['福建省', '119.007710', '25.454000'],
     '三明市': ['福建省', '117.639220', '26.263850'],
     '泉州市': ['福建省', '118.675870', '24.873890'],
     '漳州市': ['福建省', '117.647250', '24.513470'],
     '南平市': ['福建省', '118.120430', '27.331750'],
     '龙岩市': ['福建省', '117.017220', '25.075040'],
     '宁德市': ['福建省', '119.548190', '26.665710'],
     '南昌市': ['江西省', '115.857940', '28.682020'],
     '景德镇市': ['江西省', '117.178390', '29.268690'],
     '萍乡市': ['江西省', '113.854270', '27.622890'],
     '九江市': ['江西省', '116.001460', '29.705480'],
     '新余市': ['江西省', '114.917130', '27.817760'],
     '鹰潭市': ['江西省', '117.069190', '28.260190'],
     '赣州市': ['江西省', '114.934760', '25.831090'],
     '吉安市': ['江西省', '114.993760', '27.113820'],
     '宜春市': ['江西省', '114.416120', '27.814430'],
     '抚州市': ['江西省', '116.358090', '27.947810'],
     '上饶市': ['江西省', '117.943570', '28.454630'],
     '武汉市': ['湖北省', '114.305250', '30.592760'],
     '黄石市': ['湖北省', '115.038900', '30.199530'],
     '十堰市': ['湖北省', '110.798010', '32.629180'],
     '宜昌市': ['湖北省', '111.286420', '30.691860'],
     '襄阳市': ['湖北省', '112.122550', '32.009000'],
     '鄂州市': ['湖北省', '114.894950', '30.390850'],
     '荆门市': ['湖北省', '112.199450', '31.035460'],
     '孝感市': ['湖北省', '113.916450', '30.924830'],
     '荆州市': ['湖北省', '112.240690', '30.334790'],
     '黄冈市': ['湖北省', '114.872380', '30.453470'],
     '咸宁市': ['湖北省', '114.322450', '29.841260'],
     '随州市': ['湖北省', '113.382620', '31.690130'],
     '恩施土家族苗族自治州': ['湖北省', '109.488170', '30.272170'],
     '长沙市': ['湖南省', '112.938860', '28.227780'],
     '株洲市': ['湖南省', '113.133960', '27.827670'],
     '湘潭市': ['湖南省', '112.944110', '27.829750'],
     '衡阳市': ['湖南省', '112.571950', '26.893240'],
     '邵阳市': ['湖南省', '111.467700', '27.238900'],
     '岳阳市': ['湖南省', '113.129190', '29.357280'],
     '常德市': ['湖南省', '111.698540', '29.031580'],
     '张家界市': ['湖南省', '110.478390', '29.116670'],
     '益阳市': ['湖南省', '112.355160', '28.553910'],
     '郴州市': ['湖南省', '113.014850', '25.770630'],
     '永州市': ['湖南省', '111.612250', '26.420340'],
     '怀化市': ['湖南省', '110.001600', '27.569740'],
     '娄底市': ['湖南省', '111.994580', '27.697280'],
     '湘西土家族苗族自治州': ['湖南省', '109.738930', '28.311730'],
     '广州市': ['广东省', '113.264360', '23.129080'],
     '韶关市': ['广东省', '113.597230', '24.810390'],
     '深圳市': ['广东省', '114.059560', '22.542860'],
     '珠海市': ['广东省', '113.576680', '22.270730'],
     '汕头市': ['广东省', '116.682210', '23.353500'],
     '佛山市': ['广东省', '113.121920', '23.021850'],
     '江门市': ['广东省', '113.081610', '22.578650'],
     '湛江市': ['广东省', '110.358940', '21.271340'],
     '茂名市': ['广东省', '110.925230', '21.663290'],
     '肇庆市': ['广东省', '112.465280', '23.046900'],
     '惠州市': ['广东省', '114.416790', '23.110750'],
     '梅州市': ['广东省', '116.122640', '24.288440'],
     '汕尾市': ['广东省', '115.375140', '22.785660'],
     '河源市': ['广东省', '114.700650', '23.743650'],
     '阳江市': ['广东省', '111.982560', '21.858290'],
     '清远市': ['广东省', '113.056150', '23.682010'],
     '东莞市': ['广东省', '113.751790', '23.020670'],
     '中山市': ['广东省', '113.392600', '22.515950'],
     '潮州市': ['广东省', '116.622960', '23.656700'],
     '揭阳市': ['广东省', '116.372710', '23.549720'],
     '云浮市': ['广东省', '112.044530', '22.915250'],
     '海口市': ['海南省', '110.199890', '20.044220'],
     '三亚市': ['海南省', '109.512090', '18.252480'],
     '三沙市': ['海南省', '112.333560', '16.832720'],
     '儋州市': ['海南省', '109.580690', '19.520930'],
     '成都市': ['四川省', '104.064760', '30.570200'],
     '自贡市': ['四川省', '104.778440', '29.339200'],
     '攀枝花市': ['四川省', '101.718720', '26.582280'],
     '泸州市': ['四川省', '105.442570', '28.871700'],
     '德阳市': ['四川省', '104.397900', '31.126790'],
     '绵阳市': ['四川省', '104.679600', '31.467510'],
     '广元市': ['四川省', '105.843570', '32.435490'],
     '遂宁市': ['四川省', '105.592730', '30.532860'],
     '内江市': ['四川省', '105.058440', '29.580150'],
     '乐山市': ['四川省', '103.765390', '29.552210'],
     '南充市': ['四川省', '106.110730', '30.837310'],
     '眉山市': ['四川省', '103.848510', '30.075630'],
     '宜宾市': ['四川省', '104.641700', '28.751300'],
     '广安市': ['四川省', '106.633220', '30.455960'],
     '达州市': ['四川省', '107.467910', '31.208640'],
     '雅安市': ['四川省', '103.042400', '30.010530'],
     '巴中市': ['四川省', '106.747330', '31.867150'],
     '资阳市': ['四川省', '104.627980', '30.128590'],
     '阿坝藏族羌族自治州': ['四川省', '102.224770', '31.899400'],
     '甘孜藏族自治州': ['四川省', '101.962540', '30.049320'],
     '凉山彝族自治州': ['四川省', '102.267460', '27.881640'],
     '贵阳市': ['贵州省', '106.630240', '26.647020'],
     '六盘水市': ['贵州省', '104.830230', '26.593360'],
     '遵义市': ['贵州省', '106.927230', '27.725450'],
     '安顺市': ['贵州省', '105.946200', '26.253670'],
     '毕节市': ['贵州省', '105.305040', '27.298470'],
     '铜仁市': ['贵州省', '109.180990', '27.690660'],
     '黔西南布依族苗族自治州': ['贵州省', '104.904370', '25.089880'],
     '黔东南苗族侗族自治州': ['贵州省', '107.984160', '26.583640'],
     '黔南布依族苗族自治州': ['贵州省', '107.522260', '26.254270'],
     '昆明市': ['云南省', '102.833220', '24.879660'],
     '曲靖市': ['云南省', '103.796250', '25.490020'],
     '玉溪市': ['云南省', '102.547140', '24.351800'],
     '保山市': ['云南省', '99.161810', '25.112050'],
     '昭通市': ['云南省', '103.716800', '27.338170'],
     '丽江市': ['云南省', '100.227100', '26.856480'],
     '普洱市': ['云南省', '100.966240', '22.825210'],
     '临沧市': ['云南省', '100.088840', '23.884260'],
     '楚雄彝族自治州': ['云南省', '101.527670', '25.044950'],
     '红河哈尼族彝族自治州': ['云南省', '103.375600', '23.364220'],
     '文山壮族苗族自治州': ['云南省', '104.215040', '23.398490'],
     '西双版纳傣族自治州': ['云南省', '100.797390', '22.007490'],
     '大理白族自治州': ['云南省', '100.267640', '25.606480'],
     '德宏傣族景颇族自治州': ['云南省', '98.584860', '24.432320'],
     '怒江傈僳族自治州': ['云南省', '98.856700', '25.817630'],
     '迪庆藏族自治州': ['云南省', '99.703050', '27.819080'],
     '西安市': ['陕西省', '108.939840', '34.341270'],
     '铜川市': ['陕西省', '108.945150', '34.896730'],
     '宝鸡市': ['陕西省', '107.237320', '34.361940'],
     '咸阳市': ['陕西省', '108.709290', '34.329320'],
     '渭南市': ['陕西省', '109.510150', '34.499970'],
     '延安市': ['陕西省', '109.489780', '36.585290'],
     '汉中市': ['陕西省', '107.023770', '33.067610'],
     '榆林市': ['陕西省', '109.734580', '38.285200'],
     '安康市': ['陕西省', '109.029320', '32.684860'],
     '商洛市': ['陕西省', '109.940410', '33.870360'],
     '兰州市': ['甘肃省', '103.834170', '36.061380'],
     '嘉峪关市': ['甘肃省', '98.290110', '39.772010'],
     '金昌市': ['甘肃省', '102.187590', '38.520060'],
     '白银市': ['甘肃省', '104.137730', '36.544700'],
     '天水市': ['甘肃省', '105.724860', '34.580850'],
     '武威市': ['甘肃省', '102.637970', '37.928200'],
     '张掖市': ['甘肃省', '100.449810', '38.925920'],
     '平凉市': ['甘肃省', '106.665300', '35.543030'],
     '酒泉市': ['甘肃省', '98.493940', '39.732550'],
     '庆阳市': ['甘肃省', '107.642920', '35.709780'],
     '定西市': ['甘肃省', '104.625240', '35.581130'],
     '陇南市': ['甘肃省', '104.921660', '33.401000'],
     '临夏回族自治州': ['甘肃省', '103.210910', '35.601220'],
     '甘南藏族自治州': ['甘肃省', '102.911020', '34.983270'],
     '西宁市': ['青海省', '101.777820', '36.617290'],
     '海东市': ['青海省', '102.401730', '36.482090'],
     '海北藏族自治州': ['青海省', '100.900960', '36.954540'],
     '黄南藏族自治州': ['青海省', '102.015070', '35.519910'],
     '海南藏族自治州': ['青海省', '100.620370', '36.286630'],
     '果洛藏族自治州': ['青海省', '100.244750', '34.471410'],
     '玉树藏族自治州': ['青海省', '97.006500', '33.005280'],
     '海西蒙古族藏族自治州': ['青海省', '97.371220', '37.377100'],
     '南宁市': ['广西壮族自治区', '108.366900', '22.816730'],
     '柳州市': ['广西壮族自治区', '109.415520', '24.325430'],
     '桂林市': ['广西壮族自治区', '110.290020', '25.273610'],
     '梧州市': ['广西壮族自治区', '111.279170', '23.476910'],
     '北海市': ['广西壮族自治区', '109.120080', '21.481120'],
     '防城港市': ['广西壮族自治区', '108.354720', '21.687130'],
     '钦州市': ['广西壮族自治区', '108.654310', '21.979700'],
     '贵港市': ['广西壮族自治区', '109.597640', '23.113060'],
     '玉林市': ['广西壮族自治区', '110.180980', '22.654510'],
     '百色市': ['广西壮族自治区', '106.618380', '23.902160'],
     '贺州市': ['广西壮族自治区', '111.566550', '24.403460'],
     '河池市': ['广西壮族自治区', '108.085400', '24.692910'],
     '来宾市': ['广西壮族自治区', '109.222380', '23.752100'],
     '崇左市': ['广西壮族自治区', '107.364850', '22.378950'],
     '呼和浩特市': ['内蒙古自治区', '111.751990', '40.841490'],
     '包头市': ['内蒙古自治区', '109.840210', '40.657810'],
     '乌海市': ['内蒙古自治区', '106.795460', '39.653840'],
     '赤峰市': ['内蒙古自治区', '118.888940', '42.258600'],
     '通辽市': ['内蒙古自治区', '122.244690', '43.652470'],
     '鄂尔多斯市': ['内蒙古自治区', '109.780870', '39.608450'],
     '呼伦贝尔市': ['内蒙古自治区', '119.765840', '49.211630'],
     '巴彦淖尔市': ['内蒙古自治区', '107.387730', '40.743170'],
     '乌兰察布市': ['内蒙古自治区', '113.133760', '40.993910'],
     '兴安盟': ['内蒙古自治区', '122.038180', '46.082080'],
     '锡林郭勒盟': ['内蒙古自治区', '116.047750', '43.933200'],
     '阿拉善盟': ['内蒙古自治区', '105.728980', '38.851530'],
     '银川市': ['宁夏回族自治区', '106.232480', '38.486440'],
     '石嘴山市': ['宁夏回族自治区', '106.384180', '38.984100'],
     '吴忠市': ['宁夏回族自治区', '106.198790', '37.997550'],
     '固原市': ['宁夏回族自治区', '106.242590', '36.015800'],
     '中卫市': ['宁夏回族自治区', '105.196760', '37.500260'],
     '拉萨市': ['西藏自治区', '91.114500', '29.644150'],
     '日喀则市': ['西藏自治区', '88.881160', '29.267050'],
     '昌都市': ['西藏自治区', '97.172250', '31.140730'],
     '林芝市': ['西藏自治区', '94.361550', '29.648950'],
     '山南市': ['西藏自治区', '91.773130', '29.237050'],
     '那曲市': ['西藏自治区', '92.051360', '31.476140'],
     '阿里地区': ['西藏自治区', '81.145400', '30.400510'],
     '乌鲁木齐市': ['新疆维吾尔自治区', '87.616880', '43.826630'],
     '克拉玛依市': ['新疆维吾尔自治区', '84.889270', '45.579990'],
     '吐鲁番市': ['新疆维吾尔自治区', '89.189540', '42.951300'],
     '哈密市': ['新疆维吾尔自治区', '93.515380', '42.818550'],
     '昌吉回族自治州': ['新疆维吾尔自治区', '87.308220', '44.011170'],
     '博尔塔拉蒙古自治州': ['新疆维吾尔自治区', '82.066650', '44.905970'],
     '巴音郭楞蒙古自治州': ['新疆维吾尔自治区', '86.145170', '41.764040'],
     '阿克苏地区': ['新疆维吾尔自治区', '80.260080', '41.168420'],
     '克孜勒苏柯尔克孜自治州': ['新疆维吾尔自治区', '76.166610', '39.715300'],
     '喀什地区': ['新疆维吾尔自治区', '75.989760', '39.470420'],
     '和田地区': ['新疆维吾尔自治区', '79.922470', '37.114310'],
     '伊犁哈萨克自治州': ['新疆维吾尔自治区', '81.324160', '43.916890'],
     '塔城地区': ['新疆维吾尔自治区', '82.980460', '46.745320'],
     '阿勒泰地区': ['新疆维吾尔自治区', '88.140230', '47.845640']
}
#####################################


def pro_info(province):
    lat = provinces[province][0]
    lon = provinces[province][1]
    return lat, lon


def city_info(city):
    pro = cities[city][0]
    lat = cities[city][1]
    lon = cities[city][2]
    return pro, float(lat), float(lon)

########################################


def pro_add(column):
    latitude = []
    longitude = []
    for i in range(len(column)):
        lat = pro_info(column[i])[0]
        lon = pro_info(column[i])[1]
        latitude.append(lat)
        longitude.append(lon)
    return pd.DataFrame(latitude), pd.DataFrame(longitude)


def city_add(column, mode):
    zhoushi = []
    latitude = []
    longitude = []
    for i in range(len(column)):
        dijishi = city_info(column[i])[0]
        lat = city_info(column[i])[1]
        lon = city_info(column[i])[2]
        zhoushi.append(dijishi)
        latitude.append(lat)
        longitude.append(lon)
    if mode == '1':
        return pd.DataFrame(zhoushi)
    elif mode == '2':
        return pd.DataFrame(latitude), pd.DataFrame(longitude)
    else:
        return 'x'

