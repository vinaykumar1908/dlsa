from import_export import resources
from staff.models import Staff

class StaffAdminResource(resources.ModelResource):
    class Meta:
        model = Staff
        import_id_fields = ('StaffName','TokenNumber','TokenNumber','Designation','DOB','StaffFile','Staffimage','author')
        fields = ('StaffName','TokenNumber','TokenNumber','Designation','DOB','StaffFile','Staffimage','author')