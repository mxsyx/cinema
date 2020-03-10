# 爬虫-电视剧线路-解析

import os
import json
import time
import random
import scrapy
from selenium import webdriver
from laofan import emails
from laofan import settings
from laofan.items import TvseriesItem
from scrapy.http import HtmlResponse
from urllib.request import urlretrieve
from selenium.webdriver.chrome.options import Options

class TP(scrapy.Spider):
    name = "TP"
    domain = "https://www.yunbtv.com"
    
    def __init__(self, increment_low=0, increment_high=0, *args, **kwargs):
        """
        Args:
            increment_low  起始条目
            increment_high  终止条目
        """
        super(TP, self).__init__(*args, **kwargs)
        self.count = 0   # 每一轮已经完成的条目数
        self.current_item = 0
        self.increment_low = int(increment_low)
        self.increment_high = int(increment_high) 
        self.all_items = self.increment_high - self.increment_low + 1
        self.ema = emails.Email()

        # 无头浏览器配置
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('blink-settings=imagesEnabled=false')  # 禁止下载图片，加快解析速度
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=self.options)


    def start_requests(self):
        # 此处从tvseries.new.json获取URL以逐条解析数据
        with open("tmp/tvseries.new.json","r") as url_file:
            url_list = json.load(url_file)
            for i in range(self.increment_low, self.increment_high + 1):
                yield scrapy.Request(url_list[i-1], callback=self.parse)

    def parse(self, response):
        """电视剧信息解析
        
        parse函数解析了每一条电视剧主页地址，将与电视剧有关的信息例如名字、简介、年代、
        播放地址等信息提取出来封装到 TvseriesItem 类中，并将结果传送到了存储器pipelines

        每条电视剧信息都有一个对应的函数负责提取，这些函数以extract_开头
        """
        item = TvseriesItem()
        item["name"] = self.extract_name(response)
        item["introduction"] = self.extract_introduction(response)
        item["director"] = self.extract_director(response)
        item["actor"] = self.extract_actor(response)
        item["flag_time"] = self.extract_flag_time(response)
        item["flag_area"] = self.extract_flag_area(response)
        item["flag_type"] = self.extract_flag_type(response)
        item["score"] = round(random.uniform(6.5,9.5),1);  # 影片得分采用随机数方式
        item["url_img"] = self.extract_img(response)
        item["update_time"] = time.strftime("%Y-%m-%d", time.localtime())
        item["urls"] = self.extract_urls(response)
        item["mtva"] = 't'
        
        self.current_item = self.current_item + 1

        print("\n提取成功 %s  > > > 剩余 %s 条\n" % (response.url,self.all_items-self.current_item))

        self.count = self.count + 1
        # 超过自定义的每轮最大爬行次数后，重置webdriver
        if(self.count >= settings.MAX_CRAWL_NUMS):
            self.restart_driver()
        
        if(self.current_item == self.all_items):
            self.task_completed()

        yield item

    def extract_name(self,response):
        try:
            result = response.xpath(settings.YUNBTV_VIDEO_NAME)[0].extract()
            return result
        except Exception as e:
            settings.logerr.error("@TP.extract_name URL: %s  Exception: %s" % (response.url, str(e)))
            return "未知"

    def extract_introduction(self,response):
        try:
            result = response.xpath(settings.YUNBTV_VIDEO_INTRODUCTION)[2].extract().split("：")[1]
            result = result.replace("\"","").replace("\'","")
            return result
        except Exception as e:
            settings.logerr.error("@TP.extract_introduction URL: %s  Exception: %s" % (response.url, str(e)))
            return "无"

    def extract_director(self,response):
        try:
            result = response.xpath(settings.YUNBTV_VIDEO_DIRECTOR)[0].extract().replace("\"","").replace("\'","")
            return  result
        except Exception as e:
            settings.logerr.error("@TP.extract_director URL: %s  Exception: %s" % (response.url, str(e)))
            return "未知"

    def extract_actor(self,response):
        try:
            result = response.xpath(settings.YUNBTV_VIDEO_ACTOR).extract()
            str_actor = ""
            for actor in result:
                str_actor = "%s%s、" % (str_actor, actor.replace("\"","").replace("\'",""))
            if str_actor == "":
                return "未知、"
            return str_actor
        except Exception as e:
            settings.logerr.error("@MP.extract_actor URL: %s  Exception: %s" % (response.url, str(e)))
            return "未知、"

    def extract_flag_time(self,response):
        try:
            result = response.xpath(settings.YUNBTV_VIDEO_FLAG_TIME)[0].extract()
            return result
        except Exception as e:
            settings.logerr.error("@TP.extract_flag_time URL: %s  Exception: %s" % (response.url, str(e)))
            return "未知"

    def extract_flag_area(self,response):
        try:
            result = response.xpath(settings.YUNBTV_VIDEO_FLAG_AREA)[0].extract()
            return result
        except Exception as e:
            settings.logerr.error("@TP.extract_flag_time URL: %s  Exception: %s" % (response.url, str(e)))
            return "未知"

    def extract_flag_type(self,response):
        try:
            result = response.xpath(settings.YUNBTV_VIDEO_FLAG_TYPE)[0].extract()
            return result
        except Exception as e:
            settings.logerr.error("@TP.extract_flag_type URL: %s  Exception: %s" % (response.url, str(e)))
            return "未知"

    def extract_img(self,response):
        # 此处，extract_img函数通过urllib库下载了图片并存储到磁盘上
        # 同时，将图片的存储地址返回给了父函数，若未提取到有效的图片则返回默认的图片地址
        try:
            result = response.xpath(settings.YUNBTV_VIDEO_URL_IMG)[0].extract()
            img_name = "%d.jpg" % int(time.time()*1000000)
            img_dir = "imgt/%s/" % time.strftime("%Y-%m-%d", time.localtime())
            if os.path.isdir(img_dir)==False:
                os.mkdir(img_dir)
            urlretrieve(result, "%s%s" % (img_dir, img_name))    # 下载图片到指定位置
            return "/media/%s%s" % (img_dir, img_name)
        except Exception as e:
            settings.logerr.error("@MP.extract_img URL: %s  Exception: %s" % (response.url, str(e)))
            return "/static/images/404/imgnotfound.jpg"

    def extract_urls(self,response):
        absolute_urls = []
        try:
            play_addresses = response.xpath(settings.YUNBTV_VIDEO_OTHER_LINK).extract()
            nums = len(play_addresses)  # 全部剧集数
            current = 1  # 当前解析的剧集
            print("\n\n开始解析电视剧播放地址，共 %s 集，主页地址为：%s\n\n" % (nums,response.url))
            for play_address in play_addresses:
                print("当前解析第 %d 集，剩余 %d 集\n" % (current, nums - current))
                absolute_url = self.chrome_extract("%s%s" % (self.domain, play_address))
                absolute_urls.append(absolute_url)
                current = current + 1
                self.count = self.count + 1
        except Exception as e:
            settings.logerr.error("@TP.extract_url URL: %s  Exception: %s" % (response.url, str(e)))
            return absolute_urls
        return absolute_urls

    def chrome_extract(self,_url):
        # 函数加载视频播放的主页地址，并提取iframe的属性src，src属性值即为播放地址
        try:
            self.driver.get(_url)
            iframe = self.driver.find_elements_by_tag_name('iframe')[2]
            absolute_url = iframe.get_attribute('src')
            return absolute_url
        except Exception as e:
            settings.logerr.error("@TP.chrome_extract URL: %s  Exception: %s" % (_url, str(e)))
            return "none"

    def restart_driver(self):
        self.driver.quit()
        time.sleep(3)
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=self.options)
        self.count = 0

    def task_completed(self):
        self.driver.quit()
        print("\n\n\n任务完成！ 电视剧 - 信息提取完毕\n\n\n")
        self.ema.send("任务完成消息","电视剧 - 信息提取完毕")