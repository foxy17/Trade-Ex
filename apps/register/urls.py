from django.urls import path

from . import views
app_name = 'accounts'
urlpatterns = [
    path('', views.index,name='index'),
    path('register/', views.register,name='register'),
    path('success/', views.success),
    path('login/', views.user_login,name='login'),
    path('list/', views.list),
    path('logout/', views.user_logout, name ='logout')
]