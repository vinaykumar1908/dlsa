
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
from material.models import MatNeededInLoco
from staff.models import Staff
from holding.models import Loco2
from shunting.models2 import ShuntingNeededInLoco1
from repair.models import ShedIn, RepairDetail, ManNeededInLoco
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
def homeView(request):
     this_month = datetime.datetime.now().month
     qs = Loco2.objects.filter(Q(LocoType='WDM3A') | Q(LocoType='WDM3D') | Q(LocoType='WDG3A') | Q(LocoType='WDS6') | Q(LocoType='WDS6AD'))
     qs2 = Loco2.objects.filter(Q(LocoType='WDG4') | Q(LocoType='WDG4D') | Q(LocoType='WDP4B') | Q(LocoType='WDP4D'))
     qs3 = Loco2.objects.filter(Q(LocoType='WAP1') | Q(LocoType='WAG5') | Q(LocoType='WAG7'))    
     timerightnow = timezone.now()
     print(datetime.datetime.now())
     today = date.today()
     print(timerightnow)
     qs4 = RepairDetail.objects.all().filter(created_date__range=[today, timerightnow])
     
     Item = list()
     for h in qs4:
         d = MatNeededInLoco.objects.all().filter(ForJob=h).order_by('RecordCreationDate')
         r = ShuntingNeededInLoco1.objects.all().filter(ForJob=h).order_by('RecordCreationDate')
         c = ManNeededInLoco.objects.all().filter(ForJob=h).order_by('RecordCreationDate')

         place_json = [h, d, r, c]
         Item.append(place_json)
     print(qs4)
     
     shuntinglist = ShuntingNeededInLoco1.objects.all().order_by('-RecordCreationDate')

     context = {
         'a' : qs,
         'time' : timerightnow,
         'b' : qs2,
         'c' : qs3,
         'i' : qs.filter(LocoFailed=False).count(),
         'j' : qs2.filter(LocoFailed=False).count(),
         'k' : qs3.filter(LocoFailed=False).count(),
         'Item' : Item,
         'shuntinglist' : shuntinglist,

        
        
    }
     return render(request, 'home/home.html', context)




@login_required
def BookingDateChecker(request):
     this_month = datetime.datetime.now().month
     qs = Loco2.objects.filter(Q(LocoType='WDM3A') | Q(LocoType='WDM3D') | Q(LocoType='WDG3A') | Q(LocoType='WDS6') | Q(LocoType='WDS6AD'))
     qs2 = Loco2.objects.filter(Q(LocoType='WDG4') | Q(LocoType='WDG4D') | Q(LocoType='WDP4B') | Q(LocoType='WDP4D'))
     qs3 = Loco2.objects.filter(Q(LocoType='WAP1') | Q(LocoType='WAG5') | Q(LocoType='WAG7'))    
     timerightnow = timezone.now()
     print(datetime.datetime.now())
     today = date.today()
     if request.method=='POST':
        date1 = request.POST.get('From')
        date2 = request.POST.get('To')
        print(date1)
        print(date2)
        qs4 = RepairDetail.objects.all().filter(created_date__range=[date1, date2])
     Item = list()
     for h in qs4:
         d = MatNeededInLoco.objects.all().filter(ForJob=h).order_by('RecordCreationDate')
         r = ShuntingNeededInLoco1.objects.all().filter(ForJob=h).order_by('RecordCreationDate')
         c = ManNeededInLoco.objects.all().filter(ForJob=h).order_by('RecordCreationDate')

         place_json = [h, d, r, c]
         Item.append(place_json)
     print(qs4)
     shuntinglist = ShuntingNeededInLoco1.objects.all().order_by('RecordCreationDate')
     context = {
         'a' : qs,
         'time' : timerightnow,
         'b' : qs2,
         'c' : qs3,
         'i' : qs.filter(LocoFailed=False).count(),
         'j' : qs2.filter(LocoFailed=False).count(),
         'k' : qs3.filter(LocoFailed=False).count(),
         'Item' : Item,
         'shuntinglist' : shuntinglist,

        
        
        
    }
     return render(request, 'home/home.html', context)