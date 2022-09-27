from django.urls import reverse
from rest_framework.test import APITestCase


class WeatherAPITestCase(APITestCase):
    """
    Test module for Weather API
    """
    def test_invalid_period(self):
        """
        When invalid period is provided
        """
        url = reverse("get_city_temp", kwargs={"city": "London"})

        response = self.client.get(url, {"days": "ten"})
        result = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["message"], "Value provided is not an integer")
