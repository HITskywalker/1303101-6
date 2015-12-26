from django.conf.urls import include, url
from django.contrib import admin
from learn.views import *

urlpatterns = [
    url(r'^view/$', view, name='view'),
    url(r'^add/$', add, name='add'),
    url(r'^update/$', update, name='update'),
    url(r'^delete/$', delete, name='delete'),
]