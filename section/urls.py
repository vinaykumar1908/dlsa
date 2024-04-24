from django.urls import path, include
from section import views

urlpatterns = [
    path('section/', views.sectionhome, name='sectionhome'),
    # path('hhp/', views.holdingH, name='holding_hhp'),
    # path('electrical/', views.holdingE, name='holding_electrical'),
]