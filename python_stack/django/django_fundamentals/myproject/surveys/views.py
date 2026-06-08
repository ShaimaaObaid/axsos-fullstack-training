from django.shortcuts import render

def index(request):
    return render(request, "surveys/index.html")

def new(request):
    return render(request, "surveys/new.html")