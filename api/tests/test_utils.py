from django.urls import reverse
from api.utils import get_average, get_median


def test_average():
    data = [17.8, 20.5, 21.7, 13.6, 25.4]
    assert get_average(data) == 19.8


def test_median():
    data = [17.8, 20.5, 21.7, 13.6, 25.4]
    assert get_median(data) == 20.5
