from video.models import *
from video.config import SWITCH
from free.settings import logger
from operator import itemgetter
from video.config import RANKING_NUM
from urllib.parse import unquote


def ranking_by(basis, video_type, low, high):
    """ 按一定条件获取首页的排行榜条目信息

    一个排行榜条目即是一个字典，
    字典中包含该视频的ID、名字、相应的播放量
    
    Args:
        basis 条件
            可能的值：'rday' / 'rweek' / 'rmonth'
        video_type 视频类型
            可能的值：'m' / 't' / 'v' / 'a'
        low ～ high 选择的范围
    Returns:
        ranking_items 排行榜条目列表
    """
    try:
        top_videos = Ranking.objects.values('vid', basis).filter(vid__contains = video_type).order_by('-%s' % basis)[low:high]
        video_ids = [int(top['vid'].split('_')[1]) for top in top_videos]  # 提取视频ID
        video_volumes = {int(top['vid'].split('_')[1]):top[basis] for top in top_videos}  # 提取视频播放量
        ranking_items = list(SWITCH[video_type].objects.values('id','name').filter(id__in = video_ids)) # 根据ID获取视频数据

        # 将播放量的值存放进排行榜字典中去
        for rank in ranking_items:
          rank[basis] = video_volumes[rank['id']]
        return sorted(ranking_items, key=itemgetter(basis),reverse=True)
    except Exception as e:
        return []


def index_ranking():
    # 获取首页的排行榜信息，包括电影榜、电视榜、综艺榜、动漫榜
    # 函数将视频的日播放量作为依据进行排行，选取日播放量最高的七个视频
    leaderboard = {'m':[],'t':[],'v':[],'a':[]}
    leaderboard['m'].extend(ranking_by('rday', 'm', 0, 7))
    leaderboard['t'].extend(ranking_by('rday', 't', 0, 7))
    leaderboard['v'].extend(ranking_by('rday', 'v', 0, 7))
    leaderboard['a'].extend(ranking_by('rday', 'a', 0, 7))

    return leaderboard


class RankingContext(object):
    """ 获取排行信息 """
    __context = {}
    
    def __init__(self, request):
        self._request = request
        self._leaderboards = {
                'm':{'rday':[],'rweek':[],'rmonth':[]},
                't':{'rday':[],'rweek':[],'rmonth':[]},
                'v':{'rday':[],'rweek':[],'rmonth':[]},
                'a':{'rday':[],'rweek':[],'rmonth':[]}
            }

    def process(self):
        context = self.context()
        try:
            self._process_leaderboards()
            context['leaderboard'] = self._leaderboards
            self._process_history()
            return True
        except Exception as e:
            return False

    def _process_leaderboards(self):
        # 获取排行榜页的排行榜信息，包括电影榜、电视榜、综艺榜、动漫榜
        # 函数依次将日播放量、周播放量、月播放量作为依据对视频进行排行
        # 每次选取日播放量 / 周播放量 / 月播放量播放量最高的RANKING_NUM个视频
        self._leaderboards['m']['rday'].extend(ranking_by('rday', 'm', 0, RANKING_NUM))
        self._leaderboards['m']['rweek'].extend(ranking_by('rweek', 'm', 0, RANKING_NUM))
        self._leaderboards['m']['rmonth'].extend(ranking_by('rmonth', 'm', 0, RANKING_NUM))
    
        self._leaderboards['t']['rday'].extend(ranking_by('rday', 't', 0, RANKING_NUM))
        self._leaderboards['t']['rweek'].extend(ranking_by('rweek', 't', 0, RANKING_NUM))
        self._leaderboards['t']['rmonth'].extend(ranking_by('rmonth', 't', 0, RANKING_NUM))

        self._leaderboards['v']['rday'].extend(ranking_by('rday', 'v', 0, RANKING_NUM))
        self._leaderboards['v']['rweek'].extend(ranking_by('rweek', 'v', 0, RANKING_NUM))
        self._leaderboards['v']['rmonth'].extend(ranking_by('rmonth', 'v', 0, RANKING_NUM))

        self._leaderboards['a']['rday'].extend(ranking_by('rday', 'a', 0, RANKING_NUM))
        self._leaderboards['a']['rweek'].extend(ranking_by('rweek', 'a', 0, RANKING_NUM))
        self._leaderboards['a']['rmonth'].extend(ranking_by('rmonth', 'a', 0, RANKING_NUM))

    def _process_history(self):
        paths = []  # 历史记录路径列表
        names = []  # 历史记录名称列表
        if 'whp' in self._request.COOKIES:
            paths = unquote(self._request.COOKIES['whp']).split('$$')
            paths.pop(0)
        if 'whn' in self._request.COOKIES:
            names = unquote(self._request.COOKIES['whn']).split('$$')
            names.pop(0)
        self.__context['paths'] = paths
        self.__context['names'] = names

    def context(self):
        return self.__context

