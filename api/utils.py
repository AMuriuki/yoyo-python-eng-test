import statistics

WEATHER_API_BASE_URL = "http://api.weatherapi.com/v1"


def is_valid_queryparam(data):
    if data != '' and data is not None:
        try:
            int(data)
            return True
        except ValueError:
            return "Value provided is not an integer"
    else:
        return "No value provided"


def maximum(list):
    return max(list)


def minimum(list):
    return min(list)


def average(list):
    avg = sum(list) / len(list)
    return round(avg, 1)


def median(list):
    return statistics.median(list)
