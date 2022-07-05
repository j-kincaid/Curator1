from django.contrib import admin
from .models import Artwork, Comment, Tag
from . import models

class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('artwork_title',)

admin.site.register(models.Artwork, ArtworkAdmin)