from django.shortcuts import render
from .models import Book

# Create your views here.


def from_query_set_to_dict(book):
    return book.__dict__


def bring_books(request):
    books_received = {
        "books": tuple(map(from_query_set_to_dict, Book.objects.all()))
    }
    return render(request, "books/books.html", books_received)
