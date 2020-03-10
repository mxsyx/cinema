""" URL Configuration
	The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""
from django.urls import path
from django.urls import include
from django.contrib import admin
from django.conf.urls import handler404
from django.conf.urls import handler500
import video.urls
import video.views

urlpatterns = [
    path('', include('video.urls')),
    path('info/', include('video.urls')),
    path('play/', include('video.urls')),
    path('classify/', include('video.urls')),
    path('search/', include('video.urls')),
    path('ranking/', video.views.ranking, name='ranking'),
    path('redisdump/', video.views.redisdump, name='redisdump'),
    path('begfilm/', video.views.begfilm, name='begfilm'),
    path('feedback/', video.views.feedback, name='feedback'),
    path('download/', video.views.download, name='download'),
    path('admin/', admin.site.urls),
]


handler404 = video.views.page_not_found
handler500 = video.views.page_not_found

