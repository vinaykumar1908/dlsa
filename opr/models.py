from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from staff.models import Staff
from holding.models import Loco2


class OPR(models.Model):
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

    
    Date = models.DateTimeField(default=timezone.now, null=True)
    LocoFailureDate = models.DateTimeField(default=timezone.now, null=True)
    LocoNumber = models.ForeignKey(Loco2, on_delete=models.CASCADE, null=True, related_name='OPRLocoNumber')
    Div = models.CharField(max_length=4, blank=True, null=True)
    Railway = models.CharField(max_length=4, blank=True, null=True)
    Train = models.CharField(max_length=15, blank=True, null=True)
    LocoType = models.CharField(
        max_length=11, choices=WAGON_TYPE_CHOICES, default='SelectLoco', null=True, blank=True)
    Shed = models.CharField(max_length=6, blank=True, null=True)
    Load = models.CharField(max_length=30, blank=True, null=True)
    Site = models.CharField(max_length=30, blank=True, null=True)
    Section = models.CharField(max_length=6, blank=True, null=True)
    detantion_time = models.DurationField(null=True, default='[1] [[00:]00:]00')
    LPName = models.CharField(max_length=50, blank=True, null=True)
    LPHQ = models.CharField(max_length=6, blank=True, null=True)
    LPCUG = models.CharField(max_length=12, blank=True, null=True)
    LPExp = models.CharField(max_length=40, blank=True, null=True)
    NCLI = models.CharField(max_length=50, blank=True, null=True)
    LICUG = models.CharField(max_length=6, blank=True, null=True)
    RelLocoNo = models.CharField(max_length=6, blank=True, null=True)
    FailedLocoMove = models.CharField(max_length=6, blank=True, null=True)
    SupChk1 = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True, related_name='Supchk1')
    SupChk2 = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True, related_name='Supchk2')
    FailedItem2 = models.CharField(max_length=6, blank=True, null=True)
    SuspectedCauseOfFailure = models.CharField(max_length=400, blank=True, null=True)
    LastFitOfFailedItem = models.CharField(max_length=400, blank=True, null=True)
    HistoryOfSimilarFailure = models.CharField(max_length=100, blank=True, null=True)
    SuspectedItemLastAttendedInShed = models.CharField(max_length=400, blank=True, null=True)
    MakeOfSuspectedItem = models.CharField(max_length=400, blank=True, null=True)
    CodalLifeOfFailureItem = models.DurationField(null=True, default='[1] [[00:]00:]00')
    FunctionOfThisItem = models.CharField(max_length=400, blank=True, null=True)
    Responsibility = models.CharField(max_length=400, blank=True, null=True)
    DisciplinaryAction = models.CharField(max_length=400, blank=True, null=True)
    ActionTakenToAvoidInFuture = models.CharField(max_length=400, blank=True, null=True)
    CLIReport = models.FileField(upload_to='OPRCLIReport/%Y/%m/%d/', blank=True, null=True)
    FailureAvoidable = models.BooleanField(default=False, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    FailLocoFile = models.FileField(upload_to='FailLocoFile/%Y/%m/%d/', blank=True, null=True)
    LocoFailureDetails = models.CharField(max_length=2000, blank=True, null=True)
    
    
    def get_absolute_url(self):
        return reverse('Modules_detail', kwargs={'pk': self.pk})

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='oprAuth1')
    def __str__(self):
        return str(self.LocoNumber)