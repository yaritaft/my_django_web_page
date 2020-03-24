from django.urls import path, include
from suggestions.views import SuggestionView

urlpatterns = [path("", SuggestionView.as_view(), name="SuggestionView-Index")]
