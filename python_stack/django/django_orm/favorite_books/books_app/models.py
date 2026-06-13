from django.db import models
import re
import bcrypt

# Create your models here.

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}

        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters"

        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address"

        existing_user = User.objects.filter(email=postData['email'])
        if existing_user:
            errors['email_exists'] = "Email already exists"

        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"

        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = "Passwords do not match"

        return errors

    def login_validator(self, postData):
        errors = {}

        users = User.objects.filter(email=postData['email'])

        if not users:
            errors['email'] = "Invalid email or password"
        else:
            user = users[0]
            if not bcrypt.checkpw(
                postData['password'].encode(),
                user.password.encode()
            ):
                errors['password'] = "Invalid email or password"

        return errors


class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}

        if len(postData['title']) < 1:
            errors['title'] = "Title is required"

        if len(postData['description']) < 5:
            errors['description'] = "Description must be at least 5 characters"

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    uploaded_by = models.ForeignKey(
        User,
        related_name="books_uploaded",
        on_delete=models.CASCADE
    )

    users_who_like = models.ManyToManyField(
        User,
        related_name="liked_books"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BookManager()