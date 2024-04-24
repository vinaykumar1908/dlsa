from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from staff.models import Staff


@login_required
def staffhome(request):
    StaffList = Staff.objects.all().order_by('StaffName')
    context = {
        'StaffList' : StaffList,
        #  'holding' : qs3,
        #  'Type' : "Electrical",

    }
    return render(request, 'staff/staffHome.html', context)