from video.config import TYPE_LIST
from video.config import TIME_LIST
from video.config import AREA_LIST
from video.config import TYPE_DICT
from video.config import VIDOE_TYPE_TO_STR
from video.context import ContextBase


class ClassifyContext(ContextBase):
    """该类封装分类后视频信息的上下文对象

    process 函数封装必要的分类后的视频信息
    _process_pages   函数封装与页码有关的值
    _process_history 函数封装历史记录信息
    _classify_select 函数按条件从数据库获取数据
    """
    def __init__(self, request, video_type, video_time, video_area, page):
        """
        Args:
            video_type 视频类型编号
            video_time 视频年代编号
            video_area 视频地区编号
            page 当前页码
        """
        self._request = request
        self._video_type = video_type
        self._video_time = video_time
        self._video_area = video_area
        self._page = page

    def process(self):
        """完成分类视频信息的封装

        函数调用classify_select从数据库中获取符合条件的视频数据，
        并根据页码值截取一部分数据，同时将页码值、视频类型编号、视频
        年代编号、视频地区编号等信息一并封装进上下文对象中
        """
        context = self.context()
        try:
            result = self._classify_select()
            context['result'] = result[self._page*30:(self._page+1)*30]
            context['video_type'] = self._video_type
            context['video_time'] = self._video_time
            context['video_area'] = self._video_area
            context['mtva'] = VIDOE_TYPE_TO_STR[self._video_type]
            self._process_pages(result)  # 完成页码值的计算与封装
            self._process_history()
            return True
        except Exception as e:
            return False

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

    def _classify_select(self):
        """按分类选择视频

        函数通过模型映射表确定分类视频所属模型
        然后通过过滤器选择出符合条件的视频信息
        返回值：result 从数据库中的到的结果
        """
        video_type_str = TYPE_LIST[self._video_type]  # 视频类型的字符串表示
        video_time_str = TIME_LIST[self._video_time]  # 视频年代的字符串表示
        video_area_str = AREA_LIST[self._video_area]  # 视频地区的字符串表示
        video_model = TYPE_DICT[video_type_str]  # 分类视频所属模型

        # 处理特殊值，当视频的类型/年代/地区编号值为0时，
        # 应使对应的字符串表示为空，以选择出全部的数据
        if self._video_type == 0:
            video_type_str = ""
        if self._video_type == 9:
            video_type_str = ""
        if self._video_time == 0:
            video_time_str = ""
        if self._video_area == 0:
            video_area_str = ""

        result = video_model.objects.filter(flag_type__contains = video_type_str, 
                                            flag_time__contains = video_time_str, 
                                            flag_area__contains = video_area_str).order_by('-id')
        return result

