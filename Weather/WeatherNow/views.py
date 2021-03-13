import requests
from django.shortcuts import render


def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=c579b1fa460e36193367cf2b4bb6ed10'
    city = 'London'
    res = requests.get(url.format(city)).json()
    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon'],
    }
    context = {'info': city_info}
    return render(request, 'WeatherNow/index.html', context)