from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {"value": "a"}
    return render(request, "chat/index.html", context)