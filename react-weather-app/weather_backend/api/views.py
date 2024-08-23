import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class GeoLocationView(APIView):
    def get(self, request):
        url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"
        headers = {
            "x-rapidapi-key": "c11d840505mshdb364c0bd10254cp1dfd5djsn879965441341",
            "x-rapidapi-host": "wft-geo-db.p.rapidapi.com"
        }
        params = request.GET
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response({"error": "Failed to fetch location data"}, status=response.status_code)

class WeatherDataView(APIView):
    def get(self, request):
        lat = request.GET.get('lat')
        lon = request.GET.get('lon')

        current_weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=3d32d60df8e83be432e763969b3641b0&units=metric"
        forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid=3d32d60df8e83be432e763969b3641b0&units=metric"

        current_weather_response = requests.get(current_weather_url)
        forecast_response = requests.get(forecast_url)

        if current_weather_response.status_code == 200 and forecast_response.status_code == 200:
            current_weather_data = current_weather_response.json()
            forecast_data = forecast_response.json()

            return Response({
                "current_weather": current_weather_data,
                "forecast": forecast_data
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Failed to fetch weather data"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
