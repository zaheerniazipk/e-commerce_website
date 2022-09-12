from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Blog Index")
    return render(request, "blog/index.html")
