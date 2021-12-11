from django.contrib import admin
from django.urls import path
from .views import LoginView, LogoutView, RegisterView, UserProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='api-register'),
    path('login/', LoginView.as_view(), name='api-login'),
    path('user/', UserProfileView.as_view(), name='api-user'),    
    #path('logout/', LogoutView.as_view()),
]
