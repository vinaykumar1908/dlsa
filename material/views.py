
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from repair.models import RepairSection, RepairDetail
from django.utils import timezone
from material.models import MatNeededInLoco
from section.models import Section

from shunting.models import ShuntingNeededInLoco, Locations


@login_required
def addJobMaterial(request, id):
    print('addJobMaterial activated')
    print('-------id--------')
    print(id)
    if request.method=='POST':
        print("getting post")
        print('printing request')
        material = request.POST.get('MatNeeded')
        qty = request.POST.get('QtyNeeded')
        section = Section.objects.get(SectionName=request.POST.get('Section'))
        a = RepairDetail.objects.get(id=id)
        print(a)
        b = MatNeededInLoco(MaterialName=material, Quantity=qty, FromSection=section, ForJob=a)
        b.save()
        c = a.RepSection
        d = MatNeededInLoco.objects.all().filter(ForJob=a)
        b = RepairDetail.objects.all().filter(RepSection=c).order_by("created_date")
        Item = list()
        for h in b:
            d = MatNeededInLoco.objects.all().filter(ForJob=h).order_by('RecordCreationDate')
            r = ShuntingNeededInLoco.objects.all().filter(ForJob=h).order_by('RecordCreationDate')
            place_json = [h, d, r]
            Item.append(place_json)
   
    timerightnow = timezone.now()

    context = {
        'rs' : c,
        'time' : timerightnow,
        'data' : Item,
        #  'Type' : "Electrical",

    }
    return render(request, 'repair/repairdetail.html', context)



@login_required
def ChangeJobMatRequirement(request, id):
    print('ChangeJobMatRequirement activated')
    print('-------id--------')
    print(id)
    if request.method=='POST':
  
        a = RepairDetail.objects.get(id=id)
        a.save2True()
        c = a.RepSection
        d = MatNeededInLoco.objects.all().filter(ForJob=a)
        b = RepairDetail.objects.all().filter(RepSection=c).order_by("created_date")
        Item = list()
        for h in b:
            d = MatNeededInLoco.objects.all().filter(ForJob=h).order_by('RecordCreationDate')
            r = ShuntingNeededInLoco.objects.all().filter(ForJob=h).order_by('RecordCreationDate')
            place_json = [h, d, r]
            Item.append(place_json)
   
    timerightnow = timezone.now()

    context = {
        'rs' : c,
        'time' : timerightnow,
        'data' : Item,
        #  'Type' : "Electrical",

    }
    return render(request, 'repair/repairdetail.html', context)





@login_required
def ChangeMatRecRequirement(request, id):
    print('ChangeMatRecRequirement activated')
    print('-------id--------')
    print(id)
    if request.method=='POST':
        a = MatNeededInLoco.objects.get(id=id)
        print(a)
        a.save2MatRec()
        c = a.ForJob
        z = c.RepSection
        print(c)
        d = MatNeededInLoco.objects.all().filter(ForJob=c)
        print(d)
        b = RepairDetail.objects.all().filter(RepSection=c.RepSection).order_by("created_date")
        Item = list()
        for h in b:
            d = MatNeededInLoco.objects.all().filter(ForJob=h).order_by('RecordCreationDate')
            r = ShuntingNeededInLoco.objects.all().filter(ForJob=h).order_by('RecordCreationDate')
            place_json = [h, d, r]
            Item.append(place_json)
   
    timerightnow = timezone.now()

    context = {
        'rs' : z,
        'time' : timerightnow,
        'data' : Item,
        #  'Type' : "Electrical",

    }
    return render(request, 'repair/repairdetail.html', context)