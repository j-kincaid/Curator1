from django.urls import path

from . import views

urlpatterns = [
    path('entries', views.list),
    path('entries/<int:pk>', views.detail),
]