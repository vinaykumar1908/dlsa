
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
import datetime
from datetime import timedelta, date

from holding.models import Loco2
from django.utils import timezone
@login_required
def oprHome(request):
    # qs = Loco2.objects.filter(Q(LocoType='WDM3A') | Q(LocoType='WDM3D') | Q(LocoType='WDG3A') | Q(LocoType='WDS6') | Q(LocoType='WDS6AD')).order_by('LocoNumber')   
    timerightnow = timezone.now()

    context = {
        'time' : timerightnow,
        #  'holding' : qs,
        #  'Type' : "Alco",

    }
    return render(request, 'opr/home.html', context)
