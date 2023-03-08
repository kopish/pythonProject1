import requests
import xml.etree.ElementTree as ET


def convert_currency(amount, from_currency, to_currency):
    base_url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange'
    url = f'{base_url}&valcode={from_currency}&valcode={to_currency}&xml'
    response = requests.get(url)
    root = ET.fromstring(response.content)
    rates = {elem.find('cc').text: float(elem.find('rate').text) for elem in
             root.findall('.//currency')}
    exchange_rate = rates[to_currency] / rates[from_currency]
    result = round(amount * exchange_rate, 2)
    return result


result = convert_currency(100, 'USD', 'EUR')
print(result)
