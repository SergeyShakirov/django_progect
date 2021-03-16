import requests
from django.shortcuts import render
from .models import Cities
from .forms import City_form
from django.views.generic import DeleteView, DetailView


def get_city_detail(name):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=c579b1fa460e36193367cf2b4bb6ed10'
    return requests.get(url.format(name)).json()


def top(request):
    if request.method == 'POST':
        city_name_post = request.POST['name']
        res = get_city_detail(city_name_post)
        if res['cod'] == 200:
            form = City_form({
                'name': res['name'],
                'city_id': res['id']
            })
            form.save()

    form = City_form()

    cities_info = Cities.objects.all()
    all_cities = []
    for city in cities_info:
        res = get_city_detail(city.name)
        if res['cod'] != 200:
            continue
        city_info = {
            'city': res['name'],
            'city_id': city.city_id,
            'id': city.id,
            'temp': int(res['main']['temp']),
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


class NewDetailView(DetailView):
    model = Cities
    template_name = 'WeatherNow/detail.html'

    def get_context_data(self, **kwargs):
        res = get_city_detail(self.object)
        return {
            'city': res['name'],
            'temp': int(res['main']['temp']),
            'icon': res['weather'][0]['icon'],
            'all_info': Cities.objects.all()
        }


class OnDelete(DeleteView):
    model = Cities
    success_url = '/'
    template_name = 'WeatherNow/city_delete.html'

    def get_context_data(self, **kwargs):
        res = get_city_detail(self.object)
        return {
            'city': res['name'],
            'temp': int(res['main']['temp']),
            'icon': res['weather'][0]['icon'],
            'all_info': Cities.objects.all()
        }