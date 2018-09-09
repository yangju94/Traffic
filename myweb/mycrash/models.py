# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class AccidentData():
    #事故基础信息数据下拉表单
    month = (
    (' ', '未知'), ('1', '1月'), ('2', '2月'), ('3', '3月'), ('4', '4月'), ('5', '5月'), ('6', '6月'), ('7', '7月'), ('8', '8月'),
    ('9', '9月'), ('10', '10月'), ('11', '11月'), ('12', '12月'),)
    day = (
    ('0', '未知'), ('1', '1号'), ('2', '2号'), ('3', '3号'), ('4', '4号'), ('5', '5号'), ('6', '6号'), ('7', '7号'), ('8', '8号'),
    ('9', '9号'), ('10', '10号'), ('11', '11号'), ('12', '12号'), ('13', '13号'),
    ('14', '14号'), ('15', '15号'), ('16', '16号'), ('17', '17号'), ('18', '18号'), ('19', '19号'), ('20', '20号'),
    ('21', '21号'), ('22', '22号'), ('23', '23号'), ('24', '24号'), ('25', '25号'),
    ('26', '26号'), ('27', '27号'), ('28', '28号'), ('29', '29号'), ('30', '30号'), ('31', '31号'),)
    week = (
    ('0', '未知'), ('1', '星期一'), ('2', '星期二'), ('3', '星期三'), ('4', '星期四'), ('5', '星期五'), ('6', '星期六'), ('7', '星期日'),)
    hour = (
        ('0', '0时'), ('1', '1时'), ('2', '2时'), ('3', '3时'), ('4', '4时'), ('5', '5时'), ('6', '6时'), ('7', '7时'),
        ('8', '8时'),
        ('9', '9时'), ('10', '10时'), ('11', '11时'), ('12', '12时'), ('13', '13时'),
        ('14', '14时'), ('15', '15时'), ('16', '16时'), ('17', '17时'), ('18', '18时'), ('19', '19时'), ('20', '20时'),
        ('21', '21时'), ('22', '22时'), ('23', '23时'), ('99', '未知'),)
    nation_highway_system = (('0', '否'), ('1', '是'), ('9', '未知'),)
    route = (('9', '未知'), ('1', '国道'), ('2', '省道'), ('3', '县道'), ('4', '乡村道路'), ('5', '高速公路'),('6','城市道路-主干道'),('7','城市道路-其他'),('8','其他'))
    type_intersection = (
    ('1', '未知'), ('2', '非交叉路口'), ('3', '弯道处'), ('4', 'T型路口'), ('5', 'Y型路口'), ('6', '环岛'), ('7', '四道路交叉口'),
    ('8', '五道或更多'),)
    relation_road = (
    ('1', '道路上'), ('2', '路肩上'), ('3', '中央隔离带'), ('4', '路边'), ('5', '道路外部'), ('6', '道路外-位置未知'), ('7', '停车场'),
    ('99', '未知'),)
    light_condition = (
    ('1', '明亮'), ('2', '昏暗'), ('3', '昏暗-点灯'), ('4', '黎明'), ('5', '黄昏'), ('6', '黑暗'), ('7', '其他'), ('9', '未知'),)
    weather = (
    ('0', '没有其他条件'), ('1', '晴'), ('2', '雨'), ('3', '雨夹雪-冰雹'), ('5', '雾-烟-霾'), ('6', '严重侧风'), ('7', '沙尘'), ('8', '其他'),
    ('10', '多云'), ('11', '风雪'), ('99', '未知'),)
    arr_hour = (
    ('0', '0时'), ('1', '1时'), ('2', '2时'), ('3', '3时'), ('4', '4时'), ('5', '5时'), ('6', '6时'), ('7', '7时'), ('8', '8时'),
    ('9', '9时'), ('10', '10时'), ('11', '11时'), ('12', '12时'), ('13', '13时'),
    ('14', '14时'), ('15', '15时'), ('16', '16时'), ('17', '17时'), ('18', '18时'), ('19', '19时'), ('20', '20时'),
    ('21', '21时'), ('22', '22时'), ('23', '23时'), ('88', '未有'), ('99', '未知'),)
    sence_factor = (('0', '无'), ('1', '出口警示'), ('2', '路肩相关'), ('3', '其他维护或建造'), ('4', '没有或模糊的路面标记'), ('5', '地表有积水/泥沙'),
                    ('6', '道路桥梁等施工或设计缺陷'), ('7', '表面冲洗（塌陷路滑）'),('8', '非接触驾驶员的侵犯-路怒'), ('9', '非机动车人员被掉落货物撞击'), ('10', '非机动车人员撞击汽车'), ('11', '运动中的车辆抛落乘客'),
                    ('12', '涉及警方追捕'), ('13', '报废车辆'), ('14', '道路之外有事情发生'), ('15', '广场停车场相关'), ('16','道路堆积有杂物/粮食-占道'),('17','道路停放车辆-占道'),('18','驶入隧道'),('19','驶出隧道'),('99', '未知'),)
    vtrafway = (('0', '非交通路口或车道通道'), ('1', '双向-不分割'), ('2', '双向-分割'), ('3', '单向交通道路'), ('9', '未知/不适用'),)
    vnum_lan=(('0','非交通路口或车道通道'),('1','一条车道'),('2','两条车道'),('3','三条车道'),('4','四条车道'),('5','五条车道'),('6','六条车道'),('7','七条车道及以上'),('9','未知'),)
    vprofile=(('0','非交通路口或车道通道'),('1','水平'),('2','斜坡-未知坡度'),('3','顶部'),('4','底部'),('5','上坡'),('6','下坡'),('9','未知'),)
    pavetyp=(('0','非交通路口或车道通道'),('1','柏油路，含沥青物'),('2','混凝土路'),('3','砖头或砖块'),('4','渣土，砾石或石块'),('5','泥土'),('6','泥土与渣土、砾石混合物'),('7','其他'),('9','未知'),)
    surcond=(('0','非交通路口或车道通道'),('1','干燥'),('2','潮湿'),('3','雪'),('4','冰/霜'),('5','沙'),('6','水-静止/流动'),('7','油'),('8','泥浆'),('9','泥土，砾石'),('99','未知'),)
    vedio=(('0','无视频'),('1','固定式监控录像'),('2','行车记录仪'),('3','固定式与行车记录仪均有'),('4','3种视频及以上'),('8','其他视频记录设备'),('9','未知'),)
    #车辆信息数据下拉表单
    unitype=(('1','在道路上运输中的车辆'),('2','在道路外'),('9','未知/不适用'),)
    hit_run=(('0','未逃逸'),('1','肇事逃逸'),('9','未知/不适用'),)
    owner=(('0','车辆未注册'),('1','驾驶员是该车注册人'),('2','驾驶员不是该车注册人'),('3','注册为商业/公司/政府车辆'),('4','车辆注册为租赁车辆'),
           ('5','该车被盗（报警）'),('6','无人驾驶/停放的机动车'),('9','未知/不适用'))
    make=(('01','大众'),('02','吉利'),('03','本田'),('04','宝骏'),('05','别克'),('06','日产'),('07','丰田'),('08','哈弗'),('09','现代'),('10','福特'),
          ('11','长安'),('12','雪佛兰'),('13','五菱'),('14','奥迪'),('15','起亚'),('16','比亚迪'),('17','传祺'),('18','奇瑞'),('19','荣威'),('20','宝马'),
          ('21', '众泰'),('22', '奔驰'),('23','斯柯达'),('24','马自达'),('25','标致'),('26','银翔'),('27','东风风光'),('28','东风风行'),('29','长安商用'),('30','江淮'),
          ('31','WEH'),('32','凯迪拉克'),('33','雪铁龙'),('34','名爵'),('35','Jeep'),('36','启辰'),('37','华泰'),('38','奔腾'),('39','名爵'),('40','绅宝'),
          ('41','一汽'),('42','海马'),('43','铃木'),('44','中华'),('45','猎豹'),('46','东风风神'),('47','开瑞'),('48','威旺'),('49','比速汽车'),('50','沃尔沃'),
          ('51', '雷克萨斯'),('52','捷豹'),('53','林肯'),('54','保时捷'),('55','mini'),('56','法拉利'),('57','玛莎拉蒂'),('58','兰博基尼'),('59','劳斯莱斯'),('60','宾利'),
          ('61','力帆'),('62','路虎'),('63','雷诺'),('64','昌河'),('65','宝沃'),('66', '北京'),('67','东风小康'),('68','知豆'),('69','观致'),('70','凯翼'),
          ('71','野马'),('72','纳智捷'),('73','英致'),('74','康迪'),('75','英菲尼迪'),('76','福田'),('77','金杯'),('78','大通'),('79','长城'),('80','讴歌'),
          ('81','东风风度'),('82','新龙马'),('83','红旗'),('84','腾势'),('85','江铃'),('86','DS'),('87','北汽制造'),('88','东风'),('89','福迪'),('90','五十铃'),
          ('91','菲亚特'),('92','华颂'),('93','恒通'),('94','宇通'),('98','其他'),('99','不适用'))
    bodytype=(('01','微型货车'),('02','轻型货车'),('03','中型货车'),('04','中型货车'),
              ('11','轻型越野车'),('12','中型越野车'),('13','重型越野车'),('14','超重型越野车'),
              ('21', '轻型自卸车'),('22','中型自卸车'),('23','重型自卸车'),('24','矿用自卸车'),
              ('31','半挂牵引车'),('32','全挂牵引车'),
              ('41','箱式汽车'),('42','罐式汽车'),('43','起重举升车'),('44','仓栅式车'),('45','特种结构车'),('46','专用自卸车'),
              ('51', '微型客车'),('52','轻型客车'),('53','中型客车'),('54','大型客车'),('55','特大型客车'),
              ('61', '微型轿车'),('62','普通级轿车'),('63','中级轿车'),('64','中高级轿车'),('65','高级轿车'),
              ('71','轻型半挂车'),('72','中型半挂车'),('73','重型半挂车'),('74','超重半挂车'),
              ('81', '摩托车'),('82','三轮车'),('99','未知/不适用'),)
    tow_veh=(('0','无拖挂单位'),('1','有一个拖挂单位'),('2','有两个拖挂单位'),('3','有三个或以上拖挂单位'),('4','有未知拖挂单位数'),('5','一辆车牵引另一辆车-固定杆'),('6','一辆车牵引另一辆车-非固定杆'),('9','未知/不适用'),)
    cargo_bt=(('0','不适用'),('1','厢式车/封闭式车'),('2','货箱'),('3','平板车'),('4','倾卸车'),('5','混泥土搅拌车'),('6','汽车运送车'),('7','垃圾车'),('8','谷物/碎块/砾石'),('9','杆拖车'),
              ('10', '车辆牵引另一辆车'),('21','巴士（9-15人）'),('22','公共汽车（16人及以上）'),('23','未知货物类型'),('99','未知'),)
    psp_use=(('0','无特殊用途'),('1','出租车'),('2','校车'),('3','巴士'),('4','军事'),('5','警察'),('6','救护车'),('7','消防车'),('99','未知/不适用'),)
    underide=(('0','无上骑下钻'),('1','下钻-舱室入侵'),('2','下钻-无舱室入侵'),('3','上骑'),('4','未知/不适用'),)
    rollover=(('0','无翻车/翻转'),('1','翻车-被物体/车辆撞翻'),('2','翻车-自身作用'),('9','未知/不适用'),)
    rolinloc=(('0','无滚动'),('1','道路上'),('2','路肩'),('3','中央隔离带/分割线'),('4','路边'),('5','道路外'),('9','未知/不适用'),)
    deformed=(('0','无损伤'),('2','轻伤'),('4','部分功能损坏'),('6','严重损坏'),('9','未知/不适用'),)
    towed=(('1','驾驶离开'),('2','由于失能被拖走'),('3','未失能被拖走'),('4','没有拖走'),('9','未知/不适用'),)
    m_harm=(('01','翻转'),('02','火灾/爆炸'),('03','浸泡/部分浸泡'),('04','吸入气体'),('05','跳车/从车内跌落'),('06','车内受伤（非碰撞）'),('07','行人'),('08','骑自行车的人'),('09','铁路车辆'),('10','动物'),('11','运输车辆'),
            ('12','停泊的车辆'),('13','投掷或落下的物体'),('14','大石头'),('15','其他非固定物体'),('16','建筑物'),('17','碰撞缓冲垫'),('18','桥梁或支柱'),('19','混凝土交通障碍'),('20','电线杆'),('21','涵洞'),('22','路边'),
            ('23', '路堤'),('24','消防栓'),('25','灌木'),('26','树木（直立）'),('27','路面不规则-凹槽、格栅等'),('28','交通信号支撑物'),('29','防撞护栏'),('30','其他'),('99','未知/不适用'),)
    fire_exp=(('0','没有或未知'),('1','是的'),('9','不适用'),)
    dr_drink=(('0','未喝酒'),('1','喝酒'),('9','未知/不适用'),)
    l_type=(('A1','A1'),('A2','A2'),('A3','A3'),('B1','B1'),('B2','B2'),('C1','C1'),('C2','C2'),('C3','C3'),('C4','C4'),('D','D'),('E','E'),('F','F'),('M','M'),('N','N'),('NON','未获得驾驶证'),('O','不适用'),)
    l_status=(('0','无许可证'),('1','暂扣'),('2','吊销'),('3','过期'),('4','有效'),('5','无驾驶员存在'),('9','不适用'),)
    l_compl=(('0','未许可'),('1','此类车辆无需许可证'),('2','无此类车辆有效许可证'),('3','是此类车辆有效许可证'),('9','未知/不适用'),)
    speedrel=(('0','否'),('1','是，赛车'),('2','是，超速'),('8','无驾驶员'),('9','未知/不适用'),)
    dr_sf1=(('0','无/不适用'),('1','粗心驾驶'),('2','路怒/侵略性的驾驶'),('3','误判行人行为'),('4','座椅靠背不恰当-斜躺'),('5','警察或执法人员'),('6','在禁止的道路驾驶'),('7','用扣留或吊销的驾照驾驶'),('8','留下发动机运行但无人看守的车辆'),('9','乘客或货物超载或装载不当'),
            ('10','不正当推车或拖车'),('11','未开灯或未及时开灯'),('12','操作不需要的设备'),('13','错误或不合理的变道'),('14','未能保持正确的车道'),('15','故意在路肩上、沟渠或人行道上非法驾驶'),('16','不恰当地进入或退出交通路口'),('17','不恰当地启动或倒车'),
            ('18','在错误的一侧通行'),('19','通过距离不足的地方/视野不足/超车时未能避让'),('20','以错误、鲁莽、粗心的方式操作车辆'),('21','未能避让道路右侧'),('22','追捕中的警察'),('23','不遵守交通标志，交通管制的设备或交警，不遵守交规'),
            ('24','穿过或绕过屏障'),('25','左转车道右转；右转车道左转'),('26','缺乏操作经验'),('27','不熟悉道路'),('28','矫正过度'),('29','严重逆风'),('30','来自卡车的风'),('31','滑溜或松散的表面'),('32','轮胎爆破或漏气'),('33','未注意到前方物体/行人'),
            ('34','视线不佳-天气原因'),('35','视线不佳-前方物体/停驶车辆遮挡'),('36','视线不佳-行驶车辆遮挡'),('37','驾驶员疲劳驾驶/睡眠不足'),('38','对向车道灯光干扰'),('39','太阳光干扰'),('40','其他光线干扰'),('99','未知'),)
    valign=(('0','非交通路口或车道通道'),('1','直行'),('2','左转'),('3','右转'),('4','转弯-方向未知'),('9','未知/不适用'),)
    p_crash=(('0','无驾驶员'),('1','直行'),('2','在道路上减速'),('3','在道路上加速'),('4','在道路上启动'),('5','停在道路'),('6','通过或超过另一辆车'),('7','离开停车位'),('8','进入停车位'),('9','左转'),('10','右转'),('11','U型转弯'),
             ('12','倒车（停车位以外）'),('13','通过弯道'),('14','变道'),('15','成功避免前面的危险事件'),('16','其他'),('99','未知/不适用'),)
    p_crash1=(('0','无驾驶员/未知驾驶员存在'),('1','无任何措施'),('2','制动'),('3','释放制动器'),('4','向左转'),('5','向右转'),('6','制动和向右转'),('7','制动和向左转'),('8','加速'),('9','加速和向左转'),('10','加速和向右转'),('11','其他行为'),('99','未知/不适用'),)
    p_crash2=(('0','无驾驶员/未知驾驶员是否存在'),('1','留下痕迹'),('2','纵向旋转小于30°'),('3','侧滑-逆时针旋转'),('4','侧滑-顺时针旋转'),('5','翻转'),('6','稳定'),('7','其他失控'),('9','未知/不适用'),)
    acc_type=(('0','无碰撞'),('1','从道路右侧离开-控制/刹车失灵'),('2','从道路左侧离开-避免碰撞行人/车辆/物体等'),('3','从道路左侧离开-其他'),('4','从道路右侧离开-控制/刹车失灵'),('5','从道路右侧离开-避免碰撞行人/车辆/物体等'),('6','从右侧道路离开-其他'),
              ('7','碰撞前方停驶车辆'),('8','碰撞前方固定物体'),('9','碰撞前方行人/动物'),('10','前方碰撞末端分离的道路（三岔路口）'),('11','前方碰撞其他'),('20','直线追尾停驶车辆'),('21','右偏追尾停驶车辆'),('22','左偏追尾停驶车辆'),
              ('23','直线追尾慢速车辆'),('24','右偏追尾慢速车辆'),('25','左偏追尾慢速车辆'),('26','直线追尾减速车辆'),('27','右偏追尾减速车辆'),('28','左偏追尾减速车辆'),('29','追尾-避让前方车辆'),('30','追尾-避让前方物体'),('31','追尾-刹车控制失灵'),
              ('32','追尾-其他'),('40','侧面相撞-直行'),('41','侧面相撞-变道到左边'),('42','侧面相撞-变道到右边'),('43','侧面相撞-其他'),('50','正碰-侧向移动（左侧/右侧）'),('51','正碰-侧向移动（直行）'),('52','正碰-其他'),
              ('53','碾压行人'),('54','碾压车辆人员'),('99','未知/不适用'),)
    #人员信息数据下拉表单
    sex=(('1','男'),('2','女'),('9','未知'),)
    per_type=(('01','运输中的机动车驾驶员'),('02','运输中的机动车乘客'),('03','非运输中机动车乘员'),('04','非机动车乘员'),
              ('05', '行人'),('06','骑自行车的人'),('07','其他骑脚踏车的人'),('10','在建筑物内或上部的人'),('19','未知'),)
    seat_pos=(('00','不是机动车乘客'),('11','前座-左侧（驾驶员侧）'),('12','前座-中间'),('13','前座-右侧'),('18','前座-其他位置'),('19','前座-未知'),
              ('21', '第二排-左侧'),('22','第二排-中间'),('23','第二排-右侧'),('28','第二排-其他'),('29','第二排-未知'),
              ('31', '第三排-左侧'),('32','第三排-中间'),('33','第三排-右侧'),('38','第三排-其他'),('39','第三排-未知'),
              ('41', '第四排-左侧'),('42','第四排-中间'),('43','第四排-右侧'),('48','第四排-其他'),('49','第四排-未知'),
              ('50', '驾驶室（卡车）卧铺'),('51','在其他封闭区域的乘客'),('52','其他在未封闭区域的乘客'),('53','在乘客或货物区域的乘客，无论封闭与否'),
              ('54','拖尾单位'),('55','骑在车外'),('99','未知'),)
    rest_use=(('0','不适用'),('1','仅使用肩带'),('2','仅使用腰带'),('3','肩带和腰带'),('4','儿童安全座椅'),('5','符合标准的摩托车头盔'),
              ('6','自行车头盔'),('7','未使用'),('96','不是车辆乘员'),('97','其他'),('98','未知'),)
    air_bag=(('01','不适用'),('02','部署-前'),('03','部署-侧（门，座椅）'),('04','部署-窗帘（顶）'),('07','部署-其他'),('08','组合'),
             ('09','部署-未知位置'),('20','未部署'),('98','不是车辆乘员'),('99','未知'),)
    ejection=(('0','未弹出'),('1','部分弹出'),('2','完全弹出'),('3','弹出-程度未知'),('8','不适用'),('9','未知'),)#只适用于汽车
    ej_path=(('0','未弹出/不适用'),('1','侧门弹出'),('2','侧窗弹出（巴士侧窗）'),('3','前挡风玻璃'),('4','后窗弹出（厢式车等）'),('5','后门/开启的尾门'),
             ('6','开放的车顶（敞篷车等）'),('7','其他路径（皮卡背部等）'),('9','未知/未知路径'),)
    drinking=(('0','未饮酒'),('1','饮酒'),('9','未知'),)
    drug_det=(('0','未涉及药物'),('1','涉及药物'),('9','未知'),)
    max_ais = (('AIS0', '未受伤'), ('AIS1', '轻度'), ('AIS2', '中度'), ('AIS3', '重度'), ('AIS4', '严重'), ('AIS5', '伤情危急'),
               ('AIS6', '最严重的伤情，目前无法救治'), ('AIS9', '创伤等级未知'),)
    doa=(('0','不适用'),('1','当场死亡'),('2','在前往医疗机构的途中死亡'),('3','抢救无效死亡（一个月之内）'),('9','未知'),)
    location=(('0','不适用-车辆乘员'),('1','交叉路口-人行横道'),('2','交叉路口-非人行横道'),('3','交叉路口-位置未知'),
              ('11','非交叉路口-人行横道'),('12','非交叉路口-非人行横道'),('13','非交叉路口-位置未知'),
              ('20', '路肩/路边'),('21','人行横道'),('22','中央隔离带'),('99','未知'),)
    head_hurt=(('0','未受伤'),('1','受伤'),('9','未知/不适用'),)
    chest_hurt=(('0','未受伤'),('1','受伤'),('9','未知/不适用'),)#胸部伤情
    abdomen_hurt=(('0','未受伤'),('1','受伤'),('9','未知/不适用'),)#腹部伤情
    legs_hurt=(('0','未受伤'),('1','受伤'),('9','未知/不适用'),)#下肢伤情
    fracture_part=(('0','未骨折'),('1','肋骨'),('2','胸骨'),('3','盆骨'),('4','面部'),('5','上肢骨'),('6','下肢骨'),('7','脊柱'),('8','颈部'),('9','未知/不可用'),)#骨折部位
    death=(('1','死亡'),('2','受伤'),('3','未受伤'),('9','未知'),)
    death_reason=(('1','头部'),('2','胸部'),('3','腹部'),('4','胸部及腹部'),('8','综合'),('9','未知/不适用'),)
    harnpan=(('0','未骨折'),('1','颞骨'),('2','枕骨'),('3','顶骨'),('4','额骨'),('5','蝶骨'),('6','颅底'),('7','骨折，未知位置'),('9','未知/不适用'),)
    in_hemorrhage = (('0', '未出血'), ('1', '硬膜下腔'), ('2', '蛛网膜下腔'), ('3', '脑'), ('4', '硬膜外'), ('5', '脑挫裂伤'), ('6', '脑室内'), ('9', '未知/不适用'),)


class Accident(models.Model):
    NAME = models.CharField(max_length=30, default='点击保存时会自动编码', help_text='案件编码')
    CITY = models.CharField(max_length=10, default='000000', help_text='行政区划分代码')
    NUM=models.CharField(max_length=5,default="0001",help_text="地区案件编号,4位数")
    PEDS = models.PositiveIntegerField(default='0',help_text='非机动车内总人数')
    PERNOTMVIT = models.PositiveIntegerField(default='0',help_text='行人总数')
    VE_TOTAL = models.PositiveIntegerField(default='0',help_text='车辆总数')
    PVH_INVL = models.PositiveIntegerField(default='0',help_text='停放车辆总数')
    PERSONS = models.PositiveIntegerField(default='0',help_text='机动车人员总数')
    PERMVIT = models.PositiveIntegerField(default='0',help_text='运输中的机动车人员总数')

    YEAR = models.PositiveIntegerField(default='9999', help_text='事发年份')
    MONTH = models.CharField(max_length=5, help_text='事故月份', default='未知', choices=AccidentData.month)
    DAY = models.CharField(max_length=5, help_text='事故日期', choices=AccidentData.day, default='1号')
    DAY_WEEK = models.CharField(max_length=10, default='星期一', choices=AccidentData.week, help_text='事发是周几')
    HOUR=models.CharField(max_length=5,default='0',choices=AccidentData.hour,help_text="事发时小时数")
    MINUTE=models.CharField(max_length=5,default=00,help_text="事发时分钟数")
    WEATHER = models.CharField(max_length=10, choices=AccidentData.weather, default='晴', help_text='天气状况')
    LGT_COND = models.CharField(max_length=10, choices=AccidentData.light_condition,default='明亮', help_text='明暗程度')
    SURCOND=models.CharField(max_length=10,default="1",choices=AccidentData.surcond,help_text="事发时道路表面状态")
    PAVETYP=models.CharField(max_length=20,default="1",choices=AccidentData.pavetyp,help_text="事发时道路表面材质")
    VEDIO=models.CharField(max_length=15,default='0',choices=AccidentData.vedio,help_text="记录此案件或与此案件相关的视频")
    REL_ROAD = models.CharField(max_length=10, choices=AccidentData.relation_road, default='未知',help_text='发生初次有害事件时位置信息')
    NHS = models.CharField(max_length=2, choices=AccidentData.nation_highway_system,default='是', help_text='是否国家道路系统')
    ROUTE = models.CharField(max_length=10, choices=AccidentData.route,default='未知', help_text='道路标志')
    ROUTE1 = models.CharField(max_length=40,default='', help_text='具体位置')
    TYP_INT = models.CharField(max_length=10, choices=AccidentData.type_intersection,default='未知', help_text='交叉路口类型')

    ARR_HOUR = models.CharField(max_length=10,choices=AccidentData.arr_hour,default=99,help_text='医疗服务到达小时数')
    ARR_MIN=models.CharField(max_length=5,default=99,help_text='医疗服务到达分钟数，99为未知')
    SFACTOR = models.CharField(max_length=20,default='0',choices=AccidentData.sence_factor,help_text='现场勘查状况，最多4项')
    SFATOR1=models.CharField(max_length=20,default='0',choices=AccidentData.sence_factor,help_text='现场勘查状况，最多4项')
    SFATOR2 = models.CharField(max_length=20, default='0', choices=AccidentData.sence_factor, help_text='现场勘查状况，最多4项')
    SFATOR3 = models.CharField(max_length=20, default='0', choices=AccidentData.sence_factor, help_text='现场勘查状况，最多4项')
    DRUNK_DR = models.PositiveIntegerField(default=0,help_text='酒驾人员数目')
    FATALS = models.PositiveIntegerField(default=0, help_text='事发时死亡人数')
    VTRAFWAY=models.CharField(max_length=10,default="9",choices=AccidentData.vtrafway,help_text="事故之前的交通流量信息")
    VNUM_LAN=models.CharField(max_length=10,default="9",choices=AccidentData.vnum_lan,help_text="事发时车道信息，若车道相邻则算道路横截面车道")
    VSPED_LIM=models.PositiveIntegerField(default=999,help_text="道路限速（km/h），999未知")
    VPROFILE=models.CharField(max_length=10,default="9",choices=AccidentData.vprofile,help_text="事发道路是时的坡度信息")
    pub_date = models.DateTimeField(default=timezone.now)
    def __unicode__(self):
        return self.NAME

class VehicleData(models.Model):
    accident=models.ForeignKey(Accident, on_delete=models.CASCADE,default='')
    VEH_NO=models.CharField(max_length=5,default='00',help_text="事故车辆编号，行人为00,2位数")
    NAME=models.CharField(max_length=30,default="点击保存时会自动编码",help_text="车辆编码")
    OCUPANTS=models.PositiveIntegerField(default=99,help_text="本机动车内乘员人数，未知99")
    UNTYPE=models.CharField(max_length=20,default="9",choices=AccidentData.unitype,help_text="车辆状况信息")
    HIT_RUN=models.CharField(max_length=10,choices=AccidentData.hit_run,default="9",help_text="肇事逃逸状况")
    OWNER=models.CharField(max_length=20,choices=AccidentData.owner,default="9",help_text="这辆车所有者的类型")
    MAKE=models.CharField(max_length=10,default="99",choices=AccidentData.make,help_text="该汽车品牌")
    BODYTYPE=models.CharField(max_length=10,default="99",choices=AccidentData.bodytype,help_text="该车辆的车级分类")
    MOD_YEAR=models.PositiveIntegerField(default=2017,help_text="该车辆制造年份，9999未知/不适用")
    VIN=models.CharField(max_length=20,default="999999999999",help_text="该车车辆识别代码，999999999999未知/不适用")
    TOW_VEH=models.CharField(max_length=15,default="9",choices=AccidentData.tow_veh,help_text="该车辆是否有拖拽单位或者车辆")
    CARGO_BT=models.CharField(max_length=20,default="0",choices=AccidentData.cargo_bt,help_text="该车辆拉载承重类型")
    PSP_USE=models.CharField(max_length=10,choices=AccidentData.psp_use,default="99",help_text="该车辆是否有任何特殊用途")
    TRAV_SP=models.CharField(max_length=5,default=999,help_text="事发前该车速度km/h,999未知")
    UNDERIDE=models.CharField(max_length=20,default='4',choices=AccidentData.underide,help_text="该车辆是否发生上骑下钻，被撞时不计入在内/碾压也为上骑下钻")
    ROLLOVER=models.CharField(max_length=20,default='9',choices=AccidentData.rollover,help_text="该车是否翻转或翻车")
    ROLINLOC=models.CharField(max_length=10,default="9",choices=AccidentData.rolinloc,help_text="该车滚动起始位置")
    DEFORMED=models.CharField(max_length=10,default="9",choices=AccidentData.deformed,help_text="该车损伤严重程度")
    TOWED=models.CharField(max_length=10,default="9",choices=AccidentData.towed,help_text="该车移除方式")
    M_HARM=models.CharField(max_length=15,default="99",choices=AccidentData.m_harm,help_text="受伤：描述最大的伤害事件；未受伤：车辆最大财产损失")
    FIRE_EXP=models.CharField(max_length=10,default="99",choices=AccidentData.fire_exp,help_text="是否发生与碰撞相关的火灾")
    DEATH=models.PositiveIntegerField(default=99,help_text="该车辆中的总死亡人数（与此次事故相关的死亡人数都统计在内）,99不适用")
    DEATH_SEN=models.PositiveIntegerField(default=99,help_text="该车辆内当场死亡人数（不含救护途中死亡的人数），99未知")
    DR_DRINK=models.CharField(max_length=5,default="9",choices=AccidentData.dr_drink,help_text="该车驾驶员是否喝酒")
    L_TYPE=models.CharField(max_length=10,default="O",choices=AccidentData.l_type,help_text="该车驾驶员驾驶证级别")
    L_STATUS=models.CharField(max_length=10,default="9",choices=AccidentData.l_status,help_text="该车驾驶员驾驶证状态")
    L_COMPL=models.CharField(max_length=20,default="9",choices=AccidentData.l_compl,help_text="该车驾驶员是否拥有该车辆驾驶许可证")
    SPEEDREL=models.CharField(max_length=20,default="9",choices=AccidentData.speedrel,help_text="该车是否超速")
    DR_SF1=models.CharField(max_length=30,default="0",choices=AccidentData.dr_sf1,help_text="该元素表示与驾驶员相关的因素，最多4项")
    DR_SF2=models.CharField(max_length=30, default="0", choices=AccidentData.dr_sf1, help_text="该元素表示与驾驶员相关的因素，最多4项")
    DR_SF3=models.CharField(max_length=30, default="0", choices=AccidentData.dr_sf1, help_text="该元素表示与驾驶员相关的因素，最多4项")
    DR_SF4=models.CharField(max_length=30, default="0", choices=AccidentData.dr_sf1, help_text="该元素表示与驾驶员相关的因素，最多4项")
    VALIGN=models.CharField(max_length=10,default="9",choices=AccidentData.valign,help_text="事发前该车辆对准道路的信息")
    P_CRASH=models.CharField(max_length=15,default="99",choices=AccidentData.p_crash,help_text="驾驶员实意识到发生的危险事件或驾驶员未采取行动或来不及采取避让措施的碰撞之前最能描述车辆活动")
    P_CRASH1=models.CharField(max_length=15,default="99",choices=AccidentData.p_crash1,help_text="该车驾驶员在事故前采取的措施")
    P_CRASH2=models.CharField(max_length=15,default="9",choices=AccidentData.p_crash2,help_text="该车辆在事故前的稳定性")
    ACC_TYPE=models.CharField(max_length=30,default="99",choices=AccidentData.acc_type,help_text="该车辆的碰撞类型（根据第一次事故判断）")
    pub_date = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.NAME

class PersonData(models.Model):
    vehicle=models.ForeignKey(VehicleData,on_delete=models.CASCADE,default='')
    PER_NO=models.CharField(max_length=10,default='01',help_text="该人员编号，行人与乘员（含驾驶员）分开编码")
    NAME=models.CharField(max_length=30,default="点击保存时会自动编码",help_text="人员编码")
    AGE=models.PositiveIntegerField(default=999,help_text="该人年龄，999未知")
    SEX=models.CharField(max_length=2,choices=AccidentData.sex,default="未知",help_text="该人性别")
    HEIGHT=models.CharField(max_length=5,default=999,help_text="该人员身高cm,999未知")
    PER_TYPE=models.CharField(max_length=15,choices=AccidentData.per_type,default="未知",help_text="该人员类型")
    SEAT_POS=models.CharField(max_length=25,choices=AccidentData.seat_pos,default="不是机动车乘客",help_text="该人员所处于车辆内的位置")
    REST_USE=models.CharField(max_length=10,choices=AccidentData.rest_use,default="不是车辆乘员",help_text="该人员安全带的使用情况")
    AIR_BAG=models.CharField(max_length=10,choices=AccidentData.air_bag,default="不适用",help_text="安全气囊部署状况")
    EJECTION=models.CharField(max_length=10,choices=AccidentData.ejection,default=8,help_text="该人员从车内弹出状况（仅限汽车）")
    EJ_PATH=models.CharField(max_length=15,choices=AccidentData.ej_path,default="未弹出/不适用",help_text="该人员的弹出路径")
    DRINKING=models.CharField(max_length=5,choices=AccidentData.drinking,default="未饮酒",help_text="该人员饮酒与否")
    ALC_RES=models.PositiveIntegerField(default=999,help_text="酒精测试结果mg/100ml（吹气/血检），999未知")
    DRUG_DET=models.CharField(max_length=10,choices=AccidentData.drug_det,default="未涉及药物",help_text="该人员是否涉及药物（包括毒品）")
    MAX_AIS=models.CharField(max_length=15,choices=AccidentData.max_ais,default="创伤等级未知",help_text="该人员最大创伤等级")
    HEAD_HURT=models.CharField(max_length=5,default='0',choices=AccidentData.head_hurt,help_text="头部是否受伤")
    CHEST_HURT=models.CharField(max_length=5,default='0',choices=AccidentData.chest_hurt,help_text="胸部是否受伤")
    ABDOMEN_HURT=models.CharField(max_length=5,default='0',choices=AccidentData.abdomen_hurt,help_text="腹部是否受伤")
    LEGS_HURT=models.CharField(max_length=5,default='0',choices=AccidentData.legs_hurt,help_text="下肢是否受伤")
    FRACTURE = models.CharField(max_length=5, default='0', choices=AccidentData.fracture_part, help_text="骨折部位")  # 骨折部位
    FRACTURE1 = models.CharField(max_length=5, default='0', choices=AccidentData.fracture_part, help_text="骨折部位")  # 骨折部位
    FRACTURE2 = models.CharField(max_length=5, default='0', choices=AccidentData.fracture_part, help_text="骨折部位")  # 骨折部位
    FRACTURE3 = models.CharField(max_length=5, default='0', choices=AccidentData.fracture_part, help_text="骨折部位")  # 骨折部位
    FRACTURE4 = models.CharField(max_length=5, default='0', choices=AccidentData.fracture_part, help_text="骨折部位")  # 骨折部位
    FRACTURE5 = models.CharField(max_length=5, default='0', choices=AccidentData.fracture_part, help_text="骨折部位")  # 骨折部位
    FRACTURE6 = models.CharField(max_length=5, default='0', choices=AccidentData.fracture_part, help_text="骨折部位")  # 骨折部位
    DEATH=models.CharField(max_length=10,choices=AccidentData.death,default='1',help_text="该人员是否死亡")
    DREASON=models.CharField(max_length=10,choices=AccidentData.death_reason,default='9',help_text="身体哪个部位创伤导致死亡")
    HARNPAN1 = models.CharField(max_length=5, choices=AccidentData.harnpan, default='0', help_text="颅骨骨折")
    HARNPAN2 = models.CharField(max_length=5, choices=AccidentData.harnpan, default='0', help_text="颅骨骨折")
    HARNPAN3 = models.CharField(max_length=5, choices=AccidentData.harnpan, default='0', help_text="颅骨骨折")
    HARNPAN4 = models.CharField(max_length=5, choices=AccidentData.harnpan, default='0', help_text="颅骨骨折")
    HARNPAN5 = models.CharField(max_length=5, choices=AccidentData.harnpan, default='0', help_text="颅骨骨折")
    HARNPAN6 = models.CharField(max_length=5, choices=AccidentData.harnpan, default='0', help_text="颅骨骨折")
    IN_HEMORRHAGE1 = models.CharField(max_length=10, choices=AccidentData.in_hemorrhage, default='0', help_text="颅内出血")
    IN_HEMORRHAGE2 = models.CharField(max_length=10, choices=AccidentData.in_hemorrhage, default='0', help_text="颅内出血")
    IN_HEMORRHAGE3 = models.CharField(max_length=10, choices=AccidentData.in_hemorrhage, default='0', help_text="颅内出血")
    IN_HEMORRHAGE4 = models.CharField(max_length=10, choices=AccidentData.in_hemorrhage, default='0', help_text="颅内出血")
    IN_HEMORRHAGE5 = models.CharField(max_length=10, choices=AccidentData.in_hemorrhage, default='0', help_text="颅内出血")
    IN_HEMORRHAGE6 = models.CharField(max_length=10, choices=AccidentData.in_hemorrhage, default='0', help_text="颅内出血")
    DOA=models.CharField(max_length=15,choices=AccidentData.doa,default="不适用",help_text="该人员死亡地点")
    ICU_HOURS=models.PositiveIntegerField(default=999,help_text="该人员在重症监护室内所呆时间（小时），999未知/不适用")
    DEATH_HOURS=models.PositiveIntegerField(default=999,help_text="记录事故与死亡之间的时间间隔（小时），999未知/不适用")
    RACE=models.CharField(max_length=20,default="汉族",help_text="该人员民族信息，外国人则写国籍")
    LOCATION=models.CharField(max_length=20,choices=AccidentData.location,default="不适用-车辆乘员",help_text="该人员事发时所处的位置")
    pub_date = models.DateTimeField(default=timezone.now)
    def __unicode__(self):
        return self.NAME


class Photo(models.Model):
    accident=models.ForeignKey(Accident, on_delete=models.CASCADE,default='')
    NAME=models.CharField(max_length=20,default='点击保存时会自动命名')
    YEAR=models.PositiveIntegerField(default=2018,help_text="年份")
    MONTH=models.PositiveIntegerField(default=01,help_text="月份")
    DAY=models.PositiveIntegerField(default=01,help_text="号数")
    URL=models.URLField(default="",help_text="现场照片链接地址")
    def __unicode__(self):
        return self.NAME