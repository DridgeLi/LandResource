# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
import re
from LandResource.items import LandresourceItem


# 模拟点击采用js的方式
script = """
function main(splash, args)
  splash.images_enabled = false
  assert(splash:go(args.url))
  assert(splash:wait(0.5))
  js = string.format("document.querySelector('div[@<div class="option unchoosed xh-highlight" data-value="7">
                                            拍卖公告
                                        </div>').click();", args.page)
  splash:runjs(js)
  assert(splash:wait(1))
  return splash:html()
end
"""

"""
class LandresourcespSpider(scrapy.Spider):
    name = 'LandResourceSP'
    allowed_domains = ['www.cdggzy.com']
    start_urls = ['https://www.cdggzy.com/site/LandTrade/LandList.aspx/']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy_splash.SplashRequest(url, callback=self.parse, endpoint='execute', args={
                'lua_source':script
            })

    def parse(self, response):
        print(response.xpath(".//div[@class='col-xs-10 infotitle']/a[1]").extract())
"""


class LandresourcespSpider(scrapy.Spider):
    name = 'LandResourceSP'
    allowed_domains = ['www.cdggzy.com']
    start_urls = ['https://www.cdggzy.com/site/LandTrade/LandList.aspx?id=6719']

    print("开始爬取网页...")


    def parse(self, response):
        print("开始爬取第一页")
        landresource_item = LandresourceItem()
        latest_notice_number = 34
        notice_list = response.xpath("//div[@id='contentlist']/div[@class='row contentitem']")
        for i_notice in notice_list:
            landresource_item['notice_name'] = i_notice.xpath(".//div[@class='col-xs-10 infotitle']/a/text()").extract_first()
            print(landresource_item['notice_name'])
            landresource_item['notice_link'] = i_notice.xpath(".//div[@class='col-xs-10 infotitle']/a[@href]").extract()
            while re.search(r"成公资土拍告", landresource_item['notice_name']):
                notice_number = int(landresource_item['notice_name'][31:32])
                if notice_number > latest_notice_number:
                    print("找到公告号")
                    yield scrapy.Request(landresource_item['notice_link'], callback=self.parse_currentNotice(), meta={landresource_item})
                else:
                    break

    def parse_currentNotice(self, response):
        landresource_item = LandresourceItem()
        notice_content = response.xpath("//div[@id='noticecontent']")
        for i_notice_content in notice_content:
            landresource_item['time_list'] = i_notice_content.xpath(".//div[@class='noticepubtime']/text()").extract_first()
            landresource_item['serial_number'] = i_notice_content.xpath(".//iframe/table/tbody/tr[3]/span/text()").extract_first()
            print(landresource_item)


