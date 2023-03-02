price1 = float(input('Введите 1ю цену, грн: '))
price2 = float(input('Введите 2ю цену, грн: '))
price3 = float(input('Введите 3ю цену, грн: '))
"""
if price1 >= price2:
    if price1 >= price3:
        print('Акция! К оплате за три товара:', price1, 'грн')
    else:
        print('Акция! К оплате за три товара:', price3, 'грн')
else:
    if price2 >= price3:
        print('Акция! К оплате за три товара:', price2, 'грн')
    else:
        print('Акция! К оплате за три товара:', price3, 'грн')
"""
if price1 <= price2:
    price1 = price2
if price1 <= price3:
    price1 = price3
print('Акция! К оплате за три товара:', price1, 'грн')
