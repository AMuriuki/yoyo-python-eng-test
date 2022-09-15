import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.conf import settings

from api.utils import WEATHER_API_BASE_URL, get_average, get_data, is_valid_queryparam, get_maximum, get_median, get_minimum

# Create your views here.


@api_view()
def get_city_temp(request, city):

    # get api key
    api_key = settings.WEATHER_API_KEY

    # get days
    days = request.GET.get('days')

    # check if input value is valid
    if is_valid_queryparam(days) == "is valid":
        # structure url
        print(days)
        url = WEATHER_API_BASE_URL + "/forecast.json?key="+api_key + \
            "&q=" + city + "&days="+days+"&aqi=no&alerts=no"

        print(url)

        response = requests.get(url)
        result = response.json()

        if response.status_code == 200:
            data = get_data(result)
            maximum = get_maximum(data)
            minimum = get_minimum(data)
            average = get_average(data)
            median = get_median(data)
            return Response({
                "maximum": maximum,
                "minimum": minimum,
                "average": average,
                "median": median,
            })
        else:
            return Response(result)

    else:
        return Response({"message": is_valid_queryparam(days)})
