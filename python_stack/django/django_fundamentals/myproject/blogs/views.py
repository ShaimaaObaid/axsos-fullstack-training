from django.shortcuts import render, redirect

def index(request):
    return render(request, "blogs/index.html")

def new(request):
    return render(request, "blogs/new.html")

def create(request):
    return redirect('/blogs/')

def show(request, number):
    return render(request, "blogs/show.html", {'number': number})

def edit(request, number):
    return render(request, "blogs/edit.html", {'number': number})

def destroy(request, number):
    return redirect('/blogs/')