from django.db import models
import re
import bcrypt

# Create your models here.

class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}

        if len(post_data['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters."

        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters."

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid email address."

        if User.objects.filter(email=post_data['email']).exists():
            errors['email_exists'] = "Email already exists."

        if len(post_data['password']) < 8:
            errors['password'] = "Password must be at least 8 characters."

        if post_data['password'] != post_data['confirm_password']:
            errors['confirm_password'] = "Passwords do not match."

        return errors

    def login_validator(self, post_data):
        errors = {}

        users = User.objects.filter(email=post_data['email'])

        if not users:
            errors['login'] = "Invalid email or password."
        else:
            user = users[0]
            if not bcrypt.checkpw(
                post_data['password'].encode(),
                user.password.encode()
            ):
                errors['login'] = "Invalid email or password."

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"