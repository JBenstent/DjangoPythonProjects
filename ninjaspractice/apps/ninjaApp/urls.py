from django.conf.urls import url
from django.contrib import admin
from views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^ninjas$', allninjas, name='allninjas'),
    url(r'^ninjas/(?P<color>\w+)$', show, name='show'),
]
