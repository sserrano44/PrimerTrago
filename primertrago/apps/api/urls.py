from django.conf.urls.defaults import *
from tastypie.api import Api

from resources import BarResource

v1_api = Api(api_name='v1')
v1_api.register(BarResource())

urlpatterns = patterns('',
    # The normal jazz here then...
    (r'^', include(v1_api.urls)),
)