# coding = utf-8
# @Time   :   2019-03-14
# @Python :   3.6.1
# @IDE    :   Pycharm
import scrapy


class NewHouseDetailItem(scrapy.Item):
    """
    新房详细信息
    """
    name = scrapy.Field()  # 房产名称
    price = scrapy.Field()  # 价格
    score = scrapy.Field()  # 评分
    total_comment = scrapy.Field()  # 评论总数
    property_category = scrapy.Field()  # 物业类别
    advantage = scrapy.Field()  # 项目特色
    building_category = scrapy.Field()  # 建筑类别
    age = scrapy.Field()  # 产权年限
    location = scrapy.Field()  # 环线位置
    developer = scrapy.Field()  # 开发商
    address = scrapy.Field()  # 楼盘地址

    sales_status = scrapy.Field()  # 销售状态
    offer = scrapy.Field()  # 楼盘优惠
    opening_time = scrapy.Field()  # 开盘时间
    finish_time = scrapy.Field()  # 交房时间
    sale_address = scrapy.Field()  # 售楼地址
    tel = scrapy.Field()  # 咨询电话
    house_type = scrapy.Field()  # 主力户型

    floor_area = scrapy.Field()  # 占地面积
    construction_area = scrapy.Field()  # 建筑面积
    volume_rate = scrapy.Field()  # 容积率
    greening_rate = scrapy.Field()  # 绿化率
    parking = scrapy.Field()  # 停车位
    total_building = scrapy.Field()  # 楼栋总数
    total_houses = scrapy.Field()  # 总户数
    property_company = scrapy.Field()  # 物业公司
    property_costs = scrapy.Field()  # 物业费
    floor_condition = scrapy.Field()  # 楼层状况

    traffic = scrapy.Field()  # 交通
    mall = scrapy.Field()  # 综合商场
    hospital = scrapy.Field()  # 医院
    bank = scrapy.Field()  # 银行
    others = scrapy.Field()  # 其他
    support = scrapy.Field()  # 小区内部配套

    def get_insert_sql(self):
        sql = "insert into new_house_detail(name,price,score,total_comment,property_category,advantage,building_category,age,location,developer,address,sales_status,offer,opening_time,finish_time,sale_address,tel,house_type,floor_area,construction_area,volume_rate,greening_rate,parking,total_building,total_houses,property_company,property_costs,floor_condition,traffic,mall,hospital,bank,others,support)" \
              " values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        params = (
            self["name"], self["price"], self["score"], self["total_comment"],
            self["property_category"], self["advantage"],
            self["building_category"],
            self["age"], self["location"], self["developer"], self["address"],
            self["sales_status"], self["offer"], self["opening_time"],
            self["finish_time"], self["sale_address"], self["tel"],
            self["house_type"], self["floor_area"], self["construction_area"],
            self["volume_rate"], self["greening_rate"], self["parking"],
            self["total_building"], self["total_houses"],
            self["property_company"],
            self["property_costs"], self["floor_condition"], self["traffic"],
            self["mall"], self["hospital"], self["bank"], self["others"],
            self["support"])
        return sql, params
