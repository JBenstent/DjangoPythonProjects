from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^books$', views.allbookspage),
    url(r'^books/add$', views.addbookspage),
    url(r'^books/create$', views.submitbookinfo),
    url(r'^books/(?P<id>\d+)$', views.renderbookinfo),
    url(r'^books/(?P<id>\d+)/addreview$', views.addreview),
    url(r'^users/(?P<id>\d+)$', views.renderuserinfo)
]
