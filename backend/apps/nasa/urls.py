from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='nasa_index'),  # This will respond to /nasa/
]