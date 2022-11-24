from django.urls import path
from .views import indexPageView
from .views import crudPageView
from .views import featuredPageView
from .views import mapPageView

urlpatterns = [

    path('crud/', crudPageView, name='crud'),
    path('featured/', featuredPageView, name='featured'),
    path('map/', mapPageView, name='map'),
    path('', indexPageView, name='index'),
]
