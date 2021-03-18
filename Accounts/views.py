from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
from .forms import *
from .models import *


def SIGNUP(request):
    if request.user.is_authenticated:
        return redirect('Notes')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully.')
                return redirect('Login')
            else:
                form = UserCreationForm()
    context = {'form': form}
    return render(request, "Accounts/Signup.html", context)


def LOGIN(request):
    if request.user.is_authenticated:
        return redirect('Notes')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Notes')
            else:
                messages.info(request, 'User name or password is incorrect.')

    return render(request, "Accounts/Login.html")


def LOGOUT(request):
    logout(request)
    return redirect('Login')


def PASS_RECOVERY(request):
    return render(request, 'Accounts/pass_recovery.html')


def PROFILE(request):
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user)
        form = UserProfile()
        if request.method == 'POST':
            form = UserProfile(request.POST, request.FILES)
            if form.is_valid():
                form.instance.user = request.user
                form.save()
                return redirect('Profile')
            else:
                form = UserProfile()
        context = {'profile': profile, 'form': form}
        return render(request, 'Accounts/Profile.html', context)
    else:
        return render(request, "Accounts/Login.html")
