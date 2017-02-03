from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^isvalid$', views.isvalid),
    url(r'^success$', views.success),
    url(r'^success$', views.delete)
]
