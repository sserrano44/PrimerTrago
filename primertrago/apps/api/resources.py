from tastypie.resources import ModelResource

from mainapp.models import Bar

class BarResource(ModelResource):
    class Meta:
        queryset = Bar.objects.all()
        
