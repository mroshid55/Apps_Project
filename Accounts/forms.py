from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class UserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2')

class UserProfile(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('firstname','lastname','nickname','address','email','phone','image')
