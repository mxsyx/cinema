# 爬虫-电影线路-更新

import os
import time
import json
import scrapy
from selenium import webdriver
from laofan import emails
from laofan import settings
from laofan.items import MovieItem
from scrapy.http import HtmlResponse
from selenium.webdriver.chrome.options import Options

class MU(scrapy.Spider):
    name = "MU"
    domain = "https://www.yunbtv.com"

    def __init__(self, increment_low=0, increment_high=0, *args, **kwargs):
        """
        Args:
            increment_low  起始条目
            increment_high  终止条目
        """
        super(MU, self).__init__(*args, **kwargs)
        self.current_item = 0
        self.increment_low = int(increment_low)
        self.increment_high = int(increment_high) 
        self.all_items = self.increment_high - self.increment_low + 1
        self.ema = emails.Email()

        # 无头浏览器配置
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('blink-settings=imagesEnabled=false')  # 禁止下载图片，加快解析速度
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options)


    def start_requests(self):
        # 此处从movie.all.json获取URL以更新数据，
        with open("tmp/movie.all.json","r") as url_file:
            url_list = json.load(url_file)
            for i in range(self.increment_low, self.increment_high + 1):
                yield scrapy.Request(url_list[i-1], callback=self.parse)

    def parse(self, response):
        """电影播放地址更新
        
        parse函数重新解析了每一条电影的播放地址，并将更新信息传输到存储器pipelines
        """
        item = MovieItem()
        item["name"] = self.extract_name(response)
        item["update_time"] = time.strftime("%Y-%m-%d", time.localtime())
        item["url"] = self.extract_url(response)
        item["mtva"] = 'm'

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

        print("\n提取成功 %s  > > > 剩余 %d 条\n" % (response.url, self.all_items-self.current_item))
        
        # 超过自定义的每轮最大爬行次数后，重置webdriver
        if(self.current_item % settings.MAX_CRAWL_NUMS == settings.MAX_CRAWL_NUMS_):
            self.restart_driver()
        
        if(self.current_item == self.all_items):
            self.task_completed()

        yield item
    
    def extract_name(self,response):
        try:
            result = response.xpath(settings.YUNBTV_VIDEO_NAME)[0].extract()
            return result
        except Exception as e:
            settings.logerr.error("@MU.extract_name URL: %s  Exception: %s" % (response.url, str(e)))
            return "未知"

    def extract_url(self,response):
        try:
            play_addresses = response.xpath(settings.YUNBTV_VIDEO_MOVIE_LINK).extract()
            for play_address in play_addresses:
                absolute_url = self.chrome_extract("%s%s" % (self.domain, play_address))
                if(absolute_url.split('.')[-1]=='m3u8'):  # 如果解析后地址后缀名不是m3u8，说明这个地址是无效的，应舍弃
                    return absolute_url
            return ""
        except Exception as e:
            settings.logerr.error("@MU.extract_url URL: %s  Exception: %s" % (response.url, str(e)))
            return ""

    def chrome_extract(self,_url):
        # 函数加载视频播放的主页地址，并提取iframe的属性src，src属性值即为播放地址
        try:
            self.driver.get(_url)
            iframe = self.driver.find_elements_by_tag_name('iframe')[2]
            absolute_url = iframe.get_attribute('src')
            return absolute_url
        except Exception as e:
            settings.logerr.error("@MU.chrome_extract URL: %s  Exception: %s" % (_url, str(e)))
            return "none"

    def restart_driver(self):
        self.driver.quit()
        time.sleep(3)  # 等待3秒以防止webdriver未完全退出
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=self.options)

    def task_completed(self):
        self.driver.quit()
        print("\n\n\n任务完成！ 电影 - 信息更新完成\n\n\n")
        self.ema.send("任务完成消息","电影 - 信息更新完成")