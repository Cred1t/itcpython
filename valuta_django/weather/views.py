from django.shortcuts import render
import requests
import json
    
pogoda_api_key = 'fa0c69065a227aae0ae1081d5953bcfa'

# Create your views here.

pogoda_url = 'https://api.openweathermap.org/data/2.5/weather?q={city},{state}&appid={api_key}&units=metric'

def current_weather(request):
    weather = {
        'osh': 36.4,
        'bishkek': 38.4,
        'london': 24.5
    }
    return render(request, 'weather_template.html', {
        'osh': weather['osh'],
        'bishkek': weather['bishkek'], 
        'london': weather['london'],
    })
    
def weather_online(request):
    return render(request, 'weather_online.html')


def get_weather_online(request):
    city_for_url = request.POST.get('city_input')
    state_for_url = request.POST.get('state_input')
    pogoda_url_final = pogoda_url.format(city = city_for_url, state = state_for_url, api_key = pogoda_api_key)

    pogo_otvet = requests.get(pogoda_url_final)
    pogo_otvet_json = pogo_otvet.json()

    temp = pogo_otvet_json['main']['temp']
    wind = pogo_otvet_json['wind']['speed']

    return render(request, 'weather_online.html', {
        'pogoda_otvet': pogoda_url_final,
        'temparature': temp,
        'city_for_url': city_for_url,
        'wind': wind
    })