from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calendar_project.urls')),
    path('', include('django.contrib.auth.urls')),
]