from django.urls import path, include
from material import views

urlpatterns = [
    path('addJobMaterial/<int:id>/', views.addJobMaterial, name='addJobMaterial'),
    path('ChangeJobMatRequirement/<int:id>/', views.ChangeJobMatRequirement, name='ChangeJobMatRequirement'),
     path('ChangeMatRecRequirement/<int:id>/', views.ChangeMatRecRequirement, name='ChangeMatRecRequirement'),
]