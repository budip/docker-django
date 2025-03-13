from django.urls import path
from . import views
from .views import apod

urlpatterns = [
    path('', views.index, name='nasa_index'),
    path('apod/', apod, name='nasa_apod'),
]