# -*- coding: utf-8 -*-
import scrapy
from LandResource.items import LandresourceItem
# import scrapy_splash


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
    start_urls = ['https://www.cdggzy.com/site/LandTrade/LandList.aspx/']

    def parse(self, response):
        notice_list = response.xpath("//div[@id='contentlist']/div[@class='row contentitem']")
        for i_notice in notice_list:
            landresource_item = LandresourceItem()
            landresource_item['notice_name'] = i_notice.xpath("./div[@class='col-xs-10 infotitle']/a/text()").extract_first()
            print(landresource_item)


