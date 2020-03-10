from django.urls import path
from django.conf.urls import url
from video import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:movie_id>/', views.display_movie_info, name='display_movie_info'),
    path('tvseries/<int:tvseries_id>/', views.display_tvseries_info, name='display_tvseries_info'),
    path('variety/<int:variety_id>/', views.display_variety_info, name='display_variety_info'),
    path('anime/<int:anime_id>/', views.display_anime_info, name='display_anime_info'),
    path('playmovie/<int:movie_id>/', views.play_movie, name='play_movie'),
    path('playtvseries/<int:tvseries_id>/<int:episode>/', views.play_tvseries, name='play_tvseries'),
    path('playvariety/<int:variety_id>/<int:episode>/', views.play_variety, name='play_variety'),
    path('playanime/<int:anime_id>/<int:episode>/', views.play_anime, name='play_anime'),
    path('playinvalid/', views.play_invalid, name='play_invalid'),
    url(r'^type/(\d+)/time/(\d+)/area/(\d+)/page/(\d+)/$', views.classify, name='classify'),
    url(r'^keyword/(.+)/page/(\d+)/$', views.search, name='search'),
]

