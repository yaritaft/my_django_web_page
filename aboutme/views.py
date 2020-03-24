from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def about_me(request: HttpRequest) -> HttpResponse:
    """Render the about me view.

    Parameters
    ----------
    request : HttpRequest
        Get request to require about me view.

    Returns
    -------
    HttpResponse
        HTTP package with view requested.
    """
    return render(request, "aboutme/about_me.html")
