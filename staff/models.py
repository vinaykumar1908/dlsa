from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from section.models import Section


class Staff(models.Model):
    Desig_TYPE_CHOICES = ( 
        ("SelectDesig", "Please Select Designation "),  
        ("Tech-1", "Tech-1"),
        ("Tech-2", "Tech-2"),
        ("Tech-3", "Tech-3"),
        ("Sr.Tech", "Sr.Tech"),
        ("MCM","MCM"),
        ("JE", "JE"), 
        ("SSE", "SSE"),
        
    ) 

    
    StaffName = models.CharField(max_length=100)
    TokenNumber = models.IntegerField(null=True, blank=True)
    Designation = models.CharField(
        max_length=11, choices=Desig_TYPE_CHOICES, default='SelectDesig', null=True, blank=True)
    DOB = models.DateField(null=True)
    Section = models.ForeignKey(Section, on_delete=models.CASCADE,null=True, blank=True, related_name='StaffSection')
    StaffFile = models.FileField(upload_to='Staff/%Y/%m/%d/', blank=True, null=True)
    StaffMobileNumber = models.IntegerField(null=True, blank=True)
    Staffimage = models.ImageField(default='default.jpg', upload_to='staff_profile_pics')

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='staffauth1')
    def __str__(self):
        return str(self.StaffName)
    

