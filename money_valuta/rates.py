
import xmltodict

curr = open('currency.xml', 'r')
curr_xml = curr.read()
curr_dict = xmltodict.parse(curr_xml)

print('Курс Валют по: ', end = "")
print(curr_dict['CurrencyRates']['@Date'])