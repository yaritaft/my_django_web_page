from django.urls import path, include
from books.views import bring_books

urlpatterns = [path("", bring_books, name="bring_books-Index")]
