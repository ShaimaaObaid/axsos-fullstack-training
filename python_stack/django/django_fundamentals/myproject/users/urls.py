from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
path('login/', views.user_login),    path('users/new/', views.register),  # same method
    path('users/', views.users_list),
]