# -*- coding: utf-8 -*-
import scrapy
from my_scrapy.items import FlightInfoItem


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['https://www.airasia.com/zh/cn']
    start_urls = ['https://www.airasia.com/zh/cn/']

    def parse(self, response):
        city_names = response.xpath('//h3[@class="city-name"]/text()').extract()
        print(city_names)
        item = FlightInfoItem()
        # for city_name in city_names:
        #     item = FlightInfoItem()
        #     item['city'] = '深圳'
        item['city'] = '深圳'
        yield item
