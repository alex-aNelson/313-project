from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    date_of_birth = forms.DateField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'username', 'password1', 'password2']
        
