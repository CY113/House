# coding = utf-8
# @Time   :   2019-03-15
# @Python :   3.6.1
# @IDE    :   Pycharm
import scrapy

class RentHouseDetailItem(scrapy.Item):
    name = scrapy.Field() # 房源
    price = scrapy.Field() # 价格
    rent_way = scrapy.Field() # 出租方式
    room = scrapy.Field() # 户型
    area = scrapy.Field() # 建筑面积
    toward = scrapy.Field() # 朝向
    floor = scrapy.Field() # 楼层
    decoration = scrapy.Field() # 精装修
    community = scrapy.Field() # 小区
    region = scrapy.Field() # 地址


    # 数据库插入语句
    def get_insert_sql(self):
        insert_sql = "insert into rent_house_detail(name,price,rent_way,room,area,toward,floor,decoration,community,region)" \
                     "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        params = (self['name'],self['price'],self['rent_way'],self['room'],self['area'],self['toward'],self['floor'],self['decoration'],self['community'],self['region'])
        return insert_sql, params
