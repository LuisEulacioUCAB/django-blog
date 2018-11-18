from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView, AuthenticationForm

urlpatterns = [
    path('user/register/', views.RegisterUser.as_view(), name = "register"),
    path('user/user_valid/', views.valid_username, name = "valid-username"),
    path('user/', LoginView.as_view(), name = "login"),
    path('user/logout', LogoutView.as_view(), name = "logout"),
]