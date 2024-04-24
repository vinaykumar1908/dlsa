from import_export import resources
from .models import Loco2

class LocoAdminResource(resources.ModelResource):
    class Meta:
        model = Loco2
        import_id_fields = ('LocoNumber','LocoType')
        fields = ('LocoNumber','LocoType','LocoCommDate','LocoFailed','author','LocoFile')