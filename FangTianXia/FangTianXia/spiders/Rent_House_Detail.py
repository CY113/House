# -*- coding: utf-8 -*-
# @Time   :   2019-03-15
# @Python :   3.6.1
# @IDE    :   Pycharm
import scrapy
from item.Rent_House_Detail_Item import RentHouseDetailItem
from tools.QueryData import QueryData


class RentHouseDetailSpider(scrapy.Spider):
    """
    获取租房详情页信息
    """
    name = 'rent_house_detail'

    def __init__(self):
        self.url_list = QueryData().get_rent_house_url()

    def start_requests(self):
        for url in self.url_list:
            yield scrapy.Request(url=url[0], callback=self.parse)

    def parse(self, response):
        item = RentHouseDetailItem()
        item["name"] = response.xpath('//h1/text()').get()
        item["price"] = response.xpath(
            '//div[contains(@class,"trl-item sty1")]/i/text()').get() + ''.join(
            response.xpath(
                '//div[contains(@class,"trl-item sty1")]/text()').getall()).strip()
        item["rent_way"] = response.xpath('//div[@class="tt"]/text()')[0].get()
        item["room"] = response.xpath('//div[@class="tt"]/text()')[1].get()
        item["area"] = response.xpath('//div[@class="tt"]/text()')[2].get()
        item["toward"] = response.xpath('//div[@class="tt"]/text()')[3].get()
        item["floor"] = response.xpath('//div[@class="tt"]/text()')[4].get()
        item["decoration"] = response.xpath('//div[@class="tt"]/text()')[
            5].get()
        item["community"] = ''.join(response.xpath(
            '//div[@class="trl-item2 clearfix"][1]/div[2]//text()').getall())
        item["region"] = ''.join(response.xpath(
            '//div[@class="trl-item2 clearfix"][2]/div[@class="rcont"]//text()').getall()).strip()
        yield item
