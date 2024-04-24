from django.contrib import admin
from opr.models import OPR
from import_export.admin import ImportExportModelAdmin





# class DataImportExportAdmin(ImportExportModelAdmin):
#     pass
#     resource_class = LocoAdminResource
#     list_display = [ 'LocoNumber','LocoType','LocoCommDate','LocoFailed','author','LocoFile']

admin.site.register(OPR, ImportExportModelAdmin)