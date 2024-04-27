from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('sign-up/', views.signup, name='signup'),
    path('', include('django.contrib.auth.urls')),
]