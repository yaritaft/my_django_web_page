from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def cv_dark(request: HttpRequest) -> HttpResponse:
    """Render the cv view.

    Parameters
    ----------
    request : HttpRequest
        Get request to require cv view.

    Returns
    -------
    HttpResponse
        HTTP package with view requested.
    """
    return render(request, "cv/cv.html")
