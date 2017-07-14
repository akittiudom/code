# -*- coding: utf-8 -*-
import scrapy


class FormsSpider(scrapy.Spider):
    name = 'forms'
    allowed_domains = ['https://newyork.craigslist.org/search/egr']
    start_urls = ['https://newyork.craigslist.org/search/egr/']

    def parse(self, response):
       # pass
       forms = response.xpath('//form/id()').extract()
       print(forms)
