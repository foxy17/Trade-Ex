from django.conf.urls import url
from django.urls import include
from .views import home_page,login_page,register_page
from django.contrib.auth import views
from django.contrib import admin
urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^login/$', login_page, name='login'),
url(r'^register/$', register_page,name='register'),
    url(r'^admin/', admin.site.urls),
]