# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class WrestlingItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    color = scrapy.Field()
    size = scrapy.Field()
    sku = scrapy.Field()
    details = scrapy.Field()
    img_urls = scrapy.Field()
