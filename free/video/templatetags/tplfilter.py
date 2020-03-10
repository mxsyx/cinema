from django import template
from video.config import FLAG_TYPE_DICT
from video.config import VIDOE_TYPE_TO_STR
from video.config import TYPE_LIST
from video.config import TIME_LIST
from video.config import AREA_LIST

register = template.Library()

@register.filter()
def custom_star_light(score):
    """ 返回点亮的星星的个数 """
    return range(int(score/2))

@register.filter()
def custom_star_slake(score):
    """ 返回未点亮的星星的个数 """
    return range(5 - int(score/2))

@register.filter()
def custom_split_actors(actor):
    """将演员字符串分割成字符串列表
    
    Args:
        actor 演员字符串
    Returns：
        actors 分割后的演员字符串列表
    """
    try:
        actors = actor.split('、')
        actors.remove('')
        return actors
    except Exception:
       return []

@register.filter()
def custom_type_to_num(flag_type):
    """ 函数返回视频类型的编号 """
    return FLAG_TYPE_DICT[flag_type]


@register.filter()
def custom_type_to_mtva(flag_type):
    """ 函数返回视频类型的编号 """
    return VIDOE_TYPE_TO_STR[custom_type_to_num(flag_type)]

@register.filter()
def custom_range(value):
    return range(0, value)


@register.filter()
def custom_type_list(index):
    return TYPE_LIST[index]

@register.filter()
def custom_time_list(index):
    return TIME_LIST[index]

@register.filter()
def custom_area_list(index):
    return AREA_LIST[index]

@register.filter()
def custom_create_iterator(lists):
    """函数根据传递过来的数组类对象lists
    生成一个长度为lists大小的数字迭代器"""
    return range(0, len(lists))

@register.filter()
def custom_at(index, lists):
    """函数返回数组类对象lists在
    索引为index处的值"""
    return lists[index]
