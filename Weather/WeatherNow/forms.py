from .models import Cities
from django.forms import ModelForm, TextInput


class City_form(ModelForm):
    class Meta:
        model = Cities
        fields = ['name', 'city_id']