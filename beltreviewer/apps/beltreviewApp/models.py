from __future__ import unicode_literals
import re
import bcrypt
from django.db import IntegrityError
from django.db import models

REGEX_PASSWORD  = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')

class Book(models.Model):
    book_title = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

class Review(models.Model):
    contents = models.CharField(max_length=200)
    rating = models.IntegerField()
    book = models.ForeignKey(Book, related_name='reviews') #one book can have many reviews. each review has 1 book
    user = models.ForeignKey(User, related_name='reviews') #one user can have many reviews each review has one user
