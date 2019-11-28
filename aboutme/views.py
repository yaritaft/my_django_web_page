from django.shortcuts import render
from django.conf import settings


DICT_URLS = settings.DICT_URLS
# Create your views here.


def about_me(request):
    return render(request, "aboutme/about_me.html", DICT_URLS)
