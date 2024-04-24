from django.urls import path, include
from repair import views

urlpatterns = [
    path('repair/', views.repairhome, name='repairhome'),
    path('addSection/<int:id>/', views.addSection, name='addSection'),
    path('addShedInData/<int:id>/', views.addShedInData, name='addShedInData'),
    path('addFailedLoco/', views.addFailedLoco, name='addFailedLoco'),
    path('addsectionautocomplete/', views.addsectionautocomplete, name='addsectionautocomplete'),
    path('addLocoautocomplete/', views.addLocoautocomplete, name='addLocoautocomplete'),
    path('addHHPautocomplete/', views.addHHPautocomplete, name='addHHPautocomplete'),
    path('addAlcoautocomplete/', views.addAlcoautocomplete, name='addAlcoautocomplete'),
    path('addElectautocomplete/', views.addElectautocomplete, name='addElectautocomplete'),
    path('viewSectionRepairDetail/<int:id>/', views.viewSectionRepairDetail, name='viewSectionRepairDetail'),
]


