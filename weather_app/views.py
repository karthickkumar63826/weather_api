from django.shortcuts import render
from .weather_api import get_weather_data

# Create your views here.


def weather(request):
    if request.method == 'POST':
        city_name = request.POST.get('city')
        api_key = "9d5ba37c44a58b2fd3daacd9794a8446"
        weather_data = get_weather_data(city_name, api_key)

        if weather_data['cod'] == 200:
            temperature = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            context = {'temperature': temperature, 'description': description}

        else:
            context = {'error': 'City name not found'}

    else:
        context = {}

    return render(request, 'weather.html', context)
