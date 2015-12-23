from django.conf.urls import include, url
from django.contrib import admin
from cop.views import *

urlpatterns = [
    url(r'^view/$', view, name='view'),
    url(r'^add/$', add, name='add'),
    url(r'^update/(\d+)/$', update, name='update'),
    url(r'^delete/$', delete, name='delete'),
]