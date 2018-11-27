from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, re_path

from main import settings
from .views import (
    post_list,

    post_create,
post_detail,
    post_update,
    post_delete,


)
app_name='notes'
urlpatterns = [
    path('', post_list, name='home'),
    path('create', post_create,name='create_post'),

    re_path(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    re_path(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    ]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)