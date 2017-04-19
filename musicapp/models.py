from django.db import models
import json
import os.path
from decimal import Decimal
from django.contrib.auth.models import User

# Create your models here.

class Genres(models.Model):
    name = models.CharField(max_length=200, default=0, null=True, blank=True)
    genre = models.CharField(max_length=200, default=0, null=True, blank=True)

class Music(models.Model):
    title = models.CharField(max_length=200, default=0, null=True, blank=True)
    genres = models.ForeignKey(Genres, related_name='genres',null=True,blank=True)
    rating = models.CharField(max_length=300, default=0, null=True, blank=True)




