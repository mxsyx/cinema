# 信息存储器

import time
import scrapy
import MySQLdb
from laofan import emails
from laofan import settings

class MoviePipeline(object):
    def __init__(self):
        """存储器构造函数
        
        通过MySQLdb连接到Mysql数据库，值得注意的是，
        这里使用unix套接字而非地址加端口号的形式连接到数据库
        """
        self.client = MySQLdb.connect(
            unix_socket=settings.UNIX_SOCKET,
            db=settings.MYSQL_DBMAS,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        self.cur = self.client.cursor()
        self.ema = emails.Email()

    def process_item(self, item, spider):
        if(item['mtva']!='m'):
            return item
        self.add_or_update_item(item)
        return item

    def add_or_update_item(self, item):
        max_id = self.select_max_id('movie') + 1
        statement_insert_info = "insert into movie " + \
            "values (%d,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') " + \
            "on duplicate key update UPDATE_TIME='%s',URL='%s'"
        
        item_info =(max_id, item['name'], item['introduction'],item['director'], item['actor'],
            item['flag_time'], item['flag_area'], item['flag_type'],item['score'], item['url_img'], 
            item['update_time'],item['url'], item['update_time'], item['url'])

        try:
            self.cur.execute(statement_insert_info % item_info)
            self.add_ranking(max_id)  # 添加或忽略一条排行表数据
            self.client.commit()
            settings.loginfo.info("pipelines.MoviePipeline 新增或更新存储，视频名称：%s" % item['name'])
        except Exception as e:
            error_info = "@pipelines.MoviePipeline.add_or_update_item statement: %s Exception: %s"
            self.ema.send("任务异常消息",error_info % (statement_insert_info, str(e)))

    def add_ranking(self, max_id):
        # 向排行数据表中新增一条数据，忽略已经存在的数据
        try:
            statement_insert_stat = "insert ignore into ranking (VID) values ('m_%d')" % (max_id)
            self.cur.execute(statement_insert_stat)
        except Exception as e:
            error_info = "@pipelines.MoviePipeline.add_ranking statement: %s Exception: %s"
            self.ema.send("任务异常消息",error_info % (statement_insert_stat, str(e)))

    def select_max_id(self, table_name):
        statement_select_max_id = "select max(id) from %s" % table_name
        self.cur.execute(statement_select_max_id)
        max_id = self.cur.fetchone()[0]
        if(max_id):
            return max_id
        return 0


class TvseriesPipeline(object):
    def __init__(self):
        """存储器构造函数
        
        我们通过MySQLdb连接到Mystatement数据库，
        值得注意的是，这里使用unix套接字而非地址加端口号的形式连接到数据库
        """
        self.client = MySQLdb.connect(
            unix_socket=settings.UNIX_SOCKET,
            db=settings.MYSQL_DBMAS,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        self.cur = self.client.cursor()
        self.ema = emails.Email()

    def process_item(self, item, spider):        
        if(item['mtva']!='t'):
            return item
        self.add_or_update_item(item)
        return item

    def add_or_update_item(self, item):
        max_id = self.select_max_id('tvseries') + 1
        statement_insert_info = "insert into tvseries " + \
            "values (%d,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') on duplicate key update UPDATE_TIME='%s'"
        
        item_info =(max_id, item['name'], item['introduction'],item['director'], item['actor'],
            item['flag_time'], item['flag_area'], item['flag_type'],item['score'], item['url_img'], 
            item['update_time'],item['update_time'])

        try:
            self.cur.execute(statement_insert_info % item_info)
            self.add_ranking(max_id)  # 添加或忽略一条排行表数据
            self.client.commit()
            self.add_or_update_urls(item["urls"], self.select_video_id(item['name']))  # 添加或更新URLS
            settings.loginfo.info("pipelines.TvseriesPipeline 新增或更新存储，视频名称：%s" % item['name'])
        except Exception as e:
            error_info = "@pipelines.TvseriesPipeline.add_or_update_item statement: %s Exception: %s"
            self.ema.send("任务异常消息",error_info % (statement_insert_info, str(e)))
    
    def add_ranking(self, max_id):
        # 向排行数据表中新增一条数据，忽略已经存在的数据
        try:
            statement_insert_stat = "insert ignore into ranking (VID) values ('t_%d')" % (max_id)
            self.cur.execute(statement_insert_stat)
        except Exception as e:
            error_info = "@pipelines.TvseriesPipeline.add_ranking statement: %s Exception: %s"
            self.ema.send("任务异常消息",error_info % (statement_insert_stat, str(e)))

    def add_or_update_urls(self, urls, video_id):
        statement_insert_urls = "insert into u_tvseries values (%d,%d,'%s') on duplicate key update URL='%s'"
        for num in range(0,len(urls)):
            try:
                statement_insert_urls_ = statement_insert_urls % (video_id, num + 1, urls[num], urls[num])
                self.cur.execute(statement_insert_urls_)
            except Exception as e:
                error_info = "@pipelines.TvseriesPipeline.add_urls statement: %s Exception: %s"
                self.ema.send("任务异常消息",error_info % (statement_insert_urls_, str(e)))
        self.client.commit()

    def select_video_id(self, name):
        statement_select_video_id = "select id from tvseries where name='%s'" % name
        self.cur.execute(statement_select_video_id)
        video_id = self.cur.fetchone()[0]
        if(video_id):
            return video_id
        return 0

    def select_max_id(self, table_name):
        statement_select_max_id = "select max(id) from %s" % table_name
        self.cur.execute(statement_select_max_id)
        max_id = self.cur.fetchone()[0]
        if(max_id):
            return max_id
        return 0


class VarietyPipeline(object):
    def __init__(self):
        """存储器构造函数
        
        我们通过MySQLdb连接到Mystatement数据库，
        值得注意的是，这里使用unix套接字而非地址加端口号的形式连接到数据库
        """
        self.client = MySQLdb.connect(
            unix_socket=settings.UNIX_SOCKET,
            db=settings.MYSQL_DBMAS,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        self.cur = self.client.cursor()
        self.ema = emails.Email()

    def process_item(self, item, spider):        
        if(item['mtva']!='v'):
            return item
        self.add_or_update_item(item)
        return item

    def add_or_update_item(self, item):
        max_id = self.select_max_id('variety') + 1
        statement_insert_info = "insert into variety " + \
            "values (%d,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') on duplicate key update UPDATE_TIME='%s'"
        
        item_info =(max_id, item['name'], item['introduction'],item['director'], item['actor'],
            item['flag_time'], item['flag_area'], item['flag_type'],item['score'], item['url_img'], 
            item['update_time'],item['update_time'])

        try:
            self.cur.execute(statement_insert_info % item_info)
            self.add_ranking(max_id)  # 添加或忽略一条排行表数据
            self.client.commit()
            self.add_or_update_urls(item["urls"], self.select_video_id(item['name']))  # 添加或更新URLS
            settings.loginfo.info("pipelines.VarietyPipeline 新增或更新存储，视频名称：%s" % item['name'])
        except Exception as e:
            error_info = "@pipelines.VarietyPipeline.add_or_update_item statement: %s Exception: %s"
            self.ema.send("任务异常消息",error_info % (statement_insert_info, str(e)))
    
    def add_ranking(self, max_id):
        # 向排行数据表中新增一条数据，忽略已经存在的数据
        try:
            statement_insert_stat = "insert ignore into ranking (VID) values ('v_%d')" % (max_id)
            self.cur.execute(statement_insert_stat)
        except Exception as e:
            error_info = "@pipelines.VarietyPipeline.add_ranking statement: %s Exception: %s"
            self.ema.send("任务异常消息",error_info % (statement_insert_stat, str(e)))

    def add_or_update_urls(self, urls, video_id):
        statement_insert_urls = "insert into u_variety values (%d,%d,'%s') on duplicate key update URL='%s'"
        for num in range(0,len(urls)):
            try:
                statement_insert_urls_ = statement_insert_urls % (video_id, num + 1, urls[num], urls[num])
                self.cur.execute(statement_insert_urls_)
            except Exception as e:
                error_info = "@pipelines.VarietyPipeline.add_urls statement: %s Exception: %s"
                self.ema.send("任务异常消息",error_info % (statement_insert_urls_, str(e)))
        self.client.commit()

    def select_video_id(self, name):
        statement_select_video_id = "select id from variety where name='%s'" % name
        self.cur.execute(statement_select_video_id)
        video_id = self.cur.fetchone()[0]
        if(video_id):
            return video_id
        return 0

    def select_max_id(self, table_name):
        statement_select_max_id = "select max(id) from %s" % table_name
        self.cur.execute(statement_select_max_id)
        max_id = self.cur.fetchone()[0]
        if(max_id):
            return max_id
        return 0


class AnimePipeline(object):
    def __init__(self):
        """存储器构造函数
        
        我们通过MySQLdb连接到Mystatement数据库，
        值得注意的是，这里使用unix套接字而非地址加端口号的形式连接到数据库
        """
        self.client = MySQLdb.connect(
            unix_socket=settings.UNIX_SOCKET,
            db=settings.MYSQL_DBMAS,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        self.cur = self.client.cursor()
        self.ema = emails.Email()

    def process_item(self, item, spider):        
        if(item['mtva']!='a'):
            return item
        self.add_or_update_item(item)
        return item

    def add_or_update_item(self, item):
        max_id = self.select_max_id('anime') + 1
        statement_insert_info = "insert into anime " + \
            "values (%d,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') on duplicate key update UPDATE_TIME='%s'"
        
        item_info =(max_id, item['name'], item['introduction'],item['director'], item['actor'],
            item['flag_time'], item['flag_area'], item['flag_type'],item['score'], item['url_img'], 
            item['update_time'],item['update_time'])

        try:
            self.cur.execute(statement_insert_info % item_info)
            self.add_ranking(max_id)  # 添加或忽略一条排行表数据
            self.client.commit()
            self.add_or_update_urls(item["urls"], self.select_video_id(item['name']))  # 添加或更新URLS
            settings.loginfo.info("pipelines.AnimePipeline 新增或更新存储，视频名称：%s" % item['name'])
        except Exception as e:
            error_info = "@pipelines.AnimePipeline.add_or_update_item statement: %s Exception: %s"
            self.ema.send("任务异常消息",error_info % (statement_insert_info, str(e)))
    
    def add_ranking(self, max_id):
        # 向排行数据表中新增一条数据，忽略已经存在的数据
        try:
            statement_insert_stat = "insert ignore into ranking (VID) values ('a_%d')" % (max_id)
            self.cur.execute(statement_insert_stat)
        except Exception as e:
            error_info = "@pipelines.AnimePipeline.add_ranking statement: %s Exception: %s"
            self.ema.send("任务异常消息",error_info % (statement_insert_stat, str(e)))

    def add_or_update_urls(self, urls, video_id):
        statement_insert_urls = "insert into u_anime values (%d,%d,'%s') on duplicate key update URL='%s'"
        for num in range(0,len(urls)):
            try:
                statement_insert_urls_ = statement_insert_urls % (video_id, num + 1, urls[num], urls[num])
                self.cur.execute(statement_insert_urls_)
            except Exception as e:
                error_info = "@pipelines.AnimePipeline.add_urls statement: %s Exception: %s"
                self.ema.send("任务异常消息",error_info % (statement_insert_urls_, str(e)))
        self.client.commit()

    def select_video_id(self, name):
        statement_select_video_id = "select id from anime where name='%s'" % name
        self.cur.execute(statement_select_video_id)
        video_id = self.cur.fetchone()[0]
        if(video_id):
            return video_id
        return 0

    def select_max_id(self, table_name):
        statement_select_max_id = "select max(id) from %s" % table_name
        self.cur.execute(statement_select_max_id)
        max_id = self.cur.fetchone()[0]
        if(max_id):
            return max_id
        return 0

