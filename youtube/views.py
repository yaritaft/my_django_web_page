from django.shortcuts import render
from .models import YoutubeVideo


def youtube_videos_view(request):
    video_urls = tuple(
        [video.youtube_url for video in YoutubeVideo.objects.all()]
    )
    return render(request, "youtube/youtube.html", {"video_urls": video_urls})
