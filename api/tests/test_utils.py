from api.utils import WeatherData


def test_weather_data(mocker):
    data = WeatherData(
        temperature_data={
            "forecast": {
                "forecastday": [
                    {"day": {"avgtemp_c": "17.8"}},
                    {"day": {"avgtemp_c": "20.5"}},
                    {"day": {"avgtemp_c": "21.7"}},
                    {"day": {"avgtemp_c": "13.6"}},
                    {"day": {"avgtemp_c": "25.4"}},
                ]
            }
        }
    )
    assert data.summary == {
        "maximum": 25.4,
        "minimum": 13.6,
        "average": 19.8,
        "median": 20.5,
    }
