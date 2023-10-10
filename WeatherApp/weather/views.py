import requests
import os
from .models import City
from django.shortcuts import render

# Create your views here.

def index(request):
    appID = os.getenv('OpenWeatherToken')

    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=' + appID + '&units=metric'

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        response = requests.get(url.format(city.city_name)).json()
        city_info = {
        'city_name': city.city_name,
        'temp': response['main']['temp'],
        'icon': response['weather'][0]['icon']
        }
        all_cities.append(city_info)

    context = {
        'all_info': all_cities
        }

    return render(request, 'weather/index.html', context)
