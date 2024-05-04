
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from repair.models import RepairSection, RepairDetail, ShedIn, ManNeededInLoco
from django.utils import timezone
from material.models import MatNeededInLoco
from section.models import Section
from shunting.models2 import Locations, ShuntingNeededInLoco1


from django.http import JsonResponse



@login_required
def addShunting(request, id):
    print('addShunting activated')
    print('-------id--------')
    print(id)
    if request.method=='POST':
        LocationTo = request.POST.get('LocationTo')
        if Locations.objects.get(LocationName=LocationTo) is None:
            v = Locations(LocationName=LocationTo)
            v.save()
        LocationTo = Locations.objects.get(LocationName=LocationTo)
        a = RepairDetail.objects.get(id=id)
        print(a)
        c = a.RepSection
        er = c.LocoNumber.PresentLocation
        print(er)
        d = MatNeededInLoco.objects.all().filter(ForJob=a)
        b = RepairDetail.objects.all().filter(RepSection=c).order_by("created_date")
        d = ShuntingNeededInLoco1(From=er, To=LocationTo, ForJob=a)
        d.save()
    ba = RepairDetail.objects.all().filter(RepSection=c).order_by("created_date")
    timerightnow = timezone.now()
    Item = list()
    for ha in ba:
        da = MatNeededInLoco.objects.all().filter(ForJob=ha).order_by('RecordCreationDate')
        ra = ShuntingNeededInLoco1.objects.all().filter(ForJob=ha).order_by('RecordCreationDate')
        ca = ManNeededInLoco.objects.all().filter(ForJob=ha).order_by('RecordCreationDate')
        place_json = [ha, da,ra,ca]
        Item.append(place_json)
    context = {
        'rs' : c,
        'time' : timerightnow,
        'data' : Item,
    }
    return render(request, 'repair/repairdetail.html', context)



@login_required
def ChangeShuntingRequirementStatus(request, id):
    print('ChangeShuntingRequirementStatus activated')
    print('-------id--------')
    print(id)
    if request.method=='POST':
  
        a = RepairDetail.objects.get(id=id)
        a.saveShunt2True()
        c = a.RepSection
        ba = RepairDetail.objects.all().filter(RepSection=c).order_by("created_date")
    timerightnow = timezone.now()
    Item = list()
    for ha in ba:
        da = MatNeededInLoco.objects.all().filter(ForJob=ha).order_by('RecordCreationDate')
        ra = ShuntingNeededInLoco1.objects.all().filter(ForJob=ha).order_by('RecordCreationDate')
        ca = ManNeededInLoco.objects.all().filter(ForJob=ha).order_by('RecordCreationDate')
        place_json = [ha, da,ra,ca]
        Item.append(place_json)
    context = {
        'rs' : c,
        'time' : timerightnow,
        'data' : Item,
    }
    return render(request, 'repair/repairdetail.html', context)





@login_required
def ChangeShuntingCompletionStatus(request, id):
    print('ChangeShuntingCompletionStatus activated')
    print('-------id--------')
    print(id)
    if request.method=='POST':
        a = ShuntingNeededInLoco1.objects.get(id=id)
        print(a)
        a.save2shuntComplete()
        c = a.ForJob
        z = c.RepSection
        print(c)
        d = MatNeededInLoco.objects.all().filter(ForJob=c)
        print(d)
        b = RepairDetail.objects.all().filter(RepSection=c.RepSection).order_by("created_date")
        Item = list()
        for h in b:
            d = MatNeededInLoco.objects.all().filter(ForJob=h).order_by('RecordCreationDate')
            r = ShuntingNeededInLoco1.objects.all().filter(ForJob=h).order_by('RecordCreationDate')
            c = ManNeededInLoco.objects.all().filter(ForJob=h).order_by('RecordCreationDate')
            place_json = [h, d, r,c]
            Item.append(place_json)
   
    timerightnow = timezone.now()

    context = {
        'rs' : z,
        'time' : timerightnow,
        'data' : Item,
        #  'Type' : "Electrical",

    }
    return render(request, 'repair/repairdetail.html', context)



@login_required
def addLocationautocomplete(request):
    print(request)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if 'term' in request.GET:
            qs = Locations.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(LocationName__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.LocationName
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)