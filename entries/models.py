import uuid

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# within entries each artwork is a Model. It is stored in the database in the entries application.


class Artwork(models.Model):
    artwork_title = models.CharField(max_length=200)
    featured_image = models.ImageField(
        null=True, blank=True, default="default_image.jpg"
    )
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

    description = models.TextField(null=True, blank=True)

    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField("Tag", blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.artwork_title

    def get_absolute_url(self):
        return reverse("entries.detail", kwargs={"pk": self.pk})


class Review(models.Model):
    STARS = (
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
    )
    votes = models.IntegerField(default=0)
    # owner =
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=STARS)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return self.value


# Use Tag to create a Many to Many relationship. It connects the Artworks with the votes they receive.


class Tag(models.Model):
    name = models.CharField(max_length=200, default="default")
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return self.name
