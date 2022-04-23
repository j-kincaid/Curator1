from django.db import models


class Artist(models.Model):
    full_name = models.CharField(max_length=200)
    pronouns = models.CharField(max_length=200)
    bio = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')

# Each Artwork is related to a single artist. 
class Artwork(models.Model):
    question = models.ForeignKey(Artist, on_delete=models.CASCADE)
    artwork_title = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)