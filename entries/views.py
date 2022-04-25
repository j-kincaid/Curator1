from django.shortcuts import render
from django.http import Http404

from .models import Artwork


def list(request):
    all_artworks = Artwork.objects.all()
    return render(request, 'entries/entries_list.html', {'entries': all_artworks})

def detail(request, pk):
    try:
        artwork_title = Artwork.objects.get(pk=pk)
    except Artwork.DoesNotExist:
        raise Http404('That artwork does not exist. Why not create your own?')
    artwork_title = Artwork.objects.get(pk=pk)
    return render(request, 'entries/entry_detail.html', {'entry': artwork_title})
