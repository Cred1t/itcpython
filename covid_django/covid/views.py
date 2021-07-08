from django.shortcuts import render
import requests
import json

covid_url = 'https://covid-api.mmediagroup.fr/v1/cases?country={country}'


def covid_stat(request):
    return render(request, 'index.html')


def get_covid_stat(request):
    country_code = request.POST.get('country_code')
    covid_response = covid_url.format(country = country_code)
    co = requests.get(covid_response)


    covid_json = co.json()
    confirmed = covid_json['All']['confirmed']
    recovered = covid_json['All']['recovered']
    deaths = covid_json['All']['deaths']
    population = covid_json['All']['population']
    sq_km_area = covid_json['All']['sq_km_area']
    life_expectancy = covid_json['All']['life_expectancy']
    return render(request, 'index.html',{
        'country_code': country_code,
        # 'covid_response': covid_json,
        'confirmed': confirmed,
        'recovered': recovered,
        'deaths': deaths,
        'population': population,
        'sq_km_area': sq_km_area,
        'life_expectancy': life_expectancy,
        'co': covid_json,
    }
    

)