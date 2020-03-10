from free.settings import pool
from video.models import Feedback
from free.settings import logger
import time

def add_play_volume(video_type, video_id):
	"""增加某个视频的播放量

	用户每点击一次播放按钮，
	便向redis数据库更新某个视频的播放量。
	Args:
		video_type 视频类型
		  'm':movie / 't':tvseries / 'v':variety / 'a':anime
		video_id 视频ID
	"""
	try:
		r = redis.Redis(connection_pool=pool)
		r.incr("%s_%d" % (video_type, video_id))
	except Exception as e:
		pass

def process_feedback(request):
    try:
        model = Feedback()
        model.ip = request.META['REMOTE_ADDR']
        model.ttime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        model.url = request.POST.get('url','')
        model.content = request.POST.get('feedbackinfo','')
        model.email = request.POST.get('email','')
        model.save()
        return True
    except Exception as e:
        logger.error(str(e))
        return False

