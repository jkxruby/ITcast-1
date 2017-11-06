# -*- coding: utf-8 -*-
import scrapy
from ITcast.ITcast.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'   # 爬虫名称,启动爬虫时必须执行的参数
    allowed_domains = ['itcast.cn']    # 爬虫允许的域，即遇到其他网址不会爬取,是可选项
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']   # 表示开始爬时，在这域里获取信息,可以是可迭代对象

    def parse(self, response):    # 解析的方法，每个url完成下载后将被调用
        node_list = response.xpath("//div[@class='li_txt']")
        items = []
        for node in node_list:

            item = ItcastItem()
            # .extract()将xpath转换成 Unicode字符串  xpath返回的一定是列表
            name = node.xpath("./h3/text()").extract()
            title = node.xpath("./h4/text()").extract()
            info = node.xpath("./p/text()").extract()

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            items.append(item)
        return items



