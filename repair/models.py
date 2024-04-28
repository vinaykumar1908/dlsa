from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from holding.models import Loco2
from section.models import Section
class ShedIn(models.Model):
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
    RepairType = models.CharField(
        max_length=20, choices=WAGON_TYPE_CHOICES, default='SelectSchedule', null=True, blank=True)
    LocoNumber = models.ForeignKey(Loco2, on_delete=models.CASCADE, null=True, related_name='ecomments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='fcomments')
    LocoFile = models.FileField(upload_to='LocoShedIn/%Y/%m/%d/', blank=True, null=True)
    ShedInDate = models.DateTimeField(blank=True, null=True)
    workComplete = models.BooleanField(default=False)
    ShedOut = models.BooleanField(default=False)
    ShedOutDate = models.DateTimeField(blank=True, null=True)
    ShedIn = models.BooleanField(default=False)
    LocoFailDate = models.DateTimeField(blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse('Modules_detail', kwargs={'pk': self.pk})

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='locoauth14')
    def __str__(self):
        return str(self.LocoNumber)
    def approved_comments(self):
        return self.ccomments.filter(approved_comment=True)
    

class RepairSection(models.Model):
    Date = models.DateTimeField(blank=True, null=True)
    LocoNumber = models.ForeignKey(ShedIn, on_delete=models.CASCADE, related_name='ccomments')
    RepSection = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, related_name='dcomments')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='locoauth15')
    approved_comment = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.LocoNumber}{self.RepSection}{self.Date}"
    def save(self, *args, **kwargs):
        Date = self.LocoNumber.ShedInDate
        d = Date
        print(d)
        #Date = getattr(Date, 'ShedInDate')
        print(Date)
        self.Date = str(d)
        super(RepairSection, self).save(*args, **kwargs)

    


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def approved_comments(self):
        return self.bcomments.filter(approved_comment=True)
    def approve(self):
        self.approved_comment = True
        self.save()
    

class RepairDetail(models.Model):
    RepSection = models.ForeignKey(RepairSection, on_delete=models.CASCADE, related_name='bcomments')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='RepDetAuth16')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    waitingForShunting = models.BooleanField(default=False)
    waitingForMaterial = models.BooleanField(default=False)
    waitingForSA= models.BooleanField(default=False)
    MaterialNeeded = models.CharField(max_length=400, blank=True, null=True)
    SANeeded = models.CharField(max_length=400, blank=True, null=True)
    ShuntingNeeded = models.CharField(max_length=400, blank=True, null=True)
    workComplete = models.BooleanField(default=False)
    RepairDetailFile = models.FileField(upload_to='RepairFile/%Y/%m/%d/', blank=True, null=True)
    WorkStartDateTime = models.DateTimeField(blank=True, null=True)
    WorkEndDateTime = models.DateTimeField(blank=True, null=True)
    def save(self, *args, **kwargs):
        Date = self.RepSection.Date
        d = Date
        
        self.Date = str(d)
        super(RepairDetail, self).save(*args, **kwargs)
    def approve(self):
        self.approved_comment = True
        self.save()

    def save2True(self, *args, **kwargs):
        self.waitingForMaterial = True
        super(RepairDetail, self).save(*args, **kwargs)

    def saveShunt2True(self, *args, **kwargs):
        self.waitingForShunting = True
        super(RepairDetail, self).save(*args, **kwargs)

    def saveworkcomplete2True(self, *args, **kwargs):
        self.workComplete = True
        super(RepairDetail, self).save(*args, **kwargs)

    

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.RepSection} with date {self.created_date} "