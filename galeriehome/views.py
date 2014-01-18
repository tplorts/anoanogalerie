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


def viewWithML(request, template_name, context={}):
    context['ml-language-selection'] = ml_selection(request)
    return render(request, template_name, context)


def index(request):
    return viewWithML(request, 'home/index.html')

def concept(request):
    return viewWithML(request, 'home/concept.html')

def schedule(request):
    return viewWithML(request, 'home/schedule.html')

def news(request):
    return viewWithML(request, 'home/news.html')

def guide(request):
    return viewWithML(request, 'home/guide.html')

def access(request):
    return viewWithML(request, 'home/access.html')



# This sandbox is for experimenting with new creations
def sandbox(request):
    return viewWithML(request, 'home/sandbox.html')
