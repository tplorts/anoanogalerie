from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.

def index(request):
    context = {'x': 'ano ano GALERIE'}
    return render(request, 'home/index.html', context)



def sandbox(request):
    return render(request, 'home/sandbox.html', {})
