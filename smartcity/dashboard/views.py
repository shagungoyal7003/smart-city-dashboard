

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from .models import WeatherData
from .utils import get_weather

def fetch_data(request):
    data = get_weather()

    if data is None:
        return JsonResponse({"error": "API not working or invalid key"})

    WeatherData.objects.create(
        city=data['city'],
        temperature=data['temp'],
        humidity=data['humidity']
    )

    return JsonResponse({"message": "Data stored successfully"})


def dashboard_view(request):
    data = WeatherData.objects.all().order_by('-timestamp')
    return render(request, 'dashboard.html', {'data': data})