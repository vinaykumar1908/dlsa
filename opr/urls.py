from django.urls import path, include
from opr import views

urlpatterns = [
    path('', views.oprHome, name='oprHome'),
    # path('hhp/', views.holdingH, name='holding_hhp'),
    # path('electrical/', views.holdingE, name='holding_electrical'),
]