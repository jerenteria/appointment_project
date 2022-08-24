from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.index),
    path('make_appointment', views.create_appointment),
]