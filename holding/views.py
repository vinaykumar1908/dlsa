
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
import datetime
from datetime import timedelta, date
# # Create your views here.
# from django.shortcuts import render
# from django.db.models import Q
# # Create your views here.
# from django.shortcuts import render
# from django.views.generic import TemplateView, ListView, DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
from holding.models import Loco2
# #from sidingz import models as ZM
# from django.urls import reverse_lazy
# from django.db import models
# import math

# from itertools import filterfalse
# #from .forms import registerStockRecievedForm, registerStockDispatchROHform, registerStockDispatchSicklineform, registerStockDispatchedYardform, registerStockDispatchedTrainDutyform
from django.utils import timezone
# # Create your views here.
# from django.contrib.auth.decorators import login_required

# from django.db.models import Avg, Sum
# from defi.models import DPC, TC, MC, DPCArea, DPCRemark, MCArea, MCRemark, TCArea, TCRemark, Status
@login_required
def holdingA(request):
    qs = Loco2.objects.filter(Q(LocoType='WDM3A') | Q(LocoType='WDM3D') | Q(LocoType='WDG3A') | Q(LocoType='WDS6') | Q(LocoType='WDS6AD')).order_by('LocoNumber')
    #qs2 = Loco2.objects.filter(Q(LocoType='WDG4') | Q(LocoType='WDG4D') | Q(LocoType='WDP4B') | Q(LocoType='WDP4D')).count()
    #qs3 = Loco2.objects.filter(Q(LocoType='WAP1') | Q(LocoType='WAG5') | Q(LocoType='WAG7'))   
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