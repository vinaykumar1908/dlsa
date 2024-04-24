from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from repair.models import ShedIn, RepairSection
from section.models import Section
from holding.models import Loco2
from django.db.models import Q
from django.http import JsonResponse
from repair.forms import ToDoForm

@login_required
def repairhome(request):
    print('repairhome activated')
    LocoList = ShedIn.objects.all().order_by('LocoNumber').filter(ShedOut=False)
    Item = list()
    for l in LocoList:
        p = RepairSection.objects.all().order_by('-Date').filter(LocoNumber=l)
        g = Loco2.objects.get(LocoNumber=l.LocoNumber.LocoNumber)
        place_json = [g,p,l]
        Item.append(place_json)
    print(Item)

    context = {

        'form' : ToDoForm,
        'holding' : Item,
        #  'holding' : qs3,
        #  'Type' : "Electrical",

    }
    return render(request, 'repair/home.html', context)

@login_required
def addSection(request, id):
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
        place_json = [g,p,l]
        Item.append(place_json)
    print(Item)
        
    print(p)
    print("----------------")
    print(Item)
    print('----------------')
    context = {

        'holding' : Item,
        #  'holding' : qs3,
        #  'Type' : "Electrical",

    }
    return render(request, 'repair/home.html', context)


@login_required
def addFailedLoco(request):
    print(id)
    print('addsection activated')
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
        place_json = [g,p,l]
        Item.append(place_json)
    print(Item)
        
    print(p)
    print("----------------")
    print(Item)
    print('----------------')
    context = {

        'holding' : Item,
        #  'holding' : qs3,
        #  'Type' : "Electrical",

    }
    return render(request, 'repair/home.html', context)


@login_required
def addShedInData(request, id):
    print(id)
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
        place_json = [g,p,l]
        Item.append(place_json)
    print(Item)
        
    print(p)
    print("----------------")
    print(Item)
    print('----------------')
    context = {

        'holding' : Item,
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
            
            