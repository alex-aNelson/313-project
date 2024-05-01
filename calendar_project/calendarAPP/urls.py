from django.urls import path
from . import views

app_name = 'cal'
urlpatterns = [
    path('', views.home, name='home'),
    # path('/add-event', views.add, name='add')
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('event_detail/<int:pk>',views.event_detail, name="event_detail"),
    path("update_event/<int:pk>", views.update_event, name="update_event"),
    path('login/', views.login_user, name='login')
]