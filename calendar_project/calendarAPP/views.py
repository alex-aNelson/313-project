from django.shortcuts import render
from .models import Event
# Create your views here.

def event_detail(request, pk):
    event = Event.objects.get(pk = pk)
    return render(request, 'calendarAPP/event_detail.html', {'event': event})