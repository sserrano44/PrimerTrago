# Create your views here.
#from django.template.response import TemplateResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def home(request):
    return render_to_response("home.html", {}, RequestContext(request))

