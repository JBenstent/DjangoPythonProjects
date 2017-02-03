from django.conf.urls import url

from views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^register$', register_method, name='register_subroute'),
    url(r'^login$', login_method, name='login_method'),
    url(r'^logout$', logout, name='logout')
]
