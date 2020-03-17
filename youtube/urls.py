from django.urls import path
from django.shortcuts import redirect
from youtube.views import youtube_videos_view


def my_view(request):
    return redirect("/youtube")


urlpatterns = [
    path("youtube/", youtube_videos_view, name="youtube-Index"),
    path("", my_view, name="landing-page-Index"),
]
