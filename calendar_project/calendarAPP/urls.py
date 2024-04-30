from django.urls import path
from . import views

app_name = 'cal'
urlpatterns = [
    path('', views.home, name='home'),
    # path('/add-event', views.add, name='add')
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
]