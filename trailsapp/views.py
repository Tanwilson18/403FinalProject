#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def indexPageView(request):
    return render(request, 'trailsapp/index.html')


def crudPageView(request):
    return render(request, 'trailsapp/crud.html')


def featuredPageView(request):
    return render(request, 'trailsapp/featured.html')


def mapPageView(request):
    return render(request, 'trailsapp/map.html')
