from django.urls import path
from .views import indexPageView
from .views import featuredPageView
from .views import mapPageView
from .views import createPageView
from .views import updatePageView
from .views import loginPageView, register_request, logout_request
from .views import showTrailsPageView
from .views import deleteTrailPageView


urlpatterns = [
    path("logout/", logout_request, name="logout"),
    path('register/', register_request, name="register"),
    path('login/', loginPageView, name='login'),
    path('featured/', featuredPageView, name='featured'),
    path('map/', mapPageView, name='map'),
    path('create/', createPageView, name='create'),
    path('update/', updatePageView, name='update'),
    path("delete/<int:trail_id>/",
         deleteTrailPageView, name="delete"),
    path('showtrails/', showTrailsPageView, name='test'),

    path('', indexPageView, name='index'),
]
