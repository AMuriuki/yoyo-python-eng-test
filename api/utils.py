import statistics

WEATHER_API_BASE_URL = "http://api.weatherapi.com/v1"


def get_average(list):
    avg = sum(list) / len(list)
    return round(avg, 1)


def get_median(list):
    return statistics.median(list)


def get_data(result):
    data = []
    forecast = result['forecast']
    for item in forecast['forecastday']:
        data.append(item['day']['avgtemp_c'])
    return data
