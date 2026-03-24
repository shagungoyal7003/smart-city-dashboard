# Register your models here.
from django.contrib import admin
from .models import WeatherData, AirQuality, TrafficData

admin.site.register(WeatherData)
admin.site.register(AirQuality)
admin.site.register(TrafficData)