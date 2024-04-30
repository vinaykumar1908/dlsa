
from django.contrib import admin
from locations.models import Locations




# class ShedInAdmin(admin.ModelAdmin):
#     list_display = ('ShedInDate','LocoNumber')

# class RepairSectionAdmin(admin.ModelAdmin):
#     list_display = ('Date', 'LocoNumber', 'RepSection', )
#     search_fields = ['RepSection']
# class RepairDetailAdmin(admin.ModelAdmin):
#     list_display = ('created_date','RepSection',  'text', 'workComplete')
# # Register your models here.
# admin.site.register(ShedIn, ShedInAdmin)
# admin.site.register(RepairSection, RepairSectionAdmin)
admin.site.register(Locations)
