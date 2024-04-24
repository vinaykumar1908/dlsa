from import_export import resources
from section.models import Section

class SectionAdminResource(resources.ModelResource):
    class Meta:
        model = Section
        import_id_fields = ('SectionName','SectionIncharge','author')
        fields = ('SectionName','author','SectionIncharge')