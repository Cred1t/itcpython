
import requests
import xmltodict

def get_nbkr_curs():
    nbkr_url = 'https://www.nbkr.kg/XML/daily.xml'
    response = requests.get(nbkr_url)
    curs_dict = xmltodict.parse(response.text)

    date = curs_dict['CurrencyRates']['@Date']

    print('Курсы валют по НБКР на', date)
    for currency in curs_dict['CurrencyRates']['Currency']:
        # print(currency['@ISOCode'], ':', currency['Value'])
        if currency['@ISOCode'] == 'USD':
            print('Доллар', ':', currency['Value'])
        elif currency['@ISOCode'] == 'RUB':
            print('Рубль', ':', currency['Value'])
        elif currency['@ISOCode'] == 'KZT':
            print('Тенге', ':', currency['Value'])
        elif currency['@ISOCode'] == 'EUR':
            print('Евро', ':', currency['Value'])