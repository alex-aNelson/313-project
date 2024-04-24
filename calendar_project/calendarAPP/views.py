from django.shortcuts import render, redirect
from .models import Event
from django.contrib.auth.models import User
from datetime import date

# Create your views here.
def home(request):
    # if request.user.is_authenticated():
    #     event_list = Event.objects.filter(users_event_id=request.user.id)
    #     return render(request, 'calendarAPP/index.html', {'user_events' : event_list})
    # else:
    #     return redirect("home") # UPDATE TO LOGIN ONCE VIEW/URL IS MADE
    # Query to get Events specific to user logged in, also filters out events that are outdated from current date
    # event_list = Event.objects.filter(users_event_id=request.user.id, event_date__gt=date.today()).order_by("event_date") 
    # return render(request, 'calendarAPP/index.html', {'user_events' : event_list})
    
    event_list_future = Event.objects.filter(users_event_id=request.user.id, event_date__date__gt=date.today()).order_by("event_date") 
    event_list_today = Event.objects.filter(users_event_id=request.user.id, event_date__date=date.today()).order_by("event_date") 
    
    return render(request, 'calendarAPP/index.html', {'today_events' : event_list_today, 'future_events' : event_list_future})
   