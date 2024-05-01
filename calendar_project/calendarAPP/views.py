from django.shortcuts import render, redirect
from .models import Event
from django.contrib.auth.models import User
from datetime import date, datetime, timedelta
from .utils import Calendar
import calendar
from .forms import AddEventForm
from django.contrib import messages

from django.utils.safestring import mark_safe
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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

class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendarAPP/calendar.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # use today's date for the calendar
        #d = get_date(self.request.GET.get('day', None))
        d = get_date(self.request.GET.get('month', None))
        
        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(user, withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event_detail(request, pk):
    event = Event.objects.get(pk = pk)
    return render(request, 'calendarAPP/event_detail.html', {'event': event})

def update_event(request, pk):
    current_event = Event.objects.get(event_id=pk)
    form = AddEventForm(request.POST or None, instance=current_event)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(
                    request, "You have successfully updated the event!"
                )
                return redirect("cal:home")
        return render(request, "calendarAPP/update_event.html", {"form": form})
    else:
        messages.success(request, "You must be logged in")
        return redirect("cal:home")
    
    #login view
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        #authenticate
        user = authenticate(username = username, password =password)
        if user is None: 
            login(request, user)
            messages.success(request, "login was a success")
            return redirect('cal:home')
        else:
            messages.success(request, "login was not a success, try again")
            return redirect('home')
    else:
        return render(request, login.html)