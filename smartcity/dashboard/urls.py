from django.urls import path
from .views import fetch_data, dashboard_view

urlpatterns = [
    path('', dashboard_view),
    path('fetch/', fetch_data),
]