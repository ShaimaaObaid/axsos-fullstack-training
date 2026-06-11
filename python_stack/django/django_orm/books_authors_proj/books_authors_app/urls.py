from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),

    path('books/add/', views.add_book),
    path('authors/add/', views.add_author),

    path('authors/', views.authors),

    path('books/<int:id>/', views.book_details),
    path('authors/<int:id>/', views.author_details),

    path('books/<int:id>/add_author/', views.add_author_to_book),
    path('authors/<int:id>/add_book/', views.add_book_to_author),
]