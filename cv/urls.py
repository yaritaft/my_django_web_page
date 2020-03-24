from django.urls import path
from cv.views import cv_dark

urlpatterns = [
    path("", cv_dark, name="CV-Dark-Index"),
]
