# Create your views here.
#from django.template.response import TemplateResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from mainapp.models import Bar
from django.template.response import TemplateResponse
from django.http import Http404
from mainapp.forms import FilterForm


def home(request):
    
    params = {
        'filter_form': FilterForm(),
        'featured': Bar.objects.filter(featured=True),
        'bars': Bar.objects.all()
    }
    #return render_to_response("home.html", params, RequestContext(request))
    return TemplateResponse(request, "home.html", params)



def bar(request, id=None, slug=None):
    """
    
    """
    if slug:
        bar = get_object_or_404(Bar, slug=slug)
    elif id:
        bar = get_object_or_404(Bar, id=id)
    else:
        raise Http404
    
    params = {
        'bar': bar,
    }
    return TemplateResponse(request, "bar.html", params)
