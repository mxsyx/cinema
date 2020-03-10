# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MovieItem(scrapy.Item):
    name = scrapy.Field()
    introduction = scrapy.Field()
    director = scrapy.Field()
    actor = scrapy.Field()
    flag_time = scrapy.Field()
    flag_area = scrapy.Field()
    flag_type = scrapy.Field()
    score = scrapy.Field()
    url_img = scrapy.Field()
    update_time = scrapy.Field()
    url =  scrapy.Field()
    mtva = scrapy.Field()

class TvseriesItem(scrapy.Item):
    name = scrapy.Field()
    introduction = scrapy.Field()
    director = scrapy.Field()
    actor = scrapy.Field()
    flag_time = scrapy.Field()
    flag_area = scrapy.Field()
    flag_type = scrapy.Field()
    score = scrapy.Field()
    url_img = scrapy.Field()
    update_time = scrapy.Field()
    urls =  scrapy.Field()
    mtva = scrapy.Field()

class VarietyItem(scrapy.Item):
    name = scrapy.Field()
    introduction = scrapy.Field()
    director = scrapy.Field()
    actor = scrapy.Field()
    flag_time = scrapy.Field()
    flag_area = scrapy.Field()
    flag_type = scrapy.Field()
    score = scrapy.Field()
    url_img = scrapy.Field()
    update_time = scrapy.Field()
    urls =  scrapy.Field()
    mtva = scrapy.Field()

class AnimeItem(scrapy.Item):
    name = scrapy.Field()
    introduction = scrapy.Field()
    director = scrapy.Field()
    actor = scrapy.Field()
    flag_time = scrapy.Field()
    flag_area = scrapy.Field()
    flag_type = scrapy.Field()
    score = scrapy.Field()
    url_img = scrapy.Field()
    update_time = scrapy.Field()
    urls =  scrapy.Field()
    mtva = scrapy.Field()