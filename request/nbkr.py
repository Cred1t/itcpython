
import requests
import xmltodict

nbkr_url = 'https://www.nbkr.kg/XML/daily.xml'
response = requests.get(nbkr_url)
curs_dict = xmltodict.parse(response.text)

date = curs_dict['CurrencyRates']['@Date']

print('Курсы валют по НБКР на: ', date)

for currency in curs_dict['CurrencyRates']['Currency']:
    print(currency['@ISOCode'], ':', currency['Value'])
