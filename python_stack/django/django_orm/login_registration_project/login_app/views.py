from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
    return render(request, 'index.html')


def register(request):

    if request.method != "POST":
        return redirect('/')

    errors = User.objects.register_validator(request.POST)

    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    pw_hash = bcrypt.hashpw(
        request.POST['password'].encode(),
        bcrypt.gensalt()
    ).decode()

    user = User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=pw_hash
    )

    request.session['user_id'] = user.id

    return redirect('/success')


def login(request):

    if request.method != "POST":
        return redirect('/')

    users = User.objects.filter(email=request.POST['email'])

    if not users:
        messages.error(request, "Invalid email/password")
        return redirect('/')

    user = users[0]

    if bcrypt.checkpw(
        request.POST['password'].encode(),
        user.password.encode()
    ):
        request.session['user_id'] = user.id
        return redirect('/success')

    messages.error(request, "Invalid email/password")
    return redirect('/')


def success(request):

    if 'user_id' not in request.session:
        return redirect('/')

    user = User.objects.get(id=request.session['user_id'])

    context = {
        'user': user
    }

    return render(request, 'success.html', context)


def logout(request):

    request.session.clear()

    return redirect('/')