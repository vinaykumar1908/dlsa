from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from section.models import Section
from repair.models import RepairDetail

class MatNeededInLoco(models.Model):
    RecordCreationDate = models.DateTimeField(default=timezone.now, null=True)
    ReceiptDate = models.DateTimeField( null=True)
    MaterialName = models.CharField(null=True, blank=True, max_length=50)
    Quantity = models.IntegerField(null=True, blank=True)
    ForJob = models.ForeignKey(RepairDetail, on_delete=models.CASCADE, null=True)
    FromSection = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)
    MaterialReceived = models.BooleanField(default=False, blank=True)
    MaterialFile = models.FileField(upload_to='Loco/%Y/%m/%d/', blank=True, null=True)

    
    def get_absolute_url(self):
        return reverse('Modules_detail', kwargs={'pk': self.pk})
    

    def save2MatRec(self, *args, **kwargs):
        self.MaterialReceived = True
        self.ReceiptDate = timezone.now()
        super().save(*args, **kwargs)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='matneededauth1')
    def __str__(self):
        return str(f"{self.MaterialName} for {self.ForJob}")