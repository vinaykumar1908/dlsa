from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from staff.models import Staff

from django.http import JsonResponse


@login_required
def staffhome(request):
    StaffList = Staff.objects.all().order_by('StaffName')
    context = {
        'StaffList' : StaffList,
        #  'holding' : qs3,
        #  'Type' : "Electrical",

    }
    return render(request, 'staff/staffHome.html', context)






@login_required
def addstaffnameautocomplete(request):
    print(request)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if 'term' in request.GET:
            qs = Staff.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(StaffName__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = str(product.StaffName)
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)
            
            