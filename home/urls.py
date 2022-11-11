from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("login", views.LoginInterfaceView.as_view(), name="login"),
    path("logout", views.LogoutInterfaceView.as_view(), name="logout"),
    path("register", views.SignupView.as_view(), name="register"),
    path("votes", views.IndexView.as_view(), name="votes"),
]
