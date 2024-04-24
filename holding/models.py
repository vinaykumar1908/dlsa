from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

class Loco2(models.Model):
    WAGON_TYPE_CHOICES = ( 
        ("SelectLoco", "Please Select Loco Type"),  
        ("WDG4", "WDG4"),
        ("WDG4D", "WDG4D"),
        ("WDP4", "WDP4"),
        ("WDP4D", "WDP4D"),
        ("WDP4B","WDP4B"),
        ("WDM3", "WDM3"), 
        ("WDM3D", "WDM3D"),
        ("WDM3A", "WDM3A"),
        ("WDG3A", "WDG3A"),
        ("WDS6", "WDS6"),
        ("WAP1", "WAP1"),
        ("WAG7", "WAG7"),
        ("WAG5", "WAG5"),
        ("WAG11", "WAG11"),
        ("WDS6AD", "WDS6AD"),
    ) 

    
    RecordCreationDate = models.DateTimeField(default=timezone.now, null=True)
    LocoNumber = models.IntegerField(null=True, blank=True)
    LocoType = models.CharField(
        max_length=11, choices=WAGON_TYPE_CHOICES, default='SelectLoco', null=True, blank=True)
    LocoCommDate = models.DateField(null=True, )
    LocoFailed = models.BooleanField(default=False, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    LocoFile = models.FileField(upload_to='Loco/%Y/%m/%d/', blank=True, null=True)

    
    def get_absolute_url(self):
        return reverse('Modules_detail', kwargs={'pk': self.pk})

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='locoauth1')
    def __str__(self):
        return str(self.LocoNumber)