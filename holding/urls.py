from django.urls import path, include
from holding import views

urlpatterns = [
    path('alco/', views.holdingA, name='holding_alco'),
    path('hhp/', views.holdingH, name='holding_hhp'),
    path('electrical/', views.holdingE, name='holding_electrical'),
]