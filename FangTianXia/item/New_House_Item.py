# coding = utf-8
# @Time   :   2019-03-14
# @Python :   3.6.1
# @IDE    :   Pycharm
import scrapy

class NewHouseItem(scrapy.Item):
    province = scrapy.Field() # 省份
    city = scrapy.Field() # 城市
    name = scrapy.Field() # 名称
    area = scrapy.Field() # 地区
    district = scrapy.Field()
    sale = scrapy.Field() #成交量
    origin_url = scrapy.Field() # 原始url
    detail_url = scrapy.Field() # 详单级url


    # 数据库插入语句
    def get_insert_sql(self):
        insert_sql = "insert into new_house(province,city,name,area,district,sale,origin_url,detail_url)" \
                     "values (%s,%s,%s,%s,%s,%s,%s,%s)"
        params = (self['province'],self['city'],self['name'],self['area'],self['district'],self['sale'],self['origin_url'],self['detail_url'])
        return insert_sql, params
