from django.urls import path, include
from aboutme.views import about_me

urlpatterns = [path("", about_me, name="about_me-Index")]
