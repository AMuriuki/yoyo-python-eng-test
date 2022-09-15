from urllib import response
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.test import TestCase

from api.utils import maximum


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
