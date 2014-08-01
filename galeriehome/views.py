from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.db.models import Q
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
    today = datetime.date.today()
    nowQ = Q(start__lte=today) & Q(end__gte=today)
    nextQ = Q(start__gt=today)
    exhNow = models.Exhibition.objects.filter(nowQ).order_by('start')
    exhNext = models.Exhibition.objects.filter(nextQ).order_by('start')
    con = {'exhibitions_now': exhNow, 'exhibitions_next': exhNext}
    return view_with_ml(request, 'schedule', con)

def schedule_past(request):
    now = datetime.date.today()
    exh = models.Exhibition.objects.filter(end__lt=now).order_by('-start')
    con = {'exhibitions': exh}
    return view_with_ml(request, 'schedule-past', con)

def news(request):
    return view_with_ml(request, 'news')

def guide(request):
    return view_with_ml(request, 'guide', {
        'base': 'media/images/guide/',
        'pictures': ['0'+str(i+1)+'.jpg' for i in range(5)],
    })

def access(request):
    return view_with_ml(request, 'access')



# This sandbox is for experimenting with new creations
def sandbox(request):
    return view_with_ml(request, 'sandbox')
