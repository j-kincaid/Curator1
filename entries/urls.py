from django.urls import path

from entries.views import EntriesListView, EntriesDetailView, EntriesCreateView, EntriesUpdateView, EntriesDeleteView

urlpatterns = [
    path('entries', EntriesListView.as_view(), name="entries.list"),
    path('entries/<int:pk>', EntriesDetailView.as_view(), name="entries.detail"),
    path('entries/form/', EntriesCreateView.as_view(), name='entries.form'),
    path('entries/<int:pk>/edit', EntriesUpdateView.as_view(), name='entries.edit'),
    path('entries/<int:pk>/delete/', EntriesDeleteView.as_view(), name='entries.delete'),
]