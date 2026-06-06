from django.shortcuts import render, redirect
import random

def index(request):

    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
        request.session['attempts'] = 0
        request.session['status'] = ""

    return render(request, "index.html", {
        "status": request.session.get("status"),
        "attempts": request.session.get("attempts"),
    })


def guess(request):
    if request.method == "POST":
        guess = int(request.POST.get("guess"))
        number = request.session['number']

        request.session['attempts'] += 1

        if guess < number:
            request.session['status'] = "low"
        elif guess > number:
            request.session['status'] = "high"
        else:
            request.session['status'] = "correct"

        return redirect("/")

    return redirect("/")


def reset(request):
    request.session.flush()
    return redirect("/")