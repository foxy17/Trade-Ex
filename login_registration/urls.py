from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path



urlpatterns = [
path('Post/', include('products.urls')) ,
    path('', include('apps.register.urls')),


]