from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from repair.models import ShedIn, RepairSection, RepairDetail
from section.models import Section
from holding.models import Loco2
from django.db.models import Q
from django.http import JsonResponse
from repair.forms import ToDoForm
from django.utils import timezone

from material.models import MatNeededInLoco
from shunting.models import ShuntingNeededInLoco, Locations
@login_required
def repairhome(request):
    print('repairhome activated')
    timerightnow = timezone.now()
    LocoList = ShedIn.objects.all().order_by('LocoNumber').filter(ShedOut=False)
    Item = list()
    for l in LocoList:
        p = RepairSection.objects.all().order_by('-Date').filter(LocoNumber=l)
        g = Loco2.objects.get(LocoNumber=l.LocoNumber.LocoNumber)
        if l.ShedIn :
            h = timerightnow - l.ShedInDate 
        else :
            h = "Shed In Not Done"
        j = timerightnow - l.LocoFailDate
        place_json = [g,p,l, h ,j]
        Item.append(place_json)
    print(Item)
    context = {
        'holding' : Item,
        'time' : timerightnow,
        #  'holding' : qs3,
        #  'Type' : "Electrical",

    }
    return render(request, 'repair/home.html', context)

@login_required
def addSection(request, id):
    
    timerightnow = timezone.now()
    print(id)
    print('addsection activated')
    if request.method=='POST':
        print("getting post")
        SectionName = request.POST.get('addsection1')
        print(SectionName)
        loco = Loco2.objects.get(pk=id)
        print(loco)
        k = ShedIn.objects.get(LocoNumber=loco)
        print(k)
        j = Section.objects.get(SectionName=SectionName)
        newRepairSection = RepairSection(LocoNumber=k, RepSection=j)
        newRepairSection.save()
        print(f'{k}---{j}')
    LocoList = ShedIn.objects.all().order_by('LocoNumber').filter(ShedOut=False)
    Item = list()
    for l in LocoList:
        p = RepairSection.objects.all().order_by('-Date').filter(LocoNumber=l)
        g = Loco2.objects.get(LocoNumber=l.LocoNumber.LocoNumber)
        if l.ShedIn :
            h = timerightnow - l.ShedInDate 
        else :
            h = "Shed In Not Done"
        j = timerightnow - l.LocoFailDate
        place_json = [g,p,l, h , j]
        Item.append(place_json)
        
    print(p)
    print("----------------")
    print(Item)
    print('----------------')
    context = {
        'time' : timerightnow,
        'holding' : Item,
        #  'holding' : qs3,
        #  'Type' : "Electrical",

    }
    return render(request, 'repair/home.html', context)


@login_required
def addFailedLoco(request):
    print(id)
    print('addsection activated')
    timerightnow = timezone.now()
    if request.method=='POST':
        a = request.POST.get('FailLoco')
        b = Loco2.objects.get(LocoNumber=a)
        b.LocoFailed = True
        b.save()
        d = request.POST.get('ShedInDate')
        e = request.POST.get('ShedInTime')
        print(f'{d}---{e}--{b}')
        f = d+' '+e

        c = ShedIn(LocoNumber=b, LocoFailDate=f)
        c.save()
        # print("getting post")
        # SectionName = request.POST.get('addsection1')
        # print(SectionName)
        # loco = Loco2.objects.get(pk=id)
        # print(loco)
        # k = ShedIn.objects.get(LocoNumber=loco)
        # print(k)
        # j = Section.objects.get(SectionName=SectionName)
        # newRepairSection = RepairSection(LocoNumber=k, RepSection=j)
        # newRepairSection.save()
        # print(f'{k}---{j}')
    LocoList = ShedIn.objects.all().order_by('LocoNumber').filter(ShedOut=False)
    Item = list()
    for l in LocoList:
        p = RepairSection.objects.all().order_by('-Date').filter(LocoNumber=l)
        g = Loco2.objects.get(LocoNumber=l.LocoNumber.LocoNumber)
        if l.ShedIn :
            h = timerightnow - l.ShedInDate 
        else :
            h = "Shed In Not Done"
        j = timerightnow - l.LocoFailDate
        place_json = [g,p,l, h , j]
        Item.append(place_json)
        
    print(p)
    print("----------------")
    print(Item)
    print('----------------')
    context = {

        'holding' : Item,
        'time' : timerightnow,
        #  'holding' : qs3,
        #  'Type' : "Electrical",

    }
    return render(request, 'repair/home.html', context)


@login_required
def addShedInData(request, id):
    print(id)
    timerightnow = timezone.now()
    print('addsection activated')
    if request.method=='POST':
        
        print("getting post")
        print('printing request')
        print(request.POST.get('ShedInTime'))
        loco = Loco2.objects.get(pk=id)
        print(loco)
        k = ShedIn.objects.get(LocoNumber=loco)
        k.ShedIn = True
        a = request.POST.get('ShedInDate')
        b = request.POST.get('ShedInTime')
        c = a+" "+b
        k.ShedInDate = c
        k.save()
        print(c)
        # print(k)
        # j = Section.objects.get(SectionName=SectionName)
        # newRepairSection = RepairSection(LocoNumber=k, RepSection=j)
        # newRepairSection.save()
        print(f'{k}---')
    LocoList = ShedIn.objects.all().order_by('LocoNumber').filter(ShedOut=False)
    Item = list()
    for l in LocoList:
        p = RepairSection.objects.all().order_by('-Date').filter(LocoNumber=l)
        g = Loco2.objects.get(LocoNumber=l.LocoNumber.LocoNumber)
        j = timerightnow - l.LocoFailDate
        if l.ShedIn :
            h = timerightnow - l.ShedInDate 
        else :
            h = "Shed In Not Done"
        
        place_json = [g,p,l, h , j]
        Item.append(place_json)
    print(Item)
        
    print(p)
    print("----------------")
    print(Item)
    print('----------------')
    timerightnow = timezone.now()
    context = {

        'holding' : Item,
        'time' : timerightnow,
        #  'holding' : qs3,
        #  'Type' : "Electrical",

    }
    return render(request, 'repair/home.html', context)


@login_required
def addsectionautocomplete(request):
    print(request)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if 'term' in request.GET:
            qs = Section.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(SectionName__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.SectionName
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)
            

           
@login_required
def addLocoautocomplete(request):
    print(request)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if 'term' in request.GET:
            qs = Loco2.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(LocoNumber__startswith=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = str(product.LocoNumber)
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)
            
             



@login_required
def addHHPautocomplete(request):
    print(request)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if 'term' in request.GET:
            qs = Loco2.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(Q(LocoNumber__startswith=itemTerm) & (Q(LocoType='WDG4') | Q(LocoType='WDG4D') | Q(LocoType='WDP4B') | Q(LocoType='WDP4D')))
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = str(product.LocoNumber)
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)
            
            

@login_required
def addAlcoautocomplete(request):
    print(request)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if 'term' in request.GET:
            qs = Section.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(SectionName__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.SectionName
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)
            
            


@login_required
def addElectautocomplete(request):
    print(request)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if 'term' in request.GET:
            qs = Section.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(SectionName__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.SectionName
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)
            
            

@login_required
def viewSectionRepairDetail(request, id):
    print('viewSectionRepairDetail activated')
    print('-------id--------')
    print(id)
    a = RepairSection.objects.get(id=id)
    print('RepairSection.objects.get(pk=id)')
    print(a)

    
    b = RepairDetail.objects.all().filter(RepSection=a).order_by("created_date")
    print(b)
    # LocoList = ShedIn.objects.all().order_by('LocoNumber').filter(ShedOut=False)
    # Item = list()
    # for l in LocoList:
    #     p = RepairSection.objects.all().order_by('-Date').filter(LocoNumber=l)
    #     g = Loco2.objects.get(LocoNumber=l.LocoNumber.LocoNumber)
    #     place_json = [g,p,l]
    #     Item.append(place_json)
    # print(Item)
    timerightnow = timezone.now()
    Item = list()
    for h in b:
        d = MatNeededInLoco.objects.all().filter(ForJob=h).order_by('RecordCreationDate')
        r = ShuntingNeededInLoco.objects.all().filter(ForJob=h).order_by('RecordCreationDate')
        place_json = [h, d,r]
        Item.append(place_json)
    
    context = {
        'rs' : a,
        'time' : timerightnow,
        'data' : Item,
        #  'Type' : "Electrical",

    }
    return render(request, 'repair/repairdetail.html', context)




@login_required
def addSectionRepairDetail(request, id):
    print('addSectionRepairDetail activated')
    print('-------id--------')
    print(id)
    a = RepairSection.objects.get(id=id)
    print('RepairSection.objects.get(pk=id)')
    print(a)
    if request.method=='POST':
        print(request)
        j = request.POST.get('BookingDetail')
        print(j)
        k = RepairDetail(text=j, RepSection=a)
        k.save()
    
    b = RepairDetail.objects.all().filter(RepSection=a).order_by("created_date")
    print(b)
    # LocoList = ShedIn.objects.all().order_by('LocoNumber').filter(ShedOut=False)
    # Item = list()
    # for l in LocoList:
    #     p = RepairSection.objects.all().order_by('-Date').filter(LocoNumber=l)
    #     g = Loco2.objects.get(LocoNumber=l.LocoNumber.LocoNumber)
    #     place_json = [g,p,l]
    #     Item.append(place_json)
    # print(Item)
    timerightnow = timezone.now()
    Item = list()
    for h in b:
        d = MatNeededInLoco.objects.all().filter(ForJob=h).order_by('RecordCreationDate')
        r = ShuntingNeededInLoco.objects.all().filter(ForJob=h).order_by('RecordCreationDate')
        place_json = [h, d,r]
        Item.append(place_json)
    
    context = {
        'rs' : a,
        'time' : timerightnow,
        'data' : Item,
        #  'Type' : "Electrical",

    }
    return render(request, 'repair/repairdetail.html', context)


@login_required
def ChangeRepDetCompletionStatus(request, id):
    print('ChangeJobMatRequirement activated')
    print('-------id--------')
    print(id)
    if request.method=='POST':
  
        a = RepairDetail.objects.get(id=id)
        a.saveworkcomplete2True()
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