from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from section.models import Section


@login_required
def sectionhome(request):
    StaffList = Section.objects.all().order_by('SectionName')
    context = {
        'StaffList' : StaffList,
        #  'holding' : qs3,
        #  'Type' : "Electrical",

    }
    return render(request, 'section/sectionHome.html', context)