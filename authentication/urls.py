from django.contrib import admin
from django.urls import path
from .views import LoginView, LogoutView, RegisterView, UserProfileView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('user/', UserProfileView.as_view()),    
    #path('logout/', LogoutView.as_view()),
]
