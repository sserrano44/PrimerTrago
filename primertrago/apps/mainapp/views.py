# Create your views here.
#from django.template.response import TemplateResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from mainapp.models import Bar


def home(request):
    params = {
        'bars': Bar.objects.all()
    }
    return render_to_response("home.html", params, RequestContext(request))

