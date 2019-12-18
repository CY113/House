# -*- coding: utf-8 -*-
# @Time   :   2019-03-14
# @Python :   3.6.1
# @IDE    :   Pycharm
import scrapy
from item.Esf_House_Detail_Item import EsfHouseDetailItem
from tools.QueryData import QueryData


class ESFHouseDetailSpider(scrapy.Spider):
    """
    抓取二手房详情信息
    """
    name = 'esf_house_detail'

    def __init__(self):
        self.url_list = QueryData().get_esf_house_url()

    def start_requests(self):
        for url in self.url_list:
            yield scrapy.Request(url=url[0], callback=self.parse)

    def parse(self, response):
        item = EsfHouseDetailItem()
        item["name"] = response.xpath('//h1/text()').get()  # 房产名称
        item["total_price"] = response.xpath('//div[contains(@class,"price_esf")]/i/text()').get() # 总价格
        item["rooms"] = response.xpath('//div[@class="tt"]/text()').getall()[0]  # 户型
        item["area"] = response.xpath('//div[@class="tt"]/text()').getall()[1]  # 建筑面积
        item["per_price"] = response.xpath('//div[@class="tt"]/text()').getall()[2]   # 单价
        item["towards"] = response.xpath('//div[@class="tt"]/text()').getall()[3]   # 朝向
        item["floor"] = response.xpath('//div[@class="tt"]/text()').getall()[4]   # 楼层
        item["decoration"] = response.xpath('//div[@class="tt"]/text()').getall()[5]   # 装修
        try:
            item["year"] = response.xpath('//span[text()="建筑年代"]/following::*[1]/text()').get()   # 建筑年代
        except:
            item["year"] = ""
        try:
            item["elevator"] = response.xpath('//span[text()="有无电梯"]/following::*[1]/text()').get()   # 有无电梯
        except:
            item["elevator"] = ""
        try:
            item["category"] = response.xpath('//span[text()="住宅类别"]/following::*[1]/text()').get()   # 住宅类别
        except:
            item["category"] = ""
        try:
            item["building_structure"] = response.xpath('//span[text()="建筑结构"]/following::*[1]/text()').get()   # 建筑结构
        except:
            item["building_structure"] = ""
        try:
            item["building_category"] = response.xpath('//span[text()="建筑类别"]/following::*[1]/text()').get()   # 建筑类型
        except:
            item["building_category"] = ""
        try:
            item["time"] = response.xpath('//span[text()="挂牌时间"]/following::*[1]/text()').get().strip()   # 挂牌时间
        except:
            item["time"] = ""
        yield item

