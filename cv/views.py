from django.shortcuts import render
from django.conf import settings
from django.urls import reverse


def cv_dark(request):
    return render(request, "cv/cv.html", settings.DICT_URLS)
