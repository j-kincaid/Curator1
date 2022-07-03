from dataclasses import field
from re import template
from django.shortcuts import render
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import ModelForm
from .models import Artwork


class EntriesListView(ListView):
    model = Artwork
    context_object_name = "entries"
    template_name = "entries/entries_list.html"


class EntriesDetailView(DetailView):
    model = Artwork
    context_object_name = "entry"
    template_name = "entries/entries_detail.html"

"""
Using ModelForm for database-driven features. The docs say 'You do not even need to provide a success_url for CreateView or UpdateView - they will use get_absolute_url() on the model object if available'.

"""
class EntriesForm(ModelForm):
    class Meta:
        model = Artwork
        fields = ['artwork_title', 'medium', 'height_in_inches', 'width_in_inches', 'depth_in_inches', 'year_completed']


class EntriesCreateView(CreateView):
    model = Artwork
    template_name = 'entries/entries_form.html'
    fields = ['artwork_title', 'medium', 'height_in_inches', 'width_in_inches', 'depth_in_inches', 'year_completed']


class EntriesUpdateView(UpdateView):
    model = Artwork
    fields = ['artwork_title', 'medium', 'height_in_inches', 'width_in_inches', 'depth_in_inches', 'year_completed']


class EntriesDeleteView(DeleteView):
    model = Artwork
    success_url = reverse_lazy('entries_list')


