from django.shortcuts import render

from .models import Artwork


def list(request):
    all_artworks = Artwork.objects.all()
    return render(request, 'entries/entries_list.html', {'entries': all_artworks})
