import imp
from rest_framework import routers

from django.urls import path, include
from .views import *

router = routers.DefaultRouter()

urlpatterns = [
    path('locations/<string:city>', get_city_temp, name='get_city_temp')
]
