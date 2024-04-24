from django.contrib import admin
from staff.models import Staff
from import_export.admin import ImportExportModelAdmin
from staff.resources import StaffAdminResource





class StaffImportExportAdmin(ImportExportModelAdmin):
    resource_class = StaffAdminResource
    list_display = [ 'StaffName','TokenNumber','Designation','DOB','StaffFile','Staffimage','author']

admin.site.register(Staff, StaffImportExportAdmin)