from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from holding.models import Loco2

class Card(models.Model):
    WAGON_TYPE_CHOICES = ( 
        ("SelectSchedule", "Please Select Schedule / OOC "),  
        ("IOH", "IOH"),
        ("POH", "POH"),
        ("TOH", "TOH"),
        ("MTR", "MTR"),
        ("Y1","Y1"),
        ("Y2", "Y2"), 
        ("3Y", "3Y"),
        ("Y4", "Y4"),
        ("Y5", "Y5"),
        ("6Y", "6Y"),
        ("Alco-M12", "Alco-M12"),
        ("Alco-M18", "Alco-M18"),
        ("Alco-M24", "Alco-M24"),
        ("Alco-M30", "Alco-M30"),
        ("Alco-M36", "Alco-M36"),
        ("Alco-M72", "Alco-M72"),
        ("Alco-M108", "Alco-M108"),
        ("IA1", "IA1"),
        ("IB", "IB"),
        ("IA2", "IA2"),
        ("IC", "IC"),
        ("HHP-30D", "HHP-30D"),
        ("HHP-90D", "HHP-90D"),
        ("HHP-180D", "HHP-180D"),
        ("Alco-Trip(30D)", "Alco-Trip(30D)"),
        ("Alco-M(60D)", "Alco-M(60D)"),
        ("Alco-M2(120D)", "Alco-M2(120D)"),
        ("Alco-M6(180D)", "Alco-M6(180D)"),
        ("OOC", "OOC"),
    ) 
    MajorSchedule1 = models.CharField(
        max_length=20, choices=WAGON_TYPE_CHOICES, default='SelectSchedule', null=True, blank=True)
    MajorSchedule1Date = models.DateTimeField(blank=True, null=True)
    MajorSchedule2 = models.CharField(
        max_length=20, choices=WAGON_TYPE_CHOICES, default='SelectSchedule', null=True, blank=True)
    MajorSchedule2Date = models.DateTimeField(blank=True, null=True)
    MajorSchedule3 = models.CharField(
        max_length=20, choices=WAGON_TYPE_CHOICES, default='SelectSchedule', null=True, blank=True)
    MajorSchedule3Date = models.DateTimeField(blank=True, null=True)
    MajorSchedule4 = models.CharField(
        max_length=20, choices=WAGON_TYPE_CHOICES, default='SelectSchedule', null=True, blank=True)
    MajorSchedule4Date = models.DateTimeField(blank=True, null=True)
    MajorSchedule5 = models.CharField(
        max_length=20, choices=WAGON_TYPE_CHOICES, default='SelectSchedule', null=True, blank=True)
    MajorSchedule5Date = models.DateTimeField(blank=True, null=True)
    MajorSchedule6 = models.CharField(
        max_length=20, choices=WAGON_TYPE_CHOICES, default='SelectSchedule', null=True, blank=True)
    MajorSchedule6Date = models.DateTimeField(blank=True, null=True)
    MajorSchedule7 = models.CharField(
        max_length=20, choices=WAGON_TYPE_CHOICES, default='SelectSchedule', null=True, blank=True)
    MajorSchedule7Date = models.DateTimeField(blank=True, null=True)
    MajorSchedule8 = models.CharField(
        max_length=20, choices=WAGON_TYPE_CHOICES, default='SelectSchedule', null=True, blank=True)
    MajorSchedule8Date = models.DateTimeField(blank=True, null=True)
    MajorSchedule9 = models.CharField(
        max_length=20, choices=WAGON_TYPE_CHOICES, default='SelectSchedule', null=True, blank=True)
    MajorSchedule9Date = models.DateTimeField(blank=True, null=True)
    MajorSchedule10 = models.CharField(
        max_length=20, choices=WAGON_TYPE_CHOICES, default='SelectSchedule', null=True, blank=True)
    MajorSchedule10Date = models.DateTimeField(blank=True, null=True)
    MajorSchedule11 = models.CharField(
        max_length=20, choices=WAGON_TYPE_CHOICES, default='SelectSchedule', null=True, blank=True)
    MajorSchedule11Date = models.DateTimeField(blank=True, null=True)
    RecordCreationDate = models.DateTimeField(default=timezone.now, null=True)
    DateOfArrival = models.DateTimeField(default=timezone.now, null=True)
    LocoNumber = models.OneToOneField(Loco2, on_delete=models.CASCADE)
    LocoCardFile = models.FileField(upload_to='LocoCardFile/%Y/%m/%d/', blank=True, null=True)    
    def get_absolute_url(self):
        return reverse('Modules_detail', kwargs={'pk': self.pk})
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='cardauth1')
    def __str__(self):
        return str(self.LocoNumber)