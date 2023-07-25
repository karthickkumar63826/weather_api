from django.urls import path
from . import views


# declaring the url path
urlpatterns = [
    path('', views.weather, name='weather'),
]
