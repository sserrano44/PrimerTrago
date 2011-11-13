# Create your views here.
#from django.template.response import TemplateResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from mainapp.models import Bar
from django.template.response import TemplateResponse
from django.http import Http404
from mainapp.forms import FilterForm
import logging


def home(request):

    params = { }
    
    if request.GET.get("filter", None):
        form = FilterForm(request.GET)
        params['filter_form']  = form
        if form.is_valid() is False:
            return TemplateResponse(request, "home.html", params)
            
        query = Bar.objects.all()
        weekday      = form.cleaned_data.get('weekday', None)
        hour         = form.cleaned_data.get('hour', None)
        neighborhood = form.cleaned_data.get('neighborhood', None)
        
        if weekday:
            print weekday
            query = query.filter(** {'happyhour__%s' % weekday: True})
        if hour:
            print hour
            query = query.filter(happyhour__hour_start__gte=hour)
            query = query.filter(happyhour__hour_end__lte=hour)
        if neighborhood:
            print neighborhood
            query = query.filter(neighborhood=neighborhood)
        params['featured'] = query.filter(featured=True)
        params['bars'] = query.filter(featured=False)
    else:
        form = FilterForm(request.GET)
        params['filter_form']  = form
        params['featured'] = Bar.objects.filter(featured=True),
        params['bars'] = Bar.objects.all()
    
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
