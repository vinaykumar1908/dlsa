
from django.contrib import admin
from .models import Loco2
from import_export.admin import ImportExportModelAdmin
from .resources import LocoAdminResource





class DataImportExportAdmin(ImportExportModelAdmin):
    resource_class = LocoAdminResource
    list_display = [ 'LocoNumber','LocoType','LocoCommDate','LocoFailed','author','LocoFile']

admin.site.register(Loco2, DataImportExportAdmin)