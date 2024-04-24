from django.contrib import admin
from TnP.models import registerCurrentStock, registerStockRecieved, registerStockOnLoan
# Register your models here.
admin.site.register(registerCurrentStock)
admin.site.register(registerStockRecieved)
admin.site.register(registerStockOnLoan)