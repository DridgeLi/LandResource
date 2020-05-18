# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LandresourceItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #公告号码
    notice = scrapy.Field()
    #序号
    serial_number = scrapy.Field()
    #宗地编号
    land_id = scrapy.Field()
    #宗地位置
    land_location = scrapy.Field()
    #净用地面积（亩）
    land_area = scrapy.Field()
    #土地性质
    land_proprety = scrapy.Field()
    #起拍价格（万元/亩-元/㎡）
    land_startprice = scrapy.Field()
    #保证金（万元）
    land_deposit = scrapy.Field()
    #挂牌时间
    time_list = scrapy.Field()
    #保证金时间
    time_deposit = scrapy.Field()
    #拍卖时间
    time_auction = scrapy.Field()
    #计容面积
    land_countarea = scrapy.Field()
    #建筑面积
    land_destiny = scrapy.Field()
    #建筑高度
    land_height = scrapy.Field()
    #指标面积
    land_quotaarea = scrapy.Field()
    #拍卖方式
    land_auctionmode = scrapy.Field()

