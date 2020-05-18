# -*- coding: utf-8 -*-
import scrapy


class LandresourcespSpider(scrapy.Spider):
    name = 'LandResourceSP'
    allowed_domains = ['https://www.cdggzy.com/site/LandTrade/LandList.aspx']
    start_urls = ['https://www.cdggzy.com/site/LandTrade/LandList.aspx/']

    def parse(self, response):
        pass
