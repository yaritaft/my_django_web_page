from django.urls import path, include
from . import views

urlpatterns = [
    path("light/", views.cv, name="CV-Index"),
    path("", views.cv_dark, name="CV-Dark"),
]
