from django.contrib import admin
from . models import movie_info,directors,Actor,censorInfo
# Register your models here.

admin.site.register(movie_info)
admin.site.register(directors)
admin.site.register(Actor)
admin.site.register(censorInfo)

