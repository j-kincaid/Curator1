from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
import uuid

# within entries each artwork is a Model. It is stored in the database in the entries application.


class Artwork(models.Model):
    artwork_title = models.CharField(max_length=200)
    MEDIA = (
        ("Painting", "PAINTING"),
        ("Sculpture", "SCULPTURE"),
        ("Photography", "PHOTO"),
        ("Ceramic", "CERAMIC"),
        ("Textile", "TEXTILE"),
        ("Print", "PRINT"),
        ("Digital", "DIGITAL"),
        (
            "Other",
            "OTHER",
        ),
    )
    # Each Artwork has the properties that will display in the form:
    medium = models.CharField(max_length=20, null=True, choices=MEDIA)
    height_in_feet = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    height_in_inches = models.DecimalField(
        max_digits=5, decimal_places=2, default="inches"
    )
    width_in_inches = models.DecimalField(
        max_digits=5, decimal_places=2, default="inches"
    )
    depth_in_inches = models.DecimalField(
        max_digits=5, decimal_places=2, default="inches"
    )
    year_completed = models.IntegerField(default=2022)

    def __str__(self):
        return self.artwork_title

    def get_absolute_url(self):
        return reverse("entries.detail", kwargs={"pk": self.pk})


class Artist(models.Model):
    full_name = models.CharField(max_length=200)
    pronouns = models.CharField(max_length=200)
    bio = models.TextField()
    pub_date = models.DateTimeField("date published")
    artworks = models.ManyToManyField("Artwork", blank=True)

    def __str__(self):
        return self.full_name


class Comment(models.Model):
    artworks = models.ManyToManyField("Artwork", blank=True)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return self.value


class Tag(models.Model):
    artwork = models.ForeignKey("Artwork", null=True, on_delete=models.CASCADE)
    entry_score_1_to_5 = models.DecimalField(default=0, max_digits=1, decimal_places=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
