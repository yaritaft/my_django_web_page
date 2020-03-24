from django.urls import path
from youtube.views import youtube_videos_view


urlpatterns = [
    path("", youtube_videos_view, name="youtube-Index"),
]
