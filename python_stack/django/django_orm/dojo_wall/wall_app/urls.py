from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall),
    path('messages/create', views.create_message),
    path('messages/<int:message_id>/delete', views.delete_message),
    path('comments/create', views.create_comment),
    path('comments/<int:comment_id>/delete', views.delete_comment),
]