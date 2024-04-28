from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from section.models import Section
from repair.models import RepairDetail


class Locations(models.Model):
    LocationName = models.CharField( max_length=50, unique=True)
    def __str__(self):
        return str(self.LocationName)


class ShuntingNeededInLoco(models.Model):
    RecordCreationDate = models.DateTimeField(default=timezone.now, null=True)
    CompletionDate = models.DateTimeField( blank=True, null=True)
    From = models.ForeignKey(Locations, on_delete=models.CASCADE, null=True, related_name='shuntfrom')
    To = models.ForeignKey(Locations, on_delete=models.CASCADE, null=True, related_name='shuntto')
    ForJob = models.ForeignKey(RepairDetail, on_delete=models.CASCADE, null=True)
    ShuntingStatus = models.BooleanField(default=False, blank=True)
    ShuntingFile = models.FileField(upload_to='Loco/%Y/%m/%d/', blank=True, null=True)

    
    def get_absolute_url(self):
        return reverse('Modules_detail', kwargs={'pk': self.pk})
    
    

    def save2MatRec(self, *args, **kwargs):
        self.ShuntingStatus = True
        self.CompletionDate = timezone.now()
        super().save(*args, **kwargs)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='shuntauth1')
    def __str__(self):
        return str(f"From {self.From} To {self.To} for {self.ForJob}")