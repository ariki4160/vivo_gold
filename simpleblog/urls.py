# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^simpleblog/$', 'simpleblog.dblog.views.index'),
    (r'^simpleblog/writeBlog/$', 'simpleblog.dblog.views.writeBlog'),
    (r'^simpleblog/blog/postEntry/$', 'simpleblog.dblog.views.postEntry'),
    (r'^simpleblog/blog/(?P<blog_id>\d+)/$', 'simpleblog.dblog.views.readBlog'),
    (r'^simpleblog/blog/(?P<blog_id>\d+)/comment/$', 'simpleblog.dblog.views.comment'),
    (r'^simpleblog/blog/(?P<blog_id>\d+)/comment/add/$', 
                             'simpleblog.dblog.views.addComment'),
    (r'^simpleblog/blog/(?P<blog_id>\d+)/postComment/$', 
                             'simpleblog.dblog.views.postComment'),
    (r'^scripts/(?P<path>.*)$', 'django.views.static.serve', 
                                 {'document_root': '/home/ariki/public_html/django/templates/dblog/scripts'}),
    # (r'^admin/', include('django.contrib.admin.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),




)
