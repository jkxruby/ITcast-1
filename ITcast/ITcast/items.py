# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItcastItem(scrapy.Item):   # 调用存取字段
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 老师姓名
    name = scrapy.Field()
    # 老师职称
    title = scrapy.Field()
    # 老师信息
    info = scrapy.Field()
