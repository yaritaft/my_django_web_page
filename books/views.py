from django.shortcuts import render
from .models import Book
from django.conf import settings
from django.http import HttpRequest, HttpResponse

# Create your views here.


def from_query_set_to_dict(book: Book) -> dict:
    """Convert a Book object into a dict.

    Parameters
    ----------
    book : Book
        A Book object.

    Returns
    -------
    dict
        A dict with the same information.
    """
    return book.__dict__


def bring_books(request: HttpRequest) -> HttpResponse:
    """Generate a list of books and Render books view.

    Parameters
    ----------
    request : HttpRequest
        Get request to require books view.

    Returns
    -------
    HttpResponse
        HTTP package with view requested.
    """
    books_received = {
        "books": tuple(map(from_query_set_to_dict, Book.objects.all()))
    }
    return render(request, "books/books.html", books_received)
