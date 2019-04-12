from django import forms
from .models import GeoCoordinates


class CountryForm(forms.Form):
    choices = ((i.id, str(i)) for i in GeoCoordinates.objects.all())
    geofield = forms.ChoiceField(choices=choices, label='Выберите гео')
    geofield.widget.attrs.update({'class': 'form-control'})
