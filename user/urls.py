
from django.contrib import admin
from django.urls import path
from .views import register_view, login_view, profile_view, logout_view

urlpatterns = [
    path('register/', register_view),
    path('login/', login_view),
    path('profile/', profile_view),
    path('logout/', logout_view),
]
