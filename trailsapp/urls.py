from django.urls import path
from .views import indexPageView
from .views import mapPageView
from .views import createPageView
from .views import updatePageView
from .views import loginPageView, register_request, logout_request
from .views import showTrailsPageView
from .views import deleteTrailPageView
from .views import makeUpdatePageView
from .views import viewOneTrailView


urlpatterns = [
    path("logout/", logout_request, name="logout"),
    path('register/', register_request, name="register"),
    path('login/', loginPageView, name='login'),
    path('map/', mapPageView, name='map'),
    path('create/', createPageView, name='create'),
    path('update/', updatePageView, name='update'),
    path("delete/<int:trail_id>",
         deleteTrailPageView, name="delete"),
    path('showtrails/', showTrailsPageView, name='showtrails'),
    path('makeupdate/', makeUpdatePageView, name='makeupdate'),
    path('viewTrail/<int:trail_id>', viewOneTrailView, name="viewtrail"),
    path('', indexPageView, name='index'),
]
