from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.

def ml_selection(request):
    if "ml-language-selection" in request.COOKIES:
        lang = request.COOKIES["ml-language-selection"]
    else:
        lang = "en"
    return lang


def view_with_ml(request, view_name, context={}):
    context['ml-language-selection'] = ml_selection(request)
    context['present_view_name'] = view_name
    return render(request, 'home/'+view_name+'.html', context)


def index(request):
    return view_with_ml(request, 'index')

def concept(request):
    return view_with_ml(request, 'concept')

def schedule(request):
    return view_with_ml(request, 'schedule')

def news(request):
    return view_with_ml(request, 'news')

def guide(request):
    return view_with_ml(request, 'guide')

def access(request):
    return view_with_ml(request, 'access')



# This sandbox is for experimenting with new creations
def sandbox(request):
    return view_with_ml(request, 'sandbox')
