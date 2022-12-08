from django.contrib import admin

from . import models

from .models import Review, Tag


class ArtworkAdmin(admin.ModelAdmin):
    list_display = ("artwork_title",)


admin.site.register(models.Artwork, ArtworkAdmin)
admin.site.register(Review)
admin.site.register(Tag)
