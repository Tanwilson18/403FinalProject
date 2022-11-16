#from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def indexPageView(request):
    return HttpResponse('This is where our home page will go :))))))))))))))!!!!!')

def crudPageView(request):
    return HttpResponse('This is where our CRUD Page will go')

def featuredPageView(request):
    return HttpResponse('This is where our featured trails will go')

def mapPageView(request):
    return HttpResponse('This is where our map Page will go!! YAY FOR MAPS')