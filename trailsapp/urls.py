from django.urls import path
from .views import indexPageView
from .views import crudPageView
from .views import featuredPageView
from .views import mapPageView

urlpatterns = [

    path('', indexPageView, name='index'),
    path('', crudPageView, name='crud'),
    path('', featuredPageView, name='featured'),
    path('', mapPageView, name='map'),

]
# test codeS
