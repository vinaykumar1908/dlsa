
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
import datetime
from datetime import timedelta, date

from holding.models import Loco2
from django.utils import timezone
@login_required
def holdingA(request):
    qs = Loco2.objects.filter(Q(LocoType='WDM3A') | Q(LocoType='WDM3D') | Q(LocoType='WDG3A') | Q(LocoType='WDS6') | Q(LocoType='WDS6AD')).order_by('LocoNumber')   
    timerightnow = timezone.now()

    context = {
         'time' : timerightnow,
         'holding' : qs,
         'Type' : "Alco",

    }
    return render(request, 'holding/holding.html', context)



@login_required
def holdingH(request):
    #qs = Loco2.objects.filter(Q(LocoType='WDM3A') | Q(LocoType='WDM3D') | Q(LocoType='WDG3A') | Q(LocoType='WDS6') | Q(LocoType='WDS6AD'))
    qs2 = Loco2.objects.filter(Q(LocoType='WDG4') | Q(LocoType='WDG4D') | Q(LocoType='WDP4B') | Q(LocoType='WDP4D')).order_by('LocoNumber')
    #qs3 = Loco2.objects.filter(Q(LocoType='WAP1') | Q(LocoType='WAG5') | Q(LocoType='WAG7'))   
    timerightnow = timezone.now()

    context = {
         'time' : timerightnow,
         'holding' : qs2,
         'Type' : "HHP",

    }
    return render(request, 'holding/holding.html', context)

@login_required
def holdingE(request):
    #qs = Loco2.objects.filter(Q(LocoType='WDM3A') | Q(LocoType='WDM3D') | Q(LocoType='WDG3A') | Q(LocoType='WDS6') | Q(LocoType='WDS6AD')).count()
    #qs2 = Loco2.objects.filter(Q(LocoType='WDG4') | Q(LocoType='WDG4D') | Q(LocoType='WDP4B') | Q(LocoType='WDP4D')).count()
    qs3 = Loco2.objects.filter(Q(LocoType='WAP1') | Q(LocoType='WAG5') | Q(LocoType='WAG7')).order_by('LocoNumber')
    timerightnow = timezone.now()

    context = {
         'time' : timerightnow,
         'holding' : qs3,
         'Type' : "Electrical",

    }
    return render(request, 'holding/holding.html', context)