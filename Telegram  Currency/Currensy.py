import requests
import xml.etree.ElementTree as ET

def convert_currency(amount, from_currency, to_currency):
    base_url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange'
    url = f'{base_url}&symbols={from_currency},{to_currency}'
    response = requests.get(url)
    data = response.json()
    exchange_rate = data['rates'][to_currency] / data['rates'][from_currency]
    result = round(amount * exchange_rate, 2)
    return result
