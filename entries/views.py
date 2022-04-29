from typing import List
from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView


from .models import Artwork

class EntriesCreateView(CreateView):
    model = Artwork
    template_name = "entries/entries_form.html"
    context_object_name = "entries"
    
class EntriesListView(ListView):
    model = Artwork
    context_object_name = "entries"
    template_name = "entries/entries_list.html"

class EntriesDetailView(DetailView):
    model = Artwork
    context_object_name = "entry"
    template_name = "entries/entry_detail.html"

