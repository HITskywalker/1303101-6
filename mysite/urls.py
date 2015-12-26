"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from smp.views import getDoc,ViewPaper
from smp.views import register,Search,dele,login_view
import os


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^reg/$',getDoc),
    url(r'^view/$',ViewPaper),
    url(r'^register/$',register),
    url(r'^search/$',Search),
    url(r'^delete/$',dele),
    url(r'^login/$',login_view),
]

urlpatterns += ['',
    (r'^images/(?P<path>.*)$' , 'django.views.static.serve',{'document_root': os.path.join( settings.STATIC_PATH , 'images' ) } ) ,
    (r'^css/(?P<path>.*)$' , 'django.views.static.serve',{'document_root': os.path.join( settings.STATIC_PATH , 'css' ) } ) ,
    (r'^js/(?P<path>.*)$' , 'django.views.static.serve',{'document_root': os.path.join( settings.STATIC_PATH , 'js' ) } ) ,
]