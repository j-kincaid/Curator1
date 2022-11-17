# from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    # path('admin', admin.site.urls),
    path('', include('votes')), 
    path("", views.HomeView.as_view(), name="home"),
    path("login", views.LoginInterfaceView.as_view(), name="login"),
    path("logout", views.LogoutInterfaceView.as_view(), name="logout"),
    path("register", views.SignupView.as_view(), name="register"),
    path("votes", views.IndexView.as_view(), name="votes"),
]
