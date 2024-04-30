
from django.contrib import admin
from repair.models import ShedIn, RepairSection, RepairDetail, ManNeededInLoco




class ShedInAdmin(admin.ModelAdmin):
    list_display = ('ShedInDate','LocoNumber')

class RepairSectionAdmin(admin.ModelAdmin):
    list_display = ('Date', 'LocoNumber', 'RepSection', )
    search_fields = ['RepSection']
class RepairDetailAdmin(admin.ModelAdmin):
    list_display = ('created_date','RepSection',  'text', 'workComplete')
# Register your models here.
admin.site.register(ShedIn, ShedInAdmin)
admin.site.register(RepairSection, RepairSectionAdmin)
admin.site.register(RepairDetail, RepairDetailAdmin)

admin.site.register(ManNeededInLoco)
