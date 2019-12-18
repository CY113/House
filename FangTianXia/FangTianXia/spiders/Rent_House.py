# -*- coding: utf-8 -*-
# @Time   :   2019-03-15
# @Python :   3.6.1
# @IDE    :   Pycharm
import scrapy
from item.Esf_House_Item import ESF_House_Item
from item.Rent_House_Item import RentHouseItem


class RentHouseSpider(scrapy.Spider):
    """
    住区租房基本信息，获得租房详情URL列表
    """
    name = 'rent_house'
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
                    rent_house_url = "https://zu.fang.com/"
                else:
                    house_url = city_url.split("//")
                    rent_house_url = house_url[0] + "//zu." + house_url[1]
                yield scrapy.Request(url=rent_house_url,
                                     callback=self.parse_rent_house,
                                     meta={"info": (province_name, city_name)})

    def parse_rent_house(self, response):
        province, city = response.meta.get('info')
        dls = response.xpath('//div[@class="houseList"]/dl/dd')
        for dl in dls:
            name = dl.xpath('./p[@class="title"]/a/@title').get()
            address = '-'.join(dl.xpath('./p[@class="gray6 mt12"]//span/text()').getall())
            label = ','.join(dl.xpath('./p[@class="mt12"]//span/text()').getall())
            origin_url = response.url
            detail_url = response.urljoin(dl.xpath('./p[@class="title"]/a/@href').get())
            item = RentHouseItem(province=province, city=city, name=name,address=address, label=label,origin_url=origin_url,detail_url=detail_url)
            yield item
        next_page = response.xpath('//a[text()="下一页"]/@href').get()
        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page),
                                 callback=self.parse_rent_house,
                                 meta={"info": (province, city)})
