import redis
import random
from video.context import *
from django.shortcuts import render
from django.http import HttpResponse
from video.classify import ClassifyContext
from video.search import SearchContext	
from video.ranking import RankingContext
from video.dump import RedisDump
from video.features import add_play_volume
from video.begfilm import BegFilm
from video.config import ERROR_MESSAGE
from video.features import process_feedback


def index(request):
	contextobj = IndexContext(request)
	if contextobj.process():
		return render(request, 'index.tpl',contextobj.context())
	return HttpResponse(ERROR_MESSAGE)


""" 处理视频信息页面 """
def display_movie_info(request, movie_id):
	contextobj = MovieInfoContext(request, movie_id)
	if contextobj.process():
		return render(request, 'info/infomovie.tpl',contextobj.context())
	return HttpResponse(ERROR_MESSAGE)

def display_tvseries_info(request, tvseries_id):
	contextobj = VideoInfoContext(request, 't', tvseries_id)
	if contextobj.process():
		return render(request, 'info/infotvseries.tpl',contextobj.context())
	return HttpResponse(ERROR_MESSAGE)

def display_variety_info(request, variety_id):
	contextobj = VideoInfoContext(request, 'v', variety_id)
	if contextobj.process():
		return render(request, 'info/infovariety.tpl',contextobj.context())
	return HttpResponse(ERROR_MESSAGE)

def display_anime_info(request, anime_id):
	contextobj = VideoInfoContext(request, 'a', anime_id)
	if contextobj.process():
		return render(request, 'info/infoanime.tpl',contextobj.context())
	return HttpResponse(ERROR_MESSAGE)


""" 处理视频播放页面 """
def play_movie(request, movie_id):
	contextobj = PlayMovieContext(request, movie_id)
	if contextobj.process():
		add_play_volume('m', movie_id)
		return render(request, 'play/playmovie.tpl', contextobj.context())
	return HttpResponse(ERROR_MESSAGE)

def play_tvseries(request, tvseries_id, episode):
	contextobj = PlayVideoContext(request, 't', tvseries_id, episode)
	if contextobj.process():
		add_play_volume('t',tvseries_id)
		return render(request, 'play/playtvseries.tpl', contextobj.context())
	return HttpResponse(ERROR_MESSAGE)

def play_variety(request, variety_id, episode):
	contextobj = PlayVideoContext(request, 'v', variety_id, episode)
	if contextobj.process():
		add_play_volume('v',variety_id)
		return render(request, 'play/playvariety.tpl', contextobj.context())
	return HttpResponse(ERROR_MESSAGE)

def play_anime(request, anime_id, episode):
	contextobj = PlayVideoContext(request, 'a', anime_id, episode)
	if contextobj.process():
		add_play_volume('a',anime_id)
		return render(request, 'play/playanime.tpl', contextobj.context())
	return HttpResponse(ERROR_MESSAGE)

def play_invalid(request):
	""" 处理播放地址失效页面 """
	return render(request, 'play/playinvalid.tpl')


""" 处理视频分类页面 """
def classify(request, video_type, video_time, video_area, page):
	contextobj = ClassifyContext(request, int(video_type), int(video_time), int(video_area), int(page))
	if contextobj.process():
		return render(request, 'classify.tpl',contextobj.context())
	return HttpResponse(ERROR_MESSAGE)


""" 处理视频搜索页面 """
def search(request, keyword, page):
	contextobj = SearchContext(request, keyword, int(page))
	if contextobj.process():
		return render(request, 'search.tpl', contextobj.context())
	return HttpResponse(ERROR_MESSAGE)


""" 处理视频排行页面 """
def ranking(request):
	contextobj = RankingContext(request)
	if contextobj.process():
		return render(request, 'ranking.tpl', contextobj.context())
	return HttpResponse(ERROR_MESSAGE)


""" 处理REDIS持久化页面 """
def redisdump(request):
	redisdump = RedisDump()
	if redisdump.dump():
		tips = "DUMP成功"
	else:
		tips = "DUMP失败"	
	return render(request, 'tips.tpl',{'tips':tips})


""" 处理求片留言页面 """
def begfilm(request):
	contextobj = BegFilm(request)
	if request.method == 'GET':
		if contextobj.process():
			return render(request, 'begfilm.tpl', contextobj.context())
		else:
			return HttpResponse(ERROR_MESSAGE)
	else:
		response = HttpResponse()
		if contextobj.process_begfilm():
			response.status_code = 200
		else:
			response.status_code = 500
		return response


""" 处理求片反馈页面 """
def feedback(request):
	response = HttpResponse()
	if process_feedback(request):
		response.status_code = 200
	else:
		response.status_code = 500
	return response


""" 处理下载页面 """
def download(request):
	return render(request, 'download.tpl')


""" 404页面未找到 """
def page_not_found(request):
	return render(request, '404.tpl')
