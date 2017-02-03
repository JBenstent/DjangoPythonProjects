from __future__ import unicode_literals
import re
import bcrypt

from django.db import models
from django.db import IntegrityError


REGEX_EMAIL = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
REGEX_PASSWORD  = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')

class UserManager(models.Manager):
    def validate_user(self, username, email, password, confirm):
        errors = []
        if len(username) < 3:
            errors.append('username too short')
        if REGEX_EMAIL.search(email) is None:
            errors.append('invalid email')
        if REGEX_PASSWORD.search(password) is None:
            errors.append('password too weak')
        if password != confirm:
            errors.append('passwords do not match')
        return errors

    def create_user(self, username, email, password):
        errors = []
        try:
            hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            User.objects.create(username=username, email=email, password=hashed)
        except IntegrityError:
            errors.append('user already exists')
        except IndexError:
            errors.append('you suck')

        return errors

    def authenticate_user(self, username, password):
        try:
            user = User.objects.get(username=username)
            return bcrypt.hashpw(password.encode(), user.password.encode()) == user.password
        except:
            return False

class User(models.Model):
    username = models.CharField(max_length=64, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
