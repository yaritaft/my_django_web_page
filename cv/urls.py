from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.cv_dark, name="CV-Dark"),
]
