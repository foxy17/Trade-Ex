from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from login_registration import settings

from django.conf.urls.static import static
urlpatterns = [
path('Post/', include('products.urls')) ,
    path('', include('apps.register.urls')),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)