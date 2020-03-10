# 爬虫-动漫线路-更新

import os
import time
import json
import scrapy
from selenium import webdriver
from laofan import emails
from laofan import settings
from laofan.items import TvseriesItem
from scrapy.http import HtmlResponse
from selenium.webdriver.chrome.options import Options

class AU(scrapy.Spider):
    name = "AU"
    domain = "https://www.yunbtv.com"
  
    def __init__(self, increment_low=0, increment_high=0, *args, **kwargs):
        """
        Args:
            increment_low  起始条目
            increment_high  终止条目
        """
        super(AU, self).__init__(*args, **kwargs)
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
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options = self.options)


    def start_requests(self):
        # 此处从anime.all.json获取URL以更新数据
        with open("tmp/anime.all.json","r") as url_file:
            url_list = json.load(url_file)
            for i in range(self.increment_low, self.increment_high + 1):
                yield scrapy.Request(url_list[i-1], callback=self.parse)

    def parse(self, response):
        """动漫播放地址更新
        
        parse函数重新解析了每一条动漫的播放地址，并将更新信息传输到存储器pipelines
        """
        item = TvseriesItem()
        item["name"] = self.extract_name(response)
        item["update_time"] = time.strftime("%Y-%m-%d", time.localtime())
        item["urls"] = self.extract_urls(response)
        item["mtva"] = 'a'

        # 更新播放地址时无需提取下列信息
        item["introduction"] = ""
        item["director"] = ""
        item["actor"] = ""
        item["flag_time"] = ""
        item["flag_area"] = ""
        item["flag_type"] = ""
        item["score"] = 0
        item["url_img"] = ""

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
            settings.logerr.error("@T1P.extract_name URL: %s  Exception: %s" % (response.url, str(e)))
            return "未知"

    def extract_urls(self,response):
        absolute_urls = []
        try:
            play_addresses = response.xpath(settings.YUNBTV_VIDEO_OTHER_LINK).extract()
            nums = len(play_addresses)  # 全部剧集数
            current = 1  # 当前解析的剧集
            print("\n\n开始解析动漫播放地址，共 %s 集，主页地址为：%s\n\n" % (nums,response.url))
            for play_address in play_addresses:
                print("当前解析第 %d 集，剩余 %d 集\n" % (current, nums - current))
                absolute_url = self.chrome_extract("%s%s" % (self.domain, play_address))
                absolute_urls.append(absolute_url)
                current = current + 1
                self.count = self.count + 1
        except Exception as e:
            settings.logerr.error("@AU.extract_url URL: %s  Exception: %s" % (response.url, str(e)))
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
            settings.logerr.error("@AU.chrome_extract URL: %s  Exception: %s" % (_url, str(e)))
            return "none"

    def restart_driver(self):
        self.driver.quit()
        time.sleep(3)
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=self.options)
        self.count = 0

    def task_completed(self):
        self.driver.quit()
        settings.loginfo.info("任务完成！ 动漫 - 信息更新完毕\n")
        print("\n\n\n任务完成！ 动漫 - 信息更新完毕\n\n\n")
        self.ema.send("任务完成消息","动漫 - 信息更新完毕")