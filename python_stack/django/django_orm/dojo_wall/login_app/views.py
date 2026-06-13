from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User

# Create your views here.

def index(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        errors = User.objects.register_validator(request.POST)

        if errors:
            for value in errors.values():
                messages.error(request, value)
            return redirect('/')

        hashed_password = bcrypt.hashpw(
            request.POST['password'].encode(),
            bcrypt.gensalt()
        ).decode()

        user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=hashed_password
        )

        request.session['user_id'] = user.id
        request.session['first_name'] = user.first_name

        return redirect('/wall')

    return redirect('/')


def login(request):
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)

        if errors:
            for value in errors.values():
                messages.error(request, value)
            return redirect('/')

        user = User.objects.get(email=request.POST['email'])

        request.session['user_id'] = user.id
        request.session['first_name'] = user.first_name

        return redirect('/wall')

    return redirect('/')


def logout(request):
    request.session.flush()
    return redirect('/')