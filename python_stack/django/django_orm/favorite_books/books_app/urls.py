from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),

    path('books/', views.books),
    path('books/create/', views.create_book),
    path('books/<int:book_id>/', views.show_book),
    path('books/<int:book_id>/update/', views.update_book),
    path('books/<int:book_id>/delete/', views.delete_book),
    path('books/<int:book_id>/favorite/', views.add_favorite),
    path('books/<int:book_id>/unfavorite/', views.remove_favorite),

    path('users/<int:user_id>/', views.user_page),
]