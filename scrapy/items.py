# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class FlightInfoItem(scrapy.Item):
    # define the fields for your item here like:
    city = scrapy.Field()
    price = scrapy.Field()
    date = scrapy.Field()
