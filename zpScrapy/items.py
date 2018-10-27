# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuoteItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()

class DajieItem(scrapy.Item):
    keyWord = scrapy.Field()
    companyName = scrapy.Field()
    positionName = scrapy.Field()
    workYear = scrapy.Field()
    education = scrapy.Field()
    city = scrapy.Field()
    salary = scrapy.Field()





class BossZpItem(scrapy.Item):
    keyWord = scrapy.Field()
    companyName = scrapy.Field()
    positionName = scrapy.Field()
    workYear = scrapy.Field()
    education = scrapy.Field()
    city = scrapy.Field()
    salary = scrapy.Field()
