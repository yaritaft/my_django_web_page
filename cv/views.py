from django.shortcuts import render
from django.conf import settings


def cv_dark(request):
    return render(request, "cv/cv.html", settings.DICT_URLS)
