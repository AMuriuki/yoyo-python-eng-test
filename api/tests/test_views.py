from urllib import response
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class WeatherAPITestCase(APITestCase):
    """
    Test module for Weather API 
    """
    def get_city_temp(self):
        """
        Ensure we can get an API response
        """
        url = reverse('get_city_temp')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
