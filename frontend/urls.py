from django.contrib import admin
from django.urls import path
from .views import LoginView, LandingView, RegisterView, ProfileView
from django.shortcuts import redirect

urlpatterns = [
    path('', LandingView, name='landing'),
    path('register/', RegisterView, name='register'),
    path('login/', LoginView, name='login'),
    path('profile/', ProfileView, name='profile'),

]
