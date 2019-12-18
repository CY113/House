# -*- coding: utf-8 -*-
# @Time   :   2019-03-14
# @Python :   3.6.1
# @IDE    :   Pycharm
import scrapy
from item.Esf_House_Item import ESF_House_Item


class EsfHouseSpider(scrapy.Spider):
    """
    抓取二手房基本信息，主要目标为二手房详情页面
    """
    name = 'esf_house'
    start_urls = ['http://www.fang.com/SoufunFamily.htm']

    def parse(self, response):
        trs = response.xpath('//div[@class="outCont"]//tr[@id]')
        province_name = None
        for tr in trs:
            province = tr.xpath('./td[not(@class)]/strong/text()').get("")
            if province == "其它":
                continue
            if province and province != " ":
                province_name = province
            city_tds = tr.xpath('./td[last()]/a')
            for city in city_tds:
                city_name = city.xpath('./text()').get()
                city_url = city.xpath('./@href').get()

                if "bj." in city_url:
                    esf_house_url = "http://esf.fang.com/"
                else:
                    house_url = city_url.split("//")
                    esf_house_url = house_url[0] + "//esf." + house_url[1]
                yield scrapy.Request(url=esf_house_url,
                                     callback=self.parse_esf_house,
                                     meta={"info": (province_name, city_name)})

    def parse_esf_house(self, response):
        province, city = response.meta.get('info')
        dls = response.xpath('//div[@class="shop_list shop_list_4"]/dl[@id]')
        for dl in dls:
            name = dl.xpath('.//span[@class="tit_shop"]/text()').get()
            address = dl.xpath('.//p[@class="add_shop"]/a/@title').get()
            location = dl.xpath('.//p[@class="add_shop"]//span/text()').get()
            origin_url = response.url
            detail_url = response.urljoin(dl.xpath('.//h4[@class="clearfix"]/a/@href').get())
            item = ESF_House_Item(province=province, city=city, name=name,address=address, location=location,origin_url=origin_url,detail_url=detail_url)
            yield item
        next_page = response.xpath('//div[@id="list_D10_15"]/p[1]/a/@href').get()
        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page),
                                 callback=self.parse_esf_house,
                                 meta={"info": (province, city)})
