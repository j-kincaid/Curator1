from django.contrib import admin

from . import models

from .models import Artwork, Review, Tag


class ArtworkAdmin(admin.ModelAdmin):
    list_display = ("artwork_title",)


admin.site.register(models.Artwork, ArtworkAdmin)
admin.site.register(Review)
admin.site.register(Tag)
