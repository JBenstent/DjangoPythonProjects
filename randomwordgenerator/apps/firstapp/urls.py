from django.conf.urls import url, include
from django.contrib import admin

from views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^process$', process, name='process'),
    url(r'^clear$', clear, name='clear'),
]
