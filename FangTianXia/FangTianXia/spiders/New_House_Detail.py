# -*- coding: utf-8 -*-
# @Time   :   2019-03-14
# @Python :   3.6.1
# @IDE    :   Pycharm
import scrapy

from item.New_House_Detail_Item import NewHouseDetailItem
from tools.QueryData import QueryData


class NewHouseDetailSpider(scrapy.Spider):
    """
    抓取新房详情信息
    """
    name = 'new_house_detail'

    def __init__(self):
        self.url_list = QueryData().get_new_house_url()

    def start_requests(self):
        for url in self.url_list:
            yield scrapy.Request(url=url[0], callback=self.parse)

    def parse(self, response):
        detail_url ="https:"+response.xpath('//div[@class="navleft tf"]/a[2]/@href').get()
        yield scrapy.Request(url = detail_url,callback=self.parse_detail)

    def parse_detail(self,response):
        item =NewHouseDetailItem()

        # 基本信息
        item["name"] = response.xpath('//h1/a/@title').get() # 房产名称
        item["price"] = response.xpath('//div[@class="main-info-price"]/em/text()').get().strip() # 价格
        item["score"] = response.xpath('//span[@style="margin-right: 5px;"]/text()').get() # 评分
        item["total_comment"] = response.xpath('//div[@class="main-info-comment"]//span[3]/text()').get() #评论总数
        item["property_category"] = response.xpath('//div[@class="main-left"]/div[1]//li[1]/div[@class="list-right"]/text()').get().strip() # 物业类别
        item["advantage"] = ",".join(response.xpath('//div[@class="main-left"]/div[1]//li[2]/div[@class="list-right"]/span//text()').getall()) # 项目特色
        item["building_category"] = response.xpath('//span[@class="bulid-type"]/text()').get().strip()# 建筑类别
        item["age"] = ','.join(response.xpath('//p[@style="width: 130px;float: left;"]/text()').getall()) # 产权年限
        item["location"] = response.xpath('//div[@class="main-left"]/div[1]//li[4]/div[2]/text()').get().strip() # 环线位置
        item["developer"] = response.xpath('//div[@class="list-right-text"]/a/text()').get() # 开发商
        item["address"] = response.xpath('//div[@class="list-right-text"]/text()').get() # 楼盘地址

        # 销售信息
        item["sales_status"] = response.xpath('//div[@class="main-left"]/div[1]//li[1]/div[@class="list-right"]/text()')[1].get().strip() # 销售状态
        item["offer"] = response.xpath('//div[@class="main-item"]')[1].xpath('.//li[2]/div[@class="list-right"]/text()').get().strip() # 楼盘优惠
        item["opening_time"] = response.xpath('//div[@class="main-item"]')[1].xpath('.//li[3]/div[@class="list-right"]/text()').get() # 开盘时间
        item["finish_time"] = response.xpath('//div[@class="main-item"]')[1].xpath('.//li[4]/div[@class="list-right"]/text()').get() # 交房时间
        item["sale_address"] = response.xpath('//div[@class="main-item"]')[1].xpath('.//li[5]/div[@class="list-right"]/text()').get() # 售楼地址
        item["tel"] = response.xpath('//div[@class="list-right c00"]/text()').get() # 咨询电话
        item["house_type"] = ','.join(response.xpath('//div[@class="main-item"]')[1].xpath('.//li[7]/div[@class="list-right-text"]/a/text()').getall()) # 主力户型

        # 小区规划
        item["floor_area"] = response.xpath('//ul[@class="clearfix list"]/li[1]/div[2]/text()').get() # 占地面积
        item["construction_area"] = response.xpath('//ul[@class="clearfix list"]/li[2]/div[2]/text()').get() # 建筑面积
        item["volume_rate"] = response.xpath('//ul[@class="clearfix list"]/li[3]/div[2]/text()').get() # 容积率
        item["greening_rate"] = response.xpath('//ul[@class="clearfix list"]/li[4]/div[2]/text()').get() # 绿化率
        item["parking"] = response.xpath('//ul[@class="clearfix list"]/li[5]/div[2]/text()').get() # 停车位
        item["total_building"] = response.xpath('//ul[@class="clearfix list"]/li[6]/div[2]/text()').get() # 楼栋总数
        item["total_houses"] = response.xpath('//ul[@class="clearfix list"]/li[7]/div[2]/text()').get() # 总户数
        item["property_company"] = response.xpath('//ul[@class="clearfix list"]/li[8]/div[2]/text()').get() # 物业公司
        item["property_costs"] = response.xpath('//ul[@class="clearfix list"]/li[9]/div[2]/text()').get() # 物业费
        item["floor_condition"] = response.xpath('//ul[@class="clearfix list"]/li[11]/div[2]/text()').get() # 楼层状况

        # 周边设施
        if response.xpath('//span[text()="交通"]/text()'):
            item["traffic"] = ','.join(response.xpath('//li[@class="jiaotong_color"]/text()').getall())
        else:
            item["traffic"] = ""

        # if response.xpath('//span[text()="交通"]/text()'):




        item["traffic"] = ','.join(response.xpath('//li[@class="jiaotong_color"]/text()').getall()) # 交通
        item["mall"] = response.xpath('//ul[@class="sheshi_zb"]/li[2]/text()').get() # 综合商场
        item["hospital"] = response.xpath('//ul[@class="sheshi_zb"]/li[3]/text()').get() # 医院
        try:
            item["bank"] = response.xpath('//ul[@class="sheshi_zb"]/li[4]/text()').get() # 银行
        except:
            item["bank"] = ""
        try:
            item["others"] = response.xpath('//ul[@class="sheshi_zb"]/li[5]/text()').get() # 其他
        except:
            item["others"] = ""
        try:
            item["support"] = response.xpath('//ul[@class="sheshi_zb"]/li[6]/text()').get() # 小区内部配套
        except:
            item["support"] = ""
        yield item

