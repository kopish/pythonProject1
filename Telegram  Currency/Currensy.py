import requests
import xml.etree.ElementTree as ET
# імпортуємо бібліотеку xml.etree.ElementTree і даем їй псевдонім ET.
# Це дозволить нам парсити XML-документи.


def convert_currency(amount, from_currency, to_currency):
    # визначаємо функцію convert_currency, яка приймає три аргументи: amount -
    # кількість валюти для конвертації, from_currency - вихідна валюта і
    # to_currency - валюта, в яку необхідно конвертувати.
    base_url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange'
    # зберігаємо URL-адресу веб-сайту, з яким ми будемо працювати.
    url = f'{base_url}&valcode={from_currency}&valcode={to_currency}&xml'
    # створюємо URL-адресу запиту зі значеннями вихідної та кінцевої валют
    response = requests.get(url)
    # надсилаємо запит на URL-адресу і зберігаємо отриману відповідь у
    # змінну response.
    root = ET.fromstring(response.content)
    # отримуємо кореневий елемент зі відповіді в форматі XML.
    rates = {elem.find('cc').text: float(elem.find('rate').text) for elem in
             root.findall('.//currency')}
    # парсимо XML-відповідь та зберігаємо валютні курси в словник rates,
    # де ключі - коди валют, а значення - курси валют.
    exchange_rate = rates[to_currency] / rates[from_currency]
    # обчислюємо курс конвертації.
    result = round(amount * exchange_rate, 2)
    # обчислюємо результат конвертації з врахуванням курсу та кількості
    # валюти для конвертації.
    return result


result = convert_currency(100, 'USD', 'EUR')
print(result)
