from django.shortcuts import render
from django.conf import settings


def about_me(request):
    return render(request, "aboutme/about_me.html", settings.DICT_URLS)
