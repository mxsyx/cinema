import random
import logging
from video.models import Anime
from video.models import Movie
from video.models import Tvseries
from video.models import Variety
from video.models import Ranking
from free.settings import logger




def obtain_hits(model_type):
    """从数据库随机获取6个视频作为推荐的视频

    Args:
        model_type 模型类型
          0:Tvseries 1:Variety 2:Anime 3:Movie
    Returns:
        recommendations 随机获取的视频信息列表
    """
    switch = {'m':Movie,'t':Tvseries,'v':Variety,'a':Anime}
    try:
        count = switch[model_type].objects.all().count()
        rand_ids = random.sample(range(int(count*0.95), count), 12)  # 随机数获取
        recommendations= switch[model_type].objects.filter(id__in=rand_ids)
        return recommendations
    except Exception as e:
        logger.error("获取推荐信息时失败：%s" % str(e))
        return []

