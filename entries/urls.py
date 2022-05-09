from django.urls import path

from . import views


urlpatterns = [
    path('entries', views.EntriesListView.as_view(), name="entries.list"),
    path('entries/<int:pk>', views.EntriesDetailView.as_view(), name="entries.detail"),
    path('entries/new', views.EntriesCreateView.as_view(), name="notes.new"),
]