from django.contrib import admin

# Register your models here.
from .models import GeoCoordinates, InstagramUsers


admin.site.register(GeoCoordinates)
admin.site.register(InstagramUsers)
