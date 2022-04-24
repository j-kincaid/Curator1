from django.contrib import admin
from .models import Artist, Artwork
from . import models

class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('artwork_title',)

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

admin.site.register(models.Artist, ArtistAdmin)
admin.site.register(models.Artwork, ArtworkAdmin)