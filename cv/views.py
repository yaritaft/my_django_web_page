from django.shortcuts import render


def cv_dark(request):
    return render(request, "cv/cv.html")
