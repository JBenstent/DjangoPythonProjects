from __future__ import unicode_literals

from django.db import models
from ..login.models import *

class Team(models.Model):
    manager = models.ForeignKey(User, related_name='manager_of')
    employeee = models.ForeignKey(User)
