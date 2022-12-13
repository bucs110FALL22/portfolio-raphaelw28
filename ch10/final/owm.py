import requests

class OpenWeatherMapAPI:
    def __init__(self, api_key):
        self.api_key = api_key
    
    def get_weather(self, lat, lon):
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.api_key}'
        response = requests.get(url)
        data = response.json()
        return data