from dataclasses import field
from re import template
from django.shortcuts import render
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Artwork


class EntriesDeleteView(DeleteView):
    model = Artwork
    success_url = reverse_lazy('entries_list')

class EntriesUpdateView(UpdateView):
    model = Artwork
    fields = ['artwork_title', 'medium', 'height_in_inches', 'width_in_inches', 'depth_in_inches', 'year_completed']
    template_name_suffix = '_update'

class EntriesCreateView(CreateView):
    model = Artwork
    template_name = 'entries/entries_new.html'
    fields = ['artwork_title', 'medium', 'height_in_inches', 'width_in_inches', 'depth_in_inches', 'year_completed']
    success_url = '/new'

class EntriesListView(ListView):
    model = Artwork
    context_object_name = "entries"
    template_name = "entries/entries_list.html"

class EntriesDetailView(DetailView):
    model = Artwork
    context_object_name = "entry"
    template_name = "entries/entry_detail.html"

