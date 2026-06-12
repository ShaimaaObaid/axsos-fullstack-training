from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/create', views.create_course, name='create_course'),
    path('courses/destroy/<int:course_id>', views.destroy, name='destroy'),
    path('courses/<int:course_id>/comments', views.comments, name='comments'),
]
