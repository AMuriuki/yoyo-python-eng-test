import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.conf import settings

from api.utils import WeatherData


@api_view()
def get_city_temp(request, city):
    if not str(request.GET.get("days")).isnumeric():
        return Response({"message": "Value provided is not an integer"}, 400)

    response = requests.get(
        f"{settings.WEATHER_API_BASE_URL}/"
        f"forecast.json?key={settings.WEATHER_API_KEY}"
        f"&q={city}&days{request.GET.get('days')}&aqi=no&alerts=no"
    )
    try:
        response.raise_for_status
    except requests.exceptions.HTTPError:
        # Contains the appropriate error message
        return Response(
            {"error": {"code": 1006, "message": "No matching location found"}},
            400,
        )
    else:
        return Response(WeatherData(response.json()).data, 200)
