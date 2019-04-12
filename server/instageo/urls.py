from django.urls import path
from . import views


urlpatterns = [
    path('country/', views.GeoSelect.as_view(), name='country'),
    path('medias/', views.Medias.as_view(), name='medias'),
]
