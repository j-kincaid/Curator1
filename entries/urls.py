from django.urls import path

from . import views


urlpatterns = [
    path('entries', views.EntriesListView.as_view(), name="entries.list"),
    path('entries/<int:pk>', views.EntriesDetailView.as_view(), name="entries.detail"),
    path('entries/form/', views.EntriesCreateView.as_view(), name='entries.form'),
    path('entries/<int:pk>/update_form', views.EntriesUpdateView.as_view(), name='entries.update'),
    path('entries/<int:pk>/delete/', views.EntriesDeleteView.as_view(), name='entries.confirm_delete'),
    ]