from django.urls import path
from .views import GeoLocationView, WeatherDataView

urlpatterns = [
    path('geo/', GeoLocationView.as_view(), name='geo_location'),
    path('weather/', WeatherDataView.as_view(), name='weather_data'),
]
