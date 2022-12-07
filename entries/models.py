import uuid

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

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

    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.artwork_title

    def get_absolute_url(self):
        return reverse("entries.detail", kwargs={"pk": self.pk})


# class Artist(models.Model):
#     full_name = models.CharField(max_length=200)
#     pronouns = models.CharField(max_length=200)
#     bio = models.TextField()
#     pub_date = models.DateTimeField("date published")
#     artworks = models.ManyToManyField("Artwork", blank=True)

#     def __str__(self):
#         return self.full_name


# class Comment(models.Model):
#     artworks = models.ManyToManyField("Artwork", blank=True)
#     body = models.TextField(null=True, blank=True)
#     value = models.CharField(max_length=500)
#     pub_date = models.DateTimeField(auto_now_add=True)
#     id = models.UUIDField(
#         default=uuid.uuid4, unique=True, primary_key=True, editable=False
#     )

#     def __str__(self):
#         return self.value

class Review(models.Model):
    VOTE_TYPE = (
        ('poor', 1),
        ('fair', 2),
        ('good', 3),
        ('excellent', 4),
        ('sublime', 5),  
    )
    # owner = 
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.value

# Use Tag to create a Many to Many relationship. It connects the Artworks with the votes they receive.

class Tag(models.Model):
    name = models.CharField(max_length=200, default="default")
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name
