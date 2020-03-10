from video.models import Movie
from video.models import Tvseries
from video.models import Variety
from video.models import Anime
from video.models import UTvseries
from video.models import UVariety
from video.models import UAnime

# 视频类型编号为0~15，每个编号对应列表的一个下标
TYPE_LIST = ['电影','动作片','喜剧片','爱情片','科幻片','恐怖片','剧情片','战争片',
             '微电影','电视剧','国产剧','港台剧','日韩剧','欧美剧','综艺','动漫']

# 视频年代编号为0~10，每个编号对应列表的一个下标
TIME_LIST = ['全部','2019','2018','2017','2016','2015','2014','2013','2012','2011','2010']

# 视频类型编号为0~15，每个编号对应列表的一个下标
AREA_LIST = ['全部','大陆','香港','台湾','美国','法国','英国','日本','韩国','德国','泰国','印度','意大利','西班牙','加拿大','其他']

# 视频类型Model映射表
TYPE_DICT = {'电影': Movie,'动作片': Movie,'喜剧片': Movie,'爱情片': Movie,'科幻片': Movie,
             '恐怖片': Movie,'剧情片': Movie,'战争片': Movie,'微电影': Movie,'电视剧': Tvseries,
             '国产剧': Tvseries,'港台剧': Tvseries,'日韩剧': Tvseries,'欧美剧': Tvseries,'综艺': Variety,'动漫': Anime}


VIDOE_TYPE_TO_STR = ['movie','movie','movie','movie','movie','movie','movie','movie','movie',
                    'tvseries','tvseries','tvseries','tvseries','tvseries','variety','anime']

FLAG_TYPE_DICT = {'动作片': 1,'喜剧片': 2,'爱情片': 3,'科幻片': 4,'恐怖片': 5,'剧情片': 6,'战争片': 7,
                  '微电影': 8,'国产剧': 10,'港台剧': 11,'日韩剧': 12,'欧美剧': 13,'综艺': 14,'动漫': 15}

SWITCH = {'m':Movie,'t':Tvseries,'v':Variety,'a':Anime}

SWITCH_U = {'t':UTvseries,'v':UVariety,'a':UAnime}

ERROR_MESSAGE = "<h1>服务器故障，修复中......</h1>"

RANKING_NUM = 15

BEGFILM_PROMPT = "请输入您要留言的信息"
BEGFILM_SUCCESS = "留言成功"
BEGFILM_ERROR = "留言失败"
