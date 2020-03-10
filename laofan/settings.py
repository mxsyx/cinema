BOT_NAME = 'laofan'

SPIDER_MODULES = ['laofan.spiders']
NEWSPIDER_MODULE = 'laofan.spiders'

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'laofan.pipelines.MoviePipeline': 400,
    'laofan.pipelines.TvseriesPipeline': 300,
    'laofan.pipelines.VarietyPipeline': 200,
    'laofan.pipelines.AnimePipeline': 100,
}

# 配置控制台日志
LOG_LEVEL = 'INFO'
LOG_ENABLED = False

# 遵守 robots.txt
ROBOTSTXT_OBEY = True

# 配置Scrapy执行的最大并发请求（默认16）
#CONCURRENT_REQUESTS = 32

# 配置同一站点的请求延迟 (默认0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'laofan.middlewares.LaofanDownloaderMiddleware': 543,
}

############ User-defined settings

# 配置每轮最大爬行次数
MAX_CRAWL_NUMS = 200
MAX_CRAWL_NUMS_ = MAX_CRAWL_NUMS -1

# 数据库配置
MYSQL_USER = 'root'
MYSQL_PASSWD = '533657'
MYSQL_DBMAS = 'redtea'
UNIX_SOCKET = '/opt/mysqldts/mysqld.sock'

# 邮件客户端配置
SMTP_SERVER = 'smtp.163.com'
SMTP_PORT = 465
FROM_ADDR = 'zsimline@163.com'
SMTP_PASSWORD = 'srline@wyyx.top'
TO_ADDR = '1591145458@qq.com'

# www.yunbtv.com Xpath
YUNBTV_VIDEO_HOMEPAGE = "/html[1]/body[1]/section[3]/div[1]/div[2]/div[1]/div/div[1]/div[1]/a[1]/@href"
YUNBTV_VIDEO_NAME = "/html[1]/body[1]/section[2]/div[1]/div[1]/div[1]/div[2]/h2[1]/a[1]/text()"
YUNBTV_VIDEO_INTRODUCTION = "/html[1]/body[1]/section[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/text()"
YUNBTV_VIDEO_DIRECTOR = "/html[1]/body[1]/section[2]/div[1]/div[1]/div[1]/div[2]/p[2]/a[1]/text()"
YUNBTV_VIDEO_ACTOR = "/html[1]/body[1]/section[2]/div[1]/div[1]/div[1]/div[2]/p[3]/a/text()"
YUNBTV_VIDEO_FLAG_TIME = "/html[1]/body[1]/section[2]/div[1]/div[1]/div[1]/div[2]/p[4]/a[1]/text()"
YUNBTV_VIDEO_FLAG_AREA = "/html[1]/body[1]/section[2]/div[1]/div[1]/div[1]/div[2]/p[5]/a[1]/text()" 
YUNBTV_VIDEO_FLAG_TYPE = "/html[1]/body[1]/section[2]/div[1]/div[1]/div[1]/div[2]/p[1]/a[1]/text()"
YUNBTV_VIDEO_URL_IMG = "/html[1]/body[1]/section[2]/div[1]/div[1]/div[1]/div[1]/img[1]/@src"
YUNBTV_VIDEO_MOVIE_LINK = "/html[1]/body[1]/section[3]/div[1]/div[2]/div/div[1]/ul[1]/li[1]/a[1]/@href"
YUNBTV_VIDEO_OTHER_LINK = "/html[1]/body[1]/section[3]/div[1]/div[2]/div[1]/div[1]/ul[1]/li/a[1]/@href"

# 全局日志对象配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,  # 禁用所有已经存在的日志配置
    'formatters': {  # 格式器
        'verbose': {  # 详细格式
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {  # 处理器
        'file_error': {  # 错误日志文件处理器
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/opt/log/laofan-error.log',
            'formatter': 'verbose',
        },
        'file_info': {  # 消息日志文件处理器
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/opt/log/laofan-info.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {  # 记录器
        'movie.error': {  # 错误日志记录器
        	'level': 'ERROR',
            'handlers': ['file_error'],
            'propagate': True,
        },
        'movie.info':{  # 消息日志记录器
        	'level': 'INFO',
            'handlers': ['file_info'],
            'propagate': True,
        },
    },
}

# 全局日志对象
import logging
import logging.config
logging.config.dictConfig(LOGGING)
logerr = logging.getLogger("movie.error")
loginfo = logging.getLogger("movie.info")

# 配置用户代理
user_agent_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'laofan.middlewares.LaofanSpiderMiddleware': 543,
#}


# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

