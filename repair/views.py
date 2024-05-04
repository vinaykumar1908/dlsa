from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from repair.models import ShedIn, RepairSection, RepairDetail, ManNeededInLoco
from section.models import Section
from holding.models import Loco2
from django.db.models import Q
from django.http import JsonResponse
from repair.forms import ToDoForm
from django.utils import timezone
from staff.models import Staff
from material.models import MatNeededInLoco
from shunting.models2 import ShuntingNeededInLoco1
import datetime
@login_required
def repairhome(request):
    timerightnow = timezone.now()
    LocoList = ShedIn.objects.all().order_by('LocoNumber').filter(ShedOut=False)
    Item = list()
    for l in LocoList:
        p = RepairSection.objects.all().order_by('-Date').filter(LocoNumber=l)
        if l.ShedIn :
            h = timerightnow - l.ShedInDate 
        else :
            h = "Shed In Not Done"
        print("level1")
        print(p)
        jj = list()
        g = Loco2.objects.get(LocoNumber=l.LocoNumber.LocoNumber)
        for f in p:
            print("level2")
            print(f)
            
            x = bool
            ll = list()
            gg = RepairDetail.objects.all().filter(RepSection=f)
            for vv in gg:
                
                # if gg is not []:

                ll.append(vv.workComplete)
                print(ll)
                
            if False in ll:
                x = 'False'
                print("---------------")
                print(x)
                print("---------------")
            elif False not in ll:
                x = 'True'
                print("---------------")
                print(x)
                print("---------------")
            j = timerightnow - l.LocoFailDate
            
            place_json2 = [gg,x,f]
            jj.append(place_json2)
            
        place_json = [g,jj,l, h ,j]
        Item.append(place_json)    


    print(Item)
    
    context = {
        'holding' : Item,
        'time' : timerightnow,
        
    }
    return render(request, 'repair/home.html', context)


@login_required
def shedouthome(request):
    timerightnow = timezone.now()
    LocoList = ShedIn.objects.all().order_by('LocoNumber').filter(ShedOut=True)
    Item = list()
    for l in LocoList:
        p = RepairSection.objects.all().order_by('-Date').filter(LocoNumber=l)
        if l.ShedIn :
            h = timerightnow - l.ShedInDate 
        else :
            h = "Shed In Not Done"
        print("level1")
        print(p)
        jj = list()
        g = Loco2.objects.get(LocoNumber=l.LocoNumber.LocoNumber)
        for f in p:
            print("level2")
            print(f)
            
            x = bool
            ll = list()
            gg = RepairDetail.objects.all().filter(RepSection=f)
            for vv in gg:
                
                # if gg is not []:

                ll.append(vv.workComplete)
                print(ll)
                
            if False in ll:
                x = 'False'
                print("---------------")
                print(x)
                print("---------------")
            elif False not in ll:
                x = 'True'
                print("---------------")
                print(x)
                print("---------------")
            j = timerightnow - l.LocoFailDate
            
            place_json2 = [gg,x,f]
            jj.append(place_json2)
            
        place_json = [g,jj,l, h ,j]
        Item.append(place_json)    


    print(Item)
    context = {
        'holding' : Item,
        'time' : timerightnow,
        
    }
    return render(request, 'repair/shedouthome.html', context)

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
    timerightnow = timezone.now()
    LocoList = ShedIn.objects.all().order_by('LocoNumber').filter(ShedOut=False)
    Item = list()
    for l in LocoList:
        p = RepairSection.objects.all().order_by('-Date').filter(LocoNumber=l)
        if l.ShedIn :
            h = timerightnow - l.ShedInDate 
        else :
            h = "Shed In Not Done"
        print("level1")
        print(p)
        jj = list()
        g = Loco2.objects.get(LocoNumber=l.LocoNumber.LocoNumber)
        for f in p:
            print("level2")
            print(f)
            
            x = bool
            ll = list()
            gg = RepairDetail.objects.all().filter(RepSection=f)
            for vv in gg:
                
                # if gg is not []:

                ll.append(vv.workComplete)
                print(ll)
                
            if False in ll:
                x = 'False'
                print("---------------")
                print(x)
                print("---------------")
            elif False not in ll:
                x = 'True'
                print("---------------")
                print(x)
                print("---------------")
            j = timerightnow - l.LocoFailDate
            
            place_json2 = [gg,x,f]
            jj.append(place_json2)
            
        place_json = [g,jj,l, h ,j]
        Item.append(place_json)    


    print(Item)

    context = {
        'holding' : Item,
        'time' : timerightnow,
        
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

        c = ShedIn(LocoNumber=b, LocoFailDate=d)
        c.save()
        print()
        now = datetime.datetime.now()
        DefaultSection = RepairSection(LocoNumber=c, Date=now, RepSection=Section.objects.get(SectionName='CTA'))
        DefaultSection.save2()
        d = RepairDetail(RepSection=DefaultSection , text="Initialize", workComplete=False)
        d.save()
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
        print("level1")
        print(p)
        for f in p:
            print("level2")
            print(f)
            

            ll = list()
            gg = RepairDetail.objects.all().filter(RepSection=f)
            for vv in gg:
                
                # if gg is not []:

                ll.append(vv.workComplete)
                print(ll)
                x = bool
                if False in ll:
                    x = 'False'
                    print("---------------")
                    print(x)
                    print("---------------")
                elif False not in ll:
                    x = 'True'
                    print("---------------")
                    print(x)
                    print("---------------")
            j = timerightnow - l.LocoFailDate
            jj = list()
            place_json2 = [gg,x,f]
            jj.append(place_json2)
            
        place_json = [g,jj,l, h ,j]
        Item.append(place_json)    


    print(Item)

    context = {
        'holding' : Item,
        'time' : timerightnow,
        
    }
    return render(request, 'repair/home.html', context)

@login_required
def addShedInData(request, id):
    print('addsection activated')
    if request.method=='POST':
        
        print("getting post")
        print('printing request')
        print(request.POST.get('ShedInTime'))
        loco = Loco2.objects.filter(pk=id)
        
        print(loco)
        k = ShedIn.objects.all().filter(LocoNumber=loco[0])
        k = k.order_by('ShedInDate')
        k = k[0]
        k.ShedIn = True
        a = request.POST.get('ShedInDate')
        k.ShedInDate = a
        k.save()
        # print(k)
        # j = Section.objects.get(SectionName=SectionName)
        # newRepairSection = RepairSection(LocoNumber=k, RepSection=j)
        # newRepairSection.save()
        print(f'{k}---')
    timerightnow = timezone.now()
    LocoList = ShedIn.objects.all().order_by('LocoNumber').filter(ShedOut=False)
    Item = list()
    for l in LocoList:
        p = RepairSection.objects.all().order_by('-Date').filter(LocoNumber=l)
        if l.ShedIn :
            h = timerightnow - l.ShedInDate 
        else :
            h = "Shed In Not Done"
        print("level1")
        print(p)
        jj = list()
        g = Loco2.objects.get(LocoNumber=l.LocoNumber.LocoNumber)
        for f in p:
            print("level2")
            print(f)
            
            x = bool
            ll = list()
            gg = RepairDetail.objects.all().filter(RepSection=f)
            for vv in gg:
                
                # if gg is not []:

                ll.append(vv.workComplete)
                print(ll)
                
            if False in ll:
                x = 'False'
                print("---------------")
                print(x)
                print("---------------")
            elif False not in ll:
                x = 'True'
                print("---------------")
                print(x)
                print("---------------")
            j = timerightnow - l.LocoFailDate
            
            place_json2 = [gg,x,f]
            jj.append(place_json2)
            
        place_json = [g,jj,l, h ,j]
        Item.append(place_json)    


    print(Item)
 
    context = {
        'holding' : Item,
        'time' : timerightnow,
        
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
    a = RepairSection.objects.get(id=id)
    b = RepairDetail.objects.all().filter(RepSection=a).order_by("created_date")
    timerightnow = timezone.now()
    Item = list()
    for h in b:
        d = MatNeededInLoco.objects.all().filter(ForJob=h).order_by('RecordCreationDate')
        r = ShuntingNeededInLoco1.objects.all().filter(ForJob=h).order_by('RecordCreationDate')
        c = ManNeededInLoco.objects.all().filter(ForJob=h).order_by('RecordCreationDate')
        place_json = [h, d,r,c]
        Item.append(place_json)
    context = {
        'rs' : a,
        'time' : timerightnow,
        'data' : Item,
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
        r = ShuntingNeededInLoco1.objects.all().filter(ForJob=h).order_by('RecordCreationDate')
        c = ManNeededInLoco.objects.all().filter(ForJob=h).order_by('RecordCreationDate')
        place_json = [h, d,r,c]
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
    
  
    a = RepairDetail.objects.get(id=id)
    
    a.saveworkcomplete2True()
    c = a.RepSection
    d = MatNeededInLoco.objects.all().filter(ForJob=a)
    b = RepairDetail.objects.all().filter(RepSection=c).order_by("created_date")
    Item = list()
    for h in b:
        d = MatNeededInLoco.objects.all().filter(ForJob=h).order_by('RecordCreationDate')
        r = ShuntingNeededInLoco1.objects.all().filter(ForJob=h).order_by('RecordCreationDate')
        c = ManNeededInLoco.objects.all().filter(ForJob=h).order_by('RecordCreationDate')
        place_json = [h, d, r, c]
        Item.append(place_json)
   
    timerightnow = timezone.now()

    context = {
        'rs' : a.RepSection,
        'time' : timerightnow,
        'data' : Item,
        #  'Type' : "Electrical",

    }
    return render(request, 'repair/repairdetail.html', context)




@login_required
def repairdetailhome(request, id):
    a = ShedIn.objects.get(id=id)
    b = RepairSection.objects.filter(LocoNumber=a)
    Item = list()
    Item2 = list()
    for i in b:
        c = RepairDetail.objects.filter(RepSection=i)
        for u in c:
            print(u.RepSection)
            d = MatNeededInLoco.objects.filter(ForJob=u)
            print("MatNeededInLoco")
            print(d)
            e = ShuntingNeededInLoco1.objects.filter(ForJob=u)
            f = ManNeededInLoco.objects.filter(ForJob=u)
            print("ShuntingNeededInLoco")
            print(e)
            place2_json = [u, d, e,f]
            Item2.append(place2_json)
        place_json = [i, c, Item2]
        Item.append(place_json)
    
    timerightnow = timezone.now()
    context = {
        # 'rs' : c,
        'time' : timerightnow,
        'data' : Item,
        'rs' : a,

    }
    return render(request, 'repair/locorepairhome.html', context)


@login_required
def Schedule(request, id):
    a = ShedIn.objects.get(id=id)
    if request.method=='POST':
        a.RepairType = request.POST.get('Schedule')
        a.save()
    b = RepairSection.objects.filter(LocoNumber=a)
    Item = list()
    Item2 = list()
    for i in b:
        c = RepairDetail.objects.filter(RepSection=i)
        for u in c:
            print(u.RepSection)
            d = MatNeededInLoco.objects.filter(ForJob=u)
            print("MatNeededInLoco")
            print(d)
            e = ShuntingNeededInLoco1.objects.filter(ForJob=u)
            f = ManNeededInLoco.objects.filter(ForJob=u)
            print("ShuntingNeededInLoco")
            print(e)
            place2_json = [u, d, e,f]
            Item2.append(place2_json)
        place_json = [i, c, Item2]
        Item.append(place_json)
    
    timerightnow = timezone.now()
    context = {
        # 'rs' : c,
        'time' : timerightnow,
        'data' : Item,
        'rs' : a,

    }
    return render(request, 'repair/locorepairhome.html', context)

@login_required
def Schedule2(request, id):
    a = ShedIn.objects.get(id=id)
    if request.method=='POST':
        a.RepairType = request.POST.get('Schedule')
        a.save()
    timerightnow = timezone.now()
    LocoList = ShedIn.objects.all().order_by('LocoNumber').filter(ShedOut=False)
    Item = list()
    for l in LocoList:
        p = RepairSection.objects.all().order_by('-Date').filter(LocoNumber=l)
        if l.ShedIn :
            h = timerightnow - l.ShedInDate 
        else :
            h = "Shed In Not Done"
        print("level1")
        print(p)
        jj = list()
        g = Loco2.objects.get(LocoNumber=l.LocoNumber.LocoNumber)
        for f in p:
            print("level2")
            print(f)
            
            x = bool
            ll = list()
            gg = RepairDetail.objects.all().filter(RepSection=f)
            for vv in gg:
                
                # if gg is not []:

                ll.append(vv.workComplete)
                print(ll)
                
            if False in ll:
                x = 'False'
                print("---------------")
                print(x)
                print("---------------")
            elif False not in ll:
                x = 'True'
                print("---------------")
                print(x)
                print("---------------")
            j = timerightnow - l.LocoFailDate
            
            place_json2 = [gg,x,f]
            jj.append(place_json2)
            
        place_json = [g,jj,l, h ,j]
        Item.append(place_json)    


    print(Item)
    print(p)
    context = {
        'holding' : Item,
        'time' : timerightnow,
        
    }
    return render(request, 'repair/home.html', context)


@login_required
def WCD(request, id):
    a = ShedIn.objects.get(id=id)
    if request.method=='POST':
        a.workComplete = True
        a.WorkCompleteDate = request.POST.get('WCD')
        a.save()
    b = RepairSection.objects.filter(LocoNumber=a)
    Item = list()
    Item2 = list()
    for i in b:
        c = RepairDetail.objects.filter(RepSection=i)
        for u in c:
            print(u.RepSection)
            d = MatNeededInLoco.objects.filter(ForJob=u)
            print("MatNeededInLoco")
            print(d)
            e = ShuntingNeededInLoco1.objects.filter(ForJob=u)
            f = ManNeededInLoco.objects.filter(ForJob=u)
            print("ShuntingNeededInLoco")
            print(e)
            place2_json = [u, d, e,f]
            Item2.append(place2_json)
        place_json = [i, c, Item2]
        Item.append(place_json)
    
    timerightnow = timezone.now()
    context = {
        # 'rs' : c,
        'time' : timerightnow,
        'data' : Item,
        'rs' : a,

    }
    return render(request, 'repair/locorepairhome.html', context)


@login_required
def SOD(request, id):
    a = ShedIn.objects.get(id=id)
    if request.method=='POST':
        a.ShedOut = True
        a.ShedOutDate = request.POST.get('SOD')
        v = a.LocoNumber
        v.LocoFailed = False
        a.save()
        v.save()
    b = RepairSection.objects.filter(LocoNumber=a)
    Item = list()
    Item2 = list()
    for i in b:
        c = RepairDetail.objects.filter(RepSection=i)
        for u in c:
            print(u.RepSection)
            d = MatNeededInLoco.objects.filter(ForJob=u)
            print("MatNeededInLoco")
            print(d)
            e = ShuntingNeededInLoco1.objects.filter(ForJob=u)
            f = ManNeededInLoco.objects.filter(ForJob=u)
            print("ShuntingNeededInLoco")
            print(e)
            place2_json = [u, d, e,f]
            Item2.append(place2_json)
        place_json = [i, c, Item2]
        Item.append(place_json)
    
    timerightnow = timezone.now()
    context = {
        # 'rs' : c,
        'time' : timerightnow,
        'data' : Item,
        'rs' : a,

    }
    return render(request, 'repair/locorepairhome.html', context)


@login_required
def PDC(request, id):
    a = ShedIn.objects.get(id=id)
    if request.method=='POST':
        a.PDCbool = True
        a.PDC = request.POST.get('PDC')
        a.save()
    b = RepairSection.objects.filter(LocoNumber=a)
    Item = list()
    Item2 = list()
    for i in b:
        c = RepairDetail.objects.filter(RepSection=i)
        for u in c:
            print(u.RepSection)
            d = MatNeededInLoco.objects.filter(ForJob=u)
            print("MatNeededInLoco")
            print(d)
            e = ShuntingNeededInLoco1.objects.filter(ForJob=u)
            f = ManNeededInLoco.objects.filter(ForJob=u)
            print("ShuntingNeededInLoco")
            print(e)
            place2_json = [u, d, e,f]
            Item2.append(place2_json)
        place_json = [i, c, Item2]
        Item.append(place_json)
    
    timerightnow = timezone.now()
    context = {
        # 'rs' : c,
        'time' : timerightnow,
        'data' : Item,
        'rs' : a,

    }
    return render(request, 'repair/locorepairhome.html', context)



@login_required
def addstafftobooking(request, id):
    print('addstafftobooking activated')
    print('-------id--------')
    print(id)
    if request.method=='POST':
        print("getting post")
        print('printing request')
        material = request.POST.get('StaffName')
        qty = request.POST.get('workassigned')
        a = RepairDetail.objects.get(id=id)
        print(material)
        material = material.split(' -')
        print(material[0])
        StaffkaNaam = Staff.objects.get(StaffName=material[0])
        b = ManNeededInLoco(StaffName=StaffkaNaam, WorkAssigned=str(qty), ForJob=a)
        b.save()
    a = RepairDetail.objects.get(id=id)
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
def FilterShedOuts(request):
     if request.method=='POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        datetype = request.POST.get('datetype')
        timerightnow = timezone.now()
        print(datetype)
        if datetype == 'LocoFailDate':
            LocoList = ShedIn.objects.all().order_by('LocoNumber').filter(ShedOut=True).filter(LocoFailDate__range=[date1, date2])
        elif datetype == 'ShedInDate':
            LocoList = ShedIn.objects.all().order_by('LocoNumber').filter(ShedOut=True).filter(ShedInDate__range=[date1, date2])
        elif datetype == 'ShedOut':
            LocoList = ShedIn.objects.all().order_by('LocoNumber').filter(ShedOut=True).filter(ShedOutDate__range=[date1, date2])
        print(LocoList)
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
        return render(request, 'repair/shedouthome.html', context)

@login_required
def FilterShedIns(request):
     if request.method=='POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        datetype = request.POST.get('datetype')
        timerightnow = timezone.now()
        print(datetype)
        if datetype == 'LocoFailDate':
            LocoList = ShedIn.objects.all().order_by('LocoNumber').filter(ShedOut=False).filter(LocoFailDate__range=[date1, date2])
        elif datetype == 'ShedInDate':
            LocoList = ShedIn.objects.all().order_by('LocoNumber').filter(ShedOut=False).filter(ShedInDate__range=[date1, date2])
        elif datetype == 'ShedOut':
            LocoList = ShedIn.objects.all().order_by('LocoNumber').filter(ShedOut=False).filter(ShedOutDate__range=[date1, date2])
        print(LocoList)
        timerightnow = timezone.now()
     LocoList = ShedIn.objects.all().order_by('LocoNumber').filter(ShedOut=False)
     Item = list()
     for l in LocoList:
        p = RepairSection.objects.all().order_by('-Date').filter(LocoNumber=l)
        if l.ShedIn :
            h = timerightnow - l.ShedInDate 
        else :
            h = "Shed In Not Done"
        print("level1")
        print(p)
        jj = list()
        g = Loco2.objects.get(LocoNumber=l.LocoNumber.LocoNumber)
        for f in p:
            print("level2")
            print(f)
            
            x = bool
            ll = list()
            gg = RepairDetail.objects.all().filter(RepSection=f)
            for vv in gg:
                
                # if gg is not []:

                ll.append(vv.workComplete)
                print(ll)
                
            if False in ll:
                x = 'False'
                print("---------------")
                print(x)
                print("---------------")
            elif False not in ll:
                x = 'True'
                print("---------------")
                print(x)
                print("---------------")
            j = timerightnow - l.LocoFailDate
            
            place_json2 = [gg,x,f]
            jj.append(place_json2)
            
        place_json = [g,jj,l, h ,j]
        Item.append(place_json)    


        print(Item)
    
        context = {
            'holding' : Item,
            'time' : timerightnow,
        
        }
        return render(request, 'repair/home.html', context)