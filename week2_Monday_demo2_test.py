# test_weather_service.py

import unittest
from unittest.mock import patch, Mock
from week2_Monday_demo2_service import WeatherService

class TestWeatherService(unittest.TestCase):
    
    @patch('weather_service.requests.get')
    def test_get_temperature(self, mock_get):
        # Create a mock response
        mock_response = Mock()
        mock_response.json.return_value = {'temperature': 72}
        mock_get.return_value = mock_response
        
        # Test the method
        service = WeatherService()
        temp = service.get_temperature('Boston')
        
        # Assert the result
        self.assertEqual(temp, 72)
        
        # Verify the API was called correctly
        mock_get.assert_called_once_with('https://api.weather.com/v1/city/Boston/temperature')

if __name__ == '__main__':
    unittest.main()