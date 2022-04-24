from django.db import models
from django.utils.translation import gettext_lazy as _


class Artist(models.Model):
    full_name = models.CharField(max_length=200)
    pronouns = models.CharField(max_length=200)
    bio = models.TextField()
    pub_date = models.DateTimeField('date published')

# Each Artwork is related to a single artist. 
class Artwork(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    artwork_title = models.CharField(max_length=200)
    artwork_medium = models.CharField(max_length=200, default="ex. Fiber")
    height_in_inches = models.DecimalField(max_digits=5, decimal_places=2, default="inches")
    width_in_inches = models.DecimalField(max_digits=5, decimal_places=2, default="inches")
    depth_in_inches = models.DecimalField(max_digits=5, decimal_places=2, default="inches")
    year_completed = models.IntegerField(default=0)


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
    