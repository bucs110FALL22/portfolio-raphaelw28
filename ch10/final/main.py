from owm import OpenWeatherMapAPI
from uv import OpenUVAPI

#Location coordinates
lat = float(input('Enter the latitude of the location: '))
lon = float(input('Enter the longitude of the location: '))

#OpenWeatherMap API = 'ebc34c9b3544456cf05b3c08fbe985f3'
owm = OpenWeatherMapAPI('ebc34c9b3544456cf05b3c08fbe985f3')
#OpenUV API = '5bd9a7515ead00adec12f375d06473de'
uv = OpenUVAPI('5bd9a7515ead00adec12f375d06473de')

#Current weather and uv
weather = owm.get_weather(lat, lon)
uv_index = uv.get_uv_index(lat, lon)

#Convert temperature from kelvin to celcius
temp_kelvin = weather["main"]["temp"]
temp_celcius = temp_kelvin - 273.15

#print temperature and weather
print(f'The current temperature is {temp_celcius} degrees Celcius.')
print(f'The weather is currently: {weather["weather"][0]["description"]}')

# Print the current UV index and a message about its potential dangers
print(f'The current UV index is: {uv_index["result"]["uv"]}')

if uv_index["result"]["uv"] >= 8:
    print('Be sure to wear sunscreen and take other precautions to protect yourself from the sun.')
else:
    print('No need to wear sunscreen, but still take precautions against overexposure from UV rays')
