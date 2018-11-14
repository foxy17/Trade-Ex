from django.conf.urls import url
from . import views
app_name = 'accounts'
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register,name='register'),
    url(r'^success$', views.success),
    url(r'^login$', views.log_in,name='login'),
    url(r'^list$', views.list)

]