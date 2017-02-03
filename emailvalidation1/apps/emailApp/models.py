from __future__ import unicode_literals

from django.db import models

class Email(models.Model):
    emails = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class User(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     user = models.ForeignKey(Email, related_name='user')
