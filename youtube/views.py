from django.shortcuts import render
from .models import YoutubeVideo
from django.http import HttpRequest, HttpResponse


def youtube_videos_view(request: HttpRequest) -> HttpResponse:
    """Generate a list of video urls and render the youtube view.

    Parameters
    ----------
    request : HttpRequest
        Get request to require youtube view.

    Returns
    -------
    HttpResponse
        HTTP package with view requested.
    """
    video_urls = tuple(
        [video.youtube_url for video in YoutubeVideo.objects.all()]
    )
    return render(request, "youtube/youtube.html", {"video_urls": video_urls})
