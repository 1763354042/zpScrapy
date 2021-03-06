# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import pymongo

# class TextPipeline(object):                                   #对爬虫所获取item进行基本操作
#     def __init__(self):
#         self.limit = 50
#
#     def process_item(self, item, spider):
#         if item['text']:
#             if len(item['text'])>self.limit:
#                 item['text'] = item['text'][0:self.limit].rstrip() + '...'
#                 return item
#             else:
#                 return DropItem("Missing Text")
#
#         return item


class MongoPipeline(object):
    def __init__(self,mongo_uri,mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
    @classmethod        #对应的函数不需要实例化，不需要self函数，但第一个参数是表示自身类的cls参数，可以调用类的属性，类的方法，实例对象等
    def from_crawler(cls,crawler):                        #crawler是scrapy的API主要入口
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB'),
        )
    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self,item,spider):
        name = item.__class__.__name__
        self.db[name].insert(dict(item))
        return item

    def close_spider(self,spider):
        self.client.close()
