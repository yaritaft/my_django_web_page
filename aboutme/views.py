from django.shortcuts import render


def about_me(request):
    return render(request, "aboutme/about_me.html")
