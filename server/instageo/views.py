from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from .utils import MyBot
import time
from .models import GeoCoordinates, InstagramUsers


class GeoSelect(View):
    template_name = 'country.html'

    def get(self, request):
        form = CountryForm()
        return render(request, template_name=self.template_name, context={'form': form})

    def post(self, request):
        bound_form = CountryForm(request.POST)
        if bound_form.is_valid():
            request.session['geofield'] = bound_form.cleaned_data.get('geofield')
            return redirect('medias')
        return render(request, self.template_name, context={'form': bound_form})


class Medias(View):
    template_name = 'medias.html'

    def get(self, request):
        if not request.session.get('geofield'):
            return redirect('country')
        geo = GeoCoordinates.objects.get(pk=request.session.get('geofield'))
        bot = MyBot()
        user = InstagramUsers.objects.first()
        bot.login(username=user.username, password=user.password)
        time.sleep(10)
        medias = bot.get_medias_from_coordinates(geo.latitude, geo.longitude, depth=3)
        request.session.clear()

        return render(request,
                      template_name=self.template_name,
                      context={'medias': medias})
