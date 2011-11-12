import haystack
haystack.autodiscover()


import datetime
from haystack.indexes import *
from haystack import site
from mainapp.models import Bar


class BarIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    name = CharField(model_attr='name')
    neighborhoood = CharField(model_attr='neighborhood')


site.register(Bar, BarIndex)

