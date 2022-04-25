from django.urls import path

from . import views

urlpatterns = [
    path('entries', views.EntriesListView.as_view()),
    path('entries/<int:pk>', views.EntriesDetailView.as_view()),
]