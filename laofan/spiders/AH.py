""" 从站点 “www.yunbtv.com” 中提取动漫主页的地址，
    并将主页地址存入 tmp 文件夹下，通常每一个抓取的页面中包含30个URL。
"""

import json
import scrapy
from laofan import emails
from laofan import merlist
from laofan import settings

class AH(scrapy.Spider):
    name = "AH" 
    domain = "https://www.yunbtv.com"
    
    def __init__(self, start_url=None, increment=0, increment_max=0, *args, **kwargs):
        """
        Args:
            start_url 起始地址
            increment   起始条目
            increment_max  终止条目
        """
        super(AH, self).__init__(*args, **kwargs)
        self.url = start_url
        self.ema = emails.Email()
        self.current = int(increment)  # 当前条目
        self.increment = int(increment)
        self.increment_max = int(increment_max)

    def start_requests(self):
        yield scrapy.Request(self.url, callback=self.parse)

    def parse(self, response):
        try:
            homepages = response.xpath(settings.YUNBTV_VIDEO_HOMEPAGE).extract()
            homepages_dump = ["%s%s" % (self.domain, homepage) for homepage in homepages]
            # 将每一页的URL地址列表dump到一个单独的文件中去，通常每个文件有30个URL
            with open('tmp/anime/%d.json' % self.current, "w") as f:
                json.dump(homepages_dump, f)
        except Exception as e:
            settings.logerr.error("@AH.parse URL: %s  Exception: %s" % (self.url,str(e)))
            
        print("\n提取成功 %s  > > > 剩余 %d 条 " % (self.url, self.increment_max-self.current))
        
        # 判断任务是否已经完成，未完成则更新目标地址后继续任务，否则调用结束函数
        self.current = self.current + 1
        if(self.current <= self.increment_max):
            self.url = "https://www.yunbtv.com/vodtype/dongman-%d.html" % self.current
            yield scrapy.Request(self.url, callback=self.parse)
        else:
            self.task_completed()

    def task_completed(self):
        merlist.comerge("anime", self.increment, self.increment_max)  # 合并刚刚存储的URL
        print("\n\n\n任务完成！ 动漫 - 主页地址提取完毕\n\n\n")
        self.ema.send("任务完成消息","动漫 - 主页地址提取完毕")