from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, "calendarAPP/login.html", {})

# views.py
from django.shortcuts import render


def signup(request):
    return render(request, 'sign-up.html')
