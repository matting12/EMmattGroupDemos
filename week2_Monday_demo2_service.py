# weather_service.py

import requests

class WeatherService:
    def get_temperature(self, city):
        """Get current temperature for a city from weather API."""
        url = f"https://api.weather.com/v1/city/{city}/temperature"
        response = requests.get(url)
        data = response.json()
        # convert fahrenheit to celsius
        return data['temperature']