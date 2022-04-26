from typing import List
from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, ListView

from .models import Artwork

class EntriesListView(ListView):
    model = Artwork
    context_object_name = "entries"
    template_name = "entries/entries_list.html"

class EntriesDetailView(DetailView):
    model = Artwork
    context_object_name = "entry"


