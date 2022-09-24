import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.conf import settings

from api.utils import WEATHER_API_BASE_URL, get_average, get_data, get_median

# Create your views here.


@api_view()
def get_city_temp(request, city):

    # get api key
    api_key = settings.WEATHER_API_KEY

    # get days
    days = request.GET.get('days')

    # check if input value is valid
    if str(days).isnumeric():
        # structure url
        url = WEATHER_API_BASE_URL + "/forecast.json?key="+api_key + \
            "&q=" + city + "&days="+days+"&aqi=no&alerts=no"

        try:
            response = requests.get(url)
            # if response was successful
            result = response.json()
        except requests.exceptions.Timeout as e:
            print("Timeout error:", e)
        except requests.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  
        except Exception as err:
            print(f'Other error occurred: {err}')  

        if response.status_code == 200:
            data = get_data(result)
            return Response({
                "maximum": max(data),
                "minimum": min(data),
                "average": get_average(data),
                "median": get_median(data),
            })
        else:
            return Response(result)

    else:
        return Response({"message": "Value provided is not an integer"})
