from django.contrib import admin
from section.models import Section
from import_export.admin import ImportExportModelAdmin
from section.resources import SectionAdminResource





class DataImportExportAdmin(ImportExportModelAdmin):
    resource_class = SectionAdminResource
    list_display = [ 'SectionName','SectionIncharge','author']

admin.site.register(Section)