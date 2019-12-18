# coding=utf-8
# @Time   :   2019-03-14
# @Python :   3.6.1
# @IDE    :   Pycharm
import scrapy


class ESF_House_Item(scrapy.Item):
    province = scrapy.Field()  # 省份
    city = scrapy.Field()  # 城市
    name = scrapy.Field()
    address = scrapy.Field()
    location = scrapy.Field()
    origin_url = scrapy.Field()
    detail_url = scrapy.Field()

    # 数据库插入语句
    def get_insert_sql(self):
        insert_sql = "insert into esf_house(province,city,name,address,location,origin_url,detail_url)" \
                     "values (%s,%s,%s,%s,%s,%s,%s)"
        params = (self['province'], self['city'], self['name'],self['address'],self['location'],self['origin_url'],self['detail_url'])
        return insert_sql, params
