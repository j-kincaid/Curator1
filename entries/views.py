from dataclasses import field
from re import template
from django.shortcuts import render
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView

from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .forms import EntriesForm
from .models import Artwork


class EntriesDeleteView(DeleteView):
    model = Artwork
    success_url = reverse_lazy('entries_list')

class EntriesUpdateView(UpdateView):
    model = Artwork
    fields = ['artwork_title', 'medium']
    template_name_suffix = '_update_form'

class EntriesCreateView(CreateView):
    model = Artwork
    fields = ['artwork_title', 'medium']
    # fields = ['artwork_title', 'medium', 'vote_total', 'vote_average', 'height_in_inches', 'width_in_inches', 'depth_in_inches', 'year_completed']
    # success_url = '/artballot/entries'
    # form_class = EntriesForm
    # template_name = "entries/entries_form.html"
    # context_object_name = "entries"
    
# class EntriesFormView(FormView):
    template_name = 'entries_form.html'
    form_class = EntriesForm

class EntriesListView(ListView):
    model = Artwork
    context_object_name = "entries"
    template_name = "entries/entries_list.html"

class EntriesDetailView(DetailView):
    model = Artwork
    context_object_name = "entry"
    template_name = "entries/entry_detail.html"

