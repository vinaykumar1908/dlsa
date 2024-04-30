from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings


class Locations(models.Model):
    LocationName = models.CharField( max_length=50, unique=True)
    
    def __str__(self):
        return f'{self.LocationName}'

