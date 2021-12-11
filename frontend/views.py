from django.shortcuts import render, redirect

# Create your views here.

def LandingView(request):
    return render(request, 'frontend/landing.html')

def LoginView(request):
    return render(request, 'frontend/login.html')

def RegisterView(request):
    return render(request, 'frontend/register.html')

def ProfileView(request):
    return render(request, 'frontend/profile.html')