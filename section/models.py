from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings


class Section(models.Model):
    SectionName = models.CharField(max_length=100)
    SectionIncharge = models.ForeignKey("staff.Staff" , on_delete=models.DO_NOTHING)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='sectionauth1')
    def __str__(self):
        return str(self.SectionName)