from django.urls import path, include
from shunting import views

urlpatterns = [
    path('addShunting/<int:id>/', views.addShunting, name='addShunting'),
    path('ChangeShuntingRequirementStatus/<int:id>/', views.ChangeShuntingRequirementStatus, name='ChangeShuntingRequirementStatus'),
     path('ChangeShuntingCompletionStatus/<int:id>/', views.ChangeShuntingCompletionStatus, name='ChangeShuntingCompletionStatus'),
     path('addLocationautocomplete/', views.addLocationautocomplete, name='addLocationautocomplete'),
]