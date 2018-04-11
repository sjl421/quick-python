# -*- coding:utf-8 -*-
'''
- author : root
- date   : 4/11/18
- time   : 7:26 PM
- desc   : 
'''
import scrapy as scrapy
from cssselect import Selector
from scrapy import Item, Field
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import Rule

class ZhiLianItems(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    company = Field()
    url = Field()

class ZhilianSpider(scrapy.Spider):
    name = "zhilian"
    # allowed_domains =
    start_urls = ["http://jobs.zhaopin.com/bj2140003/"]

    rules = (
        Rule(SgmlLinkExtractor(allow=(r'http://jobs.zhaopin.com/[0-9]+.htm',)),callback='parse_page',follow=True),
    )

    def parse_page(self,response):
        sel = Selector(response)
        item = ZhiLianItems()
        item['name']=sel.xpath('/html/body/div[5]/div[1]/div[1]/h1/text()')
        item['company']=sel.xpath('/html/body/div[5]/div[1]/div[1]/h2/a/text()')
        return item
