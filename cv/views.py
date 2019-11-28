from django.shortcuts import render
from django.conf import settings

DICT_URLS = settings.DICT_URLS


def cv(request):
    DICT_URLS["dark_mode"] = False
    return render(request, "cv/cv.html", DICT_URLS)


def cv_dark(request):
    DICT_URLS["dark_mode"] = True
    return render(request, "cv/cv.html", DICT_URLS)
