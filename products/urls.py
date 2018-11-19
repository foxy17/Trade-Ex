from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, re_path

from .views import (
    post_list,
    post_create,

    post_update,
    post_delete,
    PostDetailView
)

urlpatterns = [
    path('', post_list, name='list'),
    path('create', post_create,name='create_post'),

    re_path(r'^(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name='detail'),
    re_path(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    ]
urlpatterns += staticfiles_urlpatterns()