from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.

def index(request):
    context = {'x': 'ano ano GALERIE'}
    return render(request, 'home/index.html', context)


def concept(request):
    return render(request, 'home/concept.html', {})

def schedule(request):
    return render(request, 'home/schedule.html', {})

def news(request):
    return render(request, 'home/news.html', {})

def guide(request):
    return render(request, 'home/guide.html', {})

def access(request):
    return render(request, 'home/access.html', {})



# This sandbox is for experimenting with new creations
def sandbox(request):
    return render(request, 'home/sandbox.html', {})
