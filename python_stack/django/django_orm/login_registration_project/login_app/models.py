from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

class UserManager(models.Manager):

    def register_validator(self, postData):

        errors = {}

        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters"

        if not postData['first_name'].isalpha():
            errors['first_name_letters'] = "First name must contain letters only"

        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters"

        if not postData['last_name'].isalpha():
            errors['last_name_letters'] = "Last name must contain letters only"

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address"

        if User.objects.filter(email=postData['email']).exists():
            errors['email_exists'] = "Email already registered"

        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"

        if postData['password'] != postData['confirm_pw']:
            errors['confirm_pw'] = "Passwords do not match"

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()