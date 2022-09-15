from urllib import response
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.test import TestCase

from api.utils import get_average, get_maximum, get_minimum, get_median


class WeatherAPITestCase(APITestCase):
    """
    Test module for Weather API 
    """

    def get_city_temp(self):
        """
        Ensure we can get an API response
        """
        url = reverse('get_city_temp', kwargs={
                      'city': 'London'})
        response = self.client.get(url, {'days': 10})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_city(self):
        """
        When a non existent city is queried.
        """
        url = reverse('get_city_temp', kwargs={
                      'city': 'Lo'})

        response = self.client.get(url, {'days': 10})
        result = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result['error']['code'], 1006)
        self.assertEqual(result['error']['message'],
                         "No matching location found.")

    def test_invalid_period(self):
        """
        When invalid period is provided
        """
        url = reverse('get_city_temp', kwargs={
                      'city': 'London'})

        response = self.client.get(url, {'days': 'ten'})
        result = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result['message'], "Value provided is not an integer")


class MathFunctionsTestCase(TestCase):
    def test_max(self):
        data = [17.8, 20.5, 21.7, 13.6, 25.4]
        max = get_maximum(data)
        self.assertEqual(max, 25.4)

    def test_min(self):
        data = [17.8, 20.5, 21.7, 13.6, 25.4]
        min = get_minimum(data)
        self.assertEqual(min, 13.6)

    def test_average(self):
        data = [17.8, 20.5, 21.7, 13.6, 25.4]
        avg = get_average(data)
        self.assertEqual(avg, 19.8)

    def test_median(self):
        data = [17.8, 20.5, 21.7, 13.6, 25.4]
        mid = get_median(data)
        self.assertEqual(mid, 20.5)
