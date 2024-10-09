from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Signup
from django.contrib.auth.hashers import make_password

def dashboard(request):
    return render(request, 'dashboard.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        # hash password, 
        hashed_password = make_password(password)
        # Save the user data
        Signup.objects.create(username=username, email=email, phone=phone, password=hashed_password)
        # For Checking
        print('User name', username)
        print('Email', email)
        print('Phone', phone)
    
        return redirect('login')
    return render(request, 'signup.html')

def login(request):

    return render(request, 'login.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')