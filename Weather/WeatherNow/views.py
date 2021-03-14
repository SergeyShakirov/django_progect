import requests
from django.shortcuts import render
from .models import Cities
from .forms import City_form


def top(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=c579b1fa460e36193367cf2b4bb6ed10'
    if request.method == 'POST':
        city_name_post = request.POST['name']
        res = requests.get(url.format(city_name_post)).json()
        if res['cod'] == 200:
            form = City_form({
                'name': city_name_post,
                'city_id': res['id']
            })
            form.save()

    form = City_form()

    cities_info = Cities.objects.all()
    all_cities = []
    for city in cities_info:
        res = requests.get(url.format(city.name)).json()
        if res['cod'] != 200:
            continue
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
        }
        all_cities.append(city_info)
    return {'form': form, 'all_cities': all_cities}


def index(request):
    data = top(request)
    context = {
        'all_info': data['all_cities'],
        'form': data['form'],
    }
    return render(request, 'WeatherNow/index.html', context)


def detail(request, city_name):
    data = top(request)

    context = {
        'all_info': data['all_cities'],
        'form': data['form'],
        'city_name': city_name,
    }
    return render(request, 'WeatherNow/detail.html', context)