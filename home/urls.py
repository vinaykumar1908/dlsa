from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.homeView, name='home'),
    # path('charts/', include('charts.urls')),
    # path('defi/', include('defi.urls')),
    path('holding/', include('holding.urls')),
    path('opr/', include('opr.urls')),
    path('repair/', include('repair.urls')),
    path('card/', include('card.urls')),
    path('section/', include('section.urls')),
    path('staff/', include('staff.urls')),
    path('TnP/', include('TnP.urls')),
    #path('sickline/', include('sickline.urls')),
    #path('yard/', include('yard.urls')),
    #path('sidings/', include('sidingz.urls')),
    #path('MessageBoard/', include('blog.urls')),
    #path('MnP/', include('mnp.urls')),
    #path('Contracts/', include('contracts.urls')),
    #path('Employee/', include('employee.urls')),
    #path('Rakes/', include('rakes.urls')),
    #path('Knowledge/', include('knowledge.urls')),
    #path('Staff/', include('staff.urls')),
    #path('Examinations/', include('exams.urls')),
    #path('Letters/', include('letters.urls')),
    #path('CCMaterialCharts', views.ccmaterialcharts, name='ccmaterialcharts'),
    #path('STRMaterialCharts', views.strmaterialcharts, name='strmaterialcharts'),
    #path('CCDetentionCharts', views.ccdetentioncharts, name='ccdetentioncharts'),
    #path('STRDetentionCharts', views.strdetentioncharts, name='strdetentioncharts'),

    
    


    
]
