# -*- coding: utf-8 -*-
# @Time   :   2019-03-14
# @Python :   3.6.1
# @IDE    :   Pycharm
import re
import scrapy
from item.New_House_Item import NewHouseItem


class FangTianXiaSpider(scrapy.Spider):
    """
    根据全国城市页面拼接目标url,并抓取新房基本信息，主要目标为新房详情页URL
    """
    name = 'new_house'
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
                    new_house_url = "http://newhouse.fang.com/house/s/"
                else:
                    house_url = city_url.split("//")
                    new_house_url = house_url[0] + "//newhouse." + house_url[
                        1] + "/house/s/"

                yield scrapy.Request(url=new_house_url,
                                     callback=self.parse_new_house,
                                     meta={"info": (province_name, city_name)})

    def parse_new_house(self, response):
        province, city = response.meta.get('info')
        lis = response.xpath(
            '//div[@id="newhouse_loupai_list"]/ul/li[not(@class)]')
        for li in lis:
            name = li.xpath('.//div[@class="nlcd_name"]/a/text()').get(
                "").strip()
            area = ",".join(li.xpath(
                './/div[@class="house_type clearfix"]/text()').getall())
            try:
                area = re.search("\d+.*米", area).group()
            except Exception:
                area = ""
            district = ",".join(li.xpath(
                './/div[contains(@class,"fangyuan")]/a//text()').getall())
            sale = li.xpath(
                './/div[contains(@class,"fangyuan")]/span/text()').get()
            origin_url = response.url
            detail_url = "https:" + li.xpath(
                './/div[@class="nlcd_name"]/a/@href').get()
            item = NewHouseItem(province=str(province), city=city, name=name,
                                area=area, district=district,
                                sale=sale, origin_url=origin_url,
                                detail_url=detail_url)
            yield item
        next_page = response.xpath('//a[@class="next"]/@href').get()
        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page),
                                 callback=self.parse_new_house,
                                 meta={"info": (province, city)})
