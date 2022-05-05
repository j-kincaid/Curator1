from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

# Each Artwork is related to a single artist. 
class Artwork(models.Model):
    # artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    # votes = models.IntegerField(default=0)
    artwork_title = models.CharField(max_length=200)
    artwork_medium = models.CharField(max_length=200, default="ex. Fiber")
    # tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_average = models.IntegerField(default=0, null=True, blank=True)
    height_in_inches = models.DecimalField(max_digits=5, decimal_places=2, default="inches")
    width_in_inches = models.DecimalField(max_digits=5, decimal_places=2, default="inches")
    depth_in_inches = models.DecimalField(max_digits=5, decimal_places=2, default="inches")
    year_completed = models.IntegerField(default=0)
    # The following line produced a ValueError "badly formed hexadecimal UUID string"
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.artwork_title


# class Artist(models.Model):
#     full_name = models.CharField(max_length=200)
#     pronouns = models.CharField(max_length=200)
#     bio = models.TextField()
#     pub_date = models.DateTimeField('date published')
#     def __str__(self):
#         return self.full_name

# Trying to add this subclass as per docs unsuccessful 4/24/22 2:31PM

    # class Medium(models.TextChoices):
    #     PAINTING = 'PA', _('Painting')
    #     SCULPTURE = 'SC', _('Sculpture')
    #     PHOTOGRAHY = 'PH', _('Photography')
    #     CERAMIC = 'CE', _('Ceramic')
    #     TEXTILE = 'TX', _('Textile')
    #     PRINT = 'PT', _('Print')
    #     DIGITAL = 'DG', _('Digital')
    #     OTHER = 'OT', _('Other')

class Comment(models.Model):
    # artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    # panelist =

    artworks = models.ManyToManyField('Artwork', blank=True)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
           return self.value

class Tag(models.Model):
    artwork = models.ForeignKey(Artwork, null=True, on_delete=models.CASCADE)
    entry_score_1_to_5 = models.DecimalField(default=0, max_digits=1, decimal_places=0)
    pub_date = models.DateTimeField('date published')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    




    