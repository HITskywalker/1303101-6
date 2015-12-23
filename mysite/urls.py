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
from smp.views import getDoc,ViewPaper,addauthor,change,delezhuanli,delezhuanzhu,changezl,changezz,stav
from smp.views import register,searchall,dele,login_view,showp,changeau,delau,sta,logout_view, Price, prizeshow,prizedele,changeprize,SearchP,addzlauthor,addzl,viewzhuanli,addzzauthor,addzz,viewzhuanzhu
from smp.views import addprauthor
admin.autodiscover()
urlpatterns = [
    url(r'^$', 'smp.views.index', name='home'),
    url(r'^index$','smp.views.index',name='index'),
    url(r'^add/$', 'smp.views.add', name='add'),
    url(r'^$', 'smp.views.index', name='home'),
    url(r'^add2/(\d+)/(\d+)/$', 'smp.views.add2', name='add2'),
    url(r'^contact/$','smp.views.contact',name='contact'),
    url(r'^about/$','smp.views.about',name='about'),
    url(r'^show/$','smp.views.show',name='show'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload/$',getDoc),
    url(r'^view/$',ViewPaper),
    url(r'^register/$',register),
    url(r'^search/$',searchall),
    url(r'^delete/$',dele),
    url(r'^login/$',login_view),
    url(r'^addauthor/$',addauthor),
    url(r'^deleteauthor/$',delau),
    url(r'^change/$',change),
    url(r'^detail/$',showp),
    url(r'^changeauthor/$',changeau),
    url(r'^stat/$',sta),
    url(r'^logout/$',logout_view),
    url(r'^addprize/$', Price),
    url(r'^viewprize/$', prizeshow),
    url(r'^deleprize/$', prizedele),
    url(r'^changeprize/$', changeprize),
    url(r'^searchprize/$', SearchP),
    url(r'^addzlaf/$', addzlauthor),
    url(r'^addzl/$', addzl),
    url(r'^viewzl/$', viewzhuanli),
    url(r'^delezhuanli/$', delezhuanli),
    url(r'^addzzaf/$', addzzauthor),
    url(r'^addzz/$', addzz),
    url(r'^viewzz/$', viewzhuanzhu),
    url(r'^delezhuanzhu/$', delezhuanzhu),
    url(r'^addpraf/$', addprauthor),
    url(r'^changezl/$', changezl),
    url(r'^changezz/$', changezz),
    url(r'^viewall/$', stav),
    url(r'^learn/', include('learn.urls', namespace='learn')),
]
urlpatterns += [url(r'^project/', include('project.urls', namespace='project')),
]
urlpatterns += [url(r'^cop/', include('cop.urls', namespace='cop')),
]

