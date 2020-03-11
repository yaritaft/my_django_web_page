from django.contrib import admin
from .models import YoutubeVideo


models_to_register = (YoutubeVideo,)
for one_model in models_to_register:
    admin.site.register(one_model)
