# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ItcastPipeline(object):
    def process_item(self, item, spider):   # 上面的类方法，帮我们处理每一个item
        return item
