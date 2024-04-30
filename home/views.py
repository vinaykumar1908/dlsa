
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

     context = {
         'a' : qs,
         'time' : timerightnow,
         'b' : qs2,
         'c' : qs3,
         'i' : qs.filter(LocoFailed=False).count(),
         'j' : qs2.filter(LocoFailed=False).count(),
         'k' : qs3.filter(LocoFailed=False).count(),
         'Item' : Item,
#         'g' : today,
#         'h' : yesterday,
#         'i' : qs7,
#         'j' : qs8,
#         'k' : qs9,
#         'l' : qs10,
#         'm' : qs11,
#         'n' : qs12,
#         'o' : qs13,
#         'p' : qs14,
#         'q' : qs15,
#         'r' : qs16,
#         's' : qs17,
#         't' : qs18,
#         'u' : qs19,
#         'v' : qs20,
#         'w' : qs21,
        
        
        
    }
     return render(request, 'home/home.html', context)
#     qs2 = TC.objects.all().count()
#     qs3 = MC.objects.all().count()
#     qs4 = DPCRemark.objects.all().count()
#     qs5 = TCRemark.objects.all().count()
#     qs6 = MCRemark.objects.all().count()
#     qs7 = DPCArea.objects.all().count()
#     qs8 = TCArea.objects.all().count()
#     qs9 = MCArea.objects.all().count()
#     mk = Status.objects.get(Status='Attended')
#     print(mk)
#     qs10 = DPCRemark.objects.all().filter(DPCStatus=mk.id).count()
#     qs11 = TCRemark.objects.all().filter(TCStatus=mk.id).count()
#     qs12 = MCRemark.objects.all().filter(MCStatus=mk.id).count()
#     mk2 = Status.objects.get(Status='Not Attended')
#     print(mk2)
#     qs13 = DPCRemark.objects.all().filter(DPCStatus=mk2.id).count()
#     qs14 = TCRemark.objects.all().filter(TCStatus=mk2.id).count()
#     qs15 = MCRemark.objects.all().filter(MCStatus=mk2.id).count()
#     mk3 = Status.objects.get(Status='Material Not Available')
#     print(mk3)
#     qs16 = DPCRemark.objects.all().filter(DPCStatus=mk3.id).count()
#     qs17 = TCRemark.objects.all().filter(TCStatus=mk3.id).count()
#     qs18 = MCRemark.objects.all().filter(MCStatus=mk3.id).count()
#     mk4 = Status.objects.get(Status='Temporarily Attended')
#     print(mk4)
#     qs19 = DPCRemark.objects.all().filter(DPCStatus=mk4.id).count()
#     qs20 = TCRemark.objects.all().filter(TCStatus=mk4.id).count()
#     qs21 = MCRemark.objects.all().filter(MCStatus=mk4.id).count()
        

#     #qs1 = RM.Rake.objects.all()

#     today = date.today()
#     yesterday = date.today() - timedelta(days=1)

#     #qs2 = CCDetails.objects.filter(Date__gt=today, Date__lt=timezone.now())
#     #qs3 = STRDetails.objects.filter(Date__gt=today, Date__lt=timezone.now())
#     #qs4 = CCDetails.objects.filter(Date__gt=yesterday, Date__lt=today)
#     #qs5 = STRDetails.objects.filter(Date__gt=yesterday, Date__lt=today)
#     #qs6 = CCDetails.objects.filter(Date__gt=yesterday, Date__lt=today)
#     #qs6 = qs2.filter(PostExamDetails=True)
#     #qs7 = STRDetails.objects.filter(Date__gt=yesterday, Date__lt=today)
#     #qs7 = qs3.filter(PostExamDetails=True)
#     #qs8 = CCDetails.objects.filter(Date__gt=yesterday, Date__lt=today).filter(PostExamDetails=True)
#     #qs9 = STRDetails.objects.filter(Date__gt=yesterday, Date__lt=today).filter(PostExamDetails=True)
#     #a = qs2.aggregate(Avg('MechanicalDetention'))
#     #b = qs2.aggregate(Sum('TrafficDetention'))





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

     context = {
         'a' : qs,
         'time' : timerightnow,
         'b' : qs2,
         'c' : qs3,
         'i' : qs.filter(LocoFailed=False).count(),
         'j' : qs2.filter(LocoFailed=False).count(),
         'k' : qs3.filter(LocoFailed=False).count(),
         'Item' : Item,
#         'g' : today,
#         'h' : yesterday,
#         'i' : qs7,
#         'j' : qs8,
#         'k' : qs9,
#         'l' : qs10,
#         'm' : qs11,
#         'n' : qs12,
#         'o' : qs13,
#         'p' : qs14,
#         'q' : qs15,
#         'r' : qs16,
#         's' : qs17,
#         't' : qs18,
#         'u' : qs19,
#         'v' : qs20,
#         'w' : qs21,
        
        
        
    }
     return render(request, 'home/home.html', context)