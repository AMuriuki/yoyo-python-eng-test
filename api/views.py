import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.conf import settings

# Create your views here.
WEATHER_API_BASE_URL = "http://api.weatherapi.com/v1"


@api_view()
def get_city_temp(request, city):

    # get api key
    api_key = settings.WEATHER_API_KEY

    # url form
    url = WEATHER_API_BASE_URL + "/forecast.json?key="+api_key+"&q=" + city + "& days = 10 & aqi = no & alerts = no"

    #TODO: 
    # 1. test cases & coverage
    # 2. best practices - input validation; error handling etc.
    # 3. well structured readme.md
    # 4. response format for request

    # get response object from api
    response = requests.get(url)

    print(response)

    return Response({

    })
