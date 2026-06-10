from django.shortcuts import render, redirect, get_object_or_404
from .models import Dojo, Ninja

def index(request):
    context = {
        "dojos": Dojo.objects.all(),
    }
    return render(request, "index.html", context)


def create_dojo(request):
    if request.method == "POST":
        Dojo.objects.create(
            name=request.POST["name"],
            city=request.POST["city"],
            state=request.POST["state"]
        )
    return redirect("/")


def create_ninja(request):
    if request.method == "POST":
        dojo = get_object_or_404(Dojo, id=request.POST["dojo_id"])
        Ninja.objects.create(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            dojo=dojo
        )
    return redirect("/")


def delete_dojo(request, dojo_id):
    dojo = get_object_or_404(Dojo, id=dojo_id)
    dojo.delete()
    return redirect("/")