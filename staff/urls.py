from django.urls import path, include
from staff import views

urlpatterns = [
    path('staff/', views.staffhome, name='staffhome'),
    path('addstaffnameautocomplete/', views.addstaffnameautocomplete, name='addstaffnameautocomplete'),
    # path('hhp/', views.holdingH, name='holding_hhp'),
    # path('electrical/', views.holdingE, name='holding_electrical'),
]