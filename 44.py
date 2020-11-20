# утилита, используя api, показывает погоду
import requests

city_name = input("Enter city name: ")
api_url = 'http://api.openweathermap.org/data/2.5/weather'

paramss = {
    'q': city_name,
    'appid': 'e2881c7dd241fe57e725d9969d580512',
    'units': 'metric'
}

res = requests.get(api_url, params=paramss)
data = res.json()
print('Temperature in {} is {} celsius'.format(city_name, data['main']['temp']))
