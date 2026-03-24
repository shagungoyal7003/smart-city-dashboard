from django.db import models

# Create your models here.
from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city
class AirQuality(models.Model):
    city = models.CharField(max_length=100)
    aqi = models.IntegerField()
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city
class TrafficData(models.Model):
    location = models.CharField(max_length=100)
    congestion_level = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.city
class PublicService(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.city