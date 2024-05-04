from django.urls import path, include
from repair import views

urlpatterns = [
    path('repair/', views.repairhome, name='repairhome'),
    path('shedouthome/', views.shedouthome, name='shedouthome'),
    path('repairdetailhome/<int:id>/', views.repairdetailhome, name='repairdetailhome'),
    path('addSection/<int:id>/', views.addSection, name='addSection'),
    path('addShedInData/<int:id>/', views.addShedInData, name='addShedInData'),
    path('addFailedLoco/', views.addFailedLoco, name='addFailedLoco'),
    path('addsectionautocomplete/', views.addsectionautocomplete, name='addsectionautocomplete'),
    path('addLocoautocomplete/', views.addLocoautocomplete, name='addLocoautocomplete'),
    path('addHHPautocomplete/', views.addHHPautocomplete, name='addHHPautocomplete'),
    path('addAlcoautocomplete/', views.addAlcoautocomplete, name='addAlcoautocomplete'),
    path('addElectautocomplete/', views.addElectautocomplete, name='addElectautocomplete'),
    path('viewSectionRepairDetail/<int:id>/', views.viewSectionRepairDetail, name='viewSectionRepairDetail'),
    path('addSectionRepairDetail/<int:id>/', views.addSectionRepairDetail, name='addSectionRepairDetail'),
    path('ChangeRepDetCompletionStatus/<int:id>/', views.ChangeRepDetCompletionStatus, name='ChangeRepDetCompletionStatus'),

    path('Schedule/<int:id>/', views.Schedule, name='Schedule'),
    path('Schedule2/<int:id>/', views.Schedule2, name='Schedule2'),
    path('WCD/<int:id>/', views.WCD, name='WCD'),
    path('SOD/<int:id>/', views.SOD, name='SOD'),
    path('PDC/<int:id>/', views.PDC, name='PDC'),
    path('addstafftobooking/<int:id>/', views.addstafftobooking, name='addstafftobooking'),
    path('FilterShedOuts/', views.FilterShedOuts, name='FilterShedOuts'),
    path('FilterShedIns/', views.FilterShedIns, name='FilterShedIns'),
]


