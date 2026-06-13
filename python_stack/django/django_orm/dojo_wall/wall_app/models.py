from django.db import models
from login_app.models import User

# Create your models here.

class MessageManager(models.Manager):
    def message_validator(self, post_data):
        errors = {}

        if len(post_data['message']) < 1:
            errors['message'] = "Message cannot be empty."

        return errors


class CommentManager(models.Manager):
    def comment_validator(self, post_data):
        errors = {}

        if len(post_data['comment']) < 1:
            errors['comment'] = "Comment cannot be empty."

        return errors


class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(
        User,
        related_name='messages',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MessageManager()


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.CASCADE
    )
    message = models.ForeignKey(
        Message,
        related_name='comments',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CommentManager()