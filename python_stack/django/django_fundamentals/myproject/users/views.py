from django.shortcuts import render

def register(request):
    return render(request, "users/register.html")

def user_login(request):
    return render(request, "users/login.html")

def users_list(request):
    return render(request, "users/users.html")