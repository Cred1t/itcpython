
from django.contrib import admin
from django.urls import path
from valuta import views as valutaViews
from weather import views as weatherViews

urlpatterns = [
    path('', valutaViews.home),
    path('convert-usd/', valutaViews.convertDollar),
    path('admin/', admin.site.urls),

    path('get-weather/', weatherViews.current_weather),
    path('weather_online/', weatherViews.weather_online),
    path('get_weather-online/', weatherViews.get_weather_online)
]
