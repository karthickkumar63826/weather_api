import requests


def get_weather_data(city_name, api_key):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city_name, 'units': 'metric', 'appid': api_key}
    response = requests.get(base_url, params=params)
    data = response.json()
    return data
