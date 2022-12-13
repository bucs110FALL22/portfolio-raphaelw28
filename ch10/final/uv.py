import requests

class OpenUVAPI:
    def __init__(self, api_key):
        self.api_key = api_key
    
    def get_uv_index(self, lat, lon):
        url = f'https://api.openuv.io/api/v1/uv?lat={lat}&lng={lon}'
        response = requests.get(url, headers={'x-access-token': self.api_key})
        data = response.json()
        return data