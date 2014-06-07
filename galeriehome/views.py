from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from galeriehome import models
import datetime


# Create your views here.
ML_COOKIE_NAME = "ml-language-selection"
ML_CONTEXT_KEY = "ml_active_language"

def ml_selection(request):
    if ML_COOKIE_NAME in request.COOKIES:
        lang = request.COOKIES[ML_COOKIE_NAME]
    else:
        lang = "en"
    return lang


def view_with_ml(request, view_name, context={}):
    context.update({
        ML_CONTEXT_KEY: ml_selection(request),
        'present_view_name': view_name,
    })
    return render(request, 'home/'+view_name+'.html', context)


def index(request):
    return view_with_ml(request, 'index')

def concept(request):
    return view_with_ml(request, 'concept')

def schedule(request):
    return view_with_ml(request, 'schedule')

def schedule_past(request):
    now = datetime.datetime.now().date()
    exh = models.Exhibition.objects.filter(end__lt=now).order_by('-start')
    con = {'exhibitions': exh}
    return view_with_ml(request, 'schedule-past', con)

def news(request):
    return view_with_ml(request, 'news')

def guide(request):
    return view_with_ml(request, 'guide')

def access(request):
    return view_with_ml(request, 'access')



# This sandbox is for experimenting with new creations
def sandbox(request):
    return view_with_ml(request, 'sandbox')
