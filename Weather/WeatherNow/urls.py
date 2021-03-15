from django.urls import path
from . import views

app_name = 'WeatherNow'
urlpatterns = [
    path('', views.index, name='home'),
    path('<str:name>', views.NewDetailView.as_view(), name='detail'),
    path('<str:name>/delete', views.OnDelete.as_view(), name='on_delete'),
]