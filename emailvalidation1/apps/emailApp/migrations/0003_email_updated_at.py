# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailApp', '0002_auto_20170124_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
