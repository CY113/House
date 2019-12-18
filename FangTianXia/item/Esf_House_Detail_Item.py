# coding = utf-8
# @Time   :   2019-03-14
# @Python :   3.6.1
# @IDE    :   Pycharm

import scrapy


class EsfHouseDetailItem(scrapy.Item):
    name = scrapy.Field()  # 房产名称
    total_price = scrapy.Field()  # 总价格
    rooms = scrapy.Field()  # 户型
    area = scrapy.Field()  # 建筑面积(平米)
    per_price = scrapy.Field()  # 单价(元/平米)
    towards = scrapy.Field()  # 朝向
    floor = scrapy.Field()  # 楼层
    decoration = scrapy.Field()  # 装修
    year = scrapy.Field()  # 建筑年代
    elevator = scrapy.Field()  # 有无电梯
    category = scrapy.Field()  # 住宅类别
    building_structure = scrapy.Field()  # 建筑结构
    building_category = scrapy.Field()  # 建筑类别
    time = scrapy.Field()  # 挂牌时间

    def get_insert_sql(self):
        """
        插入esf_house_detail表，在pipeline中调用
        :return: sql语句，插入参数
        """
        sql = "insert into esf_house_detail(name,total_price,rooms,area,per_price,towards,floor,decoration,year,elevator,category,building_structure,building_category,time)" \
              " values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        params = (
            self["name"], self["total_price"], self["rooms"], self["area"],
            self["per_price"], self["towards"], self["floor"],
            self["decoration"], self["year"],
            self["elevator"], self["category"], self["building_structure"],
            self["building_category"], self["time"])
        return sql, params
