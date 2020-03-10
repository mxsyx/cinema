import time
import redis
from free.settings import logger
from video.models import Ranking

class RedisDump(object):
    def __init__(self):
        self.__pool = redis.ConnectionPool(host='127.0.0.1',password='533657')

    def dump(self):
        today = time.localtime()[2]  # 几天是几号
        r = redis.Redis(connection_pool = self.__pool)
        keys = r.keys()
        values = r.mget(keys)

        try:
            for key,value in zip(keys, values):
                rank = Ranking.objects.get(vid = key.decode())
                rank.rday = int(value.decode())
                rank.rweek = rank.rweek + rank.rday
                rank.rmonth = rank.rmonth + rank.rday
                if(today == 1):
                    rank.rmonth = 0
                if(today % 7 == 0):
                    rank.rweek = 0    
                rank.save()
            return True
        except Exception as e:
            return False
        

