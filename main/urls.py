from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from main import settings

from django.conf.urls.static import static
urlpatterns = [
path('Post/', include('products.urls')) ,
path('Notes/', include('notes.urls')) ,
    path('', include('apps.register.urls')),
url(r"^messages/", include("pinax.messages.urls", namespace="pinax_messages")),
url(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()