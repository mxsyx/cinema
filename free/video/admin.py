from django.contrib import admin
from .models import Movie
from .models import Tvseries
from .models import Variety
from .models import Anime

admin.site.register(Movie)
admin.site.register(Tvseries)
admin.site.register(Variety)
admin.site.register(Anime)