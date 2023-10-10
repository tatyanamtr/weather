import requests
import os
from django.shortcuts import render

# Create your views here.

def index(request):
    appID = os.getenv('OpenWeatherToken')

    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=' + appID + '&units=metric'

    city_name = 'Tbilisi'

    response = requests.get(url.format(city_name)).json()
    
    city_info = {
        'city_name': city_name,
        'temp': response['main']['temp'],
        'icon': response['weather'][0]['icon']
        
    }
    
    context = {
        'info': city_info
        }

    return render(request, 'weather/index.html', context)
