from django.urls import path
from . import views

app_name = 'WeatherNow'
urlpatterns = [
    path('', views.index, name='home'),
    path('<str:city_name>', views.detail, name='detail'),
]