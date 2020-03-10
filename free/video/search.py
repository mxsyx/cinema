from video.models import Movie
from video.models import Tvseries
from video.models import Variety
from video.models import Anime
from django.db.models import Q
from video.context import ContextBase


class SearchContext(ContextBase):
    # 搜索视频信息上下文对象
    def __init__(self, request, keyword, page):
        """
        Args:
            keyword 关键字
            page 当前页码
        """
        self._request = request
        self._keyword = keyword
        self._page = page
        self._q_name = Q()
        self._q_director = Q()
        self._q_actor = Q()
        self._q_name.children.append(('name__contains', keyword))
        self._q_director.children.append(('director__contains', keyword))
        self._q_actor.children.append(('actor__contains', keyword))

    def process(self):
        context = self.context()
        try:
            results = self._search()
            context['results'] = results[self._page * 30:(self._page + 1) * 30]
            context['keyword'] = self._keyword
            self._process_pages(results)
            self._process_history()
            return True
        except Exception as e:
            return False

    def _search(self):
        """ 按照名字、导演、演员的顺序从数据库中查找影片 """
        results = []
        results.extend(self._search_by(self._q_name))
        results.extend(self._search_by(self._q_director))
        results.extend(self._search_by(self._q_actor))
        return results

    def _search_by(self, q):
        """ 通过条件查找信息
        
        根据一定的筛选条件，
        按照电影、电视剧、综艺节目、动漫的顺序从数据库中查找信息 
        """
        result_movie = list(Movie.objects.values('id','name','actor','flag_type','score','url_img').filter(q))
        result_tvseries = list(Tvseries.objects.values('id','name','actor','flag_type','score','url_img').filter(q))
        result_variety = list(Variety.objects.values('id','name','actor','flag_type','score','url_img').filter(q))
        result_anime = list(Anime.objects.values('id','name','actor','flag_type','score','url_img').filter(q))
    
        results = []
        results.extend(result_movie)
        results.extend(result_tvseries)
        results.extend(result_variety)
        results.extend(result_anime)
        return results

    def _process_pages(self, result):
        """计算与页码有关的值

        函数计算出页码迭代器、页码总数、
        前一个页码、后一个页码等值封装进上下文对象中
        """
        context = self.context()
        pages = int(len(result)/31) + 1  # 页码总数
        
        context['current_page'] = self._page + 1
        if pages <= 10:
            context['pages'] = range(1, pages+1)
        else:
            if self._page < 3:
                context['pages'] = range(1, 11)
            elif self._page + 8 <= pages:
                context['pages'] = range(self._page - 2, self._page + 8)
            else:
                context['pages'] = range(pages - 9, pages + 1)

        context['sum_pages'] = pages - 1  # 尾页页码
        # 处理前一个页码值、后一个页码值
        if self._page == 0:
            context['previous_page'] = 0
        else:
            context['previous_page'] = self._page - 1
        if self._page == pages - 1:
            context['next_page'] = pages - 1
        else:
            context['next_page'] = self._page + 1

