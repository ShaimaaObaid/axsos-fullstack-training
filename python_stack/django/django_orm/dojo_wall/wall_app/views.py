from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta

from login_app.models import User
from .models import Message, Comment

# Create your views here.

def wall(request):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'all_messages': Message.objects.all().order_by('-created_at')
    }

    return render(request, 'wall.html', context)


def create_message(request):
    if 'user_id' not in request.session:
        return redirect('/')

    if request.method == 'POST':
        errors = Message.objects.message_validator(request.POST)

        if errors:
            for value in errors.values():
                messages.error(request, value)
            return redirect('/wall')

        user = User.objects.get(id=request.session['user_id'])

        Message.objects.create(
            message=request.POST['message'],
            user=user
        )

    return redirect('/wall')


def create_comment(request):
    if 'user_id' not in request.session:
        return redirect('/')

    if request.method == 'POST':
        errors = Comment.objects.comment_validator(request.POST)

        if errors:
            for value in errors.values():
                messages.error(request, value)
            return redirect('/wall')

        user = User.objects.get(id=request.session['user_id'])
        message = Message.objects.get(id=request.POST['message_id'])

        Comment.objects.create(
            comment=request.POST['comment'],
            user=user,
            message=message
        )

    return redirect('/wall')


def delete_message(request, message_id):
    if 'user_id' not in request.session:
        return redirect('/')

    message = Message.objects.get(id=message_id)
    current_user = User.objects.get(id=request.session['user_id'])

    thirty_minutes_ago = timezone.now() - timedelta(minutes=30)

    if message.user == current_user and message.created_at >= thirty_minutes_ago:
        message.delete()
    else:
        messages.error(request, "You can only delete your own messages within 30 minutes.")

    return redirect('/wall')


def delete_comment(request, comment_id):
    if 'user_id' not in request.session:
        return redirect('/')

    comment = Comment.objects.get(id=comment_id)
    current_user = User.objects.get(id=request.session['user_id'])

    if comment.user == current_user:
        comment.delete()
    else:
        messages.error(request, "You can only delete your own comments.")

    return redirect('/wall')