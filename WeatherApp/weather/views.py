import requests
from django.shortcuts import render

# Create your views here.

def index(request):
    appID = '02274ac1b8ecba7cbb4b0ac942c964f8'

    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=' + appID + '&units=metric'

    city_name = 'Tbilisi'

    response = requests.get(url.format(city_name)).json()
    
    city_info = {
        'city_name': city_name,
        'temp': response["main"]["temp"],
        
    }
    print(city_info)

    return render(request, 'weather/index.html')
