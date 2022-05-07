from django.contrib import admin
from .models import Artwork, Comment, Tag
from . import models

class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('artwork_title',)

# class ArtistAdmin(admin.ModelAdmin):
#     list_display = ('full_name',)

admin.site.register(models.Artwork, ArtworkAdmin)
# admin.site.register(models.Artist)
# admin.site.register(models.Comment)
# admin.site.register(models.Tag)