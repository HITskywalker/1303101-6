from django.conf.urls import url
from .models import *
from .views import *

urlpatterns =[
    url(r'^pcreate/$', create_project2, name='create_project'),
    url(r'^plist/$', list_project, name='list_project'),
    url(r'^pedit/(?P<id>[^/]+)/$', edit_project, name='edit_project'),
    url(r'^pview/(?P<id>[^/]+)/$', view_project, name='view_project'),
    url(r'^icreate/$', create_projectidentify, name='create_projectidentify'),
    url(r'^icreate2/(?P<id>[^/]+)/$', create_projectidentify2, name='create_projectidentify2'),

    url(r'^ilist/$', list_projectidentify, name='list_projectidentify'),
    url(r'^iedit/(?P<id>[^/]+)/$', edit_projectidentify, name='edit_projectidentify'),
    url(r'^iview/(?P<id>[^/]+)/$', view_projectidentify, name='view_projectidentify'),
    url(r'^ccreate/$', create_projectcheck, name='create_projectcheck'),
    url(r'^ccreate2/(?P<id>[^/]+)/$', create_projectcheck2, name='create_projectcheck2'),
    url(r'^clist/$', list_projectcheck, name='list_projectcheck'),
    url(r'^cedit/(?P<id>[^/]+)/$', edit_projectcheck, name='edit_projectcheck'),
    url(r'^cview/(?P<id>[^/]+)/$', view_projectcheck, name='view_projectcheck'),
    # url(r'^mcreate/$', create_member, name='create_member'),
    # url(r'^mlist/$', list_member, name='list_member'),
    # url(r'^medit/(?P<id>[^/]+)/$', edit_member, name='edit_member'),
]
