""" URL管理器

    tmp目录下有两种类型的url文件，xx.new.json, xx.all.json
    xx.new.json：存储计划任务中的URL
    xx.all.json：存储某个站点全部的URL
"""

import os
import sys
import json
import shutil

def merge_urls(ldir, low, high):
    """合并URL到一个文件

    Returns:
        urls_list 合并后的URL列表
    """
    urls_list = []
    for i in range(int(low),int(high)+1):
        with open("tmp/%s/%d.json" % (ldir, i),'r') as file_url:
            urls = json.load(file_url)
            urls_list.extend(urls)
    return urls_list


def extend_urls(ldir, urls_list):
    """扩展URL，并将最新的URL扩展到xx.all.json

    Args:
        urls_list 合并后的URL列表
    """
    with open("tmp/%s.all.json" % ldir,"r+") as file_all:
        items_tmp = set(urls_list)
        items_all = set(json.load(file_all))
        items_extend = list(items_tmp | items_all)
        # 将全部的URL存放进文件中
        file_all.seek(0)
        file_all.truncate()
        json.dump(items_extend, file_all)         


def comerge(ldir,low,high):
    """合并与扩展URL

    Args:
        ldir 存储单个URL文件的目录
        low  起始URL文件编号
        high 终止URL文件编号
    """
    urls_list = merge_urls(ldir, low, high)
    with open("tmp/%s.new.json" % ldir,"w") as file_new:
        json.dump(urls_list, file_new)
    extend_urls(ldir, urls_list)

