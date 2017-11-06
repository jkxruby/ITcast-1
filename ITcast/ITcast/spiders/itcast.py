# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'   # 爬虫名称
    allowed_domains = ['http://www.itcast.cn']    # 爬虫允许的域，即遇到其他网址不会爬取
    start_urls = ['http://http://www.itcast.cn/']   # 表示开始爬时，在这域里获取信息

    def parse(self, response):    # 解析的方法，每个url完成下载后将被调用
        pass
