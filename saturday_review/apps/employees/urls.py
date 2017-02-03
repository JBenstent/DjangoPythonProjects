from django.conf.urls import url
from views import *
# from django.contrib import admin

urlpatterns = [
    url(r'^$', employees, name='emp_home'),
]
