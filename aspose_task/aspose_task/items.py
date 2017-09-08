# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AsposeTaskItem(scrapy.Item):
    name = scrapy.Field()
    prefix = scrapy.Field()
    detail = scrapy.Field()
